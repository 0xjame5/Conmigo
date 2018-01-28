#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydub import AudioSegment
import speech_recognition as sr


def split_recording(raw_file_path, output_path, seg_lim=30000):

    print "Splitting file..."
    song = AudioSegment.from_wav(raw_file_path)

    # get the first seg_lim milliseconds
    song[:seg_lim].export("answer.wav", format="wav")


with open("procs/google_creds.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()


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

    raw_file_path = "raw.wav"
    output_path = "answer.wav"

    split_recording(raw_file_path, output_path)
    transcribe(output_path)
