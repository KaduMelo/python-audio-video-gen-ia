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
                "voice_id": "2d5b0e6cf36f460aa7fc47e3eee4ba54"
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

video_id = "e393388f890443ee800d546dc5566f52"

video_status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
while True:
    response = requests.get(video_status_url, headers=headers)
    status = response.json()["data"]["status"]

    if status == "completed":
        video_url = response.json()["data"]["video_url"]
        thumbnail_url = response.json()["data"]["thumbnail_url"]
        print(
            f"Video generation completed! \nVideo URL: {video_url} \nThumbnail URL: {thumbnail_url}"
        )

        # Save the video to a file
        video_filename = "generated_video.mp4"
        with open(video_filename, "wb") as video_file:
            video_content = requests.get(video_url).content
            video_file.write(video_content)
        break
        
    elif status == "processing" or status == "pending":
        print("Video is still processing. Checking status...")
        time.sleep(5)  # Sleep for 5 seconds before checking again
        
    elif status == "failed":
        error = response.json()["data"]["error"]
        print(f"Video generation failed. '{error}'")
        break