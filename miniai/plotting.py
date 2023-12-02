# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_plotting.ipynb.

# %% ../nbs/02_plotting.ipynb 2
from __future__ import annotations
import pickle,gzip,math,os,time,shutil,torch,matplotlib as mpl,numpy as np,matplotlib.pyplot as plt
from pathlib import Path
from operator import itemgetter
from itertools import zip_longest
import fastcore.all as fc

from torch import tensor,nn,optim
from torch.utils.data import DataLoader,default_collate
import torch.nn.functional as F
import torchvision.transforms.functional as TF

from datasets import load_dataset,load_dataset_builder
from matplotlib.pyplot import axes as ax

from typing import List

# %% auto 0
__all__ = ['show_image', 'subplots', 'get_grid', 'show_images']

# %% ../nbs/02_plotting.ipynb 7
@fc.delegates(plt.Axes.imshow)
def show_image(img, ax=None, title=None, noframe=True, figsize=None, **kwargs):
    # prepare images.  Check if pytorch tensor by using attributes
    if fc.hasattrs(img, ('cpu', 'permute', 'detach')):
        img = img.detach().cpu()
        if len(img.shape)==3 and img.shape[0]<8:
            img = img.permute(1,2,0)
        elif not isinstance(img, np.ndarray):
            img = np.asarray(img)
    # If only one channel remove the dimension
    if img.shape[-1] == 1:
        img = img[...,0]
    # if axes do not exist then create them
    if ax is None: _,ax = plt.subplots(figsize=figsize)
    # plot the array
    ax.imshow(img, **kwargs)
    # Add a title
    if title is not None: ax.set_title(title)
    # turn off tick marks
    ax.set_xticks([])
    ax.set_yticks([])
    # Finally set whether or not to show a frame
    if noframe:
        ax.axis('off')
    return ax

# %% ../nbs/02_plotting.ipynb 26
@fc.delegates(plt.subplots, keep=True)
def subplots(
    nrows: int=1, # Number of rows
    ncols: int=1, # Number of columns
    figsize: tuple=None, #Size of overall figure that will be produced in default units
    imsize: float=3, # size of individual images in default units
    suptitle: str=None, # Title for the plot
    **kwargs
    ) -> (plt.Figure, plt.Axes):
    """ create grid of axes ready for assignment of images to each axis
        Args:
            nrows (int): number of rows
            ncols (int): number of columns
            figsize (Tuple[float, float]): Size of overall figure that will be produced in default units
            imsize (float): size of individual images in default units
            suptitle (Union[str, None]): title for the overall figure
    
        Returns:
            fig: plt.Figure
            ax: np.array(plt.Axes)
    """
    # calculate fig size if not supplied
    if figsize is None:
        figsize = (ncols*imsize, nrows*imsize)
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, **kwargs)
    if suptitle is not None: fig.suptitle(suptitle)

    # If only one axes then turn into a array to allow consistent processing (multiple axes are stored as arrays)
    if ncols*nrows==1: ax=array([ax])
    return fig, ax 

# %% ../nbs/02_plotting.ipynb 31
@fc.delegates(subplots)
def get_grid(
    n: int, # Number of axes
    nrows: int=None, # Number of rows
    ncols: int=None, # Number of columns
    #title: str=None, # Plot title, optional
    weight: str='bold', # Weight to apply to the title
    size: int=14, # size of the title font
    **kwargs
    
):
    # "Return a grid of n axes over a combination of rows and columns."
    # If the rows are specified then ncols will be used if specified but if not then the columns needed
    # will be calculated.  Note that "or" will return the first value unless it is None, when it returns 
    # the second
    if nrows: ncols = ncols or int(np.ceil(n/nrows))
    elif ncols: nrows = int(np.ceil(n/ncols))
    else:
        nrows = int(np.ceil(math.sqrt(n)))
        ncols = int(np.ceil(n/nrows))
        
    # Avoid passing cmap to subplots
    _ = kwargs.pop('cmap', None)
    # Avoid passing suptitle to subplots
    suptitle = kwargs.pop('suptitle', None) if 'suptitle' in kwargs.keys() else None
    fig, axs = subplots(nrows, ncols, **kwargs)
    # Turn of the display of axis where there are no images (ie where there are unused positions on the grid)
    for i in range(n, nrows*ncols): axs.flat[i].set_axis_off()
    # Add the overall plot title if necessary
    if suptitle is not None:
        fig.suptitle(suptitle, weight=weight, size=size)
    return fig, axs

# %% ../nbs/02_plotting.ipynb 34
@fc.delegates(subplots)
def show_images(
    imgs: list, # List of images to show
    nrows: int=1, # Number of rows
    ncols: int=None, # Number of columns
    titles: List[str]=None, # list of individual sub-plot headings
    #suptitle: str=None, # Plot title, optional, list of titles for each image
    **kwargs
):
    # Create a grid of axes ready to plot the images
    axs = get_grid(len(imgs), **kwargs)[1].flat
    # Remove unwanted kwargs that are used by get_grid but not needed by show_image
    _ = kwargs.pop('imsize', None)
    _ = kwargs.pop('suptitle', None)
    # plot images and individual labels
    for img, t, ax in zip_longest(imgs, titles or [], axs[:len(imgs)]):
        show_image(img, ax, t, **kwargs)
