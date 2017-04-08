import re
import requests

# Configurations
ENDPOINT = "http://www.bing.com/HPImageArchive.aspx"
DIRECTORY = "/home/suresh/Pictures/bing/"
VALID_FILENAME = regex = re.compile('[^- ,a-zA-Z0-9]')
MARKET = 'en-IN'

# Helper Methods
def get_api_response(count=1, market=MARKET):
    params = dict(
        format='js',  # Response format
        idx=0,  # Offset from today
        n=1,  # Number of images in history
        mkt=market  # Market
    )
    api_response = requests.get(ENDPOINT, params=params)
    if api_response.status_code == 200:
        return api_response.json()
    raise RuntimeError('Failed to fetch API response')


def save_image(buffer, filename, directory=DIRECTORY):
    path = directory + filename + '.jpg'
    with open(path, 'w') as f:
        f.write(buffer)


# Main
if __name__ == '__main__':
    for image in get_api_response()['images']:

        image_url = "http://bing.com/{urlbase}_1920x1080.jpg".format(urlbase=image['urlbase'])
        response = requests.get(image_url)
        if response.status_code == 200:
            save_image(response.content, VALID_FILENAME.sub('', image['copyright']))
