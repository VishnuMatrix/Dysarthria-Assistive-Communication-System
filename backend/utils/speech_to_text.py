import whisper

asr_model = whisper.load_model("base")

def speech_to_text(audio_path):

    print("\n====================")
    print("FILE RECEIVED:", audio_path)
    print("====================")

    result = asr_model.transcribe(
        audio_path,
        language="en"
    )

    print("\nTRANSCRIPT:")
    print(result["text"])
    print("====================\n")

    return result["text"].strip()