# NOTE!!!!!
# NEED TO SOURCE INTO ENV CONFIG.
# Example:
#   source env_config
# also, gcs is basically re-routing to google cloud servers.
# DONT WORRY ABOUT IT UNLESS WE"RE STORING SOUNDS INTO GCS

"""
Google Cloud Speech API sample application using the REST API for batch
processing.
"""
import argparse
import io

# [START def_transcribe_file]
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_sync_request]
    # [START migration_audio_config_file]
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')
    # [END migration_audio_config_file]

    # [START migration_sync_response]
    response = client.recognize(config, audio)
    # [END migration_sync_request]
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    # [END migration_sync_response]
# [END def_transcribe_file]


if __name__ == '__main__':

    file_name = "audio.raw"
    transcribe_file(file_name)