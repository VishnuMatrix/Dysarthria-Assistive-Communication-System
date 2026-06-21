# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles

# import shutil
# import os
# import uuid

# from utils.waveform_generator import (
#     generate_waveform
# )

# from utils.vad_analysis import (
#     analyze_vad
# )

# from utils.audio_comparison import (
#     compare_audio
# )

# from utils.severity_score import (
#     calculate_severity
# )

# from utils.formant_analysis import (
#     analyze_formants
# )

# from utils.report_generator import (
#     generate_report
# )

# from utils.audio_enhancement import (
#     enhance_audio
# )

# from utils.pitch_analysis import (
#     analyze_pitch
# )

# from utils.speech_analysis import (
#     analyze_speech
# )

# from utils.emotion_detection import (
#     detect_emotion
# )

# from utils.dysarthria_predictor import (
#     predict_dysarthria
# )

# from utils.speech_to_text import (
#     speech_to_text
# )

# from utils.text_to_speech import (
#     text_to_speech
# )

# app = FastAPI()

# # -----------------------------------
# # CORS
# # -----------------------------------

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -----------------------------------
# # Folders
# # -----------------------------------

# UPLOAD_FOLDER = "uploads"
# GENERATED_FOLDER = "generated_audio"
# REPORT_FOLDER = "reports"

# os.makedirs(
#     REPORT_FOLDER,
#     exist_ok=True
# )

# os.makedirs(
#     UPLOAD_FOLDER,
#     exist_ok=True
# )

# os.makedirs(
#     GENERATED_FOLDER,
#     exist_ok=True
# )

# # -----------------------------------
# # Static Files
# # -----------------------------------

# app.mount(
#     "/uploads",
#     StaticFiles(directory=UPLOAD_FOLDER),
#     name="uploads"
# )

# app.mount(
#     "/generated_audio",
#     StaticFiles(directory=GENERATED_FOLDER),
#     name="generated_audio"
# )
# app.mount(
#     "/reports",
#     StaticFiles(
#         directory=REPORT_FOLDER
#     ),
#     name="reports"
# )
# # -----------------------------------
# # Home Route
# # -----------------------------------

# @app.get("/")
# def home():

#     return {
#         "message":
#         "Backend Running Successfully"
#     }

# # -----------------------------------
# # Predict Route
# # -----------------------------------

# @app.post("/predict")
# async def predict_audio(
#     file: UploadFile = File(...)
# ):

#     unique_name = (
#         f"{uuid.uuid4()}_{file.filename}"
#     )

#     file_path = os.path.join(
#         UPLOAD_FOLDER,
#         unique_name
#     )

#     with open(
#         file_path,
#         "wb"
#     ) as buffer:

#         shutil.copyfileobj(
#             file.file,
#             buffer
#         )

#     # CNN Prediction

#     # result = predict_dysarthria(
#     #     file_path
#     # )

#     # # Whisper STT

#     # transcript = speech_to_text(
#     #     file_path
#     # )
#     enhanced_audio = enhance_audio(
#     file_path
#     )

#     comparison_stats = compare_audio(
#     file_path,
#     enhanced_audio
#     )

#     result = predict_dysarthria(
#     enhanced_audio
#    )

#     transcript = speech_to_text(
#     enhanced_audio
#     )

#     formant_stats = analyze_formants(
#     enhanced_audio
#     )

#     emotion_stats = detect_emotion(
#     enhanced_audio
#     )

#     print("\nEMOTION STATS:")
#     print(emotion_stats)
#     print(type(emotion_stats))

#     pitch_stats = analyze_pitch(
#     file_path
#     )

#     vad_stats = analyze_vad(
#     file_path
#     )

#     speech_stats = analyze_speech(
#     file_path,
#     transcript
#     )

#     speech_stats = analyze_speech(
#     enhanced_audio,
#     transcript
#     )
#     severity_stats = calculate_severity(

#     result["confidence"],

#     speech_stats["speech_rate"],

#     vad_stats["speech_ratio"],

#     pitch_stats["pitch_range"]

#     )

#     waveform_image = generate_waveform(
#     file_path
#     )

#     # TTS

#     generated_audio = text_to_speech(
#         transcript
#     )

#     report_file = generate_report({

#     "Prediction":
#     result["prediction"],

#     "Confidence":
#     result["confidence"],

#     "Transcript":
#     transcript,

#     "Emotion":
#     emotion_stats["emotion"],

#     "Severity":
#     severity_stats["severity_level"],

#     "Severity Score":
#     severity_stats["severity_score"],

#     "Duration":
#     speech_stats["duration"],

#     "Speech Rate":
#     speech_stats["speech_rate"],

#     "Average Pitch":
#     pitch_stats["avg_pitch"],

#     "F1":
#     formant_stats["F1"],

