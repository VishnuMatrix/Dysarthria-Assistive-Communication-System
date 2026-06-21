// import { useState } from "react";

// import Header from "./components/Header";
// import UploadCard from "./components/UploadCard";
// import AudioRecorder from "./components/AudioRecorder";
// import ResultCard from "./components/ResultCard";
// import LoadingSpinner from "./components/LoadingSpinner";

// import api from "./services/api";

// import "./index.css";

// function App() {
//   const [result, setResult] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [loadingMessage, setLoadingMessage] = useState("");

//   const handleRecordedAudio = async (blob) => {
//     try {
//       setLoading(true);
//       setLoadingMessage("Uploading Recording...");

//       const formData = new FormData();
//       formData.append("file", blob, "recording.wav");

//       setLoadingMessage("Extracting MFCC Features...");
//       const response = await api.post("/predict", formData);

//       setLoadingMessage("Generating Analysis Report...");
//       setResult(response.data);
//     } catch (error) {
//       console.error(error);
//       alert("Recording Analysis Failed");
//     } finally {
//       setLoading(false);
//       setLoadingMessage("");
//     }
//   };

//   return (
//     <div className="app">
//       <Header />

//       {loading && <LoadingSpinner message={loadingMessage} />}

//       <div className="dashboard">

//         {/* Top Row: Upload | Record | Download Report */}
//         <div className="top-row">
//           <UploadCard
//             setResult={setResult}
//             setLoading={setLoading}
//             setLoadingMessage={setLoadingMessage}
//           />

//           <AudioRecorder onAudioReady={handleRecordedAudio} />

//           {result?.report && (
//             <div className="report-card">
//               <h4>Analysis Report</h4>
//               <a
//                 href={`http://localhost:8000${result.report}`}
//                 target="_blank"
//                 rel="noreferrer"
//                 className="download-btn"
//               >
//                 📄 Download Full Report
//               </a>
//             </div>
//           )}
//         </div>

//         {/* Summary Stats Row */}
//         {result && (
//           <div className="summary-grid">
//             <div className="summary-card">
//               <h4>Prediction</h4>
//               <p className={result.prediction === "Normal Speech" ? "normal" : "dysarthric"}>
//                 {result.prediction}
//               </p>
//             </div>
//             <div className="summary-card">
//               <h4>Confidence</h4>
//               <p>{result.confidence}%</p>
//             </div>
//             <div className="summary-card">
//               <h4>Severity</h4>
//               <p>{result.severity_level}</p>
//             </div>
//             <div className="summary-card">
//               <h4>Emotion</h4>
//               <p>{result.emotion}</p>
//             </div>
//             <div className="summary-card">
//               <h4>Duration</h4>
//               <p>{result.duration} sec</p>
//             </div>
//             <div className="summary-card">
//               <h4>Speech Rate</h4>
//               <p>{result.speech_rate} WPM</p>
//             </div>
//             <div className="summary-card">
//               <h4>Speech Ratio</h4>
//               <p>{result.speech_ratio}%</p>
//             </div>
//             <div className="summary-card">
//               <h4>Avg Pitch</h4>
//               <p>{result.avg_pitch} Hz</p>
//             </div>
//           </div>
//         )}

//         {/* Full Result Card */}
//         <ResultCard result={result} />

//       </div>
//     </div>
//   );
// }

// export default App;

import { useState } from "react";

import Header from "./components/Header";
import UploadCard from "./components/UploadCard";
import AudioRecorder from "./components/AudioRecorder";
import ResultCard from "./components/ResultCard";
import LoadingSpinner from "./components/LoadingSpinner";

