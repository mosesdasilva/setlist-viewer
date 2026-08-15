import type { Metadata } from "next";
import { ChartView } from "./ChartView";
import { masChart } from "./chart-data";

export const metadata: Metadata = {
  title: "Your site is taking shape",
  description:
    "Your first version will appear here automatically when it’s ready.",
  other: {
    "codex-preview": "development",
  },
};

export default function Home() {
  return <ChartView chart={masChart} />;
}
