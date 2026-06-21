from utils.dysarthria_predictor import (
    predict_dysarthria
)

result = predict_dysarthria(
    "uploads/speech.wav"
)

print(result)