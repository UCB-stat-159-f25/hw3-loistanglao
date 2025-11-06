from ligotools.utils import whiten
from ligotools.utils import write_wavfile
import numpy as np
from scipy.io import wavfile
import os

def test_whiten_output_length():
    # Test that output has same length as input
    strain = np.random.randn(1000)
    dt = 1/4096
    interp_psd = lambda f: np.ones_like(f)  # flat PSD
    
    result = whiten(strain, interp_psd, dt)
    assert len(result) == len(strain)

def test_write_wavfile_correct_sample_rate():
    # Test that WAV file has correct sample rate
    data = np.random.randn(1000)
    fs = 44100
    filename = 'test_sr.wav'
    
    write_wavfile(filename, fs, data)
    
    fs_read, data_read = wavfile.read('audio/' + filename)
    assert fs_read == fs
    os.remove('audio/' + filename)