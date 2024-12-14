from reazonspeech.k2.asr import load_model, transcribe, audio_from_path

audio = audio_from_path("JA_B00000_S00529_W000007.mp3")
model = load_model()
ret = transcribe(model, audio)
print(ret.text)
