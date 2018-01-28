
import requests
import shutil
import json
import sys

WATSON_KEYS = {
  "url": "https://stream.watsonplatform.net/text-to-speech/api",
  "username": "f6fb4cce-bfea-444a-aa81-b370b9bdfc59",
  "password": "LgMmkAhpzGAE"
}


"""

curl -X POST -u "{username}":"{password}"
--header "Content-Type: application/json"
--header "Accept: audio/wav"
--data "{\"text\":\"Hello world\"}"
--output hello_world.wav

"""

def text_to_speech(text):
    # url = WATSON_KEYS["url"] + "/v1/synthesize?voice=en-US_AllisonVoice"
    # url = WATSON_KEYS["url"] + "/v1/synthesize?voice=es-ES_EnriqueVoice"
    url = WATSON_KEYS["url"] + "/v1/synthesize?voice=es-LA_SofiaVoice"

    auth = requests.auth.HTTPBasicAuth(WATSON_KEYS["username"],
                                       WATSON_KEYS["password"])

    headers = {
        "Content-Type": "application/json",
        "Accept":"audio/wav"
    }

    data = json.dumps({"text": text})
    output = requests.post(url=url, headers=headers, data=data, auth=auth)

    fname = "{0}wav".format(text)

    with open(fname, 'wb') as f:
        f.write(output.content)

def main():
    with open("the_list.txt", 'r') as f:
      for line in f:
        line = line[:len(line) - 1]
        text_to_speech(line)
        print(line)
        # break
main()