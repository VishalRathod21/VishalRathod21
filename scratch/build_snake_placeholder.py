import random

# Generate a dark contribution snake SVG matching GitHub dark theme
snake_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 140" width="100%" height="100%">
  <defs>
    <linearGradient id="snakeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F8CFF"/>
      <stop offset="50%" stop-color="#7C5CFF"/>
      <stop offset="100%" stop-color="#B28DFF"/>
    </linearGradient>

    <filter id="glowSnake" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', monospace; }
    @keyframes moveSnake {
      0% { transform: translate(0px, 0px); }
      25% { transform: translate(120px, 20px); }
      50% { transform: translate(300px, -10px); }
      75% { transform: translate(500px, 30px); }
      100% { transform: translate(750px, 0px); }
    }
  </style>

  <rect width="880" height="140" rx="16" fill="#04070E" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>

  <!-- Matrix Grid -->
  <g transform="translate(30, 20)">
'''

# Add 52 columns x 7 rows of contribution dots
cols = 52
rows = 7
cell_size = 12
cell_gap = 4

colors = ["#0A1224", "#0A1224", "#0A1224", "#1E293B", "#4F8CFF", "#7C5CFF", "#B28DFF"]

grid_xml = ""
for c in range(cols):
    for r in range(rows):
        x = c * (cell_size + cell_gap)
        y = r * (cell_size + cell_gap)
        # pick pseudo-random color based on pos
        val = (c * 7 + r * 13) % len(colors)
        color = colors[val]
        grid_xml += f'    <rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{color}"/>\n'

snake_head_xml = '''
    <!-- Animated Snake -->
    <g style="animation: moveSnake 8s linear infinite ease-in-out;" filter="url(#glowSnake)">
      <circle cx="10" cy="10" r="7" fill="url(#snakeGrad)"/>
      <circle cx="2" cy="10" r="5" fill="#7C5CFF" opacity="0.8"/>
      <circle cx="-5" cy="10" r="4" fill="#4F8CFF" opacity="0.6"/>
      <circle cx="-11" cy="10" r="3" fill="#B28DFF" opacity="0.4"/>
    </g>
  </g>

  <!-- Watermark -->
  <text x="850" y="128" fill="#94A3B8" font-size="10" class="mono" text-anchor="end" opacity="0.6">CONTRIBUTION MATRIX // SNAKE ENGINE</text>
</svg>'''

full_snake_svg = snake_svg + grid_xml + snake_head_xml

with open("assets/github-contribution-grid-snake-dark.svg", "w") as f:
    f.write(full_snake_svg)

with open("assets/github-contribution-grid-snake.svg", "w") as f:
    f.write(full_snake_svg)

print("Generated snake SVGs!")
