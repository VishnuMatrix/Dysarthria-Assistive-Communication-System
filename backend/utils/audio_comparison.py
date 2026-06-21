import librosa
import numpy as np


def compare_audio(
    original_audio,
    enhanced_audio
):

    original, sr = librosa.load(
        original_audio,
        sr=16000
    )

    enhanced, sr = librosa.load(
        enhanced_audio,
        sr=16000
    )

    # Volume

    original_volume = np.mean(
        np.abs(original)
    )

    enhanced_volume = np.mean(
        np.abs(enhanced)
    )

    # Noise Estimate

    original_noise = np.std(
        original
    )

    enhanced_noise = np.std(
        enhanced
    )

    noise_reduction = (
        (
            original_noise -
            enhanced_noise
        )
        /
        (original_noise + 1e-8)
    ) * 100

    volume_improvement = (
        (
            enhanced_volume -
            original_volume
        )
        /
        (original_volume + 1e-8)
    ) * 100

    return {

        "original_volume":
        round(
            float(original_volume),
            4
        ),

        "enhanced_volume":
        round(
            float(enhanced_volume),
            4
        ),

        "noise_reduction":
        round(
            float(noise_reduction),
            2
        ),

        "volume_improvement":
        round(
            float(volume_improvement),
            2
        )
    }