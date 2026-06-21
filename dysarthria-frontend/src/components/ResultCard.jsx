// import "../style/ResultCard.css";

// function ResultCard({ result }) {
//   if (!result) {
//     return (
//       <div className="result-card">
//         <h2>Analysis Result</h2>
//         <p>Upload an audio file and click Analyze Speech.</p>
//       </div>
//     );
//   }

//   const timestamp = Date.now();

//   return (
//     <div className="result-card">
//       {/* ── Severity & Confidence Progress Bars ── */}
//       <div className="two-col-grid">
//         <div className="result-section">
//           <h3>Dysarthria Severity</h3>
//           <div className="progress">
//             <div
//               className="progress-fill"
//               style={{ width: `${result.severity_score}%` }}
//             />
//           </div>
//           <p>Score: {result.severity_score}/100</p>
//           <p>Level: {result.severity_level}</p>
//         </div>

//         <div className="result-section">
//           <h3>Confidence</h3>
//           <div className="progress">
//             <div
//               className="progress-fill confidence-fill"
//               style={{ width: `${result.confidence}%` }}
//             />
//           </div>
//           <p>{result.confidence}%</p>
//         </div>
//       </div>

//       {/* ── Audio & Transcript ── */}
//       <h2 className="section-title">Audio &amp; Transcript</h2>

//       <div className="two-col-grid">
//         <div className="result-section">
//           <h3>Original Audio</h3>
//           <p className="debug-path">{result.original_audio}</p>
//           <audio key={result.original_audio} controls>
//             <source
//               src={`http://localhost:8000${result.original_audio}?v=${timestamp}`}
//               type="audio/wav"
//             />
//           </audio>
//         </div>

//         <div className="result-section">
//           <h3>Transcript</h3>
//           <p>{result.transcript}</p>
//         </div>
//       </div>

//       <div className="two-col-grid">
//         {result.enhanced_audio && (
//           <div className="result-section">
//             <h3>Enhanced Audio</h3>
//             <p className="debug-path">{result.enhanced_audio}</p>
//             <audio key={result.enhanced_audio} controls preload="none">
//               <source
//                 src={`http://localhost:8000${result.enhanced_audio}?v=${timestamp}`}
//                 type="audio/wav"
//               />
//             </audio>
//           </div>
//         )}

//         <div className="result-section">
//           <h3>Generated Speech</h3>
//           <p className="debug-path">{result.audio_file}</p>
//           <audio key={result.audio_file} controls>
//             <source
//               src={`http://localhost:8000${result.audio_file}?v=${timestamp}`}
//               type="audio/mpeg"
//             />
//           </audio>
//           <br />
//           <a
//             href={`http://localhost:8000${result.audio_file}?v=${timestamp}`}
//             download
//             className="download-btn"
//           >
//             ⬇️ Download Generated Audio
//           </a>
//         </div>
//       </div>

//       {/* ── Analytics Grid ── */}
//       <h2 className="section-title">Speech Analytics</h2>

//       <div className="analytics-grid">
//         <div className="result-section">
//           <h3>Speech Analysis</h3>
//           <p>Duration: {result.duration} sec</p>
//           <p>Total Words: {result.words}</p>
//           <p>Speaking Rate: {result.speech_rate} WPM</p>
//           <p>Volume: {result.volume}</p>
//           <p>Noise Level: {result.noise}</p>
//         </div>

//         <div className="result-section">
//           <h3>Pitch Analysis</h3>
//           <p>Average Pitch: {result.avg_pitch} Hz</p>
//           <p>Minimum Pitch: {result.min_pitch} Hz</p>
//           <p>Maximum Pitch: {result.max_pitch} Hz</p>
//           <p>Pitch Range: {result.pitch_range} Hz</p>
//         </div>

//         <div className="result-section">
//           <h3>Voice Activity Detection</h3>
//           <p>Speech Duration: {result.speech_duration} sec</p>
//           <p>Silence Duration: {result.silence_duration} sec</p>
//           <p>Speech Ratio: {result.speech_ratio} %</p>
//           <p>Voice Segments: {result.segments}</p>
//         </div>

//         <div className="result-section">
//           <h3>Formant Analysis</h3>
//           <p>F1: {result.F1} Hz</p>
//           <p>F2: {result.F2} Hz</p>
//           <p>F3: {result.F3} Hz</p>
//         </div>
//       </div>

//       {/* ── Clinical Assessment ── */}
//       <h2 className="section-title">Clinical Assessment</h2>

//       <div className="two-col-grid">
//         <div className="result-section">
//           <h3>Clinical Speech Comparison</h3>
//           <p>
//             Pitch Status: <strong>{result.pitch_status}</strong>
//           </p>
//           <p>
//             Speech Rate Status: <strong>{result.speech_rate_status}</strong>
//           </p>
//           <p>
//             Speech Ratio Status: <strong>{result.speech_ratio_status}</strong>
//           </p>
//           <p>
//             Clinical Assessment: <strong>{result.clinical_assessment}</strong>
//           </p>
//         </div>

