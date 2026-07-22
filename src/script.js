(function () {
  const catalog = window.SETLIST_SONGS || [];
  const body = document.body;
  const songList = document.getElementById("song-list");
  const songMap = document.getElementById("song-map");
  const songTitle = document.getElementById("song-title");
  const songArtist = document.getElementById("song-artist");
  const songMeta = document.getElementById("song-meta");
  const songCount = document.getElementById("song-count");
  const legacyBadge = document.getElementById("legacy-badge");
  const prevButton = document.getElementById("prev-song");
  const nextButton = document.getElementById("next-song");
  const layoutButtons = Array.from(document.querySelectorAll(".layout-button"));
  const melodyToggle = document.getElementById("melody-toggle");
  const paletteToggle = document.getElementById("palette-toggle");
  const themeToggle = document.getElementById("theme-toggle");
  const songPickerTrigger = document.getElementById("song-picker-trigger");
  const songPicker = document.getElementById("song-picker");
  const songPickerClose = document.getElementById("song-picker-close");
  const songSearch = document.getElementById("song-search");
  const songPickerStatus = document.getElementById("song-picker-status");
  const songPickerResults = document.getElementById("song-picker-results");
  const multiColumnMedia = window.matchMedia("(min-width: 700px)");
  const fourColumnMedia = window.matchMedia("(min-width: 1200px)");

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
    sectionsElement.classList.add("legacy-sections");
    sectionsElement.setAttribute("aria-label", "Legacy Section summary");
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
    songMap.hidden = song.type !== "chart";
    if (songMap.hidden) {
      return;
    }
    songMap.setAttribute("aria-label", "Song Map for " + song.title);
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
        updateActiveMapTarget(sectionIndex);
        const headerHeight = document.querySelector(".song-header").offsetHeight;
        const targetTop = sectionElement.getBoundingClientRect().top + window.scrollY - headerHeight - 8;
        window.scrollTo({ top: targetTop, behavior: "smooth" });
      });
    });
    updateActiveMapTarget(0);
  }

  function updateActiveMapTarget(activeSectionIndex) {
    Array.from(songMap.querySelectorAll(".map-chip")).forEach(function (chip, chipIndex) {
      const active = chipIndex === activeSectionIndex;
      chip.classList.toggle("is-active", active);
      if (active) {
        chip.setAttribute("aria-current", "location");
      } else {
        chip.removeAttribute("aria-current");
      }
    });
  }

  catalog.forEach(renderSong);

  const songs = Array.from(songList.querySelectorAll(".song"));
  let activeIndex = 0;

  function renderPickerResults(query) {
    const normalizedQuery = query.trim().toLocaleLowerCase();
    const matches = catalog
      .map(function (song, index) { return { song: song, index: index }; })
      .filter(function (entry) {
        const song = entry.song;
        return (
          !normalizedQuery ||
          song.title.toLocaleLowerCase().includes(normalizedQuery) ||
          (song.artist || "").toLocaleLowerCase().includes(normalizedQuery)
        );
      });

    clear(songPickerResults);
    songPickerStatus.textContent = matches.length === 1 ? "1 Song" : matches.length + " Songs";

    matches.forEach(function (entry) {
      const song = entry.song;
      const button = appendTextElement(songPickerResults, "button", "picker-result", "");
      const isActive = entry.index === activeIndex;
      button.type = "button";
      button.dataset.target = String(entry.index);
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-current", isActive ? "true" : "false");
      appendTextElement(button, "span", "picker-result-title", song.title);
      appendTextElement(button, "span", "picker-result-artist", song.artist || "Artist not listed");
      const badges = appendTextElement(button, "span", "picker-result-badges", "");
      if (song.type === "legacy") {
        appendTextElement(badges, "span", "legacy-badge", "Legacy");
      }
      if (isActive) {
        appendTextElement(badges, "span", "current-badge", "Current");
      }
      button.addEventListener("click", function () {
        setActiveSong(entry.index);
        closeSongPicker();
      });
    });
  }

  function openSongPicker() {
    songSearch.value = "";
    renderPickerResults("");
    songPicker.showModal();
    songPickerTrigger.setAttribute("aria-expanded", "true");
    songSearch.focus();
  }

  function closeSongPicker() {
    if (songPicker.open) {
      songPicker.close();
    }
  }

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
    themeToggle.setAttribute("aria-pressed", String(dark));
    const label = dark ? "Use light mode" : "Use dark mode";
    themeToggle.setAttribute("aria-label", label);
    themeToggle.setAttribute("title", label);
    savePreference("theme", dark ? "dark" : "light");
  }

  function applyColumns(columns) {
    if (!["1", "2", "4"].includes(columns)) {
      columns = "2";
    }
    ["1", "2", "4"].forEach(function (candidate) {
      body.classList.toggle("layout-columns-" + candidate, candidate === columns);
    });
    body.dataset.layoutPreference = columns;
    updateRenderedColumns();
    savePreference("columns", columns);
  }

  function updateRenderedColumns() {
    const preferred = body.dataset.layoutPreference || "2";
    let rendered = preferred;
    if (!multiColumnMedia.matches) {
      rendered = "1";
    } else if (preferred === "4" && !fourColumnMedia.matches) {
      rendered = "2";
    }
    body.dataset.renderedColumns = rendered;
    layoutButtons.forEach(function (button) {
      button.setAttribute("aria-pressed", String(button.dataset.columns === rendered));
    });
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
    updateHeader(catalog[activeIndex], activeIndex);
    rebuildSongMap(catalog[activeIndex], songs[activeIndex]);
    if (songPicker.open) {
      renderPickerResults(songSearch.value);
    }
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

  layoutButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      applyColumns(button.dataset.columns);
    });
  });

  melodyToggle.addEventListener("click", function () {
    applyMelody(body.classList.contains("melody-hidden") ? "on" : "off");
  });

  paletteToggle.addEventListener("click", function () {
    applyPalette(body.classList.contains("pastel-palette") ? "strong" : "pastel");
  });

  songPickerTrigger.addEventListener("click", openSongPicker);
  songPickerClose.addEventListener("click", closeSongPicker);
  songSearch.addEventListener("input", function () {
    renderPickerResults(songSearch.value);
  });
  songPicker.addEventListener("cancel", function (event) {
    event.preventDefault();
    closeSongPicker();
  });
  songPicker.addEventListener("close", function () {
    songSearch.value = "";
    renderPickerResults("");
    songPickerTrigger.setAttribute("aria-expanded", "false");
    songPickerTrigger.focus();
  });
  songPicker.addEventListener("click", function (event) {
    if (event.target === songPicker) {
      const bounds = songPicker.getBoundingClientRect();
      const outside =
        event.clientX < bounds.left || event.clientX > bounds.right ||
        event.clientY < bounds.top || event.clientY > bounds.bottom;
      if (outside) {
        closeSongPicker();
      }
    }
  });

  document.addEventListener("keydown", function (event) {
    if (songPicker.open) {
      if (event.key === "Escape") {
        event.preventDefault();
        closeSongPicker();
      }
      return;
    }
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
  renderPickerResults("");

  multiColumnMedia.addEventListener("change", updateRenderedColumns);
  fourColumnMedia.addEventListener("change", updateRenderedColumns);

  if (songs.length) {
    setActiveSong(0);
  } else {
    songCount.textContent = "No songs";
  }
})();
