import requests
import secrets
import time

with open('input.txt', 'r', encoding='utf-8') as f:
    input = f.read()

char_thresh = 4096 
done = False

sentences = input.split('.')

buffer = ''
i = 0
last = 0

while not done:

    print()
    print()

    while len(buffer) < char_thresh:
        i += 1
        if i == len(sentences) + 1: 
            done = True
            break
        buffer = '.'.join(sentences[last:i])

    # buffer is now 'over-full' decrease i by 1

    buffer = '.'.join(sentences[last:i-1])
    print('buffer len', len(buffer))

    if last == i-1: break # special case, perfectly sized last batch

    # print(buffer)
    print('Processing sentences {} to {} of {}'.format(last, i-1, len(sentences)))

    url = "https://api.openai.com/v1/audio/speech"
    headers = {
        "Authorization": 'Bearer {}'.format(secrets.openai_key),
        "Content-Type": "application/json"
    }
    data = {
        "model": "tts-1",
        "input": buffer,
        "voice": "alloy"
    }

    start_time = time.time()
    response = requests.post(url, headers=headers, json=data)
    stop_time = time.time()

    print('API call took {:.2f} seconds'.format(stop_time-start_time))

    if response.status_code == 200:
        with open("output/speech_{}.mp3".format(last), "wb") as file:
            file.write(response.content)
        print("Audio saved")
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)

    # prepare for next loop
    last = i-1

    # if i > 20: break # debug
