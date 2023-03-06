# Unlabeled Samples

![gnuradio screenshot](gnuradio_screenshot.png)

- Date: 2023-03-05
- Format: Python Numpy file, Compressed NPZ
- PsyLink Version: [P9.2](https://psylink.me/p9.2)
- Arduino Firmware: [AnalogToBLE 1.1](https://psylink.me/sabt1.1/) [(source code)](https://codeberg.org/psylink/psylink/src/commit/6fcf7106994c005129073e6d00aa8bab947311f1/arduino/AnalogToBLE1.1/AnalogToBLE1.1.ino)
- Recorded with ["plot_signals_and_record.grc"](https://codeberg.org/psylink/psylink/src/commit/6fcf7106994c005129073e6d00aa8bab947311f1/gnuradio/prototype9/plot_signals_and_record.grc) GNURadio script, see screenshot
- Video of sample recording [on PeerTube](https://peertube.linuxrocks.online/w/w9iEcUuub2hAPasKWwjnUd)
- Sample Rate: 500Hz
- Channels: 14
    - 8 EMG Channels
        - 1-4: underside of the forearm
        - 5-8: upside of the forearm
    - 3 Gyroscope Channels (X, Y, Z)
    - 3 Accelerometer Channels (X, Y, Z)
- Samples: 116975 x 14
    - Originally, values between 0 and 255
    - Normalized to floats between 0.0 and 1.0 (by dividing by 256)
    - Steps between possible sample values: 0.00390625 (=1/256)

See [load_recordings.py](load_recordings.py) for a sample script on how to work with these samples.
