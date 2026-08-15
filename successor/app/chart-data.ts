export type ChartSection = {
  id: string;
  name: string;
  bars: string[];
};

export type Chart = {
  id: string;
  title: string;
  artist: string;
  key: string;
  tempo: number;
  timeSignature: string;
  sections: ChartSection[];
  arrangement: string[];
};

const sections: ChartSection[] = [
  { id: "intro", name: "Intro", bars: ["4", "2", "6", "3", "4", "2", "6", "3"] },
  { id: "verse", name: "Verse", bars: ["4", "2", "6", "3", "4", "2", "6", "3"] },
  { id: "tag", name: "Tag", bars: ["3"] },
  { id: "pre-chorus", name: "Pre-Chorus", bars: ["4", "2", "6", "3", "4", "2", "6", "3"] },
  { id: "chorus-1", name: "Chorus 1", bars: ["4", "2", "6", "3", "4", "2", "6", "3"] },
  { id: "chorus-2", name: "Chorus 2", bars: ["4", "2", "6", "3", "4", "2", "6", "3"] },
  { id: "instrumental", name: "Instrumental", bars: ["6", "6", "6", "6", "6", "6", "6", "6"] },
  { id: "bridge", name: "Bridge", bars: ["4", "5", "6", "1/3", "4", "5", "6", "1/3"] },
  { id: "ending", name: "Ending", bars: ["2", "3", "4", "<3>"] },
];

const arrangement: string[] = [
  "intro", "verse", "tag", "pre-chorus", "tag", "chorus-1", "chorus-2",
  "intro", "verse", "tag", "pre-chorus", "chorus-1", "chorus-2", "instrumental",
  "bridge", "bridge", "bridge", "tag", "chorus-1", "bridge", "bridge", "ending",
];

export const masChart: Chart = {
  id: "mas",
  title: "Más",
  artist: "Miel San Marcos",
  key: "D",
  tempo: 140,
  timeSignature: "4/4",
  sections,
  arrangement,
};
