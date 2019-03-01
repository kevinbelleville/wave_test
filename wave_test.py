import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

file = 'test.wav'

test_range = 10000000//2

with wave.open(file) as wav_file:
	params = wav_file.getparams()
	framerate = params[2]
	total_frames = params[3]
	nchannels = params[0]
	sampwidth = params[1]
	frames = wav_file.readframes(test_range)

print(params)

a = struct.unpack("h"*test_range*2, frames)


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


_ = np.array(value_list)
yf = np.fft.fft(_)
xf_space = len(yf)/32000
xf = np.linspace(0, 32000, len(yf)//2)

N = len(yf)
yf = 2.0/N * np.abs(yf[:N//2])

# let's try cutting between f = 100 and f = 1000
start_100 = 0
end_1000 = 0
for i in range(len(xf)):
	if xf[i] > 100:
		start_100 = xf.item(i)
for i in range(len(xf)):
	if xf[i] > 1000:
		end_1000 = xf.item(i)

# for f in xf:
# 	if f > 100:
# 		start_100 = f
# 		break
# for f in xf:
# 	if f > 1000:
# 		end_1000 = f

new_xf = xf[start_100:end_1000]
new_yf = yf[start_100:end_1000]




plt.plot(new_xf, new_yf)
plt.show()




# yf = np.fft.fft(value_list)
# xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# # plt.plot(x, y)
# plt.show()

# print(test)
# plt.plot(time_list, value_list, "r-")
# plt.show()
