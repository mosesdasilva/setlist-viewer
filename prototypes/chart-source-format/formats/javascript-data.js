// PROTOTYPE — executable authoring data
const row = (bars, ...notes) => ({ bars, notes });
const melody = (...fragments) => ({ type: "melody", fragments });
const direction = (text) => ({ type: "direction", text });
const section = (code, name, ...rows) => ({ code, name, rows });

const intro = section("IN", "Intro",
  row(["4", "2", "6", "3"], melody("17 65", "32 12", "17 65", "5156 5")),
  row(["4", "2", "6", "3"], melody("17 65", "32 12", "17 65", "5156 5"), direction("oct ↑")));
const verse = section("VS", "Verse",
  row(["4", "2", "6", "3"], direction("Rakes")),
  row(["4", "2", "6", "3"]));
const tag = section("TG", "Tag", row(["3", null, null, null]));
const preChorus = section("PC", "Pre-Chorus",
  row(["4", "2", "6", "3"], melody("17 65", "32 12", "17 65", "5156 5")));
const chorusA = { ...section("CH", "Chorus",
  row(["4", "2", "6", "3"], melody("6 3", "6 -", "6 3", "7 -"))), ordinal: 1 };
const chorusB = { ...section("CH", "Chorus",
  row(["4", "2", "6", "3"], melody("656 3", "656 3", "656 3", "7"))), ordinal: 2 };
const instrumental = section("IS", "Instrumental",
  row(["6", "6", "6", "6"], melody("265 61", "3322 1265", "265 61", "3322 3511")));
const bridge = section("BR", "Bridge",
  row(["4", "5", "6", "1/3"]), row(["4", "5", "6", "1/3"]));
const ending = section("EN", "Ending",
  row(["2", "3", "4", { chord: "3", diamond: true }]));

export default {
  title: "Más", artist: "Miel San Marcos", key: "D", tempo: 140, timeSignature: "4/4",
  arrangement: [intro, verse, tag, preChorus, tag, chorusA, chorusB, intro, verse, tag,
    preChorus, chorusA, chorusB, instrumental, bridge, bridge, bridge, tag, chorusA,
    bridge, bridge, ending]
};
