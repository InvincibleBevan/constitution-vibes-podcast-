import { useEffect, useRef, useState } from "react";
import { Play, Pause, Download, Volume2, VolumeX } from "lucide-react";

export default function App() {
  const [episodes, setEpisodes] = useState([]);
  const [current, setCurrent] = useState(null);
  const [audio, setAudio] = useState(null);
  const [bgReady, setBgReady] = useState(false);
  const [bgMuted, setBgMuted] = useState(false);
  const bgAudioRef = useRef(null);

  useEffect(() => {
    fetch("/api/episodes")
      .then((r) => r.json())
      .then((data) => setEpisodes(data))
      .catch(() => setEpisodes([]));
  }, []);

  useEffect(() => {
    const bg = new Audio("/anthem_instrumental.mp3");
    bg.loop = true;
    bg.volume = 0.25;
    bgAudioRef.current = bg;
    bg.play().then(() => {
      setBgReady(true);
    }).catch(() => {
      setBgReady(false); // needs user gesture
    });
    return () => {
      bg.pause();
      bg.currentTime = 0;
    };
  }, []);

  const toggleBg = () => {
    const bg = bgAudioRef.current;
    if (!bg) return;
    if (bg.paused) {
      bg.play();
      setBgMuted(false);
    } else {
      bg.pause();
      setBgMuted(true);
    }
  };

  const playEpisode = (file) => {
    if (audio) {
      audio.pause();
    }
    const newAudio = new Audio(`/episodes/${file}`);
    // lower background slightly while narration plays
    if (bgAudioRef.current && !bgAudioRef.current.paused) {
      bgAudioRef.current.volume = 0.12;
      newAudio.addEventListener("ended", () => {
        bgAudioRef.current.volume = 0.25;
      });
    }
    newAudio.play();
    setAudio(newAudio);
    setCurrent(file);
  };

  return (
    <div className="min-h-screen relative overflow-hidden">
      {/* Kenyan flag animated background */}
      <div className="absolute inset-0 -z-10">
        <video autoPlay loop muted className="w-full h-full object-cover opacity-20">
          <source src="/kenya_flag.mp4" type="video/mp4" />
        </video>
        <div className="absolute inset-0 bg-gradient-to-b from-black/70 via-black/40 to-black/90" />
      </div>

      <header className="py-8 text-center">
        <h1 className="text-3xl md:text-4xl font-bold">
          <span className="text-green-500">🇰🇪 Constitution Vibes</span>{" "}
          <span className="text-white/80">Podcast</span>
        </h1>
        <p className="text-white/60 mt-2">Prepared with <span className="text-green-400">SiR J</span>, powered by <span className="text-red-400">VibesOfTheTribe</span></p>
      </header>

      <main className="container mx-auto px-4 pb-24">
        {/* Background audio control */}
        <div className="flex justify-center mb-6">
          <button
            onClick={toggleBg}
            className="glass rounded-2xl px-4 py-2 flex items-center gap-2 hover:bg-white/10 transition"
            title="Toggle background anthem"
          >
            {bgAudioRef.current && !bgAudioRef.current.paused ? <Volume2 size={18} /> : <VolumeX size={18} />}
            <span>{bgAudioRef.current && !bgAudioRef.current.paused ? "Mute background" : "Enable background audio"}</span>
          </button>
        </div>

        {!bgReady && (
          <div className="max-w-xl mx-auto glass rounded-2xl p-4 text-center text-sm text-white/80 mb-6">
            Your browser blocked autoplay with sound. Click <b>Enable background audio</b> above.
          </div>
        )}

        <div className="max-w-3xl mx-auto grid gap-3">
          {episodes.length === 0 && (
            <div className="glass rounded-2xl p-6 text-center text-white/70">
              No episodes found yet. Run <code className="bg-black/50 px-2 py-1 rounded">python generator/build_episodes.py</code> to generate them.
            </div>
          )}
          {episodes.map((ep, i) => (
            <div key={i} className="glass rounded-2xl p-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-green-600/80 flex items-center justify-center font-bold">{i+1}</div>
                <span className="text-base md:text-lg">{ep.title}</span>
              </div>
              <div className="flex items-center gap-3">
                <button
                  onClick={() => playEpisode(ep.file)}
                  className="px-3 py-2 rounded-xl bg-green-600 hover:bg-green-500 transition"
                >
                  {current === ep.file ? <Pause size={18} /> : <Play size={18} />}
                </button>
                <a
                  href={`/episodes/${ep.file}`}
                  download
                  className="px-3 py-2 rounded-xl bg-red-600 hover:bg-red-500 transition"
                >
                  <Download size={18} />
                </a>
              </div>
            </div>
          ))}
        </div>
      </main>

      <footer className="text-center text-white/50 py-8">
        © {new Date().getFullYear()} Constitution Vibes · All Rights Reserved
      </footer>
    </div>
  );
}
