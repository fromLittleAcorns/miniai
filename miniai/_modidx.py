# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/miniai',
                'doc_host': 'https://fromLittleAcorns.github.io',
                'git_url': 'https://github.com/fromLittleAcorns/miniai',
                'lib_path': 'miniai'},
  'syms': { 'miniai.core': { 'miniai.core.foo': ('core.html#foo', 'miniai/core.py'),
                             'miniai.core.say_hello': ('core.html#say_hello', 'miniai/core.py')},
            'miniai.datasets': { 'miniai.datasets.DataLoaders': ('datasets.html#dataloaders', 'miniai/datasets.py'),
                                 'miniai.datasets.DataLoaders.__init__': ('datasets.html#dataloaders.__init__', 'miniai/datasets.py'),
                                 'miniai.datasets.DataLoaders.from_dd': ('datasets.html#dataloaders.from_dd', 'miniai/datasets.py'),
                                 'miniai.datasets.collate_dict': ('datasets.html#collate_dict', 'miniai/datasets.py'),
                                 'miniai.datasets.get_dls': ('datasets.html#get_dls', 'miniai/datasets.py'),
                                 'miniai.datasets.inplace': ('datasets.html#inplace', 'miniai/datasets.py')},
            'miniai.learner': { 'miniai.learner.Callback': ('learner.html#callback', 'miniai/learner.py'),
                                'miniai.learner.CancelBatchException': ('learner.html#cancelbatchexception', 'miniai/learner.py'),
                                'miniai.learner.CancelEpochException': ('learner.html#cancelepochexception', 'miniai/learner.py'),
                                'miniai.learner.CancelFitException': ('learner.html#cancelfitexception', 'miniai/learner.py'),
                                'miniai.learner.DeviceCB': ('learner.html#devicecb', 'miniai/learner.py'),
                                'miniai.learner.DeviceCB.__init__': ('learner.html#devicecb.__init__', 'miniai/learner.py'),
                                'miniai.learner.DeviceCB.before_batch': ('learner.html#devicecb.before_batch', 'miniai/learner.py'),
                                'miniai.learner.DeviceCB.before_fit': ('learner.html#devicecb.before_fit', 'miniai/learner.py'),
                                'miniai.learner.LRFinderCB': ('learner.html#lrfindercb', 'miniai/learner.py'),
                                'miniai.learner.LRFinderCB.__init__': ('learner.html#lrfindercb.__init__', 'miniai/learner.py'),
                                'miniai.learner.LRFinderCB.after_batch': ('learner.html#lrfindercb.after_batch', 'miniai/learner.py'),
                                'miniai.learner.LRFinderCB.before_fit': ('learner.html#lrfindercb.before_fit', 'miniai/learner.py'),
                                'miniai.learner.LRFinderCB.cleanup_fit': ('learner.html#lrfindercb.cleanup_fit', 'miniai/learner.py'),
                                'miniai.learner.Learner': ('learner.html#learner', 'miniai/learner.py'),
                                'miniai.learner.Learner.__getattr__': ('learner.html#learner.__getattr__', 'miniai/learner.py'),
                                'miniai.learner.Learner.__init__': ('learner.html#learner.__init__', 'miniai/learner.py'),
                                'miniai.learner.Learner._fit': ('learner.html#learner._fit', 'miniai/learner.py'),
                                'miniai.learner.Learner._one_batch': ('learner.html#learner._one_batch', 'miniai/learner.py'),
                                'miniai.learner.Learner._one_epoch': ('learner.html#learner._one_epoch', 'miniai/learner.py'),
                                'miniai.learner.Learner.callback': ('learner.html#learner.callback', 'miniai/learner.py'),
                                'miniai.learner.Learner.fit': ('learner.html#learner.fit', 'miniai/learner.py'),
                                'miniai.learner.Learner.one_epoch': ('learner.html#learner.one_epoch', 'miniai/learner.py'),
                                'miniai.learner.Learner.training': ('learner.html#learner.training', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB': ('learner.html#metricscb', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.__init__': ('learner.html#metricscb.__init__', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB._log': ('learner.html#metricscb._log', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.after_batch': ('learner.html#metricscb.after_batch', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.after_epoch': ('learner.html#metricscb.after_epoch', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.before_epoch': ('learner.html#metricscb.before_epoch', 'miniai/learner.py'),
                                'miniai.learner.MetricsCB.before_fit': ('learner.html#metricscb.before_fit', 'miniai/learner.py'),
                                'miniai.learner.MomentumLearner': ('learner.html#momentumlearner', 'miniai/learner.py'),
                                'miniai.learner.MomentumLearner.__init__': ('learner.html#momentumlearner.__init__', 'miniai/learner.py'),
                                'miniai.learner.MomentumLearner.zero_grad': ('learner.html#momentumlearner.zero_grad', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB': ('learner.html#progresscb', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.__init__': ('learner.html#progresscb.__init__', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB._log': ('learner.html#progresscb._log', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.after_batch': ('learner.html#progresscb.after_batch', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.after_epoch': ('learner.html#progresscb.after_epoch', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.before_epoch': ('learner.html#progresscb.before_epoch', 'miniai/learner.py'),
                                'miniai.learner.ProgressCB.before_fit': ('learner.html#progresscb.before_fit', 'miniai/learner.py'),
                                'miniai.learner.SingleBatchCB': ('learner.html#singlebatchcb', 'miniai/learner.py'),
                                'miniai.learner.SingleBatchCB.after_batch': ('learner.html#singlebatchcb.after_batch', 'miniai/learner.py'),
                                'miniai.learner.TrainCB': ('learner.html#traincb', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.__init__': ('learner.html#traincb.__init__', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.backward': ('learner.html#traincb.backward', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.get_loss': ('learner.html#traincb.get_loss', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.predict': ('learner.html#traincb.predict', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.step': ('learner.html#traincb.step', 'miniai/learner.py'),
                                'miniai.learner.TrainCB.zero_grad': ('learner.html#traincb.zero_grad', 'miniai/learner.py'),
                                'miniai.learner.TrainLearner': ('learner.html#trainlearner', 'miniai/learner.py'),
                                'miniai.learner.TrainLearner.backward': ('learner.html#trainlearner.backward', 'miniai/learner.py'),
                                'miniai.learner.TrainLearner.get_loss': ('learner.html#trainlearner.get_loss', 'miniai/learner.py'),
                                'miniai.learner.TrainLearner.predict': ('learner.html#trainlearner.predict', 'miniai/learner.py'),
                                'miniai.learner.TrainLearner.step': ('learner.html#trainlearner.step', 'miniai/learner.py'),
                                'miniai.learner.TrainLearner.zero_grad': ('learner.html#trainlearner.zero_grad', 'miniai/learner.py'),
                                'miniai.learner.lr_find': ('learner.html#lr_find', 'miniai/learner.py'),
                                'miniai.learner.run_cbs': ('learner.html#run_cbs', 'miniai/learner.py'),
                                'miniai.learner.with_cbs': ('learner.html#with_cbs', 'miniai/learner.py'),
                                'miniai.learner.with_cbs.__call__': ('learner.html#with_cbs.__call__', 'miniai/learner.py'),
                                'miniai.learner.with_cbs.__init__': ('learner.html#with_cbs.__init__', 'miniai/learner.py')},
            'miniai.model_blocks': { 'miniai.model_blocks.DownBlock': ('model_blocks.html#downblock', 'miniai/model_blocks.py'),
                                     'miniai.model_blocks.DownBlock.__init__': ( 'model_blocks.html#downblock.__init__',
                                                                                 'miniai/model_blocks.py'),
                                     'miniai.model_blocks.DownBlock.forward': ( 'model_blocks.html#downblock.forward',
                                                                                'miniai/model_blocks.py'),
                                     'miniai.model_blocks.EmbUNetModel': ('model_blocks.html#embunetmodel', 'miniai/model_blocks.py'),
                                     'miniai.model_blocks.EmbUNetModel.__init__': ( 'model_blocks.html#embunetmodel.__init__',
                                                                                    'miniai/model_blocks.py'),
                                     'miniai.model_blocks.EmbUNetModel.forward': ( 'model_blocks.html#embunetmodel.forward',
                                                                                   'miniai/model_blocks.py'),
                                     'miniai.model_blocks.UpBlock': ('model_blocks.html#upblock', 'miniai/model_blocks.py'),
                                     'miniai.model_blocks.UpBlock.__init__': ( 'model_blocks.html#upblock.__init__',
                                                                               'miniai/model_blocks.py'),
                                     'miniai.model_blocks.UpBlock.forward': ('model_blocks.html#upblock.forward', 'miniai/model_blocks.py'),
                                     'miniai.model_blocks._conv_block': ('model_blocks.html#_conv_block', 'miniai/model_blocks.py'),
                                     'miniai.model_blocks.conv': ('model_blocks.html#conv', 'miniai/model_blocks.py'),
                                     'miniai.model_blocks.saved': ('model_blocks.html#saved', 'miniai/model_blocks.py')},
            'miniai.plotting': { 'miniai.plotting.get_grid': ('plotting.html#get_grid', 'miniai/plotting.py'),
                                 'miniai.plotting.show_image': ('plotting.html#show_image', 'miniai/plotting.py'),
                                 'miniai.plotting.show_images': ('plotting.html#show_images', 'miniai/plotting.py'),
                                 'miniai.plotting.subplots': ('plotting.html#subplots', 'miniai/plotting.py')},
            'miniai.utils': { 'miniai.utils.collate_device': ('utils.html#collate_device', 'miniai/utils.py'),
                              'miniai.utils.set_seed': ('utils.html#set_seed', 'miniai/utils.py'),
                              'miniai.utils.to_cpu': ('utils.html#to_cpu', 'miniai/utils.py'),
                              'miniai.utils.to_device': ('utils.html#to_device', 'miniai/utils.py')}}}
