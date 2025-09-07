import React, { useEffect, useState } from "react";

function App() {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("/episodes")
      .then((res) => res.json())
      .then((data) => setEpisodes(data))
      .catch((err) => console.error("Error fetching episodes:", err));
  }, []);

  return (
    <div className="relative w-full h-screen overflow-hidden">
      {/* Fullscreen video background */}
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover"
      >
        <source src="/static/Kenya_flag.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      {/* Background anthem (plays automatically) */}
      <audio autoPlay loop>
        <source src="/static/anthem.mp3" type="audio/mpeg" />
        Your browser does not support the audio element.
      </audio>

      {/* Overlay content */}
      <div className="absolute inset-0 bg-black bg-opacity-50 flex flex-col items-center justify-center text-white p-6">
        <h1 className="text-4xl md:text-6xl font-bold mb-6 text-center">
          Constitution Vibes Podcast
        </h1>
        <p className="text-lg md:text-2xl mb-8 text-center max-w-2xl">
          Kenyan Constitution explained with vibes, sheng, and the spirit of the nation 🇰🇪
        </p>

        {/* Episodes list */}
        <div className="w-full max-w-3xl space-y-4">
          {episodes.length === 0 ? (
            <p className="text-center text-gray-300">
              🎙️ No episodes yet… check back soon!
            </p>
          ) : (
            episodes.map((ep, idx) => (
              <div
                key={idx}
                className="bg-white bg-opacity-10 p-4 rounded-xl shadow-lg hover:bg-opacity-20 transition"
              >
                <h2 className="text-2xl font-semibold">{ep.title}</h2>
                <p className="text-gray-200">{ep.description}</p>
                <audio controls className="w-full mt-2">
                  <source src={ep.file} type="audio/mpeg" />
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
