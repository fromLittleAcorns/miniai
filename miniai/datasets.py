# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_datasets.ipynb.

# %% ../nbs/01_datasets.ipynb 2
from __future__ import annotations
import math,numpy as np,matplotlib.pyplot as plt
from operator import itemgetter
from itertools import zip_longest
import fastcore.all as fc

from torch.utils.data import default_collate

# %% auto 0
__all__ = ['inplace', 'collate_dict']

# %% ../nbs/01_datasets.ipynb 22
def inplace(f):
    """ This function allows a function that does not return anything directly (ie one that modifies things
    without a return statenent) to then be used in an application that required a return.  So this function
    is a wrapper of another function that simply executes the function and then returns the modified input
    """
    def _f(b):
        f(b)
        return b
    return _f

# %% ../nbs/01_datasets.ipynb 26
def collate_dict(ds):
    """ when a dataset is defined by a dictionary this will identify the features and split into inputs and outputs
    as tensor arrays ready for input to a model
    """
    get = itemgetter(*ds.features)
    def _f(b):
        """ return a tuple containing the values associated with each of the keys returned by the itemgetter 
        given that default_collate return a dict with two keys and a stacked tensor for each """
        return get(default_collate(b))
    return _f