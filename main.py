import pandas as pd
import unidecode
from elevenlabs_audio import generate_mp3
from heygen_generate_video import generate_video
from heygen_download_video import download_video 
import os

path_file = os.getenv("PATH_FILE")
df = pd.read_excel(path_file, usecols='B')

if not os.path.exists('audios'):
   os.makedirs('audios')

for text in df['texto'].values.tolist():
   name = unidecode.unidecode(text.split(',')[0].lower())
   print(name)
   # generate_mp3(text, name)
   video_id = generate_video(text)
   # video_id = ''
   download_video(video_id, name)