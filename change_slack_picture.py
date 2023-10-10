import os
import random
import requests
from PIL import Image

def main():
    # Change the directory path accordingly
    image_dir = './profile-pictures/'
    images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    image_path = random.choice(images)

    with open(image_path, 'rb') as f:
        image_content = f.read()

    headers = {
        "Authorization": f"Bearer {os.environ['SLACK_OAUTH_TOKEN']}",
        "Content-Type": "application/json; charset=utf-8"
    }

    payload = {
        "image": image_content
    }

    response = requests.post('https://slack.com/api/users.setPhoto', headers=headers, data=payload)
    print(response.text)

if __name__ == "__main__":
    main()
