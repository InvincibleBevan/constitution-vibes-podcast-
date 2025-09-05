import { useState } from "react";
import { Play, Pause, Download } from "lucide-react";

const episodes = [
  { title: "Intro", file: "Intro.mp3" },
  { title: "Preamble", file: "Episode_0_Preamble.mp3" },
  { title: "Chapter 1 – Sovereignty", file: "Episode_1.mp3" },
  { title: "Chapter 2 – Republic", file: "Episode_2.mp3" },
  { title: "Outro", file: "Outro.mp3" }
];

export default function App() {
  const [current, setCurrent] = useState(null);
  const [audio, setAudio] = useState(null);

  const playEpisode = (file) => {
    if (audio) {
      audio.pause();
    }
    const newAudio = new Audio(`/episodes/${file}`);
    newAudio.play();
    setAudio(newAudio);
    setCurrent(file);
  };

  return (
    <div className="min-h-screen bg-black text-white relative flex flex-col items-center justify-center p-6">
      {/* Flag background */}
      <div className="absolute inset-0 -z-10">
        <video autoPlay loop muted className="w-full h-full object-cover opacity-20">
          <source src="/kenya_flag.mp4" type="video/mp4" />
        </video>
      </div>

      {/* Anthem background */}
      <audio autoPlay loop>
        <source src="/anthem_instrumental.mp3" type="audio/mp3" />
      </audio>

      <h1 className="text-3xl font-bold mb-6 text-green-400">
        🇰🇪 Constitution Vibes Podcast
      </h1>

      <div className="grid gap-4 w-full max-w-2xl">
        {episodes.map((ep, i) => (
          <div key={i} className="flex justify-between items-center bg-gray-900 rounded-2xl p-4 shadow-lg">
            <span className="text-lg">{ep.title}</span>
            <div className="flex gap-3">
              <button
                onClick={() => playEpisode(ep.file)}
                className="p-2 rounded-full bg-green-600 hover:bg-green-500"
              >
                {current === ep.file ? <Pause size={20} /> : <Play size={20} />}
              </button>
              <a
                href={`/episodes/${ep.file}`}
                download
                className="p-2 rounded-full bg-red-600 hover:bg-red-500"
              >
                <Download size={20} />
              </a>
            </div>
          </div>
        ))}
      </div>

      <footer className="mt-10 text-gray-400 text-sm">
        Prepared with <span className="text-green-500">SiR J</span>, powered by{" "}
        <span className="text-red-500">VibesOfTheTribe</span>
      </footer>
    </div>
  );
}
