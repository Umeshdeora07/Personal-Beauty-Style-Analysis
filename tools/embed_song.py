#!/usr/bin/env python3
"""Embed an mp3 inside taniya.html so the letter is one self-contained file.

Usage:  python3 tools/embed_song.py [song.mp3] [page.html]
Defaults: music/barsaat.mp3 and taniya.html (paths relative to the repo root).
Re-run it after replacing the song; it rewrites the <script id="songData"> block.
"""
import base64, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
song = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'music' / 'barsaat.mp3'
page = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'taniya.html'

b64 = base64.b64encode(song.read_bytes()).decode('ascii')
wrapped = '\n'.join(b64[i:i + 4000] for i in range(0, len(b64), 4000))
block = f'<script type="application/octet-stream" id="songData">\n{wrapped}\n</script>\n'

html = page.read_text(encoding='utf-8')
html, n = re.subn(r'<script type="application/octet-stream" id="songData">.*?</script>\n', lambda m: block, html, flags=re.S)
if n == 0:
    # first time: put it after the main script, so the letter is usable while the song downloads
    html, n = re.subn(r'</script>\n</body>', lambda m: '</script>\n' + block + '</body>', html, count=1)
if n != 1:
    sys.exit('could not find where to put the song in ' + str(page))
page.write_text(html, encoding='utf-8')
print(f'embedded {song.name} ({song.stat().st_size / 1e6:.2f} MB) into {page.name} ({page.stat().st_size / 1e6:.2f} MB)')
