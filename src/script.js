(function () {
  const catalog = window.SETLIST_SONGS || [];
  const songList = document.getElementById("song-list");
  const prevButton = document.getElementById("prev-song");
  const nextButton = document.getElementById("next-song");
  const themeToggle = document.getElementById("theme-toggle");
  const songCount = document.getElementById("song-count");
  const directory = document.getElementById("song-directory");
  const body = document.body;

  function appendTextElement(parent, tagName, className, text) {
    const element = document.createElement(tagName);
    element.className = className;
    element.textContent = text;
    parent.appendChild(element);
    return element;
  }

  function sectionClass(sectionName) {
    return sectionName
      .replace(/\s+\d+$/, "")
      .toLowerCase()
      .replace(/[^a-z]+/g, "");
  }

  function renderLegacySong(song, article) {
    const mapCard = appendTextElement(article, "div", "map-card", "");
    appendTextElement(mapCard, "h2", "", "Map");
    const mapList = appendTextElement(mapCard, "ol", "map-list", "");

    song.sections.forEach(function (section) {
      appendTextElement(mapList, "li", "section " + sectionClass(section.name), section.name);
    });
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

  function renderBarEvent(barSlot, event) {
    const eventElement = appendTextElement(
      barSlot,
      "span",
      "bar-event " + (event.type === "no-chord" ? "no-chord" : "chord-event"),
      ""
    );

    if (event.beats) {
      const dots = appendTextElement(eventElement, "span", "beat-dots", "•".repeat(event.beats));
      dots.setAttribute("aria-label", event.beats + (event.beats === 1 ? " beat" : " beats"));
    }

    if (event.diamond) {
      const diamond = appendTextElement(eventElement, "span", "diamond-chord", "");
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

  function renderBar(barGrid, bar) {
    const barSlot = appendTextElement(barGrid, "div", "bar-slot", "");
    if (bar === null) {
      barSlot.classList.add("empty-bar-slot");
      barSlot.setAttribute("aria-label", "Empty Bar Slot");
      return;
    }

    bar.forEach(function (event) {
      renderBarEvent(barSlot, event);
    });
  }

  function renderRowNote(rowNotes, note) {
    if (note.type === "direction") {
      const direction = appendTextElement(
        rowNotes,
        "div",
        "row-note performance-direction",
        ""
      );
      appendTextElement(direction, "span", "note-label", "Direction");
      appendTextElement(direction, "span", "note-text", note.text);
      return;
    }

    const melody = appendTextElement(rowNotes, "div", "row-note melody-passage", "");
    appendTextElement(melody, "span", "note-label", "Melody");
    const fragments = appendTextElement(melody, "div", "melody-fragments", "");
    note.fragments.forEach(function (fragment) {
      appendTextElement(fragments, "span", "melody-fragment", fragment);
    });
  }

  function renderChartRow(sectionBody, row) {
    const chartRow = appendTextElement(sectionBody, "div", "chart-row", "");
    const barGrid = appendTextElement(chartRow, "div", "bar-grid", "");
    row.bars.forEach(function (bar) {
      renderBar(barGrid, bar);
    });

    const rowNotes = appendTextElement(chartRow, "aside", "row-notes", "");
    if (!row.notes.length) {
      rowNotes.classList.add("no-row-notes");
      rowNotes.setAttribute("aria-label", "No Row Notes");
    }
    row.notes.forEach(function (note) {
      renderRowNote(rowNotes, note);
    });
  }

  function renderChartSong(song, article) {
    article.classList.add("chart-song");
    const chartCard = appendTextElement(article, "div", "chart-card", "");
    appendTextElement(chartCard, "h2", "chart-card-title", "Expanded Arrangement");

    song.sections.forEach(function (section) {
      const sectionElement = appendTextElement(
        chartCard,
        "section",
        "chart-section " + sectionClass(section.name),
        ""
      );
      sectionElement.dataset.sectionCode = section.code;
      if (section.ordinal) {
        sectionElement.dataset.sectionOrdinal = String(section.ordinal);
      }

      const heading = appendTextElement(sectionElement, "header", "chart-section-heading", "");
      appendTextElement(heading, "h3", "chart-section-name", section.name);
      appendTextElement(
        heading,
        "span",
        "section-code",
        section.code + (section.ordinal || "")
      );
      const sectionBody = appendTextElement(sectionElement, "div", "chart-section-body", "");
      section.rows.forEach(function (row) {
        renderChartRow(sectionBody, row);
      });
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

    const songMain = appendTextElement(article, "div", "song-main", "");
    const titleRow = appendTextElement(songMain, "div", "song-heading", "");
    appendTextElement(titleRow, "h2", "song-title", song.title);
    if (song.type === "legacy") {
      appendTextElement(titleRow, "span", "legacy-badge", "Legacy");
    }

    const metadata = appendTextElement(songMain, "div", "meta", "");
    if (song.artist) {
      appendTextElement(metadata, "span", "chip", "Artist: " + song.artist);
    }
    appendTextElement(metadata, "span", "chip", song.tempo);
    appendTextElement(metadata, "span", "chip", "Key: " + song.key);
    if (song.timeSignature) {
      appendTextElement(metadata, "span", "chip", "Time: " + song.timeSignature);
    }
    if (song.leadVocal) {
      appendTextElement(metadata, "span", "chip", "Lead Vocal: " + song.leadVocal);
    }

    const detailsCard = appendTextElement(songMain, "div", "details-card", "");
    appendTextElement(detailsCard, "h2", "", "Details");
    appendTextElement(
      detailsCard,
      "p",
      song.detailsEmpty || !song.details ? "empty-detail" : "",
      song.details || "No additional details."
    );

    const renderContent = contentRenderers[song.type];
    if (!renderContent) {
      throw new Error("Unsupported song type: " + song.type);
    }
    renderContent(song, article);

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

  catalog.forEach(renderSong);

  const songs = Array.from(songList.querySelectorAll(".song"));
  const directoryButtons = Array.from(directory.querySelectorAll(".directory-button"));
  let activeIndex = 0;

  if (!songs.length) {
    songCount.textContent = "No songs";
    return;
  }

  function updateThemeButton() {
    const isDark = body.classList.contains("dark-theme");
    themeToggle.textContent = isDark ? "Light Mode" : "Dark Mode";
  }

  function setTheme(theme) {
    body.classList.toggle("dark-theme", theme === "dark");
    updateThemeButton();
    try {
      localStorage.setItem("setlist-theme", theme);
    } catch (error) {
    }
  }

  function setActiveSong(index) {
    activeIndex = (index + songs.length) % songs.length;

    songs.forEach(function (song, songIndex) {
      song.classList.toggle("active", songIndex === activeIndex);
    });

    directoryButtons.forEach(function (button, buttonIndex) {
      button.classList.toggle("is-active", buttonIndex === activeIndex);
    });

    songCount.textContent = "Song " + (activeIndex + 1) + " of " + songs.length;
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  prevButton.addEventListener("click", function () {
    setActiveSong(activeIndex - 1);
  });

  nextButton.addEventListener("click", function () {
    setActiveSong(activeIndex + 1);
  });

  themeToggle.addEventListener("click", function () {
    const nextTheme = body.classList.contains("dark-theme") ? "light" : "dark";
    setTheme(nextTheme);
  });

  document.addEventListener("keydown", function (event) {
    if (event.target && /input|textarea|select/i.test(event.target.tagName)) {
      return;
    }

    if (event.key.toLowerCase() === "d") {
      const nextTheme = body.classList.contains("dark-theme") ? "light" : "dark";
      setTheme(nextTheme);
    }

    if (event.key === "ArrowRight") {
      setActiveSong(activeIndex + 1);
    }

    if (event.key === "ArrowLeft") {
      setActiveSong(activeIndex - 1);
    }
  });

  let savedTheme = "light";

  try {
    savedTheme = localStorage.getItem("setlist-theme") || "light";
  } catch (error) {
  }

  setTheme(savedTheme);
  setActiveSong(0);
})();
