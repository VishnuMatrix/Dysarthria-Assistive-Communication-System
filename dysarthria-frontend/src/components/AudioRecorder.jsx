import { useState, useRef } from "react";

import "../style/AudioRecorder.css";

function AudioRecorder({ onAudioReady }) {
  const [recording, setRecording] = useState(false);

  const [audioURL, setAudioURL] = useState(null);

  const [loading, setLoading] = useState(false);

  const mediaRecorderRef = useRef(null);

  const chunksRef = useRef([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true,
    });

    const recorder = new MediaRecorder(stream);

    mediaRecorderRef.current = recorder;

    recorder.ondataavailable = (event) => {
      chunksRef.current.push(event.data);
    };

    recorder.onstop = async () => {
      setLoading(true);

      const blob = new Blob(chunksRef.current, {
        type: "audio/wav",
      });

      chunksRef.current = [];

      const url = URL.createObjectURL(blob);

      setAudioURL(url);

      await onAudioReady(blob);

      setLoading(false);
    };

    recorder.start();

    setRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();

    setRecording(false);
  };

  return (
    <div className="recorder-card">
      <h2>Live Recording</h2>

      {!recording ? (
        <button className="record-btn" onClick={startRecording}>
          🎤 Start Recording
        </button>
      ) : (
        <button className="stop-btn" onClick={stopRecording}>
          ⏹ Stop Recording
        </button>
      )}

      {loading && (
        <div className="record-loading">
          <div className="spinner"></div>

          <p>Analyzing Recording...</p>
        </div>
      )}

      {audioURL && (
        <div className="preview-section">
          <h3>Recording Preview</h3>

          <audio controls src={audioURL} />
        </div>
      )}
    </div>
  );
}

export default AudioRecorder;
