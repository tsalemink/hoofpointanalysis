'''
MAP Client Plugin
'''

__version__ = '0.1.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Hoof Point Analysis'
__location__ = ''

# import class that derives itself from the step mountpoint.
from mapclientplugins.hoofpointanalysisstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
