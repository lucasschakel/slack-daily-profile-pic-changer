import os
import random
import requests
from PIL import Image

def main():
    image_dir = './profile-pictures/'
    images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    image_path = random.choice(images)

    headers = {
        "Authorization": f"Bearer {os.environ['SLACK_OAUTH_TOKEN']}"
    }

    with open(image_path, 'rb') as f:
        files = {'image': f}
        response = requests.post('https://slack.com/api/users.setPhoto', headers=headers, files=files)
        print(response.text)

if __name__ == "__main__":
    main()
