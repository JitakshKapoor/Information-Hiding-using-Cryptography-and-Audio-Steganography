from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
input_data = read("song.wav")
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title
plt.title("Plot of Original Song")
# display the plot
plt.show()