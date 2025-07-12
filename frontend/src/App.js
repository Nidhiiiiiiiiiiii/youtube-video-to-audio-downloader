// import React, { useState } from 'react';
// import axios from 'axios';

// function App() {
//   const [youtubeURL, setYoutubeURL] = useState('');
//   const [downloadLink, setDownloadLink] = useState('');

//   const handleDownload = async () => {
//     const formData = new FormData();
//     formData.append('youtube_url', youtubeURL);

//     try {
//       const response = await axios.post('http://localhost:8000/download-audio/', formData);
//       setDownloadLink(response.data.file);
//     } catch (error) {
//       alert('Error downloading audio');
//       console.error(error);
//     }
//   };

//   return (
//     <div style={{ padding: '2rem' }}>
//       <h2>YouTube to Audio Converter</h2>
//       <input
//         type="text"
//         placeholder="Paste YouTube link here"
//         value={youtubeURL}
//         onChange={(e) => setYoutubeURL(e.target.value)}
//         style={{ width: '300px', marginRight: '10px' }}
//       />
//       <button onClick={handleDownload}>Convert to Audio</button>

//       {downloadLink && (
//         <div style={{ marginTop: '20px' }}>
//           <a href={downloadLink} download>Download Audio</a>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;


import React, { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [message, setMessage] = useState("");

  const handleDownload = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/download-audio/", {
        url: url,
      });
      setMessage(res.data.message + ": " + res.data.filename);
    } catch (err) {
      setMessage("Error: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>YouTube to MP3</h2>
      <input
        type="text"
        value={url}
        placeholder="Paste YouTube link"
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "300px", padding: "0.5rem" }}
      />
      <button onClick={handleDownload} style={{ marginLeft: "1rem", padding: "0.5rem 1rem" }}>
        Download
      </button>
      <p>{message}</p>
    </div>
  );
}

export default App;