//         <div className="result-section">
//           <h3>Audio Comparison</h3>
//           <p>Original Volume: {result.original_volume}</p>
//           <p>Enhanced Volume: {result.enhanced_volume}</p>
//           <p>Noise Reduction: {result.noise_reduction} %</p>
//           <p>Volume Improvement: {result.volume_improvement} %</p>
//         </div>
//       </div>

//       <div className="result-section">
//         <h3>Emotion Detection</h3>
//         <p>Emotion: {result.emotion}</p>
//         <p>Emotion Pitch: {result.emotion_pitch} Hz</p>
//         <p>Energy: {result.emotion_energy}</p>
//       </div>

//       {/* ── Visual Analysis ── */}
//       <h2 className="section-title">Visual Analysis</h2>

//       <div className="two-col-grid">
//         {result.waveform && (
//           <div className="result-section">
//             <h3>Waveform</h3>
//             <img
//               src={`http://localhost:8000${result.waveform}?v=${timestamp}`}
//               alt="Waveform"
//               className="analysis-image"
//             />
//           </div>
//         )}

//         {result.mfcc_image && (
//           <div className="result-section">
//             <h3>MFCC Features</h3>
//             <img
//               src={`http://localhost:8000${result.mfcc_image}?v=${timestamp}`}
//               alt="MFCC"
//               className="analysis-image"
//             />
//           </div>
//         )}
//       </div>

//       <div className="two-col-grid">
//         {result.spectrogram && (
//           <div className="result-section">
//             <h3>Spectrogram</h3>
//             <img
//               src={`http://localhost:8000${result.spectrogram}?v=${timestamp}`}
//               alt="Spectrogram"
//               className="analysis-image"
//             />
//           </div>
//         )}

//         {result.pitch_image && (
//           <div className="result-section">
//             <h3>Pitch Contour</h3>
//             <img
//               src={`http://localhost:8000${result.pitch_image}?v=${timestamp}`}
//               alt="Pitch Contour"
//               className="analysis-image"
//             />
//           </div>
//         )}
//       </div>
//     </div>
//   );
// }

// export default ResultCard;
import "../style/ResultCard.css";

