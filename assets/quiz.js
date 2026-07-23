(function () {
  document.querySelectorAll("[data-quiz]").forEach(function (quiz) {
    const feedback = quiz.querySelector("[data-feedback]");
    quiz.querySelectorAll("button[data-answer]").forEach(function (button) {
      button.addEventListener("click", function () {
        const correct = button.dataset.answer === "correct";
        quiz.querySelectorAll("button[data-answer]").forEach(function (candidate) {
          candidate.classList.remove("correct", "incorrect");
        });
        button.classList.add(correct ? "correct" : "incorrect");
        feedback.textContent = correct
          ? "Correct. Edit the source, then regenerate the output."
          : "Try again. The generated file is replaced by the build.";
      });
    });
  });
})();
