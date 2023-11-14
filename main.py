import json
import requests
import time

API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
          '.eyJ1c2VyX2lkIjoiMWYwOGMxZmQtZTNjNy00NWI0LWI1OTctYjEyZjkxMTg5ZGFhIiwidHlwZSI6ImFwaV90b2tlbiJ9' \
          '.0B7lpfCQ03Wd_WkXt-PHtuSISQM3wcBwnQSlv39lX6w'


def convert_to_text():
    headers = {"Authorization": f"Bearer {API_KEY}"}

    url = "https://api.edenai.run/v2/audio/speech_to_text_async"

    data = {"providers": "openai", "language": "ru-RU"}

    files = {'file': open(r"C:\Users\Kain\Desktop\1662550439_samurayki-vhlam.mp3", 'rb')}

    response = requests.post(url, data=data, files=files, headers=headers)
    unx_time = int(time.time())
    result = json.loads(response.text)

    with open(f"{unx_time}.json", "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    url_finish = f'https://api.edenai.run/v2/audio/speech_to_text_async/{result["public_id"]}'

    r = requests.get(url_finish, headers=headers)
    r1 = r.json()["results"]["openai"]["text"]

    with open(f'{unx_time}.txt', "w") as f:
        f.write(r1)

    print(r1)


def main():
    convert_to_text()


if __name__ == '__main__':
    main()
