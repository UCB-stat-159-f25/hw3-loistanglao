from ligotools import read_frame
from ligotools import read_hdf5
import numpy as np

def test_read_frame():
    filename = 'hw3-loistanglao/data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    ifo = 'H1'
    assert read_frame(filename, ifo, readstrain=True, strain_chan=None, dq_chan=None, inj_chan=None) == ...

def test_read_hdf5():
    filename = 'hw3-loistanglao/data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = read_hdf5(filename)
    assert isinstance(strain, np.ndarray)
    assert gpsStart == 1126259446