function ResultCard({ result }) {
  const timestamp = Date.now();

  return (
    <div className="result-wrapper">
      {/* ══ Audio & Transcript label ══ */}
      <div className="row-section-label">
        <h2>Audio &amp; Transcript</h2>
      </div>

      {/* ══ ROW 3: Original | Enhanced | Generated | Transcript ══ */}
      <div className="dashboard-row row-audio">
        <div className="dash-card">
          <h3>Original Audio</h3>
          <p className="debug-path">{result.original_audio}</p>
          <audio key={result.original_audio} controls>
            <source
              src={`http://localhost:8000${result.original_audio}?v=${timestamp}`}
              type="audio/wav"
            />
          </audio>
        </div>

        {result.enhanced_audio ? (
          <div className="dash-card">
            <h3>Enhanced Audio</h3>
            <p className="debug-path">{result.enhanced_audio}</p>
            <audio key={result.enhanced_audio} controls preload="none">
              <source
                src={`http://localhost:8000${result.enhanced_audio}?v=${timestamp}`}
                type="audio/wav"
              />
            </audio>
          </div>
        ) : (
          <div className="dash-card placeholder-card">
            <p>No enhanced audio</p>
          </div>
        )}

        <div className="dash-card">
          <h3>Generated Speech</h3>
          <p className="debug-path">{result.audio_file}</p>
          <audio key={result.audio_file} controls>
            <source
              src={`http://localhost:8000${result.audio_file}?v=${timestamp}`}
              type="audio/mpeg"
            />
          </audio>
          <a
            href={`http://localhost:8000${result.audio_file}?v=${timestamp}`}
            download
            className="dl-btn"
          >
            ⬇ Download Generated Audio
          </a>
        </div>

        <div className="dash-card transcript-card">
          <h3>Transcript</h3>
          <p className="transcript-text">{result.transcript}</p>
        </div>
      </div>

      {/* ══ Visual Analysis label ══ */}
      <div className="row-section-label">
        <h2>Visual Analysis</h2>
      </div>

      {/* ══ ROW 4: Waveform | MFCC | Spectrogram | Pitch Contour ══ */}
      <div className="dashboard-row row-visuals">
        {result.waveform ? (
          <div className="dash-card">
            <h3>Waveform</h3>
            <img
              src={`http://localhost:8000${result.waveform}?v=${timestamp}`}
              alt="Waveform"
              className="analysis-image"
            />
          </div>
        ) : (
          <div className="dash-card placeholder-card">
            <p>No waveform</p>
          </div>
        )}

        {result.mfcc_image ? (
          <div className="dash-card">
            <h3>MFCC Features</h3>
            <img
              src={`http://localhost:8000${result.mfcc_image}?v=${timestamp}`}
              alt="MFCC"
              className="analysis-image"
            />
          </div>
        ) : (
          <div className="dash-card placeholder-card">
            <p>No MFCC</p>
          </div>
        )}

        {result.spectrogram ? (
          <div className="dash-card">
            <h3>Spectrogram</h3>
            <img
              src={`http://localhost:8000${result.spectrogram}?v=${timestamp}`}
              alt="Spectrogram"
              className="analysis-image"
            />
          </div>
        ) : (
          <div className="dash-card placeholder-card">
            <p>No spectrogram</p>
          </div>
        )}

        {result.pitch_image ? (
          <div className="dash-card">
            <h3>Pitch Contour</h3>
            <img
              src={`http://localhost:8000${result.pitch_image}?v=${timestamp}`}
              alt="Pitch Contour"
              className="analysis-image"
            />
          </div>
        ) : (
          <div className="dash-card placeholder-card">
            <p>No pitch image</p>
          </div>
        )}
      </div>

      {/* ══ ROW 5: Speech | Pitch | VAD | Formant | Clinical | Audio Comparison ══ */}
      <div className="dashboard-row row-analytics">
        <div className="dash-card analytics-card">
          <h3>Speech Analytics</h3>
          <ul className="stat-list">
            <li>
              <span>Duration</span>
              <strong>{result.duration} sec</strong>
            </li>
            <li>
              <span>Words</span>
              <strong>{result.words}</strong>
            </li>
            <li>
              <span>Speech Rate</span>
              <strong>{result.speech_rate} WPM</strong>
            </li>
            <li>
              <span>Volume</span>
              <strong>{result.volume}</strong>
            </li>
            <li>
              <span>Noise</span>
              <strong>{result.noise}</strong>
            </li>
          </ul>
        </div>

        <div className="dash-card analytics-card">
          <h3>Pitch Analysis</h3>
          <ul className="stat-list">
            <li>
              <span>Avg Pitch</span>
              <strong>{result.avg_pitch} Hz</strong>
            </li>
            <li>
              <span>Min Pitch</span>
              <strong>{result.min_pitch} Hz</strong>
            </li>
            <li>
              <span>Max Pitch</span>
              <strong>{result.max_pitch} Hz</strong>
            </li>
            <li>
              <span>Pitch Range</span>
              <strong>{result.pitch_range} Hz</strong>
            </li>
          </ul>
        </div>

        <div className="dash-card analytics-card">
          <h3>Voice Activity Detection</h3>
          <ul className="stat-list">
            <li>
              <span>Speech Dur.</span>
              <strong>{result.speech_duration} sec</strong>
            </li>
            <li>
              <span>Silence Dur.</span>
              <strong>{result.silence_duration} sec</strong>
            </li>
            <li>
              <span>Speech Ratio</span>
              <strong>{result.speech_ratio}%</strong>
            </li>
            <li>
              <span>Segments</span>
              <strong>{result.segments}</strong>
            </li>
          </ul>
        </div>

        <div className="dash-card analytics-card">
          <h3>Formant Analysis</h3>
          <ul className="stat-list">
            <li>
              <span>F1</span>
              <strong>{result.F1} Hz</strong>
            </li>
            <li>
              <span>F2</span>
              <strong>{result.F2} Hz</strong>
            </li>
            <li>
              <span>F3</span>
              <strong>{result.F3} Hz</strong>
            </li>
          </ul>
        </div>

        <div className="dash-card analytics-card">
          <h3>Clinical Assessment</h3>
          <ul className="stat-list dot-list">
            <li>
              <span>Pitch Status</span>
              <strong>{result.pitch_status}</strong>
            </li>
            <li>
              <span>Speech Rate</span>
              <strong>{result.speech_rate_status}</strong>
            </li>
            <li>
              <span>Speech Ratio</span>
              <strong>{result.speech_ratio_status}</strong>
            </li>
            <li>
              <span>Assessment</span>
              <strong>{result.clinical_assessment}</strong>
            </li>
          </ul>
        </div>

        <div className="dash-card analytics-card">
          <h3>Audio Comparison</h3>
          <ul className="stat-list">
            <li>
              <span>Orig. Volume</span>
              <strong>{result.original_volume}</strong>
            </li>
            <li>
              <span>Enh. Volume</span>
              <strong>{result.enhanced_volume}</strong>
            </li>
            <li>
              <span>Noise Reduc.</span>
              <strong>{result.noise_reduction}%</strong>
            </li>
            <li>
              <span>Vol. Improve</span>
              <strong>{result.volume_improvement}%</strong>
            </li>
          </ul>
        </div>
      </div>

      {/* ══ ROW 6: Download Report ══ */}
      {result.report && (
        <div className="dashboard-row row-report">
          <div className="dash-card report-card">
            <p>
              Complete AI report with all measurements, visualizations and
              clinical assessment.
            </p>
            <a
              href={`http://localhost:8000${result.report}`}
              target="_blank"
              rel="noreferrer"
              className="report-btn"
            >
              📄 Download Full PDF Report
            </a>
          </div>
        </div>
      )}
    </div>
  );
}

export default ResultCard;
