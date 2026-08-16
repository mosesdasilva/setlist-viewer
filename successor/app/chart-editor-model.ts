export type ChartRowDraft = [
  string, string, string, string
];

export type ChartSectionDraft = {
  id: string;
  name: string;
  rows: ChartRowDraft[];
};

export type ChartDraft = {
  id: string;
  title: string;
  artist: string;
  key: string;
  tempo: string;
  timeSignature: string;
  sections: ChartSectionDraft[];
  arrangement: string[];
};

export const emptyChartDraft: ChartDraft = {
  id: "new-chart",
  title: "",
  artist: "",
  key: "",
  tempo: "",
  timeSignature: "4/4",
  sections: [{
    id: "section-1",
    name: "",
    rows: [["", "", "", ""]],
  }],
  arrangement: ["section-1"],
};
