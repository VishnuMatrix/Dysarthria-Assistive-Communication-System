import { useState } from "react";

import api from "../services/api";

import "../style/UploadCard.css";

function UploadCard({ setResult }) {
  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a WAV file");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();

      formData.append("file", file);

      const response = await api.post("/predict", formData);

      setResult(response.data);
    } catch (error) {
      console.error(error);

      alert("Error processing audio");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">
      <h2>Upload Audio</h2>

      <input
        type="file"
        accept=".wav"
        className="file-input"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button className="predict-btn" onClick={handleUpload} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Speech"}
      </button>

      {loading && (
        <div className="loading-container">
          <div className="spinner"></div>

          <h3>AI Processing...</h3>

          <div className="processing-steps">
            <p>📤 Uploading Audio...</p>

            <p>🎵 Extracting MFCC Features...</p>

            <p>📊 Generating Spectrogram...</p>

            <p>🎙 Analyzing Pitch...</p>

            <p>😊 Detecting Emotion...</p>

            <p>🧠 Running CNN Model...</p>

            <p>📝 Whisper Speech Recognition...</p>

            <p>🔊 Generating Speech Output...</p>

            <p>📄 Creating PDF Report...</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default UploadCard;
