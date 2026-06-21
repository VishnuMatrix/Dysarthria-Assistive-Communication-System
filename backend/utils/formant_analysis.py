import librosa
import numpy as np


def analyze_formants(audio_path):

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    lpc_order = 16

    lpc_coeffs = librosa.lpc(
        audio,
        order=lpc_order
    )

    roots = np.roots(
        lpc_coeffs
    )

    roots = [
        r for r in roots
        if np.imag(r) >= 0
    ]

    angles = np.arctan2(
        np.imag(roots),
        np.real(roots)
    )

    frequencies = sorted(
        angles * (
            sr / (2 * np.pi)
        )
    )

    print("\nLPC COEFFS:")
    print(lpc_coeffs)

    print("\nROOTS:")
    print(roots)

    print("\nFREQUENCIES:")
    print(frequencies[:20])

    formants = []

    for f in frequencies:

        if 90 < f < 5000:

            formants.append(
                round(float(f), 2)
            )

    print("\nVALID FORMANTS:")
    print(formants)

    while len(formants) < 3:

        formants.append(0)

    return {

        "F1": float(formants[0]),
        "F2": float(formants[1]),
        "F3": float(formants[2])

    }