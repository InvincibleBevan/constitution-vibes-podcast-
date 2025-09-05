import React, { useEffect, useState } from "react";

function App() {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("/api/episodes")
      .then((res) => res.json())
      .then((data) => setEpisodes(data));
  }, []);

  return (
    <div className="relative w-full h-screen overflow-hidden text-white">
      {/* Background Video */}
      <video
        className="absolute top-0 left-0 w-full h-full object-cover"
        src="/static/Kenya_flag.mp4"
        autoPlay
        muted
        loop
        playsInline
      ></video>

      {/* Dark overlay */}
      <div className="absolute top-0 left-0 w-full h-full bg-black bg-opacity-60"></div>

      {/* Anthem autoplay (low volume) */}
      <audio src="/static/anthem_instrumental.mp3" autoPlay loop controls={false} />

      {/* Content */}
      <div className="relative z-10 flex flex-col items-center p-6">
        <h1 className="text-4xl font-bold mb-6 text-center">
          🇰🇪 Constitution Vibes Podcast
        </h1>
        <p className="text-lg mb-8 text-center max-w-2xl">
          Breaking down the Constitution of Kenya for Wanjiku, prepared with SiR J,
          powered by VibesOfTheTribe.
        </p>

        {/* Episodes list */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl">
          {episodes.map((ep, index) => (
            <div
              key={index}
              className="bg-gray-900 bg-opacity-80 rounded-xl shadow-lg p-4 hover:scale-105 transition"
            >
              <h2 className="text-xl font-semibold mb-2">{ep.title}</h2>
              <audio controls className="w-full">
                <source src={ep.url} type="audio/mpeg" />
                Your browser does not support the audio element.
              </audio>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
