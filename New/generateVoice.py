import requests

def generate_voice(text):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/ANRi8ArRKSmw415run3K"

    payload = {
        "model_id": "eleven_turbo_v2",
        "text": text,
        "voice_settings": {
            "similarity_boost": 0.5,
            "stability": 0.5,
            "style": 0.5,
            "use_speaker_boost": True
        }
    }
    headers = {
        "xi-api-key": "fbb993426355de2be33ab32f916e573e",
        "Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)


    import os
    os.system("mpg123 output.mp3")



