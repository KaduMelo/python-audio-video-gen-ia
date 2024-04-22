import requests
import os

url = "https://api.heygen.com/v2/video/generate"

headers = {  
    "accept": "application/json",  
    "content-type": "application/json",  
    "x-api-key": os.getenv("HEYGEN_API_KEY"),  
}

data = {  
    "video_inputs": [  
        {  
            "character": {  
                "type": "avatar",  
                "avatar_id": "Daisy-inskirt-20220818",
                "avatar_style": "normal",  
            },  
            "voice": {
                "type": "text",
                "input_text": "Welcome to the HeyGen API",
                "voice_id": "2d5b0e6cf36f460aa7fc47e3eee4b54"
            },
            "background": {
                "type": "color",
                "value": "#008000"
            }
        }  
    ],  
    "test": True,  
    "aspect_ratio": "16:9",  
    "dimension": {
        "width": 1280,
        "height": 720
    },  
}

res = requests.post(url, headers=headers, json=data)

print(res.json())