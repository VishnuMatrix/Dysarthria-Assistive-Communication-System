import { useState } from "react";

import UploadCard from "../components/UploadCard";
import ResultCard from "../components/ResultCard";

import "../style/Home.css";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <div className="home">
      <div className="hero">
        <h1>Dysarthria Assistive Communication System</h1>

        <p>Detect dysarthric speech and analyze audio samples.</p>
      </div>

      <div className="container">
        <div className="left-panel">
          <UploadCard setResult={setResult} />
        </div>

        <div className="right-panel">
          <ResultCard result={result} />
        </div>
      </div>
    </div>
  );
}

export default Home;
