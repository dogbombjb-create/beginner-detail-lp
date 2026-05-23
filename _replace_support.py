from pathlib import Path
path=Path("index.html")
text=path.read_text(encoding="utf-8")
start=text.find("<section id=\"support\">")
end=text.find("    <!-- Voices -->", start)
if start==-1 or end==-1:
    raise SystemExit("support section not found")
new_section = '''    <section id="support">
      <div class="section-label">Support</div>
      <h2 class="section-title">プロが作るサンプル花材と 学び直せる仕組み</h2>
      <div class="card">
        <div class="slider" id="sample-slider">
          <div class="slides">
            <div class="slide"><img src="images/IMG_0406.JPG" alt="講師が制作したサンプル花材"></div>
            <div class="slide"><img src="images/IMG_6733.JPG" alt="講師が制作したサンプル花材"></div>
            <div class="slide"><img src="images/IMG_7641.JPG" alt="講師が制作したサンプル花材"></div>
          </div>
          <div class="slider-dots">
            <button class="slider-dot is-active" aria-label="1枚目へ"></button>
            <button class="slider-dot" aria-label="2枚目へ"></button>
            <button class="slider-dot" aria-label="3枚目へ"></button>
          </div>
        </div>
        <p class="section-lead">
          ひとりで作り切れない ブーケ慣れするまでが不安な方へ<br />
          レッスン外の時間にも 手を動かしやすいように設計しています
        </p>
        <ul class="benefit-list">
          <li>
            プロ講師が仕上げたサンプル花材をお届け<br />
            形・色・質感のゴールを手元で確認しながら練習できます
          </li>
          <li>
            全回録画つきで、あとから何度でも見直しOK<br />
            1回で作り切れなくても ゆっくり自分のペースで復習できます
          </li>
          <li>
            再受講枠・フォローも用意し、つまずきポイントを一緒に解消します
          </li>
        </ul>
      </div>
    </section>
'''
new_text = text[:start] + new_section + text[end:]
path.write_text(new_text, encoding="utf-8")
