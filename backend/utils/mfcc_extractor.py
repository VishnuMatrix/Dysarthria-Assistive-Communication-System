import librosa
import librosa.display

import numpy as np

import matplotlib.pyplot as plt

import os
import uuid

MAX_LEN = 256
N_MFCC = 64


def extract_mfcc(audio_path):

    os.makedirs(
        "generated_audio",
        exist_ok=True
    )

    # --------------------
    # Load Audio
    # --------------------

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    # --------------------
    # MFCC
    # --------------------

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=N_MFCC
    )

    # --------------------
    # Unique MFCC Image
    # --------------------

    mfcc_filename = (
        f"mfcc_{uuid.uuid4()}.png"
    )

    mfcc_path = os.path.join(
        "generated_audio",
        mfcc_filename
    )

    plt.figure(
        figsize=(8, 4)
    )

    librosa.display.specshow(
        mfcc,
        x_axis="time"
    )

    plt.colorbar()

    plt.title(
        "MFCC Features"
    )

    plt.tight_layout()

    plt.savefig(
        mfcc_path
    )

    plt.close()

    # --------------------
    # Spectrogram
    # --------------------

    D = librosa.amplitude_to_db(
        np.abs(
            librosa.stft(audio)
        ),
        ref=np.max
    )

    spectrogram_filename = (
        f"spectrogram_{uuid.uuid4()}.png"
    )

    spectrogram_path = os.path.join(
        "generated_audio",
        spectrogram_filename
    )

    plt.figure(
        figsize=(8, 4)
    )

    librosa.display.specshow(
        D,
        sr=sr,
        x_axis="time",
        y_axis="hz"
    )

    plt.colorbar()

    plt.title(
        "Spectrogram"
    )

    plt.tight_layout()

    plt.savefig(
        spectrogram_path
    )

    plt.close()

    # --------------------
    # Normalize MFCC
    # --------------------

    mfcc = (
        mfcc - np.mean(mfcc)
    ) / (
        np.std(mfcc) + 1e-8
    )

    # --------------------
    # Padding
    # --------------------

    if mfcc.shape[1] < MAX_LEN:

        pad_width = (
            MAX_LEN - mfcc.shape[1]
        )

        mfcc = np.pad(
            mfcc,
            ((0, 0), (0, pad_width)),
            mode="constant"
        )

    else:

        mfcc = mfcc[:, :MAX_LEN]

    # --------------------
    # CNN Shape
    # --------------------

    mfcc = np.expand_dims(
        mfcc,
        axis=-1
    )

    mfcc = np.expand_dims(
        mfcc,
        axis=0
    )

    return (
        mfcc,
        mfcc_filename,
        spectrogram_filename
    )