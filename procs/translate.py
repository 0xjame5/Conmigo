#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports the Google Cloud client library
from google.cloud import translate

from string import punctuation
from os import path
import random

from db import KEYWORDS

# Instantiates a client
translate_client = translate.Client.from_service_account_json(
    "google_creds.json"
)


def translate_corpus(lang="es", new_corpus="sent_spanish_50.txt"):

    data = []
    with open("procs/sent_english_50.txt") as sent_file:
        for line in sent_file:
            data.append(
                translate_client.translate(
                    line.replace("\n", ""),
                    target_language=lang
                )["translatedText"]
            )

    with open(new_corpus, "w") as new_corpus_file:
        new_corpus_file.write("\n".join(data).encode("utf-8"))


def get_random_sent(lang="es"):

    english = []
    spanish = []
    with open("procs/sent_english_50.txt") as sent_file:
        english = sent_file.read().split("\n")

    with open("procs/sent_spanish_50.txt") as sent_file:
        spanish = sent_file.read().split("\n")

    chosen_sent = random.choice(english)
    translated_sent = spanish[english.index(chosen_sent)]
    normalized_sent = translated_sent.translate(None, punctuation).split()
    keyword = [i for i in normalized_sent if i in KEYWORDS.keys()][0]

    return {
        "sentence": chosen_sent,
        "keyword": keyword,
        "url": KEYWORDS[keyword],
        "audio_path": path.join(
            "static", "wav", translated_sent.replace(" ", "_").replace("ó", "o") + "wav"),
        "translated": translated_sent
    }


if __name__ == '__main__':

    print get_random_sent()
