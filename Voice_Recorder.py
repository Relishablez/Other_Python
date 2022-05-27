import pyaudio
import wave
import datetime

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

try:
	while True:
		data = stream.read(1024)
		frames.append(data)
except KeyboardInterrupt:
	pass

stream.stop_stream()
stream.close()
audio.terminate()

today = datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S %p")
#"{:%Y-%m-%d_%H:%M:%S}".format(datetime.datetime.today()) :%Y-%m-%d_%H:%M:%S
filename = str(today) + ".wav"
print("New audio file created: " + filename)
sound_file = wave.open(f"Audio_Files/{filename}", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()
