lines = [
    "\u2580\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2593\u2593\u2584\u2584\u2588\u2588\u2593\u2584  \u2588\u2584   \u2580\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2593\u2593\u2593\u2593\u2584  \u2580\u2588\u2588\u2588\u2588\u2588\u2593\u2593\u2593\u2584  \u2584\u2588\u2588\u2588\u2588\u2588\u2593\u2593\u2593\u2580",
    "  \u2580  \u2584 \u2580\u2593\u2593\u2593\u2580 \u2593\u2593\u2592  \u2593\u2593\u2592\u2584   \u2580  \u2584    \u2580\u2593\u2593\u2592   \u2580     \u2593\u2593\u2593 \u2588\u2593\u2593    \u2580  ",
    "   \u2588\u2593\u2593  \u2593\u2592\u2592  \u2592\u2592\u2591  \u2592\u2592\u2592     \u2588\u2593\u2593   \u2584\u2592\u2591\u2580   \u2584\u2591 \u2584   \u2592\u2592\u2591 \u2593\u2592\u2592       ",
    "   \u2593\u2592\u2592  \u2591\u2591   \u2591\u2591   \u2592\u2591      \u2593\u2592\u2592  \u2580\u2591 \u2584      \u2580\u2591\u2591\u2591     \u2592\u2591\u2591       ",
    "   \u2592\u2591   \u2591\u2591\u2592  \u2591\u2591\u2592  \u2591\u2591\u2592     \u2591 \u2591    \u2591\u2591\u2592  \u2591\u2591\u2592  \u2580  \u2591\u2591\u2592 \u2591\u2591\u2592       ",
    "  \u2584\u2591\u2592\u2592  \u2592\u2592\u2593  \u2592\u2592\u2593 \u2584\u2592\u2592\u2593    \u2584\u2591\u2592\u2593    \u2592\u2592\u2593  \u2592\u2592\u2593    \u2584\u2592\u2592\u2593 \u2592\u2592\u2593    \u2584  ",
    "   \u2580\u2593\u2593  \u2593\u2593\u2588  \u2593\u2593\u2588  \u2580\u2593\u2593     \u2580\u2593\u2593    \u2593\u2593\u2588  \u2580\u2593\u2593     \u2580\u2593\u2593  \u2580\u2593\u2588\u2593\u2593\u2593\u2593\u2593\u2584",
    "     \u2580              \u2580       \u2580           \u2580       \u2580           ",
]

CW, CH = 12, 24  # cell width / height

# char -> (y_offset_fraction, height_fraction, opacity)
GLYPHS = {
    "\u2588": (0.0, 1.0, 1.00),
    "\u2593": (0.0, 1.0, 0.72),
    "\u2592": (0.0, 1.0, 0.45),
    "\u2591": (0.0, 1.0, 0.22),
    "\u2580": (0.0, 0.5, 1.00),
    "\u2584": (0.5, 0.5, 1.00),
}

width = max(len(l) for l in lines)
lines = [l.ljust(width) for l in lines]
W, H = width * CW, len(lines) * CH

rects = []
for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        if ch not in GLYPHS:
            continue
        dy, fh, op = GLYPHS[ch]
        x = col * CW
        y = row * CH + dy * CH
        h = fh * CH
        # +0.5 overlap kills hairline seams between adjacent rects
        rects.append(
            f'<rect x="{x}" y="{y:.1f}" width="{CW + 0.5}" height="{h + 0.5:.1f}" '
            f'opacity="{op}"/>'
        )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Mirac">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="{H}" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#f472ff"/>
      <stop offset="55%" stop-color="#c04ae0"/>
      <stop offset="100%" stop-color="#6b5b95"/>
    </linearGradient>
  </defs>
  <g fill="url(#g)" shape-rendering="crispEdges">
    {chr(10).join("    " + r for r in rects).strip()}
  </g>
</svg>
'''

with open("/mnt/user-data/outputs/mirac.svg", "w") as f:
    f.write(svg)

print(f"{width} cols x {len(lines)} rows -> {W}x{H}px, {len(rects)} rects")
