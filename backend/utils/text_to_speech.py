from gtts import gTTS
import os
import uuid

def text_to_speech(text):

    os.makedirs(
        "generated_audio",
        exist_ok=True
    )

    filename = f"{uuid.uuid4()}.mp3"

    output_path = os.path.join(
        "generated_audio",
        filename
    )

    print("Generating:", output_path)

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(output_path)

    return filename