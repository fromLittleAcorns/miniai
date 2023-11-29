# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/12_callbacks.ipynb.

# %% auto 0
__all__ = ['CancelFitException', 'CancelBatchException', 'CancelEpochException', 'Callback', 'SingleBatchCB', 'MetricsCB',
           'DeviceCB', 'TrainCB', 'ProgressCB', 'BaseSchedCB', 'BatchSchedCB', 'OneCycleLrCB', 'EpochSchedCB',
           'HasLearnCB', 'RecorderCB']

# %% ../nbs/12_callbacks.ipynb 1
import fastcore.all as fc
from torch.optim import lr_scheduler
from torcheval.metrics import MulticlassAccuracy,Mean
from copy import copy
from fastprogress import progress_bar,master_bar
import matplotlib.pyplot as plt

from .utils import def_device, to_device, to_cpu

# %% ../nbs/12_callbacks.ipynb 2
class CancelFitException(Exception): pass
class CancelBatchException(Exception): pass
class CancelEpochException(Exception): pass

# %% ../nbs/12_callbacks.ipynb 3
class Callback(): order = 0

# %% ../nbs/12_callbacks.ipynb 4
class SingleBatchCB(Callback):
    order = 1
    def after_batch(self, learn): raise CancelFitException()

# %% ../nbs/12_callbacks.ipynb 5
class MetricsCB(Callback):
    def __init__(self, *ms, **metrics):
        for o in ms: metrics[type(o).__name__] = o
        self.metrics = metrics
        self.all_metrics = copy(metrics)
        self.all_metrics['loss'] = self.loss = Mean()

    def _log(self, d): print(d)
    def before_fit(self, learn): learn.metrics = self
    def before_epoch(self, learn): [o.reset() for o in self.all_metrics.values()]

    def after_epoch(self, learn):
        log = {k:f'{v.compute():.3f}' for k,v in self.all_metrics.items()}
        log['epoch'] = str(learn.epoch)
        log['train'] = 'train' if learn.model.training else 'eval'
        self._log(log)

    def after_batch(self, learn):
        x,y,*_ = to_cpu(learn.batch)
        for m in self.metrics.values(): m.update(to_cpu(learn.preds), y)
        self.loss.update(to_cpu(learn.loss), weight=len(x))

# %% ../nbs/12_callbacks.ipynb 6
class DeviceCB(Callback):
    def __init__(self, device=def_device): fc.store_attr()
    def before_fit(self, learn):
        if hasattr(learn.model, 'to'): learn.model.to(self.device)
    def before_batch(self, learn): learn.batch = to_device(learn.batch, device=self.device)

# %% ../nbs/12_callbacks.ipynb 8
class TrainCB(Callback):
    def __init__(self, n_inp=1): self.n_inp = n_inp
    def predict(self, learn): learn.preds = learn.model(*learn.batch[:self.n_inp])
    def get_loss(self, learn): learn.loss = learn.loss_func(learn.preds, *learn.batch[self.n_inp:])
    def backward(self, learn): learn.loss.backward()
    def step(self, learn): learn.opt.step()
    def zero_grad(self, learn): learn.opt.zero_grad()

# %% ../nbs/12_callbacks.ipynb 9
class ProgressCB(Callback):
    order = MetricsCB.order+1
    def __init__(self, plot=False): self.plot = plot
    def before_fit(self, learn):
        learn.epochs = self.mbar = master_bar(learn.epochs)
        self.first = True
        if hasattr(learn, 'metrics'): learn.metrics._log = self._log
        self.losses = []
        self.val_losses = []

    def _log(self, d):
        if self.first:
            self.mbar.write(list(d), table=True)
            self.first = False
        self.mbar.write(list(d.values()), table=True)

    def before_epoch(self, learn): learn.dl = progress_bar(learn.dl, leave=False, parent=self.mbar)
    def after_batch(self, learn):
        learn.dl.comment = f'{learn.loss:.3f}'
        if self.plot and hasattr(learn, 'metrics') and learn.training:
            self.losses.append(learn.loss.item())
            if self.val_losses: self.mbar.update_graph([[fc.L.range(self.losses), self.losses],[fc.L.range(learn.epoch).map(lambda x: (x+1)*len(learn.dls.train)), self.val_losses]])
    
    def after_epoch(self, learn): 
        if not learn.training:
            if self.plot and hasattr(learn, 'metrics'): 
                self.val_losses.append(learn.metrics.all_metrics['loss'].compute())
                self.mbar.update_graph([[fc.L.range(self.losses), self.losses],[fc.L.range(learn.epoch+1).map(lambda x: (x+1)*len(learn.dls.train)), self.val_losses]])

