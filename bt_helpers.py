def long_audio_transcript(storage_uri, language_code = "en-US", sample_rate_hertz = 44100):
    from google.cloud import speech_v1
    from google.cloud.speech_v1 import enums
    client = speech_v1.SpeechClient()

    encoding = enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    response = operation.result()

    result = ""

    for partial_result in response.results:
        alternative = partial_result.alternatives[0]
        result += alternative.transcript

    return result
        


def short_audio_transcript(storage_uri, language_code = 'en-US', sample_rate_hertz = 44100):
    from google.cloud import speech_v1p1beta1
    from google.cloud.speech_v1p1beta1 import enums

    client = speech_v1p1beta1.SpeechClient()

    encoding = enums.RecognitionConfig.AudioEncoding.MP3
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    audio = {"uri": storage_uri}

    response = client.recognize(config, audio)
    result = ""

    for partial_result in response.results:
        alternative = partial_result.alternatives[0]
        result += alternative.transcript

    return result
    


def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)