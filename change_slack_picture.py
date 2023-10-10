import os
import random
import requests
from PIL import Image

def main():
    # Change the directory path accordingly
    image_dir = './profile-pictures/'
    images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    image_path = random.choice(images)

    # The headers now only contain the Authorization. The content type will be determined automatically by `requests` 
    # when using the files parameter.
    headers = {
        "Authorization": f"Bearer {os.environ['SLACK_OAUTH_TOKEN']}"
    }

    # The files dictionary is used to send the image as multipart/form-data.
    with open(image_path, 'rb') as f:
        files = {'image': f}
        response = requests.post('https://slack.com/api/users.setPhoto', headers=headers, files=files)
        print(response.text)

if __name__ == "__main__":
    main()
