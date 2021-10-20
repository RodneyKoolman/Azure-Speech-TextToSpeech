import random
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat

# Subscription settings from Azure
# Region can be westeurope for example
subscription_key = '[AZURE_SPEECH_API_KEY]'
subscription_region = '[AZURE_SPEECH_API_REGION]'

# Input SSML file
# Open this file to change or fine-tune the pitch, pronunciation, speaking rate, volume, voice, language and more
# https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/Speech-Service/language-support.md#neural-voices
input_folder = 'input/'
input_file = 'ssml.xml'

# https://docs.microsoft.com/nl-nl/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.speechsynthesisoutputformat?view=azure-python
audio_format = 'Riff24Khz16BitMonoPcm'

# Output folder and file
output_folder = 'output/'
output_file = f'file-{random.randint(10000,99999)}.wav'

speech_config = SpeechConfig(subscription=subscription_key, region=subscription_region)
speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat[audio_format])
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)

input = open(f"{input_folder}{input_file}", "r").read()
result = synthesizer.speak_ssml_async(input).get()

stream = AudioDataStream(result)
stream.save_to_wav_file(f"{output_folder}{output_file}")