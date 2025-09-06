import React, { useEffect, useRef } from "react";

export default function App() {
  const audioRef = useRef(null);

  useEffect(() => {
    const audio = audioRef.current;
    if (audio) {
      audio.volume = 0.7;
      audio.play().catch((err) => {
        console.log("Autoplay blocked, user must interact:", err);
      });
    }
  }, []);

  return (
    <div className="relative h-screen w-screen overflow-hidden">
      {/* Fullscreen video background */}
      <video
        className="absolute top-0 left-0 w-full h-full object-cover -z-10"
        src="/static/Kenya_flag.mp4"
        autoPlay
        muted
        loop
        playsInline
      />

      {/* Transparent overlay */}
      <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
        <h1 className="text-white text-5xl font-bold drop-shadow-lg text-center">
          🇰🇪 Constitution Vibes 🇰🇪 <br />
          Unity • Freedom • Vibes
        </h1>
      </div>

      {/* Theme song looping */}
      <audio ref={audioRef} src="/static/anthem.mp3" autoPlay loop />
    </div>
  );
}
