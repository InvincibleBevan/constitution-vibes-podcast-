import React, { useEffect, useState } from "react";

export default function App() {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("/episodes")
      .then((res) => res.json())
      .then(setEpisodes);
  }, []);

  return (
    <div className="relative w-full h-screen overflow-hidden">
      {/* Background Video */}
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover"
      >
        <source src="/Kenya_flag.mp4" type="video/mp4" />
      </video>

      {/* Overlay */}
      <div className="absolute inset-0 bg-black/60 flex flex-col items-center justify-center text-center">
        <h1 className="text-4xl font-bold mb-6">🇰🇪 Constitution Vibes</h1>
        <p className="mb-8 text-lg">Kenya’s Constitution, Simplified for Everyone</p>

        <audio autoPlay loop>
          <source src="/anthem_instrumental.mp3" type="audio/mpeg" />
        </audio>

        <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 w-3/4 max-w-2xl">
          <h2 className="text-2xl mb-4">🎧 Latest Episodes</h2>
          {episodes.length === 0 ? (
            <p>No episodes uploaded yet.</p>
          ) : (
            <ul className="space-y-4">
              {episodes.map((ep, idx) => (
                <li key={idx}>
                  <audio controls preload="none" className="w-full">
                    <source src={`/episodes/${ep}`} type="audio/mpeg" />
                  </audio>
                  <p className="mt-2">{ep}</p>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
