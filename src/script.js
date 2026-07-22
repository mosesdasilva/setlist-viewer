(function () {
  const catalog = window.SETLIST_SONGS || [];
  const body = document.body;
  const songList = document.getElementById("song-list");
  const directory = document.getElementById("song-directory");
  const songMap = document.getElementById("song-map");
  const songTitle = document.getElementById("song-title");
  const songArtist = document.getElementById("song-artist");
  const songMeta = document.getElementById("song-meta");
  const songCount = document.getElementById("song-count");
  const legacyBadge = document.getElementById("legacy-badge");
  const prevButton = document.getElementById("prev-song");
  const nextButton = document.getElementById("next-song");
  const layoutToggle = document.getElementById("layout-toggle");
  const melodyToggle = document.getElementById("melody-toggle");
  const paletteToggle = document.getElementById("palette-toggle");
  const themeToggle = document.getElementById("theme-toggle");

  const legacySectionCodes = {
    intro: "IN",
    instrumental: "IS",
    verse: "VS",
    tag: "TG",
    prechorus: "PC",
    postchorus: "PS",
    chorus: "CH",
    bridge: "BR",
    turnaround: "TR",
    ending: "EN",
    outro: "OU",
    flow: "FL",
    medley: "MD"
  };

  function appendTextElement(parent, tagName, className, text) {
    const element = document.createElement(tagName);
    element.className = className;
    element.textContent = text;
    parent.appendChild(element);
    return element;
  }

  function clear(element) {
    while (element.firstChild) {
      element.removeChild(element.firstChild);
    }
  }

  function compactSectionName(sectionName) {
    return sectionName
      .replace(/\s+\d+$/, "")
      .toLowerCase()
      .replace(/[^a-z]+/g, "");
  }

  function sectionCode(section) {
    return section.code || legacySectionCodes[compactSectionName(section.name)] || "--";
  }

  function sectionLabel(section) {
    return sectionCode(section) + (section.ordinal || "");
  }

  function renderSectionHeading(sectionElement, section) {
    const heading = appendTextElement(sectionElement, "header", "section-heading", "");
    appendTextElement(heading, "h2", "section-name", section.name);
    appendTextElement(heading, "span", "section-code", sectionLabel(section));
  }

  function renderChordSymbol(parent, chord) {
    const parts = chord.match(
      /^([b#]?)([1-7])(maj7|sus2|sus4|add9|dim|aug|m7|m|7)?(?:\/([b#]?)([1-7]))?$/
    );
    if (!parts) {
      parent.textContent = chord;
      return;
    }

    if (parts[1]) {
      appendTextElement(parent, "span", "chord-accidental", parts[1]);
    }
    appendTextElement(parent, "span", "chord-degree", parts[2]);
    if (parts[3]) {
      appendTextElement(parent, "span", "chord-suffix", parts[3]);
    }
    if (parts[5]) {
      appendTextElement(parent, "span", "slash-divider", "/");
      const bass = appendTextElement(parent, "span", "slash-bass", "");
      if (parts[4]) {
        appendTextElement(bass, "span", "chord-accidental", parts[4]);
      }
      appendTextElement(bass, "span", "chord-degree", parts[5]);
    }
  }

  function renderBarEvent(barEvents, event) {
    const eventElement = appendTextElement(
      barEvents,
      "span",
      "bar-event " + (event.type === "no-chord" ? "no-chord" : "chord-event"),
      ""
    );

    if (event.beats) {
      const dots = appendTextElement(eventElement, "span", "beat-dots", "•".repeat(event.beats));
      dots.setAttribute("aria-label", event.beats + (event.beats === 1 ? " beat" : " beats"));
    }

    if (event.diamond) {
      const diamond = appendTextElement(eventElement, "span", "diamond", "");
      const diamondSymbol = appendTextElement(diamond, "span", "diamond-symbol", "");
      renderChordSymbol(diamondSymbol, event.chord);
      diamond.setAttribute("aria-label", "Diamond " + event.chord);
      return;
    }

    const eventSymbol = appendTextElement(
      eventElement,
      "span",
      "event-symbol",
      event.type === "no-chord" ? "X" : ""
    );
    if (event.type !== "no-chord") {
      renderChordSymbol(eventSymbol, event.chord);
    }
  }

  function renderBar(rowElement, bar, melodyPassages, barIndex) {
    const barElement = appendTextElement(rowElement, "div", "bar", "");
    if (bar === null) {
      barElement.classList.add("empty-bar");
      barElement.setAttribute("aria-label", "Empty Bar Slot");
    } else {
      const barEvents = appendTextElement(barElement, "div", "bar-events", "");
      bar.forEach(function (event) {
        renderBarEvent(barEvents, event);
      });
    }

    const melodies = appendTextElement(barElement, "div", "bar-melodies melody-fragments", "");
    melodyPassages.forEach(function (passage) {
      const fragment = passage.fragments[barIndex];
      if (!fragment) {
        return;
      }
      const melody = appendTextElement(
        melodies,
        "span",
        "bar-melody melody-passage melody-fragment",
        fragment
      );
      melody.dataset.noteIndex = String(passage.noteIndex);
      melody.setAttribute("aria-hidden", "true");
    });
  }

  function renderChartRow(sectionElement, row) {
    const chartRow = appendTextElement(sectionElement, "div", "chart-row", "");
    const barsAndNotes = appendTextElement(chartRow, "div", "bars-and-notes", "");
    const melodies = row.notes
      .map(function (note, noteIndex) {
        return { type: note.type, fragments: note.fragments, noteIndex: noteIndex };
      })
      .filter(function (note) { return note.type === "melody"; });

    row.bars.forEach(function (bar, barIndex) {
      renderBar(barsAndNotes, bar, melodies, barIndex);
    });

    const rowNotes = appendTextElement(barsAndNotes, "aside", "row-notes", "");
    rowNotes.setAttribute("aria-label", "Row Notes");
    if (!row.notes.length) {
      rowNotes.classList.add("no-row-notes");
    }
    row.notes.forEach(function (note, noteIndex) {
      if (note.type === "direction") {
        const direction = appendTextElement(
          rowNotes,
          "span",
          "ordered-row-note performance-direction",
          note.text
        );
        direction.dataset.noteIndex = String(noteIndex);
        return;
      }

      const passage = appendTextElement(
        rowNotes,
        "span",
        "ordered-row-note ordered-melody-passage melody-passage visually-hidden",
        "Melody: " + note.fragments.join(" | ")
      );
      passage.dataset.noteIndex = String(noteIndex);
    });
  }

  function createSectionElement(sectionsElement, section, sectionIndex, rowCount) {
    const sectionElement = appendTextElement(
      sectionsElement,
      "section",
      "section-band",
      ""
    );
    sectionElement.id = sectionsElement.parentElement.id + "-section-" + sectionIndex;
    sectionElement.dataset.code = sectionCode(section);
    sectionElement.dataset.rowCount = String(rowCount);
    sectionElement.style.setProperty("--row-count", String(Math.max(1, rowCount)));
    if (section.ordinal) {
      sectionElement.dataset.sectionOrdinal = String(section.ordinal);
    }
    renderSectionHeading(sectionElement, section);
    return sectionElement;
  }

  function renderChartSong(song, sectionsElement) {
    song.sections.forEach(function (section, sectionIndex) {
      const sectionElement = createSectionElement(
        sectionsElement,
        section,
        sectionIndex,
        section.rows.length
      );
      section.rows.forEach(function (row) {
        renderChartRow(sectionElement, row);
      });
    });
  }

  function renderLegacySong(song, sectionsElement) {
    song.sections.forEach(function (section, sectionIndex) {
      const sectionElement = createSectionElement(sectionsElement, section, sectionIndex, 1);
      sectionElement.classList.add("legacy-section-band");
    });
  }

  const contentRenderers = {
    legacy: renderLegacySong,
    chart: renderChartSong
  };

  function renderSong(song, index) {
    const article = appendTextElement(songList, "article", "song", "");
    article.id = song.id;
    article.dataset.index = String(index);
    article.dataset.songType = song.type;

    const details = appendTextElement(article, "div", "song-details", "");
    if (song.leadVocal) {
      const lead = appendTextElement(details, "span", "", "");
      appendTextElement(lead, "span", "detail-label", "Lead Vocal: ");
      lead.appendChild(document.createTextNode(song.leadVocal));
    }
    const detail = appendTextElement(details, "span", "", "");
    appendTextElement(detail, "span", "detail-label", "Details: ");
    detail.appendChild(document.createTextNode(song.details || "No additional details."));

    const sectionsElement = appendTextElement(article, "div", "sections", "");
    const renderContent = contentRenderers[song.type];
    if (!renderContent) {
      throw new Error("Unsupported song type: " + song.type);
    }
    renderContent(song, sectionsElement);

    const button = appendTextElement(
      directory,
      "button",
      "directory-button",
      song.title + (song.type === "legacy" ? " — Legacy" : "")
    );
    button.type = "button";
    button.dataset.target = String(index);
    button.addEventListener("click", function () {
      setActiveSong(index);
    });
  }

  function metadataChip(text) {
    appendTextElement(songMeta, "span", "", text);
  }

  function updateHeader(song, index) {
    songTitle.textContent = song.title;
    songArtist.textContent = song.artist || "";
    songArtist.hidden = !song.artist;
    legacyBadge.hidden = song.type !== "legacy";
    clear(songMeta);
    metadataChip("Key " + song.key);
    metadataChip(song.tempo);
    if (song.timeSignature) {
      metadataChip(song.timeSignature);
    }
    songCount.textContent = "Song " + (index + 1) + " of " + catalog.length;
  }

  function rebuildSongMap(song, article) {
    clear(songMap);
    const sections = Array.from(article.querySelectorAll(".section-band"));
    sections.forEach(function (sectionElement, sectionIndex) {
      const section = song.sections[sectionIndex];
      const chip = appendTextElement(songMap, "a", "map-chip", sectionLabel(section));
      chip.dataset.code = sectionCode(section);
      chip.href = "#" + sectionElement.id;
      chip.setAttribute(
        "aria-label",
        "Go to " + section.name + ", position " + (sectionIndex + 1)
      );
      chip.addEventListener("click", function (event) {
        event.preventDefault();
        Array.from(songMap.querySelectorAll(".map-chip")).forEach(function (candidate) {
          candidate.classList.toggle("is-active", candidate === chip);
        });
        const headerHeight = document.querySelector(".song-header").offsetHeight;
        const targetTop = sectionElement.getBoundingClientRect().top + window.scrollY - headerHeight - 8;
        window.scrollTo({ top: targetTop, behavior: "smooth" });
      });
    });
  }

  catalog.forEach(renderSong);

  const songs = Array.from(songList.querySelectorAll(".song"));
  const directoryButtons = Array.from(directory.querySelectorAll(".directory-button"));
  let activeIndex = 0;

  function savePreference(name, value) {
    try {
      localStorage.setItem("setlist-" + name, value);
    } catch (error) {
    }
  }

  function loadPreference(name, fallback) {
    try {
      return localStorage.getItem("setlist-" + name) || fallback;
    } catch (error) {
      return fallback;
    }
  }

  function applyTheme(theme) {
    const dark = theme === "dark";
    body.classList.toggle("dark-theme", dark);
    themeToggle.textContent = dark ? "☀" : "☾";
    const label = dark ? "Use light mode" : "Use dark mode";
    themeToggle.setAttribute("aria-label", label);
    themeToggle.setAttribute("title", label);
    savePreference("theme", dark ? "dark" : "light");
  }

  function applyColumns(columns) {
    const single = columns === "1";
    body.classList.toggle("single-column", single);
    layoutToggle.textContent = single ? "▤" : "▥";
    layoutToggle.setAttribute("aria-pressed", String(single));
    const label = single ? "Layout: one column" : "Layout: two columns";
    layoutToggle.setAttribute("aria-label", label);
    layoutToggle.setAttribute("title", label);
    savePreference("columns", single ? "1" : "2");
  }

  function applyMelody(visibility) {
    const visible = visibility !== "off";
    body.classList.toggle("melody-hidden", !visible);
    melodyToggle.textContent = visible ? "♫" : "×";
    melodyToggle.setAttribute("aria-pressed", String(visible));
    const label = visible ? "Hide melody" : "Show melody";
    melodyToggle.setAttribute("aria-label", label);
    melodyToggle.setAttribute("title", label);
    savePreference("melody", visible ? "on" : "off");
  }

  function applyPalette(palette) {
    const pastel = palette === "pastel";
    body.classList.toggle("pastel-palette", pastel);
    paletteToggle.setAttribute("aria-pressed", String(pastel));
    const label = pastel ? "Use strong Section colors" : "Use pastel Section colors";
    paletteToggle.setAttribute("aria-label", label);
    paletteToggle.setAttribute("title", label);
    savePreference("palette", pastel ? "pastel" : "strong");
  }

  function setActiveSong(index) {
    if (!songs.length) {
      return;
    }
    activeIndex = (index + songs.length) % songs.length;
    songs.forEach(function (song, songIndex) {
      song.classList.toggle("active", songIndex === activeIndex);
    });
    directoryButtons.forEach(function (button, buttonIndex) {
      button.classList.toggle("is-active", buttonIndex === activeIndex);
      button.setAttribute("aria-current", buttonIndex === activeIndex ? "true" : "false");
    });
    updateHeader(catalog[activeIndex], activeIndex);
    rebuildSongMap(catalog[activeIndex], songs[activeIndex]);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  prevButton.addEventListener("click", function () {
    setActiveSong(activeIndex - 1);
  });

  nextButton.addEventListener("click", function () {
    setActiveSong(activeIndex + 1);
  });

  themeToggle.addEventListener("click", function () {
    applyTheme(body.classList.contains("dark-theme") ? "light" : "dark");
  });

  layoutToggle.addEventListener("click", function () {
    applyColumns(body.classList.contains("single-column") ? "2" : "1");
  });

  melodyToggle.addEventListener("click", function () {
    applyMelody(body.classList.contains("melody-hidden") ? "on" : "off");
  });

  paletteToggle.addEventListener("click", function () {
    applyPalette(body.classList.contains("pastel-palette") ? "strong" : "pastel");
  });

  document.addEventListener("keydown", function (event) {
    if (event.target && /input|textarea|select/i.test(event.target.tagName)) {
      return;
    }
    if (event.key.toLowerCase() === "d") {
      applyTheme(body.classList.contains("dark-theme") ? "light" : "dark");
    } else if (event.key === "ArrowRight") {
      setActiveSong(activeIndex + 1);
    } else if (event.key === "ArrowLeft") {
      setActiveSong(activeIndex - 1);
    }
  });

  applyTheme(loadPreference("theme", "light"));
  applyColumns(loadPreference("columns", "2"));
  applyMelody(loadPreference("melody", "on"));
  applyPalette(loadPreference("palette", "strong"));

  if (songs.length) {
    setActiveSong(0);
  } else {
    songCount.textContent = "No songs";
  }
})();
