# Những tiền xử lý với audio.

import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import librosa
import IPython.display as ipd

# load data #thực hiện load dữ liệu:
audio_data='E:\Edge.AI_Project\SmartRoom_Action_Keyword\wav_tests\compyter.wav'
signal, sr = librosa.load(audio_data,sr=22050)      #tần số lấy mẫu là 22050Hz
print('signal : ',len(signal), type(signal))
print('sr : ',sr ,type(sr))
librosa.load(audio_data, sr=22050)
ipd.Audio(audio_data)


# waveform in time domain     #dạng sóng ở miền thời gian:
plt.figure(figsize=(15,5))
librosa.display.waveplot(signal,sr=sr)
plt.title('Miền thời gian', size=20)
plt.xlabel("thời gian", size = 15)
plt.ylabel("biên độ", size = 15)
plt.show()


# waveform in the frequency domain    #dạng sóng ở miền tần số:
# perform Fourier transform     #thực hiện biến đổi fourier
fft = np.fft.fft(signal)
magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

left_frequency = frequency[:int(len(frequency)/2)]
left_magnitude = magnitude[:int(len(frequency)/2)] 
plt.plot(left_frequency,left_magnitude)
# (hoặc) plt.plot(np.abs(fft)/np.sum(np.abs(fft)))  

plt.title('Miền tần số', size=20)
plt.grid(False)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.ylabel('Cường độ (norm)', size=15)
plt.xlabel('Tần số (hertz)', size=15)
plt.show()


# FFT -> power spectrum     #quang phổ của tín hiệu:
n_fft = 2048
hop_length = 512

stft = librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)
spectrogram = np.abs(stft)

log_spectrogram = librosa.amplitude_to_db(spectrogram)
librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()
plt.show()


#MFCCs     #phổ MFCCs:
MFCCs = librosa.feature.mfcc(signal, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)
librosa.display.specshow(MFCCs, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCCs")
plt.colorbar()
plt.show()
print(MFCCs)

