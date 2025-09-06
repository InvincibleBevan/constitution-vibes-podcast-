import React, { useState, useEffect } from "react";

function App() {
  const [episodes, setEpisodes] = useState([]);
  const [current, setCurrent] = useState(null);

  // Fetch available episodes from backend
  useEffect(() => {
    fetch("/episodes")
      .then((res) => res.json())
      .then((data) => setEpisodes(data))
      .catch((err) => console.error("Failed to load episodes:", err));
  }, []);

  return (
    <div className="relative min-h-screen text-white">
      {/* Kenyan flag video background */}
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover -z-10"
      >
        <source src="/static/Kenya_flag.mp4" type="video/mp4" />
      </video>

      {/* Anthem playing in background */}
      <audio src="/static/anthem.mp3" autoPlay loop hidden />

      {/* Main content overlay */}
      <div className="bg-black bg-opacity-70 min-h-screen p-6 flex flex-col items-center">
        <h1 className="text-4xl font-bold mb-6 text-center">
          🇰🇪 Constitution Vibes Podcast
        </h1>

        {episodes.length === 0 ? (
          <p className="text-gray-300">No episodes yet. Run podcast.py to generate.</p>
        ) : (
          <ul className="space-y-4 w-full max-w-2xl">
            {episodes.map((ep, i) => (
              <li
                key={i}
                className="bg-gray-800 rounded-lg p-4 shadow-lg hover:bg-gray-700 cursor-pointer"
                onClick={() => setCurrent(ep)}
              >
                🎙️ {ep.replace(".mp3", "").replace("_", " ")}
              </li>
            ))}
          </ul>
        )}

        {current && (
          <div className="mt-6 w-full max-w-2xl bg-gray-900 p-4 rounded-lg">
            <h2 className="text-xl font-semibold mb-2">Now Playing: {current}</h2>
            <audio src={`/episodes/${current}`} controls autoPlay className="w-full" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
