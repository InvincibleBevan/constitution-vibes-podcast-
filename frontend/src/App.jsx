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
    <div className="relative h-screen w-screen overflow-hidden bg-black text-white">
      {/* Background Kenyan flag video */}
      <video
        className="absolute top-0 left-0 w-full h-full object-cover"
        src="/kenya_flag.mp4"
        autoPlay
        loop
        muted
      />

      {/* Anthem audio */}
      <audio src="/anthem_instrumental.mp3" autoPlay loop />

      {/* Overlay */}
      <div className="absolute inset-0 bg-black bg-opacity-70 flex flex-col items-center justify-center">
        <h1 className="text-4xl font-bold mb-6">🇰🇪 Constitution Vibes</h1>
        <p className="mb-8 text-lg text-gray-300">
          Kenyan Constitution, explained in style.
        </p>

        {/* Podcast episodes */}
        <div className="w-3/4 max-w-2xl space-y-4">
          {episodes.length === 0 ? (
            <p className="text-gray-400">No episodes available yet.</p>
          ) : (
            episodes.map((ep, i) => (
              <div
                key={i}
                className="bg-gray-900 bg-opacity-80 rounded-xl p-4 shadow-lg"
              >
                <h2 className="text-xl font-semibold mb-2">{ep.title}</h2>
                <audio controls className="w-full">
                  <source src={ep.file} type="audio/mpeg" />
                  Your browser does not support the audio element.
                </audio>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
