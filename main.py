import pandas as pd
from elevenlabs_audio import generate_mp3
import os

df = pd.read_csv('textos.csv')

if not os.path.exists('audios'):
   os.makedirs('audios')

for index, row in df.iterrows():
    print(row['Texto'])
    generate_mp3(row['Texto'], "audios/teste.wav")