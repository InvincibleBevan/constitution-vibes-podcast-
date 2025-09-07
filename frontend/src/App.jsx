import { useState, useEffect } from "react";

export default function App() {
  const [episode, setEpisode] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Play anthem on load
    const anthem = document.getElementById("anthem");
    anthem.volume = 0.5;
    anthem.play().catch(() => {
      console.log("Autoplay blocked, user interaction needed.");
    });

    // Fetch first episode
    fetchEpisode();
  }, []);

  async function fetchEpisode() {
    setLoading(true);
    try {
      const res = await fetch("/generate", { method: "POST" });
      const data = await res.json();
      if (data.success) {
        setEpisode(data);
      } else {
        console.error("Error:", data.error);
      }
    } catch (err) {
      console.error("Fetch failed:", err);
    }
    setLoading(false);
  }

  return (
    <div className="relative w-screen h-screen overflow-hidden">
      {/* Kenyan flag fullscreen video */}
      <video
        src="/static/Kenya_flag.mp4"
        autoPlay
        muted
        loop
        playsInline
        className="absolute inset-0 w-full h-full object-cover -z-10"
      />

      {/* Anthem audio */}
      <audio id="anthem" src="/static/anthem.mp3" loop />

      {/* Overlay content */}
      <div className="relative z-10 flex flex-col items-center justify-center h-full bg-black/60 text-white p-6 text-center">
        <h1 className="text-4xl font-bold mb-4">🇰🇪 Constitution Vibes Podcast</h1>

        {loading && <p className="text-lg">Loading episode...</p>}

        {episode && (
          <>
            <p className="max-w-2xl text-lg mb-6">{episode.script}</p>
            <audio controls autoPlay src={`/${episode.audio_file}`} className="w-full max-w-md" />
          </>
        )}

        <button
          onClick={fetchEpisode}
          className="mt-6 px-6 py-3 bg-red-600 hover:bg-red-700 rounded-xl shadow-lg"
        >
          🎙️ Generate New Episode
        </button>
      </div>
    </div>
  );
}
