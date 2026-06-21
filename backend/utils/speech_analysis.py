import librosa
import numpy as np

def analyze_speech(audio_path, transcript):

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    # Duration

    duration = round(
        librosa.get_duration(
            y=audio,
            sr=sr
        ),
        2
    )

    # RMS Energy

    rms = librosa.feature.rms(
        y=audio
    )

    rms_mean = np.mean(rms)

    if rms_mean < 0.02:
        volume = "Low"

    elif rms_mean < 0.08:
        volume = "Normal"

    else:
        volume = "High"

    # Noise Estimate

    zcr = librosa.feature.zero_crossing_rate(
        audio
    )

    zcr_mean = np.mean(zcr)

    if zcr_mean < 0.08:
        noise = "Low"

    elif zcr_mean < 0.15:
        noise = "Moderate"

    else:
        noise = "High"

    # Speech Rate

    words = len(
        transcript.split()
    )

    if duration > 0:

        speech_rate = round(
            (words / duration) * 60,
            2
        )

    else:

        speech_rate = 0

    return {

        "duration": duration,

        "words": words,

        "speech_rate": speech_rate,

        "volume": volume,

        "noise": noise
    }