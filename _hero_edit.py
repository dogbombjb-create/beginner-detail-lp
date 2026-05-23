from pathlib import Path
p = Path("index.html")
t = p.read_text(encoding="utf-8")
old = '''          <p class="hero-note hero-note-lg">
            早期お申し込み特典：<br />
            平川かなえ講師とのZoom30分<br />
            個別アドバイスセッションをプレゼント
          </p>'''
new = '''          <p class="hero-note hero-note-lg">
            早期特典：ジャパンケーキショーGPの平川かなえによる個別アドバイス<br />
            Zoom30分のマンツーマンをプレゼント<br />
            （通常は経験者向けの個別サポートです）
          </p>'''
if old not in t:
    raise SystemExit('hero note pattern not found')
p.write_text(t.replace(old, new, 1), encoding="utf-8")
