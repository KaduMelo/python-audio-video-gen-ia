import pandas as pd
import unidecode
from elevenlabs_audio import generate_mp3
import os

path_file = os.getenv("PATH_FILE")
df = pd.read_excel(path_file, usecols='B')

if not os.path.exists('audios'):
   os.makedirs('audios')

for text in df['texto'].values.tolist():
   name = unidecode.unidecode(text.split(',')[0].lower())
   file_name = "{}/{}.{}".format("audios", name, "wav")
   print(file_name)
   generate_mp3(text, file_name)