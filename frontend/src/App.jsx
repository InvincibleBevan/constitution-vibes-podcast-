import React, { useEffect, useState } from "react";

function App() {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("/api/episodes")
      .then((res) => res.json())
      .then((data) => setEpisodes(data))
      .catch((err) => console.error("Error fetching episodes:", err));
  }, []);

  return (
    <div className="relative min-h-screen flex flex-col items-center justify-center text-white bg-black">
      {/* Background video */}
      <video
        autoPlay
        loop
        muted
        className="absolute top-0 left-0 w-full h-full object-cover -z-10"
      >
        <source src="/kenya_flag.mp4" type="video/mp4" />
      </video>

      {/* Anthem audio */}
      <audio autoPlay loop>
        <source src="/anthem_instrumental.mp3" type="audio/mp3" />
      </audio>

      {/* Content */}
      <div className="bg-black bg-opacity-70 p-6 rounded-2xl shadow-xl">
        <h1 className="text-4xl font-bold mb-4">Constitution Vibes</h1>
        <h2 className="text-lg mb-6">Episodes</h2>
        <ul className="space-y-2">
          {episodes.length > 0 ? (
            episodes.map((ep, idx) => (
              <li key={idx} className="border-b border-gray-700 pb-2">
                <h3 className="text-xl">{ep.title}</h3>
                <p className="text-sm text-gray-400">{ep.date}</p>
                <audio controls className="mt-2 w-full">
                  <source src={ep.audio} type="audio/mpeg" />
                </audio>
              </li>
            ))
          ) : (
            <p>No episodes available.</p>
          )}
        </ul>
      </div>
    </div>
  );
}

export default App; // ✅ This fixes the build error
