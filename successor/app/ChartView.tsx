"use client";

import { useState } from "react";
import type { Chart, ChartSection } from "./chart-data";
import { SongTitle } from "./SongTitle";

type ViewMode = "song" | "section";

function Bar({ value }: { value: string }) {
  return <span>{value}</span>;
}

export function ChartSectionView({ section }: { section: ChartSection }) {
  return (
    <section>
      <h2>{section.name}</h2>
      <div>
        {section.bars.map((bar, index) => (
          <Bar key={`${section.id}-${index}`} value={bar} />
        ))}
      </div>
    </section>
  );
}

export function ChartView({ chart }: { chart: Chart }) {
  const [view, setView] = useState<ViewMode>("song");
  const [sectionIndex, setSectionIndex] = useState(0);
  return (
    <main>
      <SongTitle title={chart.title} />
      <p>{chart.artist} · Key {chart.key} · {chart.tempo} BPM</p>
      <nav aria-label="Chart views">
        <button type="button" onClick={() => {
          setView("song");
        }}>Song View</button>
        <button type="button" onClick={() => {
          setView("section");
        }}>Section View</button>
      </nav>
      {view === "song" ? (
        chart.sections.map((section) => (
          <ChartSectionView key={section.id} section={section} />
        ))
      ) : (
        <div>
          <button type="button" disabled={sectionIndex === 0} onClick={() => {
            setSectionIndex(sectionIndex - 1);
          }}>Previous Section</button>
          <span>Section {sectionIndex + 1} of {chart.sections.length}</span>
          <button type="button" disabled={sectionIndex === chart.sections.length - 1} onClick={() => {
            setSectionIndex(sectionIndex + 1);
          }}>Next Section</button>
          <ChartSectionView section={chart.sections[sectionIndex]} />
        </div>
      )}
    </main>
  );
}
