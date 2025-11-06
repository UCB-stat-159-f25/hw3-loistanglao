from ligotools.readligo import loaddata
from ligotools.readligo import read_hdf5
import numpy as np

def test_loaddata():
    filename = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    strain, time, channel_dict = loaddata(filename)
    assert isinstance(strain, np.ndarray), "Strain should be a NumPy array"
    assert isinstance(time, np.ndarray), "Time should be a NumPy array"
    assert isinstance(channel_dict, dict), "Channel dict should be a dictionary"

def test_read_hdf5():
    filename = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = read_hdf5(filename)
    
    assert isinstance(strain, np.ndarray)
    assert gpsStart == 1126259446
    assert isinstance(ts, float)
    assert isinstance(qmask, np.ndarray)
    assert isinstance(shortnameList, list)
    assert isinstance(injmask, np.ndarray)
    assert isinstance(injnameList, list)