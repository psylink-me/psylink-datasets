# Spelling Out "hello" 

This data set is a recording of various arm movements, including 4 gestures which were labeled by pressing a certain key on the keyboard at the same time as performing the gestures.  The 4 gestures represent a letter.  The letters were "h", "e", "l", and "o", with the intention to spell out "hello" with the gestures later.  [This video](https://peertube.linuxrocks.online/w/7BzhGuUMBKbzDHTddJaCy4) shows the recording process.  From minute 7 on, it shows how a neural network trained on this data set predicts the letters, along with a successful attempt to spell out "hello", although the results are not perfect.

- Date: 2023-03-05
- Format:
    - Signals: Python Numpy file, Compressed NPZ
    - Labels: JSON array
    - Label order: JSON array (used for loading pretrained PsyLink neural network models)
- PsyLink Version: [P9.2](https://psylink.me/p9.2)
- Arduino Firmware: [AnalogToBLE 1.1](https://psylink.me/sabt1.1/) [(source code)](https://codeberg.org/psylink/psylink/src/commit/6fcf7106994c005129073e6d00aa8bab947311f1/arduino/AnalogToBLE1.1/AnalogToBLE1.1.ino)
- Recorded with [PsyLink UI](https://psylink.me/s3)
- Video of sample recording [on PeerTube](https://peertube.linuxrocks.online/w/7BzhGuUMBKbzDHTddJaCy4)
- Sample Rate: 500Hz
    - EMG data is updated every tick
    - IMU data (gyroscope, accelerometer) is updated approx. every 25th tick
- Channels: 14
    - 8 EMG Channels
        - 1-4: underside of the forearm
        - 5-8: upside of the forearm
    - 3 Gyroscope Channels (X, Y, Z)
    - 3 Accelerometer Channels (X, Y, Z)
- Samples: 201275 x 250 x 14
    - Values between 0 and 255
    - 201275 time steps
    - Each time step includes 250 EMG/IMU datasets with 14 channels each
        - The last of the 250 data sets are the most recent signals
        - The data sets before that are historical signals which are shifted to the left each time a new signal comes in, forming a Toeplitz matrix
        - Occasionally, bluetooth packets are dropped, causing a reset of the buffer of historical signals, and therefore a discontinuity in the Toeplitz matrix
- Load these recorded samples into [PsyLink UI](https://psylink.me/s3) by copying this folder to `psylink/python/save_default`, running `ui.py`, and clicking "File" -> "Load recorded samples"

See [load_signals.py](load_signals.py) for a sample script on how to work with these samples.

[Data Sample:](load_signals.py)

```
Tick: 20052
Label: ""
EMG0: 115 116 119 119 120 117 119 121 118 120
EMG1: 144 144 143 145 143 144 144 144 144 145
EMG2: 207 205 206 207 207 206 207 208 208 208
EMG3: 105 104 105 103 107 105 104 105 105 105
EMG4: 129 127 128 127 125 126 126 130 125 126
EMG5: 116 116 115 116 116 116 116 116 115 115
EMG6: 116 119 120 118 119 118 120 117 118 118
EMG7: 170 169 168 169 171 168 170 172 174 172
GyrX: 130 130 130 130 130 130 130 130 123 123
GyrY: 123 123 123 123 123 123 123 123 122 122
GyrZ: 124 124 124 124 124 124 124 124 126 126
AccX: 113 113 113 113 113 113 113 113 128 128
AccY:  81  81  81  81  81  81  81  81  77  77
AccZ: 244 244 244 244 244 244 244 244 237 237

Tick: 20053
Label: ""
EMG0: 116 119 119 120 117 119 121 118 120 120
EMG1: 144 143 145 143 144 144 144 144 145 145
EMG2: 205 206 207 207 206 207 208 208 208 206
EMG3: 104 105 103 107 105 104 105 105 105 105
EMG4: 127 128 127 125 126 126 130 125 126 129
EMG5: 116 115 116 116 116 116 116 115 115 116
EMG6: 119 120 118 119 118 120 117 118 118 116
EMG7: 169 168 169 171 168 170 172 174 172 181
GyrX: 130 130 130 130 130 130 130 123 123 123
GyrY: 123 123 123 123 123 123 123 122 122 122
GyrZ: 124 124 124 124 124 124 124 126 126 126
AccX: 113 113 113 113 113 113 113 128 128 128
AccY:  81  81  81  81  81  81  81  77  77  77
AccZ: 244 244 244 244 244 244 244 237 237 237

Tick: 20054
Label: "e"
EMG0: 119 119 120 117 119 121 118 120 120 120
EMG1: 143 145 143 144 144 144 144 145 145 143
EMG2: 206 207 207 206 207 208 208 208 206 206
EMG3: 105 103 107 105 104 105 105 105 105 103
EMG4: 128 127 125 126 126 130 125 126 129 125
EMG5: 115 116 116 116 116 116 115 115 116 117
EMG6: 120 118 119 118 120 117 118 118 116 118
EMG7: 168 169 171 168 170 172 174 172 181 172
GyrX: 130 130 130 130 130 130 123 123 123 123
GyrY: 123 123 123 123 123 123 122 122 122 122
GyrZ: 124 124 124 124 124 124 126 126 126 126
AccX: 113 113 113 113 113 113 128 128 128 128
AccY:  81  81  81  81  81  81  77  77  77  77
AccZ: 244 244 244 244 244 244 237 237 237 237
```
