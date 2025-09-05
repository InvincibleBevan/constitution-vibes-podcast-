import React, { useEffect, useState } from "react";

export default function App() {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("/episodes") // new endpoint from Flask
      .then((res) => res.json())
      .then((data) => setEpisodes(data))
      .catch((err) => console.error("Error fetching episodes:", err));
  }, []);

  return (
    <div className="relative w-full h-screen text-white">
      {/* Background video */}
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover -z-10"
      >
        <source src="/static/Kenya_flag.mp4" type="video/mp4" />
      </video>

      {/* Content */}
      <div className="relative flex flex-col items-center justify-center h-full bg-black bg-opacity-50">
        <h1 className="text-4xl font-bold mb-6 drop-shadow-lg">
          🇰🇪 Constitution Vibes Podcast
        </h1>

        <h3 className="text-xl mb-4">Latest Episodes:</h3>
        <ul className="space-y-6 w-3/4 max-w-2xl">
          {episodes.length > 0 ? (
            episodes.map((file, i) => (
              <li key={i} className="text-lg text-center">
                🎧 {file}
                <br />
                <audio controls preload="none" className="w-full mt-2">
                  <source src={`/episodes/${file}`} type="audio/mpeg" />
                  Your browser does not support the audio element.
                </audio>
              </li>
            ))
          ) : (
            <p>No episodes available yet. Generate from Admin panel.</p>
          )}
        </ul>

        <p className="mt-8">
          <a href="/admin" className="text-green-400 hover:underline">
            Admin Panel
          </a>
        </p>
      </div>
    </div>
  );
}
