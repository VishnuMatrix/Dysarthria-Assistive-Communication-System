import os
import gdown

from tensorflow.keras.models import load_model
from utils.mfcc_extractor import extract_mfcc

MODEL_PATH = "models/dysarthria_cnn_64mfcc.keras"

os.makedirs("models", exist_ok=True)

if not os.path.exists(MODEL_PATH):

    print("Downloading CNN model...")

    gdown.download(
        "https://drive.google.com/uc?id=1P7d4HJH743FBkDsM9RX_rWjXIrGWl2in",
        MODEL_PATH,
        quiet=False
    )

model = load_model(MODEL_PATH)

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