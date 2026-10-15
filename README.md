# 💗 A Little Surprise

A cute, romantic, fully interactive digital surprise card. One single
`index.html` file — no build step, no dependencies, no server required.
Just open it (or host it anywhere) and it works.

## The journey

| Step | What happens |
|------|--------------|
| 1 | Animated welcome screen with "the one very important rule" and an **Okay, I understand 💗** button |
| 2 | The big question: **💗 ME** or **🥒 KARELA** |
| 3 | The KARELA button runs away — dodging, shrinking, tilting and teasing her with funny messages |
| 4 | She clicks ME → flash, confetti, floating hearts, a happy chime, and a zoom into "I KNEW IT! 😌❤️" |
| 5 | An animated gift box explodes into 5 surprises, revealed one by one |
| 6 | A full-screen finale that builds line by line, plus a hidden **One More Surprise? 👀** |

Everything happens on one page. Nothing ever reloads.

## Make it yours

Open `index.html` and edit the **`CONFIG`** object at the top of the JS block
at the bottom of the file. That is the only place you need to touch.

```js
const CONFIG = {
  herName: "",            // her name — leave "" to keep it generic
  music: "",              // "music/our-song.mp3" — or "" for the built-in loop
  musicVolume: 0.35,
  photos: {
    surprise: PHOTOS.her1,  // Surprise #4  (or a path: "photos/her1.jpg")
    finale:   PHOTOS.her2   // hidden final surprise
  },
  surprises: [ ... ],     // the 5 gift-box cards: tag, icon, title, body
  finalHidden: { ... },   // the hidden one-more-surprise card
  taunts: [ ... ]         // the funny KARELA messages
};
```

- **Photos** — two photos are already embedded (as base64, at the very top of
  `<body>`) so `index.html` stays a single portable file you can send as-is.
  They appear as Surprise #4 and in the hidden final surprise. To change one,
  either replace its base64 string, or just set `CONFIG.photos.surprise` /
  `.finale` to a file path like `"photos/her1.jpg"`. Optimized copies live in
  `photos/`, and the full-resolution originals are kept in the repo root.
  Photos render uncropped at their natural shape in a soft polaroid frame.
- **Music** — drop a track in `music/` and set `CONFIG.music`. If it's empty
  (or the file is missing) the page generates its own soft romantic piano loop
  in-browser, so there is always background music. The 🔈 button in the corner
  mutes and unmutes everything.
- **Surprises** — add or remove entries in `CONFIG.surprises`; the page adapts
  to however many there are.

## How the runaway KARELA works

- It lives inside the choice arena and is repositioned in **arena-relative
  pixels**, clamped to the arena's bounds — so it can never leave the visible
  screen, at any size.
- Desktop: a proximity check on `mousemove` moves it before the cursor arrives.
- Mobile: `touchstart` / `touchmove` are intercepted so it dodges before her
  finger can land.
- Three dodge flavours — a small hop, a random jump, or a leap to the opposite
  side — plus occasional tilts and a cheeky shrink-and-return.
- Moves are throttled (~260ms) so it stays funny instead of frantic, and it
  always lands clear of the **ME** button, which never moves and is always
  clickable.
- After a dozen dodges it quietly hints that the other button isn't running away,
  so the card can always be completed.
- If she somehow *does* catch it, she gets a cheer — and it dodges anyway. 😌

## Tested

Driven end to end with Playwright on desktop (1280×820) and mobile (390×844,
touch): every stage advances, the KARELA button stayed inside the viewport
across every dodge, the ME button stayed clickable, all 5 surprises render,
and the finale plus hidden surprise reveal correctly. Both embedded photos
decode and display at their true 2:3 ratio with no placeholders left over.
No console errors.

## Accessibility & polish

- Respects `prefers-reduced-motion` (animations collapse, smooth scroll off).
- The gift box is keyboard-reachable (Tab, then Enter or Space).
- Responsive from small phones to desktop; fonts and spacing scale fluidly.
- Sound is off-by-default until she interacts, respecting browser autoplay rules.

---

# 💌 Taniya ji ka letter — `taniya-letter.html`

A separate, single-file digital letter-card (Hinglish), made to be opened on a
phone. Ten screens, one at a time: a cute "Ruko! ✋" start → a sealed envelope
with a heart wax seal that opens in 3D → hello → the 14 July calendar →
six flip-open notes → dil ki baat → three shayari cards → four gift boxes
(including a Tension Exchange Coupon) → the SORRY surprise with the
Haan / Nahi game → the closing letter, which folds back into the envelope.

## Fill in your details

Open `taniya-letter.html`, find the `CONFIG` block at the top of the
`<script>` near the bottom, and replace the `____` values:

```js
const CONFIG = {
  myName:   "____",   // your name → signature on the last screen
  meetTime: "____",   // e.g. "shaam 5 baje" → added to the 14 July line
  outfit:   "____",   // e.g. "blue kurti"  → added to the 14 July line
  loves:    "____",   // e.g. "red roses, momos, pink" → swaps the bouquet / chocolate gifts
  whatsapp: "____"    // e.g. "91XXXXXXXXXX" → shows a "Reply bhejo 💬" button
};
```

Anything left as `____` (or empty) is simply left out and the sentence is
written without it; no blanks or underscores ever appear on the card.
Colours in `loves` are ignored for the gift swap; a flower (rose, sunflower,
tulip…) replaces the bouquet and the first non-flower favourite replaces the
chocolate.

## Notes

- One file, plain HTML/CSS/JS. Everything is drawn with CSS, SVG and emoji;
  the only network request is Google Fonts (Dancing Script + Poppins), with
  system-font fallbacks if she's offline.
- The 🎵 button (off by default) plays a soft music-box tune generated with the
  Web Audio API, so there are no audio files.
- Tap empty space for a tiny heart. On the last screen there's a hidden heart
  in the bottom-right corner of the letter. 😉
- Phone back gesture / browser back works screen by screen.
- Respects `prefers-reduced-motion`.
