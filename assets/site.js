// Mobile navigation toggle
(function () {
  var nav = document.querySelector(".nav");
  var btn = document.querySelector(".nav-toggle");
  if (!nav || !btn) return;
  btn.addEventListener("click", function () {
    var open = nav.getAttribute("data-open") === "true";
    nav.setAttribute("data-open", open ? "false" : "true");
    btn.setAttribute("aria-expanded", open ? "false" : "true");
  });
  nav.querySelectorAll(".nav-links a").forEach(function (a) {
    a.addEventListener("click", function () {
      nav.setAttribute("data-open", "false");
      btn.setAttribute("aria-expanded", "false");
    });
  });
})();
