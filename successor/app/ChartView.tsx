import type { Chart, ChartSection } from "./chart-data";
import { SongTitle } from "./SongTitle";

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
  return (
    <main>
      <SongTitle title={chart.title} />
      <p>{chart.artist} · Key {chart.key} · {chart.tempo} BPM</p>
      {chart.sections.map((section) => (
        <ChartSectionView key={section.id} section={section} />
      ))}
    </main>
  );
}
