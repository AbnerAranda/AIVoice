from elevenlabs import clone, generate, play, set_api_key, save

set_api_key('355a17c10caa7feaece29f8aefaca4c5')
file = open("/Users/abner/Documents/AiVoice/text_sample_2", "r")
text_script = file.read()

voice = clone(
    name="Tucker",
    description="The voice of free America",
    files=["Tucker_Carlson/1.mp3",
           "Tucker_Carlson/2.mp3",
           "Tucker_Carlson/3.mp3"]
)

audio = generate(
    text=text_script,
    #model="eleven_monolingual_v1",
    voice=voice
)

play(audio)
#save(audio, 'tucker_carlson_Hi_Alex.mp3')
file.close()