# %% ../nbs/12_callbacks.ipynb 11
class BaseSchedCB(Callback):
    """ Base scheduling class that will trigger events.  Initialised with a Pytorch type scheduler
    The scheduler is assigned to the learner optimiser before fit and the scheduler step method
    implemented whenever the optimiser is stepped by the learner
    """
    def __init__(self, sched, **kwargs): 
        self.sched = sched
        self.kwargs=kwargs
        
    def before_fit(self, learn): self.schedo = self.sched(learn.opt)
    def _step(self, learn):
        if learn.training: self.schedo.step()

# %% ../nbs/12_callbacks.ipynb 12
class BatchSchedCB(BaseSchedCB):
    """ Inherits from the BaseSchedCD class and adds an additional scheduler step after each batch
    """
    def after_batch(self, learn): self._step(learn)

# %% ../nbs/12_callbacks.ipynb 13
class OneCycleLrCB(BatchSchedCB):
    """ Inherits from the BatchSchedCD class and works out the scheduler to cover the period of 
    the fit (ie the number of epoch and batches in a specific fit
    """
    
    def __init__(self, max_lr: float = 0.01, **kwargs):
        """ Define the parameters for the one cyc
        """
        self.max_lr = max_lr
        self.kwargs = kwargs
    
    def before_fit(self, learn):
        # Assign scheduler
        num_batches = len(learn.dls.train)
        total_steps = num_batches * learn.n_epochs
        self.schedo = lr_scheduler.OneCycleLR(learn.opt, total_steps=total_steps,
                         max_lr=self.max_lr, **self.kwargs)
        
    def after_batch(self, learn): self._step(learn)

# %% ../nbs/12_callbacks.ipynb 14
class EpochSchedCB(BaseSchedCB):
    """ Inherits from the BaseSchedCD class and adds an additional scheduler step after each epoch.
    Provides a more granular change in the optimiser parameters than the batch scheduler for where
    that would be valuable
    """
    def after_epoch(self, learn): self._step(learn)

# %% ../nbs/12_callbacks.ipynb 15
class HasLearnCB(Callback):
    def before_fit(self, learn): self.learn = learn 
    def after_fit(self, learn): self.learn = None

# %% ../nbs/12_callbacks.ipynb 17
class RecorderCB(Callback):
    """ Class to record specific items during training.  Examples
    of possible cases would be:
    
    RecorderCB(lr=lr_) where lr_ is a callable that will return from the 
    learner the value to be saved as lr
    
    In the above case lr_ could be as follows:
    
        def lr_(cb): cb.pg['lr']
        
    would then return the parameter group value for 'lr'.  The same could be done for 
    momentum...
    
    This reliess upon the way in which the learner is setup as self for callbacks
    
    """
    def __init__(self, **d): 
        """ Define parameters to track
        """
        self.d = d
        
    def before_fit(self, learn):
        # Create empty lists for each keyword
        self.recs = {k:[] for k in self.d}
        # Define the parameter group as the first one (it there are multiple the others
        # will be ignored at present)
        self.pg = learn.opt.param_groups[0]
    
    def after_batch(self, learn):
        """ Append values to be recorded afer each batch using the callable assiciated 
        with each keyword
        """
        if not learn.training: return
        for k,v in self.d.items():
            self.recs[k].append(v(self))

    def plot(self):
        for k,v in self.recs.items():
            plt.plot(v, label=k)
            plt.legend()
            plt.show()