import api from "./services/api";
import "./index.css";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState("");

  const handleRecordedAudio = async (blob) => {
    try {
      setLoading(true);
      setLoadingMessage("Uploading Recording...");
      const formData = new FormData();
      formData.append("file", blob, "recording.wav");
      setLoadingMessage("Extracting MFCC Features...");
      const response = await api.post("/predict", formData);
      setLoadingMessage("Generating Analysis Report...");
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Recording Analysis Failed");
    } finally {
      setLoading(false);
      setLoadingMessage("");
    }
  };

  const NA = "—";

  return (
    <div className="app">
      <Header />
      {loading && <LoadingSpinner message={loadingMessage} />}

      <div className="dashboard">
        {/* ══ ROW 1: Upload | Record | Prediction | Severity | Confidence | Emotion ══ */}
        <div className="dashboard-row row-top">
          <UploadCard
            setResult={setResult}
            setLoading={setLoading}
            setLoadingMessage={setLoadingMessage}
          />

          <AudioRecorder onAudioReady={handleRecordedAudio} />

          {/* Prediction */}
          <div className="top-stat-card">
            <div className="tsc-icon pred-icon">🧠</div>
            <h4>Prediction</h4>
            {result ? (
              <p
                className={
                  result.prediction === "Normal Speech"
                    ? "label-normal"
                    : "label-dysarthric"
                }
              >
                {result.prediction}
              </p>
            ) : (
              <p className="tsc-empty">{NA}</p>
            )}
          </div>

          {/* Severity */}
          <div className="top-stat-card">
            <div className="tsc-icon sev-icon">📊</div>
            <h4>Severity</h4>
            {result ? (
              <>
                <p className="tsc-value sev-value">{result.severity_level}</p>
                <span className="tsc-sub">
                  Score: {result.severity_score}/100
                </span>
                <div className="tsc-bar">
                  <div
                    className="tsc-fill sev-fill"
                    style={{ width: `${result.severity_score}%` }}
                  />
                </div>
              </>
            ) : (
              <p className="tsc-empty">{NA}</p>
            )}
          </div>

          {/* Confidence */}
          <div className="top-stat-card">
            <div className="tsc-icon conf-icon">🎯</div>
            <h4>Confidence</h4>
            {result ? (
              <>
                <p className="tsc-value conf-value">{result.confidence}%</p>
                <div className="tsc-bar">
                  <div
                    className="tsc-fill conf-fill"
                    style={{ width: `${result.confidence}%` }}
                  />
                </div>
              </>
            ) : (
              <p className="tsc-empty">{NA}</p>
            )}
          </div>

          {/* Emotion */}
          <div className="top-stat-card">
            <div className="tsc-icon emo-icon">😊</div>
            <h4>Emotion</h4>
            {result ? (
              <p className="tsc-value emo-value">{result.emotion}</p>
            ) : (
              <p className="tsc-empty">{NA}</p>
            )}
          </div>
        </div>

        {/* ══ ROW 2: Duration | Speech Rate | Total Words | Volume | Noise | Speech Ratio ══ */}
        <div className="dashboard-row row-stats">
          <div className="mini-stat-card">
            <div className="msc-icon">⏱️</div>
            <div>
              <h4>Duration</h4>
              <p>{result ? `${result.duration} sec` : NA}</p>
            </div>
          </div>

          <div className="mini-stat-card">
            <div className="msc-icon">📈</div>
            <div>
              <h4>Speech Rate</h4>
              <p>{result ? `${result.speech_rate} WPM` : NA}</p>
            </div>
          </div>

          <div className="mini-stat-card">
            <div className="msc-icon">📝</div>
            <div>
              <h4>Total Words</h4>
              <p>{result ? result.words : NA}</p>
            </div>
          </div>

          <div className="mini-stat-card">
            <div className="msc-icon">🔊</div>
            <div>
              <h4>Volume</h4>
              <p>{result ? result.volume : NA}</p>
            </div>
          </div>

          <div className="mini-stat-card">
            <div className="msc-icon">🎚️</div>
            <div>
              <h4>Noise Level</h4>
              <p>{result ? result.noise : NA}</p>
            </div>
          </div>

          <div className="mini-stat-card">
            <div className="msc-icon">⏳</div>
            <div>
              <h4>Speech Ratio</h4>
              <p>{result ? `${result.speech_ratio}%` : NA}</p>
            </div>
          </div>
        </div>

        {/* ══ Detailed sections — only when result exists ══ */}
        {result && <ResultCard result={result} />}

        {!result && (
          <div className="empty-state">
            🎤 Upload or record an audio file above to see the full analysis
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
