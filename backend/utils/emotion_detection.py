import librosa
import numpy as np


def detect_emotion(audio_path):

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    # Pitch

    pitches, magnitudes = librosa.piptrack(
        y=audio,
        sr=sr
    )

    pitch_values = pitches[
        pitches > 0
    ]

    avg_pitch = (
        np.mean(pitch_values)
        if len(pitch_values) > 0
        else 0
    )

    # Energy

    rms = librosa.feature.rms(
        y=audio
    )

    energy = np.mean(rms)

    # Rule-based Emotion Detection

    if avg_pitch > 220 and energy > 0.08:
        emotion = "Happy"

    elif avg_pitch > 200 and energy > 0.06:
        emotion = "Excited"

    elif avg_pitch < 130 and energy < 0.03:
        emotion = "Sad"

    elif energy > 0.12:
        emotion = "Angry"

    else:
        emotion = "Neutral"

    return {
        "emotion": str(emotion),
        "avg_pitch": float(round(avg_pitch, 2)),
        "energy": float(round(float(energy), 4))
    }