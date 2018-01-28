#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

import speech_recognition as sr


with open("google_creds.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()


def transcribe(output_path, to_lang="es"):

    print "Converting file..."
    args = "ffmpeg -i {0}.webm -acodec pcm_s16le -ar 48000 -y {0}.wav".format(
        output_path)

    p = subprocess.Popen(args.split(" "))

    p.wait()

    print "Transcribing file..."
    recognizer = sr.Recognizer()
    with sr.AudioFile(output_path + ".wav") as source:
        audio = recognizer.record(source)

    # Transcribe audio file
    text = recognizer.recognize_google_cloud(
        audio,
        language=to_lang,
        credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS
    )

    return text


if __name__ == '__main__':

    output_path = "raw"
    transcribe(output_path, to_lang="en")
