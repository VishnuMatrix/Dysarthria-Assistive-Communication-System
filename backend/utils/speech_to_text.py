import os

os.environ["PATH"] += os.pathsep + r"C:\Users\kumar\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"

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