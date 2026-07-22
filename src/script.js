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

  const contentRenderers = {
    legacy: renderLegacySong
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
    appendTextElement(metadata, "span", "chip", song.tempo);
    appendTextElement(metadata, "span", "chip", "Key: " + song.key);
    appendTextElement(metadata, "span", "chip", "Lead Vocal: " + song.leadVocal);

    const detailsCard = appendTextElement(songMain, "div", "details-card", "");
    appendTextElement(detailsCard, "h2", "", "Details");
    appendTextElement(
      detailsCard,
      "p",
      song.detailsEmpty ? "empty-detail" : "",
      song.details
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
