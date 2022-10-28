import requests


def main():
    url = "https://random.responsiveimages.io/v1/docs"
    if check_internet() is False:
        return 'connection'
    if requests.get(url).status_code != 200:
        return 'something'
    elif requests.get(url).status_code == 200:
        with open('random_image.png', 'wb') as file:
            file.write(requests.get(url).content)
        return 'correct'


def check_internet():
    url = "https://random.responsiveimages.io/v1/docs"
    try:
        requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        return False
