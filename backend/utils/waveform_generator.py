import librosa
import matplotlib.pyplot as plt
import os
import uuid


def generate_waveform(audio_path):

    os.makedirs(
        "generated_audio",
        exist_ok=True
    )

    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    filename = (
        f"waveform_{uuid.uuid4()}.png"
    )

    output_path = os.path.join(
        "generated_audio",
        filename
    )

    plt.figure(figsize=(10,3))

    plt.plot(audio)

    plt.title("Waveform")

    plt.xlabel("Samples")

    plt.ylabel("Amplitude")

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()

    return filename