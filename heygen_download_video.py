import requests
import os
import time


def download_video(video_id: str, name: str):

    print(f"Nome: {name} ------> {video_id}")

    video_status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"

    headers = {  
        "accept": "application/json",  
        "content-type": "application/json",  
        "x-api-key": os.getenv("HEYGEN_API_KEY"),  
    }

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
            file_name = "{}/{}.{}".format("videos", name, "mp4")
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            with open(file_name, "wb") as video_file:
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