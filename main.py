import pandas as pd
from elevenlabs_audio import generate_mp3

df = pd.read_csv('textos.csv')

for index, row in df.iterrows():
    print(row['Texto'])
    generate_mp3(row['Texto'], "teste.mp3")