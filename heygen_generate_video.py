import requests
import os

url = "https://api.heygen.com/v2/video/generate"

headers = {  
    "accept": "application/json",  
    "content-type": "application/json",  
    "x-api-key": os.getenv("HEYGEN_API_KEY"),  
}

def generate_video(text: str):

    data = {  
        "video_inputs": [
            {  
                "character": {  
                    "type": "avatar",
                    "avatar_id": os.getenv("AVATAR_ID_HEYGEN"),
                    "avatar_style": "normal",  
                },  
                "voice": {
                    "type": "text",
                    "input_text": text,
                    "voice_id": os.getenv("VOICE_ID_HEYGEN"),
                    "language": "Portuguese (Brazil)",
                    "speed": 0.9
                },
                "background": {
                    "type": "color",
                    "value": "#008000"
                }
            }  
        ],
        "aspect_ratio": "16:9",  
        "dimension": {
            "width": 1280,
            "height": 720
        },
    }

    res = requests.post(url, headers=headers, json=data)

    print(f"Resultado: {res.json()}")
    return res.json()['data']['video_id']