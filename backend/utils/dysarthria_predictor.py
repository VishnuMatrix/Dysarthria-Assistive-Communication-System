from tensorflow.keras.models import load_model

from utils.mfcc_extractor import (
    extract_mfcc
)

# Load model once

model = load_model(
    "models/dysarthria_cnn_64mfcc.keras"
)


def predict_dysarthria(audio_path):

    mfcc, mfcc_image, spectrogram_image = extract_mfcc(
        audio_path
    )

    probability = model.predict(
        mfcc,
        verbose=0
    )[0][0]

    probability = float(probability)

    print(
        "Raw Probability =",
        probability
    )

    if probability >= 0.5:

        prediction = (
            "Dysarthric Speech"
        )

        confidence = round(
            probability * 100,
            2
        )

    else:

        prediction = (
            "Normal Speech"
        )

        confidence = round(
            (1 - probability) * 100,
            2
        )

    return {

        "prediction":
        prediction,

        "confidence":
        float(confidence),

        "mfcc_image":
        mfcc_image,

        "spectrogram_image":
        spectrogram_image

    }