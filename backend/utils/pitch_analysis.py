import librosa
import numpy as np
import matplotlib.pyplot as plt
import os
import uuid


def analyze_pitch(audio_path):

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    pitch = librosa.yin(
        audio,
        fmin=50,
        fmax=500
    )

    pitch = pitch[
        ~np.isnan(pitch)
    ]

    avg_pitch = round(
        float(np.mean(pitch)),
        2
    )

    min_pitch = round(
        float(np.min(pitch)),
        2
    )

    max_pitch = round(
        float(np.max(pitch)),
        2
    )

    pitch_range = round(
        max_pitch - min_pitch,
        2
    )

    os.makedirs(
        "generated_audio",
        exist_ok=True
    )

    filename = (
        f"pitch_{uuid.uuid4()}.png"
    )

    output_path = os.path.join(
        "generated_audio",
        filename
    )

    plt.figure(figsize=(10, 3))

    plt.plot(pitch)

    plt.title(
        "Pitch Contour"
    )

    plt.xlabel(
        "Frames"
    )

    plt.ylabel(
        "Frequency (Hz)"
    )

    plt.tight_layout()

    plt.savefig(
        output_path
    )

    plt.close()

    return {
        "avg_pitch": avg_pitch,
        "min_pitch": min_pitch,
        "max_pitch": max_pitch,
        "pitch_range": pitch_range,
        "pitch_image": filename
    }