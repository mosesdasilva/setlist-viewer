(function () {
  const songs = Array.from(document.querySelectorAll(".song"));
  const prevButton = document.getElementById("prev-song");
  const nextButton = document.getElementById("next-song");
  const themeToggle = document.getElementById("theme-toggle");
  const songCount = document.getElementById("song-count");
  const directory = document.getElementById("song-directory");
  const body = document.body;

  if (!songs.length) {
    return;
  }

  const slugify = (text) =>
    text
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");

  songs.forEach((song, index) => {
    const title = song.querySelector(".song-title")?.textContent?.trim() || "Song";
    const id = slugify(title) || "song-" + (index + 1);
    song.id = id;
    song.dataset.index = String(index);

    const button = document.createElement("button");
    button.type = "button";
    button.className = "directory-button";
    button.textContent = title;
    button.dataset.target = String(index);
    button.addEventListener("click", function () {
      setActiveSong(index);
    });
    directory.appendChild(button);
  });

  const directoryButtons = Array.from(directory.querySelectorAll(".directory-button"));
  let activeIndex = 0;

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

    songs.forEach((song, songIndex) => {
      song.classList.toggle("active", songIndex === activeIndex);
    });

    directoryButtons.forEach((button, buttonIndex) => {
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
