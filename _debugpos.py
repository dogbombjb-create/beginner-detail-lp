from pathlib import Path
text = Path('index.html').read_text(encoding='utf-8', errors='ignore')
start = text.find('<section id="teacher">')
end = text.find('    <!-- Support -->', start)
print(start, end)