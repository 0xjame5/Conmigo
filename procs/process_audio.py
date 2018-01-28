#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

import speech_recognition as sr


with open("procs/google_creds.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()


def convert_to_wav(file_path):

    args = "ffmpeg -i {0}.webm -acodec pcm_s16le -ar 48000 -y {0}.wav".format(
        file_path)

    subprocess.Popen(args.split(" "))


def transcribe(output_path, to_lang="es"):

    print "Transcribing file..."
    recognizer = sr.Recognizer()
    with sr.AudioFile(output_path) as source:
        audio = recognizer.record(source)

    # Transcribe audio file
    text = recognizer.recognize_google_cloud(
        audio,
        language=to_lang,
        credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS
    )

    with open("transcript.txt", "w") as f:
        f.write(text.encode("utf-8"))


if __name__ == '__main__':

    convert_to_wav("raw")
    output_path = "raw.wav"

    # split_recording(raw_file_path, output_path)
    transcribe(output_path, to_lang="en")
