import React, { useEffect, useState } from "react";

function App() {
  const [episodes, setEpisodes] = useState([]);
  const [password, setPassword] = useState("");
  const [status, setStatus] = useState("");

  useEffect(() => {
    fetch("/api/episodes")
      .then((res) => res.json())
      .then((data) => setEpisodes(data));
  }, [status]);

  const regenerate = async () => {
    const res = await fetch("/api/regenerate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    });
    const data = await res.json();
    if (data.error) {
      setStatus("❌ Wrong password");
    } else {
      setStatus("✅ Episodes regenerated");
    }
  };

  return (
    <div className="relative min-h-screen bg-black text-white flex flex-col items-center justify-center">
      {/* Background Video */}
      <video
        autoPlay
        loop
        muted
        className="fixed top-0 left-0 w-full h-full object-cover -z-10"
      >
        <source src="/static/bg.mp4" type="video/mp4" />
      </video>

      {/* Overlay */}
      <div className="bg-black bg-opacity-70 p-8 rounded-2xl shadow-xl text-center max-w-3xl w-full">
        <h1 className="text-4xl font-bold mb-4">🇰🇪 Constitution Vibes Podcast</h1>
        <p className="mb-6">Celebrating Kenya with vibes, unity, and knowledge.</p>

        {episodes.length === 0 ? (
          <p>No episodes yet. Use the admin panel below.</p>
        ) : (
          <div className="space-y-4">
            {episodes.map((ep, idx) => (
              <div key={idx} className="p-4 bg-gray-900 rounded-xl shadow">
                <h2 className="text-xl font-semibold">{ep.title}</h2>
                <audio controls className="mt-2 w-full">
                  <source src={ep.url} type="audio/mp3" />
                </audio>
              </div>
            ))}
          </div>
        )}

        {/* Admin Section */}
        <div className="mt-8 p-4 bg-gray-800 rounded-xl shadow">
          <h2 className="text-lg font-semibold mb-2">🔑 Admin</h2>
          <input
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="p-2 rounded text-black w-full"
          />
          <button
            onClick={regenerate}
            className="mt-2 px-4 py-2 bg-green-600 rounded-xl shadow hover:bg-green-700"
          >
            Regenerate Episodes
          </button>
          {status && <p className="mt-2">{status}</p>}
        </div>
      </div>
    </div>
  );
}

export default App;
