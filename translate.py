# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client.from_service_account_json("key.json")

# The text to translate
text = u'Wake me up WAKE ME UP INSIDE'
# The target language
target = 'es'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
