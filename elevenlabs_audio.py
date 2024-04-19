import os
from elevenlabs import Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key=os.getenv("ELEVEN_API_KEY"), # Defaults to ELEVEN_API_KEY
)

def generate_mp3(text: str, filename: str):
    audio = client.generate(
             text=text,
             model="eleven_multilingual_v2",
             voice=Voice(
                 settings=VoiceSettings(
                     stability=0.50,
                     similarity_boost=0.50,
                     style=0.50
                 ),
                 voice_id=os.getenv("VOICE_ID")
             ))

    save(audio, filename)