import librosa
import numpy as np

def analyze_vad(audio_path):

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    intervals = librosa.effects.split(
        audio,
        top_db=25
    )

    speech_samples = 0

    for start, end in intervals:

        speech_samples += (
            end - start
        )

    total_samples = len(audio)

    speech_duration = round(
        speech_samples / sr,
        2
    )

    total_duration = round(
        total_samples / sr,
        2
    )

    silence_duration = round(
        total_duration -
        speech_duration,
        2
    )

    speech_ratio = round(
        (
            speech_duration /
            total_duration
        ) * 100,
        2
    )

    return {

        "speech_duration":
        speech_duration,

        "silence_duration":
        silence_duration,

        "speech_ratio":
        speech_ratio,

        "segments":
        len(intervals)
    }