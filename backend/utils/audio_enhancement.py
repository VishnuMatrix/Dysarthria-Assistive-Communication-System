import librosa
import soundfile as sf
import numpy as np
import os
import uuid


def enhance_audio(audio_path):

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    # Simple noise reduction

    threshold = 0.02

    enhanced = np.where(
        np.abs(audio) < threshold,
        0,
        audio
    )

    filename = (
        f"enhanced_{uuid.uuid4()}.wav"
    )

    output_path = os.path.join(
        "uploads",
        filename
    )

    sf.write(
        output_path,
        enhanced,
        sr
    )

    return output_path