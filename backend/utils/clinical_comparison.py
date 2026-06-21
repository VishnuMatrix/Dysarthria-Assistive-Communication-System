def clinical_comparison(
    pitch_range,
    speech_rate,
    speech_ratio,
    confidence
):

    results = {}

    # Pitch

    if 80 <= pitch_range <= 250:
        results["pitch_status"] = "Normal"
    else:
        results["pitch_status"] = "Abnormal"

    # Speech Rate

    if 120 <= speech_rate <= 180:
        results["speech_rate_status"] = "Normal"
    else:
        results["speech_rate_status"] = "Abnormal"

    # Speech Ratio

    if 60 <= speech_ratio <= 90:
        results["speech_ratio_status"] = "Normal"
    else:
        results["speech_ratio_status"] = "Abnormal"

    abnormal_count = sum([

        results["pitch_status"] == "Abnormal",

        results["speech_rate_status"] == "Abnormal",

        results["speech_ratio_status"] == "Abnormal"

    ])

    if abnormal_count >= 2:

        results["clinical_assessment"] = (
            "Speech characteristics resemble Dysarthric Speech"
        )

    else:

        results["clinical_assessment"] = (
            "Speech characteristics are within Normal Limits"
        )

    return results