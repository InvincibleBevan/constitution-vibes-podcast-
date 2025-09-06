import React, { useEffect, useState } from "react";

export default function App() {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("/episodes")
      .then((res) => res.json())
      .then((data) => setEpisodes(data))
      .catch((err) => console.error("Failed to load episodes:", err));
  }, []);

  return (
    <div className="w-full h-screen relative overflow-hidden bg-black text-white">
      {/* Background Video */}
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover z-0"
      >
        <source src="/static/Kenya_flag.mp4" type="video/mp4" />
      </video>

      {/* Dark overlay for readability */}
      <div className="absolute top-0 left-0 w-full h-full bg-black bg-opacity-50 z-10"></div>

      {/* Anthem Audio */}
      <audio autoPlay loop>
        <source src="/static/anthem.mp3" type="audio/mpeg" />
      </audio>

      {/* Main Content */}
      <div className="relative z-20 flex flex-col items-center justify-center h-full px-6">
        <h1 className="text-4xl md:text-6xl font-bold mb-6 text-center">
          Constitution Vibes Podcast 🇰🇪
        </h1>
        <p className="text-lg md:text-2xl mb-10 text-center">
          Breaking down Kenya’s Constitution with vibes, freedom, and unity.
        </p>

        {/* Episodes List */}
        <div className="bg-white bg-opacity-20 p-6 rounded-2xl shadow-lg w-full max-w-2xl">
          <h2 className="text-2xl font-semibold mb-4 text-center">🎧 Episodes</h2>
          {episodes.length === 0 ? (
            <p className="text-center">Loading episodes...</p>
          ) : (
            <ul className="space-y-4">
              {episodes.map((ep, i) => (
                <li key={i} className="flex flex-col items-center bg-black bg-opacity-40 p-4 rounded-xl">
                  <p className="mb-2 text-lg font-medium">{ep}</p>
                  <audio controls className="w-full">
                    <source src={`/episodes/${ep}`} type="audio/mpeg" />
                  </audio>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
