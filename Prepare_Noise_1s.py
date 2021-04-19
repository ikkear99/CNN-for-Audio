# Cắt từng đoạn 1s từ 1 file data dài vài phút và lưu dưới dạng WAV

from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("_background_noise_data\im-lặng-2.wav" , "wav") 
chunk_length_ms = 1000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = "BackGr_Noise_setG{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")