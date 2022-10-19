import requests


def main():
    url = "https://random.responsiveimages.io/v1/docs"
    image = requests.get(url)

    if image.status_code == 200:
        with open('random_image.png', 'wb') as file:
            file.write(image.content)

