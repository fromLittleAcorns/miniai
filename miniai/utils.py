# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_utils.ipynb.

# %% auto 0
__all__ = ['def_device', 'to_device', 'collate_device', 'to_cpu', 'set_seed']

# %% ../nbs/03_utils.ipynb 2
import random
import numpy as np
import torch
from torch import nn

from torch.utils.data import default_collate
from typing import Mapping
import fastcore.test as fct

# %% ../nbs/03_utils.ipynb 3
def_device = 'mps' if torch.backends.mps.is_available() else 'cuda' if torch.cuda.is_available() else 'cpu'

def to_device(x, device=def_device):
    if isinstance(x, torch.Tensor): return x.to(device)
    if isinstance(x, Mapping): return {k:v.to(device) for k,v in x.items()}
    return type(x)(to_device(o, device) for o in x)

def collate_device(b): return to_device(default_collate(b))

# %% ../nbs/03_utils.ipynb 4
def to_cpu(x):
    """recursively move items to the cpu.  Works with tuples, lists or dictionaries 
    of tensors. As well as moving to the cpu detaches the tensor.  If the tensor is 16 bit then
    returns a standard float tensor
    """
    # Iterate through a dictionary
    if isinstance(x, Mapping): return {k:to_cpu(v) for k,v in x.items()}
    # Iteratively move all items in a list into a new list
    if isinstance(x, list): return [to_cpu(o) for o in x]
    # Convert a tuple by first converting to a list and then re-creating after moving
    if isinstance(x, tuple): return tuple(to_cpu(list(x)))
    try:
        res = x.detach().cpu()
    except: raise AttributeError("Attempting to convert item without detach method: {type(x)}")
    return res.float() if res.dtype==torch.float16 else res

# %% ../nbs/03_utils.ipynb 11
def set_seed(seed: int, deterministic:bool=False):
    """ Sets the seeds for torch, random and numpy.  If the deterministic flag is set torch will 
    attempt to use deterministic algorithms, if these are not available an error will be raised
    """
    torch.use_deterministic_algorithms(deterministic)
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
