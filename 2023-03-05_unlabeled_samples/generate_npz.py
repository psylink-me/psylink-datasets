#!/usr/bin/python
# Converts the raw data from GNURadio's File Sink into a more easily readable format, a numpy .npz file.
# The raw data file is not included here since it's large and redundant, but this script has been left as a reference.

import numpy as np

CHANNELS = 14  # (8 EMG channels, 3 gyroscope channels (x/y/z), 3 accelerometer channels (x/y/z)

samples = np.fromfile(open('recordings.bin', 'r'), dtype=np.float32)
total_samples = samples.shape[0]

assert total_samples % CHANNELS == 0, "Total number of samples (%d) is not divisible by the expected number of channels (%d), something must have gone wrong here" % (total_samples, CHANNELS)

frames = samples.reshape(int(total_samples / CHANNELS), CHANNELS)
np.savez_compressed('recordings.npz', frames)
