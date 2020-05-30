import bt_helpers
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../api-keys.json"

print("iniciando transcrição...")
# result = bt_helpers.long_audio_transcript('gs://bt-speech-transcriber/mav.mp3', language_code='pt-BR')
result = bt_helpers.short_audio_transcript('gs://bt-speech-transcriber/example.mp3', language_code='pt-BR')

file = open('../results/output_2.txt', 'w')
file.write(result)