#     "F2":
#     formant_stats["F2"],

#     "F3":
#     formant_stats["F3"]

# })

#     print("\n====================")
#     print("Uploaded File :", unique_name)
#     print("Transcript    :", transcript)
#     print("Generated MP3 :", generated_audio)
#     print("====================\n")

#     return {

#         "prediction":
#         result["prediction"],

#         "confidence":
#         result["confidence"],

#         "transcript":
#         transcript,

#         "audio_file":
#         f"/generated_audio/{generated_audio}",

#         "original_audio":
#         f"/uploads/{unique_name}",

#         "mfcc_image":
#         f"/generated_audio/{result['mfcc_image']}",

#         "spectrogram":
#         f"/generated_audio/{result['spectrogram_image']}",

#         "waveform":
#         f"/generated_audio/{waveform_image}",

#         "duration":
#         speech_stats["duration"],

#         "words":
#         speech_stats["words"],

#         "speech_rate":
#         speech_stats["speech_rate"],

#         "volume":
#         speech_stats["volume"],

#         "noise":
#         speech_stats["noise"],

#         "avg_pitch":
#         pitch_stats["avg_pitch"],

#         "min_pitch":
#         pitch_stats["min_pitch"],

#          "max_pitch":
#         pitch_stats["max_pitch"],

#         "pitch_range":
#         pitch_stats["pitch_range"],

#         "pitch_image":
#         f"/generated_audio/{pitch_stats['pitch_image']}",

#         "speech_duration":
#         vad_stats["speech_duration"],

#         "silence_duration":
#         vad_stats["silence_duration"],

#         "speech_ratio":
#         vad_stats["speech_ratio"],

#         "segments":
#         vad_stats["segments"],

#         "enhanced_audio":
#         f"/uploads/{os.path.basename(enhanced_audio)}",

#         "F1":
#         formant_stats["F1"],

#         "F2":
#         formant_stats["F2"],

#         "F3":
#         formant_stats["F3"],

#         "emotion":
#         emotion_stats["emotion"],

#         "emotion_pitch":
#         emotion_stats["avg_pitch"],

#         "emotion_energy":
#         emotion_stats["energy"],

#         "severity_score":
#         severity_stats["severity_score"],

#         "severity_level":
#         severity_stats["severity_level"],

#         "report":
#         f"/reports/{report_file}",

#         "original_volume":
#         comparison_stats["original_volume"],

#         "enhanced_volume":
#         comparison_stats["enhanced_volume"],

#         "noise_reduction":
#         comparison_stats["noise_reduction"],

#         "volume_improvement":
#         comparison_stats["volume_improvement"],

#     }

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import shutil
import os
import uuid

from utils.waveform_generator import generate_waveform
from utils.vad_analysis import analyze_vad
from utils.audio_comparison import compare_audio
from utils.severity_score import calculate_severity
from utils.formant_analysis import analyze_formants
from utils.report_generator import generate_report
from utils.audio_enhancement import enhance_audio
from utils.pitch_analysis import analyze_pitch
from utils.speech_analysis import analyze_speech
from utils.emotion_detection import detect_emotion
from utils.dysarthria_predictor import predict_dysarthria
from utils.speech_to_text import speech_to_text
from utils.text_to_speech import text_to_speech
from utils.clinical_comparison import clinical_comparison

app = FastAPI()

# -----------------------------------
# CORS
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# Folders
# -----------------------------------

UPLOAD_FOLDER = "uploads"
GENERATED_FOLDER = "generated_audio"
REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

# -----------------------------------
# Static Files
# -----------------------------------

app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")
app.mount("/generated_audio", StaticFiles(directory=GENERATED_FOLDER), name="generated_audio")
app.mount("/reports", StaticFiles(directory=REPORT_FOLDER), name="reports")

# -----------------------------------
# Home Route
# -----------------------------------

@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}

# -----------------------------------
# Predict Route
# -----------------------------------

