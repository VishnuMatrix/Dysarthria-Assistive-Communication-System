def calculate_severity(
    confidence,
    speech_rate,
    speech_ratio,
    pitch_range
):

    score = 0

    # CNN Confidence Contribution

    score += confidence * 0.5

    # Speech Rate

    if speech_rate < 100:
        score += 20

    elif speech_rate < 140:
        score += 10

    # Voice Activity

    if speech_ratio < 50:
        score += 15

    elif speech_ratio < 70:
        score += 8

    # Pitch Variation

    if pitch_range < 80:
        score += 15

    elif pitch_range < 120:
        score += 8

    score = min(
        round(score),
        100
    )

    # Severity Level

    if score <= 25:

        level = "Normal"

    elif score <= 50:

        level = "Mild"

    elif score <= 75:

        level = "Moderate"

    else:

        level = "Severe"

    return {
        "severity_score": score,
        "severity_level": level
    }