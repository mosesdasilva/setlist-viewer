"use client";

import type { Chart, ChartSection } from "./chart-data";
import { SongTitle } from "./SongTitle";

function Bar({ value }: { value: string }) {
  return <span>{value}</span>;
}

export function ChartSectionView({
  section,
  occurrenceId,
}: {
  section: ChartSection;
  occurrenceId: string;
}) {
  return (
    <section id={occurrenceId}>
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
  const arrangedSections = chart.arrangement.map((sectionId, occurrenceIndex) => {
    const section = chart.sections.find(
      (candidate) => candidate.id === sectionId,
    );
    if (!section) {
      throw new Error(`Unknown Section ID: ${sectionId}`);
    }
    return {
      occurrenceId: `${sectionId}-${occurrenceIndex}`,
      section,
    };
  });
  return (
    <main>
      <SongTitle title={chart.title} />
      <p>{chart.artist} · Key {chart.key} · {chart.tempo} BPM</p>
      <nav aria-label="Song Map">
        {arrangedSections.map(({ occurrenceId, section }) => (
          <a key={occurrenceId} href={`#${occurrenceId}`}>
            {section.name}
          </a>
        ))}
      </nav>
      {arrangedSections.map(({ occurrenceId, section }) => (
        <ChartSectionView
          key={occurrenceId}
          occurrenceId={occurrenceId}
          section={section}
        />
      ))}
    </main>
  );
}