@app.post("/predict")
async def predict_audio(file: UploadFile = File(...)):

    unique_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Audio Enhancement
    enhanced_audio = enhance_audio(file_path)

    # Audio Comparison
    comparison_stats = compare_audio(file_path, enhanced_audio) or {
        "original_volume": 0.0, "enhanced_volume": 0.0,
        "noise_reduction": 0.0, "volume_improvement": 0.0
    }

    # CNN Prediction
    result = predict_dysarthria(enhanced_audio) or {
        "prediction": "Unknown", "confidence": 0.0,
        "mfcc_image": "", "spectrogram_image": ""
    }

    # Whisper STT
    transcript = speech_to_text(enhanced_audio) or ""

    # Formant Analysis
    formant_stats = analyze_formants(enhanced_audio) or {"F1": 0.0, "F2": 0.0, "F3": 0.0}

    # Emotion Detection
    emotion_stats = detect_emotion(enhanced_audio) or {"emotion": "Unknown", "avg_pitch": 0.0, "energy": 0.0}

    print("\nEMOTION STATS:")
    print(emotion_stats)
    print(type(emotion_stats))

    # Pitch Analysis
    pitch_stats = analyze_pitch(file_path) or {
        "avg_pitch": 0.0, "min_pitch": 0.0, "max_pitch": 0.0,
        "pitch_range": 0.0, "pitch_image": ""
    }

    # VAD Analysis
    vad_stats = analyze_vad(file_path) or {
        "speech_duration": 0.0, "silence_duration": 0.0,
        "speech_ratio": 0.0, "segments": []
    }

    # Speech Analysis
    speech_stats = analyze_speech(enhanced_audio, transcript) or {
        "duration": 0.0, "words": 0, "speech_rate": 0.0,
        "volume": 0.0, "noise": 0.0
    }

    # Severity Score
    severity_stats = calculate_severity(
        result["confidence"],
        speech_stats["speech_rate"],
        vad_stats["speech_ratio"],
        pitch_stats["pitch_range"]
    )

    # Clinical Comparison

    clinical_stats = clinical_comparison(

    pitch_stats["pitch_range"],

    speech_stats["speech_rate"],

    vad_stats["speech_ratio"],

    result["confidence"]

)

    # Waveform
    waveform_image = generate_waveform(file_path)

    # TTS
    generated_audio = text_to_speech(transcript)

    # Report
    report_file = generate_report({
        "Prediction": result["prediction"],
        "Confidence": result["confidence"],
        "Transcript": transcript,
        "Emotion": emotion_stats["emotion"],
        "Severity": severity_stats["severity_level"],
        "Severity Score": severity_stats["severity_score"],
        "Duration": speech_stats["duration"],
        "Speech Rate": speech_stats["speech_rate"],
        "Average Pitch": pitch_stats["avg_pitch"],
        "F1": formant_stats["F1"],
        "F2": formant_stats["F2"],
        "F3": formant_stats["F3"],
        "Pitch Status":clinical_stats["pitch_status"],
        "Speech Rate Status":clinical_stats["speech_rate_status"],
        "Speech Ratio Status":clinical_stats["speech_ratio_status"],
        "Clinical Assessment":clinical_stats["clinical_assessment"],

    })

    print("\n====================")
    print("Uploaded File :", unique_name)
    print("Transcript    :", transcript)
    print("Generated MP3 :", generated_audio)
    print("====================\n")

    return {
        "prediction": result["prediction"],
        "confidence": result["confidence"],
        "transcript": transcript,
        "audio_file": f"/generated_audio/{generated_audio}",
        "original_audio": f"/uploads/{unique_name}",
        "mfcc_image": f"/generated_audio/{result['mfcc_image']}",
        "spectrogram": f"/generated_audio/{result['spectrogram_image']}",
        "waveform": f"/generated_audio/{waveform_image}",
        "duration": speech_stats["duration"],
        "words": speech_stats["words"],
        "speech_rate": speech_stats["speech_rate"],
        "volume": speech_stats["volume"],
        "noise": speech_stats["noise"],
        "avg_pitch": pitch_stats["avg_pitch"],
        "min_pitch": pitch_stats["min_pitch"],
        "max_pitch": pitch_stats["max_pitch"],
        "pitch_range": pitch_stats["pitch_range"],
        "pitch_image": f"/generated_audio/{pitch_stats['pitch_image']}",
        "speech_duration": vad_stats["speech_duration"],
        "silence_duration": vad_stats["silence_duration"],
        "speech_ratio": vad_stats["speech_ratio"],
        "segments": vad_stats["segments"],
        "enhanced_audio": f"/uploads/{os.path.basename(enhanced_audio)}",
        "F1": formant_stats["F1"],
        "F2": formant_stats["F2"],
        "F3": formant_stats["F3"],
        "emotion": emotion_stats["emotion"],
        "emotion_pitch": emotion_stats["avg_pitch"],
        "emotion_energy": emotion_stats["energy"],
        "severity_score": severity_stats["severity_score"],
        "severity_level": severity_stats["severity_level"],
        "report": f"/reports/{report_file}",
        "original_volume": comparison_stats["original_volume"],
        "enhanced_volume": comparison_stats["enhanced_volume"],
        "noise_reduction": comparison_stats["noise_reduction"],
        "volume_improvement": comparison_stats["volume_improvement"],
        "pitch_status":clinical_stats["pitch_status"],
        "speech_rate_status":clinical_stats["speech_rate_status"],
        "speech_ratio_status":clinical_stats["speech_ratio_status"],
        "clinical_assessment":clinical_stats["clinical_assessment"],
    }