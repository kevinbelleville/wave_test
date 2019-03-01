import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

file = 'test.wav'

test_range = 1000000

with wave.open(file) as wav_file:
	params = wav_file.getparams()
	framerate = params[2]
	total_frames = params[3]
	nchannels = params[0]
	sampwidth = params[1]
	frames = wav_file.readframes(test_range)


print(params)

a = struct.unpack("i"*test_range, frames)

# generate value list
value_list = []
for i in range(len(a)):
	if a[i] >= 0:
		value_list.append(a[i])


# let's generate the time
time_step = 1/framerate
time_list = []
time = 0
for i in range(len(value_list)):
	time += time_step
	time_list.append(time)



plt.plot(time_list, value_list, "r*")
plt.show()
