document.addEventListener("DOMContentLoaded", function () {
  // 画像設定
  applyConfiguredImages();

  // スライダー初期化
  initSlider("#sample-slider");

  // FAQアコーディオン
  var buttons = document.querySelectorAll(".faq-trigger");
  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      item.classList.toggle("is-open");
      var content = item.querySelector(".faq-answer");
      if (item.classList.contains("is-open")) {
        content.style.maxHeight = content.scrollHeight + "px";
      } else {
        content.style.maxHeight = null;
      }
    });
  });

  // 画像置換ロジック (既存維持)
  function applyConfiguredImages() {
    if (!window.imageConfig) return;
    var images = document.querySelectorAll("[data-image-key]");
    images.forEach(function (img) {
      var key = img.getAttribute("data-image-key");
      var conf = window.imageConfig[key];
      if (!conf) return;
      if (conf.src) img.setAttribute("src", conf.src);
      if (conf.alt) img.setAttribute("alt", conf.alt);
    });
  }

  // スライダーロジック (シンプル版)
  function initSlider(selector) {
    var slider = document.querySelector(selector);
    if (!slider) return;
    var track = slider.querySelector(".slides");
    var slides = Array.from(slider.querySelectorAll(".slide"));
    var dotsContainer = slider.querySelector(".slider-dots");
    var index = 0;
    
    // Create dots
    if (dotsContainer) {
      dotsContainer.innerHTML = "";
      slides.forEach((_, i) => {
        var dot = document.createElement("span");
        dot.className = i === 0 ? "dot active" : "dot";
        dot.addEventListener("click", () => goTo(i));
        dotsContainer.appendChild(dot);
      });
    }
    
    // Dot Style Injection for this specific design
    var style = document.createElement('style');
    style.innerHTML = `
      .dot { display:inline-block; width:8px; height:8px; background:#e0e0e0; border-radius:50%; margin:0 6px; cursor:pointer; transition:0.3s; }
      .dot.active { background:#a8948a; transform:scale(1.2); }
    `;
    document.head.appendChild(style);

    function goTo(i) {
      index = i;
      var w = slides[0].clientWidth + 20; // width + margin
      track.style.transform = `translateX(-${index * w}px)`;
      
      var dots = dotsContainer.querySelectorAll(".dot");
      dots.forEach((d, idx) => d.classList.toggle("active", idx === index));
    }
  }
});