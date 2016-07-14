#!/usr/bin/python

from netCDF4 import Dataset   # for read nc file
import numpy as np		    # for numerical calculation: array average
import matplotlib.pyplot as plt     # for plotting
#from mpl_toolkits.basemap import Basemap, shiftgrid # for plotting on world map


path1 = '../data/sc0C.phys.nc'    # this string stores path name of nc file

root1 = Dataset(path1, mode='r')       # load the entire nc file
time = np.array(root1.variables['Time'][:])


print time
