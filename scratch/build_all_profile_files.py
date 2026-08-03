import os
import base64

# Read profile image base64
profile_path = 'assets/profile.png'
if os.path.exists(profile_path):
    with open(profile_path, 'rb') as f:
        profile_b64 = base64.b64encode(f.read()).decode('utf-8')
    print(f"Loaded profile image ({len(profile_b64)} chars)")
else:
    profile_b64 = ""
    print("Warning: profile.png not found")

os.makedirs('assets', exist_ok=True)
os.makedirs('.github/workflows', exist_ok=True)

# ----------------------------------------------------
# 1. banner-dark.svg (1400x700, rx=40)
# ----------------------------------------------------
banner_dark_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 700" width="1400" height="700">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap');

      * {{ box-sizing: border-box; }}
      text {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
      .mono {{ font-family: 'JetBrains Mono', monospace; }}

      @keyframes floatGlow {{
        0%, 100% {{ transform: translate(0, 0) scale(1); opacity: 0.15; }}
        50% {{ transform: translate(30px, -20px) scale(1.1); opacity: 0.25; }}
      }}

      @keyframes particleFloat1 {{
        0% {{ transform: translateY(0px) translateX(0px); opacity: 0.2; }}
        50% {{ transform: translateY(-80px) translateX(20px); opacity: 0.8; }}
        100% {{ transform: translateY(-160px) translateX(-10px); opacity: 0; }}
      }}

      @keyframes particleFloat2 {{
        0% {{ transform: translateY(0px) translateX(0px); opacity: 0.3; }}
        50% {{ transform: translateY(-100px) translateX(-30px); opacity: 0.9; }}
        100% {{ transform: translateY(-200px) translateX(15px); opacity: 0; }}
      }}

      @keyframes typeLine1 {{ 0%, 5% {{ opacity: 0; }} 10%, 100% {{ opacity: 1; }} }}
      @keyframes typeLine2 {{ 0%, 20% {{ opacity: 0; }} 25%, 100% {{ opacity: 1; }} }}
      @keyframes typeLine3 {{ 0%, 35% {{ opacity: 0; }} 40%, 100% {{ opacity: 1; }} }}
      @keyframes typeLine4 {{ 0%, 50% {{ opacity: 0; }} 55%, 100% {{ opacity: 1; }} }}
      @keyframes typeLine5 {{ 0%, 65% {{ opacity: 0; }} 70%, 100% {{ opacity: 1; }} }}
      @keyframes typeLine6 {{ 0%, 80% {{ opacity: 0; }} 85%, 100% {{ opacity: 1; }} }}

      @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}

      @keyframes scanLine {{
        0% {{ transform: translateY(0px); opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ transform: translateY(480px); opacity: 0; }}
      }}

      @keyframes hologramReveal {{
        0% {{ opacity: 0; transform: scale(0.95); }}
        100% {{ opacity: 1; transform: scale(1); }}
      }}

      @keyframes glassPulse {{
        0%, 100% {{ stroke: rgba(255, 255, 255, 0.12); }}
        50% {{ stroke: rgba(79, 140, 255, 0.35); }}
      }}

      @keyframes nodePulse {{
        0%, 100% {{ r: 3px; opacity: 0.4; }}
        50% {{ r: 5px; opacity: 1; }}
      }}
    </style>

    <clipPath id="banner-clip">
      <rect width="1400" height="700" rx="40" ry="40"/>
    </clipPath>

    <clipPath id="terminal-clip">
      <rect x="50" y="70" width="410" height="560" rx="24" ry="24"/>
    </clipPath>

    <clipPath id="char-frame-clip">
      <rect x="940" y="70" width="410" height="560" rx="28" ry="28"/>
    </clipPath>

    <mask id="char-mask">
      <rect x="940" y="70" width="410" height="560" fill="white"/>
      <rect x="940" y="470" width="410" height="160" fill="url(#bottom-fade-grad)"/>
    </mask>

    <linearGradient id="bottom-fade-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="black" stop-opacity="0"/>
      <stop offset="100%" stop-color="black" stop-opacity="1"/>
    </linearGradient>

    <radialGradient id="bg-glow-primary" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#4F8CFF" stop-opacity="0.22"/>
      <stop offset="50%" stop-color="#7C5CFF" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#04070E" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="bg-glow-accent" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#B28DFF" stop-opacity="0.18"/>
      <stop offset="60%" stop-color="#7C5CFF" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#04070E" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="char-bg-glow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#4F8CFF" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#7C5CFF" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0A1224" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="text-title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="40%" stop-color="#4F8CFF"/>
      <stop offset="70%" stop-color="#7C5CFF"/>
      <stop offset="100%" stop-color="#B28DFF"/>
    </linearGradient>

    <linearGradient id="glass-border-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="rgba(255,255,255,0.22)"/>
      <stop offset="50%" stop-color="rgba(79,140,255,0.15)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0.05)"/>
    </linearGradient>

    <linearGradient id="scan-line-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#4F8CFF" stop-opacity="0"/>
      <stop offset="20%" stop-color="#4F8CFF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#B28DFF" stop-opacity="1"/>
      <stop offset="80%" stop-color="#4F8CFF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#4F8CFF" stop-opacity="0"/>
    </linearGradient>

    <pattern id="grid-pattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(79, 140, 255, 0.04)" stroke-width="1"/>
      <circle cx="40" cy="40" r="1" fill="rgba(255, 255, 255, 0.08)"/>
    </pattern>

    <pattern id="dot-matrix" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="0.8" fill="rgba(148, 163, 184, 0.12)"/>
    </pattern>
  </defs>

  <g clip-path="url(#banner-clip)">
    <rect width="1400" height="700" fill="#04070E"/>
    <rect width="1400" height="700" fill="url(#grid-pattern)"/>

    <circle cx="700" cy="200" r="450" fill="url(#bg-glow-primary)" style="animation: floatGlow 12s ease-in-out infinite;"/>
    <circle cx="1100" cy="350" r="350" fill="url(#bg-glow-accent)" style="animation: floatGlow 16s ease-in-out infinite reverse;"/>
    <circle cx="250" cy="450" r="300" fill="url(#bg-glow-primary)" style="animation: floatGlow 14s ease-in-out infinite 2s;"/>

    <g opacity="0.6">
      <circle cx="180" cy="600" r="1.5" fill="#4F8CFF" style="animation: particleFloat1 8s ease-in-out infinite;"/>
      <circle cx="320" cy="550" r="2" fill="#B28DFF" style="animation: particleFloat2 11s ease-in-out infinite 1s;"/>
      <circle cx="500" cy="620" r="1" fill="#F8FAFC" style="animation: particleFloat1 9s ease-in-out infinite 3s;"/>
      <circle cx="650" cy="580" r="2.5" fill="#7C5CFF" style="animation: particleFloat2 13s ease-in-out infinite 2s;"/>
      <circle cx="820" cy="640" r="1.5" fill="#4F8CFF" style="animation: particleFloat1 10s ease-in-out infinite 4s;"/>
      <circle cx="1020" cy="590" r="2" fill="#B28DFF" style="animation: particleFloat2 12s ease-in-out infinite 1.5s;"/>
      <circle cx="1250" cy="610" r="1" fill="#F8FAFC" style="animation: particleFloat1 7s ease-in-out infinite 2.5s;"/>
    </g>

    <g opacity="0.4">
      <circle cx="120" cy="90" r="1" fill="#F8FAFC"/>
      <circle cx="380" cy="50" r="1.2" fill="#4F8CFF"/>
      <circle cx="620" cy="80" r="0.8" fill="#F8FAFC"/>
      <circle cx="850" cy="40" r="1.5" fill="#B28DFF"/>
      <circle cx="1280" cy="90" r="1" fill="#F8FAFC"/>
    </g>

    <!-- LEFT SIDE TERMINAL -->
    <g transform="translate(0, 0)">
      <rect x="50" y="70" width="410" height="560" rx="24" fill="rgba(0,0,0,0.4)" filter="blur(10px)"/>
      <rect x="50" y="70" width="410" height="560" rx="24" fill="rgba(10, 18, 36, 0.65)" stroke="url(#glass-border-grad)" stroke-width="1.5" style="animation: glassPulse 8s ease-in-out infinite;"/>
      <rect x="51" y="71" width="408" height="558" rx="23" fill="url(#dot-matrix)" opacity="0.5"/>

      <rect x="50" y="70" width="410" height="42" rx="24" fill="rgba(255, 255, 255, 0.04)"/>
      <line x1="50" y1="112" x2="460" y2="112" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

      <circle cx="78" cy="91" r="5.5" fill="#FF5F56" opacity="0.85"/>
      <circle cx="96" cy="91" r="5.5" fill="#FFBD2E" opacity="0.85"/>
      <circle cx="114" cy="91" r="5.5" fill="#27C93F" opacity="0.85"/>

      <text x="255" y="96" fill="#94A3B8" font-size="12" font-weight="500" text-anchor="middle" class="mono" letter-spacing="1">ai-core-kernel.v4 ~ zsh</text>
      
      <rect x="385" y="83" width="55" height="16" rx="8" fill="rgba(39, 201, 63, 0.15)" stroke="rgba(39, 201, 63, 0.4)" stroke-width="0.8"/>
      <circle cx="395" cy="91" r="2.5" fill="#27C93F"/>
      <text x="418" y="94" fill="#27C93F" font-size="9" font-weight="600" text-anchor="middle" class="mono">LIVE</text>

      <g transform="translate(75, 140)" class="mono" font-size="12">
        <g style="animation: typeLine1 10s ease-in-out infinite;">
          <text x="0" y="0" fill="#4F8CFF" font-weight="600">&gt;</text>
          <text x="16" y="0" fill="#94A3B8">Initializing AI Core...</text>
        </g>
        <g style="animation: typeLine2 10s ease-in-out infinite;">
          <text x="0" y="22" fill="#4F8CFF" font-weight="600">&gt;</text>
          <text x="16" y="22" fill="#94A3B8">Loading Neural Network...</text>
        </g>
        <g style="animation: typeLine3 10s ease-in-out infinite;">
          <text x="0" y="44" fill="#4F8CFF" font-weight="600">&gt;</text>
          <text x="16" y="44" fill="#94A3B8">Loading Memory...</text>
        </g>
        <g style="animation: typeLine4 10s ease-in-out infinite;">
          <text x="0" y="66" fill="#4F8CFF" font-weight="600">&gt;</text>
          <text x="16" y="66" fill="#94A3B8">Loading Projects...</text>
        </g>
        <g style="animation: typeLine5 10s ease-in-out infinite;">
          <text x="0" y="88" fill="#4F8CFF" font-weight="600">&gt;</text>
          <text x="16" y="88" fill="#94A3B8">Loading Models...</text>
        </g>
        <g style="animation: typeLine6 10s ease-in-out infinite;">
          <text x="0" y="110" fill="#27C93F" font-weight="600">✓</text>
          <text x="16" y="110" fill="#27C93F" font-weight="600">Ready.</text>
        </g>
      </g>

      <line x1="75" y1="270" x2="435" y2="270" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" stroke-dasharray="4 4"/>

      <g transform="translate(75, 295)" class="mono">
        <text x="0" y="0" fill="#B28DFF" font-size="13" font-weight="600">$ whoami</text>
        <text x="0" y="28" fill="#F8FAFC" font-size="18" font-weight="700">Vishal Rathod</text>
        
        <g transform="translate(0, 42)">
          <rect x="0" y="0" width="105" height="22" rx="6" fill="rgba(79, 140, 255, 0.12)" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1"/>
          <text x="52.5" y="14.5" fill="#4F8CFF" font-size="10" font-weight="600" text-anchor="middle">AI Engineer</text>

          <rect x="113" y="0" width="145" height="22" rx="6" fill="rgba(124, 92, 255, 0.12)" stroke="rgba(124, 92, 255, 0.3)" stroke-width="1"/>
          <text x="185.5" y="14.5" fill="#7C5CFF" font-size="10" font-weight="600" text-anchor="middle">Machine Learning</text>

          <rect x="0" y="28" width="115" height="22" rx="6" fill="rgba(178, 141, 255, 0.12)" stroke="rgba(178, 141, 255, 0.3)" stroke-width="1"/>
          <text x="57.5" y="42.5" fill="#B28DFF" font-size="10" font-weight="600" text-anchor="middle">Generative AI</text>

          <rect x="123" y="28" width="125" height="22" rx="6" fill="rgba(79, 140, 255, 0.12)" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1"/>
          <text x="185.5" y="42.5" fill="#4F8CFF" font-size="10" font-weight="600" text-anchor="middle">Agentic AI Builder</text>
        </g>
      </g>

      <line x1="75" y1="415" x2="435" y2="415" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" stroke-dasharray="4 4"/>

      <g transform="translate(75, 440)">
        <text x="0" y="0" fill="#94A3B8" font-size="11" font-weight="600" class="mono" letter-spacing="1">CURRENT MISSION</text>
        <rect x="0" y="12" width="360" height="85" rx="12" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
        <text x="16" y="38" fill="#F8FAFC" font-size="12.5" font-weight="500">"Building AI systems that solve</text>
        <text x="16" y="58" fill="#F8FAFC" font-size="12.5" font-weight="500">real-world problems."</text>
        <rect x="16" y="72" width="8" height="2" fill="#4F8CFF" style="animation: blink 1s step-end infinite;"/>
      </g>
    </g>

    <!-- CENTER BRANDING -->
    <g transform="translate(490, 180)">
      <rect x="0" y="0" width="265" height="28" rx="14" fill="rgba(79, 140, 255, 0.1)" stroke="rgba(79, 140, 255, 0.25)" stroke-width="1"/>
      <circle cx="16" cy="14" r="3.5" fill="#4F8CFF" style="animation: nodePulse 2s ease-in-out infinite;"/>
      <text x="30" y="18" fill="#4F8CFF" font-size="11" font-weight="600" class="mono" letter-spacing="1.5">AI RESEARCH LABORATORY</text>

      <g transform="translate(0, 80)">
        <text x="0" y="0" fill="url(#text-title-grad)" font-size="54" font-weight="900" letter-spacing="4">VISHAL RATHOD</text>
        <text x="0" y="0" fill="none" stroke="#4F8CFF" stroke-width="4" stroke-opacity="0.15" font-size="54" font-weight="900" letter-spacing="4" filter="blur(8px)">VISHAL RATHOD</text>
      </g>

      <g transform="translate(0, 115)">
        <text x="0" y="0" fill="#94A3B8" font-size="16" font-weight="500" letter-spacing="3" class="mono">ARTIFICIAL INTELLIGENCE ENGINEER</text>
      </g>

      <g transform="translate(0, 150)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="125" height="32" rx="10" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
          <text x="14" y="20" fill="#4F8CFF" font-size="12" font-weight="600" class="mono">❖ LLMs</text>
        </g>
        <g transform="translate(135, 0)">
          <rect x="0" y="0" width="135" height="32" rx="10" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
          <text x="14" y="20" fill="#7C5CFF" font-size="12" font-weight="600" class="mono">❖ Deep Learning</text>
        </g>
        <g transform="translate(280, 0)">
          <rect x="0" y="0" width="130" height="32" rx="10" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
          <text x="14" y="20" fill="#B28DFF" font-size="12" font-weight="600" class="mono">❖ Agentic AI</text>
        </g>
      </g>

      <g transform="translate(0, 215)">
        <rect x="0" y="0" width="410" height="110" rx="16" fill="rgba(10, 18, 36, 0.5)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
        <text x="18" y="26" fill="#94A3B8" font-size="10" font-weight="600" class="mono" letter-spacing="1">SYSTEM TELEMETRY // ACTIVE WORKSPACE</text>
        <circle cx="390" cy="22" r="3" fill="#27C93F"/>

        <g transform="translate(18, 45)">
          <text x="0" y="12" fill="#64748B" font-size="10" font-weight="500" class="mono">CORE ENGINE</text>
          <text x="0" y="32" fill="#F8FAFC" font-size="15" font-weight="700">PyTorch &amp; vLLM</text>
        </g>

        <line x1="145" y1="45" x2="145" y2="90" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>

        <g transform="translate(165, 45)">
          <text x="0" y="12" fill="#64748B" font-size="10" font-weight="500" class="mono">LOCATION</text>
          <text x="0" y="32" fill="#F8FAFC" font-size="15" font-weight="700">India 🇮🇳</text>
        </g>

        <line x1="280" y1="45" x2="280" y2="90" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>

        <g transform="translate(300, 45)">
          <text x="0" y="12" fill="#64748B" font-size="10" font-weight="500" class="mono">STATUS</text>
          <text x="0" y="32" fill="#4F8CFF" font-size="15" font-weight="700">Online</text>
        </g>
      </g>
    </g>

    <!-- RIGHT SIDE HOLOGRAM CHAMBER -->
    <g transform="translate(0, 0)">
      <circle cx="1145" cy="350" r="220" fill="url(#char-bg-glow)"/>
      <rect x="940" y="70" width="410" height="560" rx="28" fill="rgba(10, 18, 36, 0.55)" stroke="url(#glass-border-grad)" stroke-width="1.5" style="animation: glassPulse 8s ease-in-out infinite 4s;"/>

      <g opacity="0.5">
        <line x1="990" y1="180" x2="1060" y2="130" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1" stroke-dasharray="2 2"/>
        <line x1="1060" y1="130" x2="1180" y2="160" stroke="rgba(124, 92, 255, 0.3)" stroke-width="1"/>
        <line x1="1180" y1="160" x2="1280" y2="120" stroke="rgba(178, 141, 255, 0.3)" stroke-width="1" stroke-dasharray="2 2"/>
        
        <circle cx="990" cy="180" r="3" fill="#4F8CFF" style="animation: nodePulse 3s infinite;"/>
        <circle cx="1060" cy="130" r="4" fill="#7C5CFF" style="animation: nodePulse 2.5s infinite 1s;"/>
        <circle cx="1180" cy="160" r="3.5" fill="#B28DFF" style="animation: nodePulse 3.5s infinite 0.5s;"/>
        <circle cx="1280" cy="120" r="3" fill="#4F8CFF" style="animation: nodePulse 2s infinite 1.5s;"/>
      </g>

      <g clip-path="url(#char-frame-clip)" mask="url(#char-mask)">
        <image href="data:image/png;base64,{profile_b64}" x="920" y="50" width="450" height="600" preserveAspectRatio="xMidYMid slice" opacity="0.92" style="animation: hologramReveal 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;"/>
      </g>

      <g transform="translate(1210, 95)" opacity="0.85">
        <rect x="0" y="0" width="120" height="42" rx="8" fill="rgba(10, 18, 36, 0.7)" stroke="rgba(79, 140, 255, 0.4)" stroke-width="1"/>
        <text x="10" y="16" fill="#64748B" font-size="8" font-weight="600" class="mono">MODEL ACCURACY</text>
        <text x="10" y="32" fill="#4F8CFF" font-size="13" font-weight="700" class="mono">99.4% [SOTA]</text>
      </g>

      <g transform="translate(960, 560)" opacity="0.85">
        <rect x="0" y="0" width="130" height="42" rx="8" fill="rgba(10, 18, 36, 0.7)" stroke="rgba(178, 141, 255, 0.4)" stroke-width="1"/>
        <text x="10" y="16" fill="#64748B" font-size="8" font-weight="600" class="mono">AGENT STATE</text>
        <text x="10" y="32" fill="#B28DFF" font-size="13" font-weight="700" class="mono">AUTONOMOUS</text>
      </g>

      <g clip-path="url(#char-frame-clip)">
        <g style="animation: scanLine 4s ease-in-out infinite 1s;">
          <rect x="940" y="70" width="410" height="3" fill="url(#scan-line-grad)"/>
          <rect x="940" y="65" width="410" height="12" fill="url(#scan-line-grad)" opacity="0.3" filter="blur(4px)"/>
        </g>
      </g>

      <text x="1145" y="92" fill="#94A3B8" font-size="10" font-weight="600" text-anchor="middle" class="mono" letter-spacing="1.5">NEURAL ARCHITECT // AVATAR</text>
    </g>
  </g>
</svg>
'''

with open('assets/banner-dark.svg', 'w') as f:
    f.write(banner_dark_content)
print("Generated assets/banner-dark.svg")

# ----------------------------------------------------
# 2. banner-light.svg
# ----------------------------------------------------
banner_light_content = banner_dark_content.replace(
    'fill="#04070E"', 'fill="#F8FAFC"'
).replace(
    'fill="rgba(10, 18, 36, 0.65)"', 'fill="rgba(255, 255, 255, 0.85)"'
).replace(
    'fill="rgba(10, 18, 36, 0.5)"', 'fill="rgba(241, 245, 249, 0.8)"'
).replace(
    'fill="rgba(10, 18, 36, 0.55)"', 'fill="rgba(241, 245, 249, 0.85)"'
).replace(
    'fill="rgba(10, 18, 36, 0.7)"', 'fill="rgba(255, 255, 255, 0.9)"'
).replace(
    'fill="#F8FAFC"', 'fill="#0F172A"'
).replace(
    'fill="#94A3B8"', 'fill="#475569"'
).replace(
    'fill="#64748B"', 'fill="#475569"'
).replace(
    'stroke="rgba(255, 255, 255, 0.08)"', 'stroke="rgba(15, 23, 42, 0.1)"'
)

with open('assets/banner-light.svg', 'w') as f:
    f.write(banner_light_content)
print("Generated assets/banner-light.svg")

# ----------------------------------------------------
# 3. skills.svg (900x420, rx=24)
# ----------------------------------------------------
skills_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="900" height="420">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;600&amp;display=swap');
      * { box-sizing: border-box; }
      text { font-family: 'Inter', sans-serif; }
      .mono { font-family: 'JetBrains Mono', monospace; }

      @keyframes floatCard {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-6px); }
      }

      @keyframes pulseBorder {
        0%, 100% { stroke: rgba(255, 255, 255, 0.12); }
        50% { stroke: rgba(79, 140, 255, 0.35); }
      }
    </style>

    <linearGradient id="card-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="rgba(10, 18, 36, 0.75)"/>
      <stop offset="100%" stop-color="rgba(4, 7, 14, 0.85)"/>
    </linearGradient>

    <linearGradient id="badge-grad-1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="rgba(79, 140, 255, 0.15)"/>
      <stop offset="100%" stop-color="rgba(79, 140, 255, 0.05)"/>
    </linearGradient>
  </defs>

  <rect width="900" height="420" rx="24" fill="#04070E" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(35, 45)">
    <circle cx="8" cy="8" r="4" fill="#4F8CFF"/>
    <text x="22" y="12" fill="#4F8CFF" font-size="12" font-weight="700" class="mono" letter-spacing="2">TECHNICAL CAPABILITIES // SKILL MATRIX</text>
  </g>

  <!-- Skill Category 1: Languages -->
  <g transform="translate(35, 80)" style="animation: floatCard 6s ease-in-out infinite;">
    <rect width="260" height="300" rx="18" fill="url(#card-grad)" stroke="rgba(255,255,255,0.1)" stroke-width="1.2" style="animation: pulseBorder 8s infinite;"/>
    
    <g transform="translate(24, 30)">
      <text x="0" y="0" fill="#F8FAFC" font-size="18" font-weight="700">Languages</text>
      <text x="0" y="18" fill="#94A3B8" font-size="11" class="mono">Core Software Engineering</text>
      
      <line x1="0" y1="32" x2="212" y2="32" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

      <g transform="translate(0, 50)" class="mono" font-size="12">
        <!-- Item 1 -->
        <rect x="0" y="0" width="212" height="38" rx="8" fill="url(#badge-grad-1)" stroke="rgba(79, 140, 255, 0.25)" stroke-width="1"/>
        <text x="14" y="24" fill="#F8FAFC" font-weight="600">Python</text>
        <text x="198" y="24" fill="#4F8CFF" font-size="10" text-anchor="end">EXPERT</text>

        <!-- Item 2 -->
        <rect x="0" y="48" width="212" height="38" rx="8" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="14" y="72" fill="#F8FAFC" font-weight="600">C++</text>
        <text x="198" y="72" fill="#94A3B8" font-size="10" text-anchor="end">ADVANCED</text>

        <!-- Item 3 -->
        <rect x="0" y="96" width="212" height="38" rx="8" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="14" y="120" fill="#F8FAFC" font-weight="600">SQL</text>
        <text x="198" y="120" fill="#94A3B8" font-size="10" text-anchor="end">PRO</text>

        <!-- Item 4 -->
        <rect x="0" y="144" width="212" height="38" rx="8" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="14" y="168" fill="#F8FAFC" font-weight="600">JavaScript</text>
        <text x="198" y="168" fill="#94A3B8" font-size="10" text-anchor="end">PRO</text>
      </g>
    </g>
  </g>

  <!-- Skill Category 2: Artificial Intelligence -->
  <g transform="translate(320, 80)" style="animation: floatCard 6s ease-in-out infinite 1s;">
    <rect width="260" height="300" rx="18" fill="url(#card-grad)" stroke="rgba(124, 92, 255, 0.3)" stroke-width="1.5"/>
    
    <g transform="translate(24, 30)">
      <text x="0" y="0" fill="#F8FAFC" font-size="18" font-weight="700">AI &amp; Intelligence</text>
      <text x="0" y="18" fill="#B28DFF" font-size="11" class="mono">LLMs, GenAI &amp; Agents</text>
      
      <line x1="0" y1="32" x2="212" y2="32" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

      <g transform="translate(0, 50)" class="mono" font-size="11">
        <!-- Badges grid -->
        <rect x="0" y="0" width="100" height="32" rx="8" fill="rgba(124, 92, 255, 0.15)" stroke="rgba(124, 92, 255, 0.3)"/>
        <text x="50" y="20" fill="#B28DFF" font-weight="600" text-anchor="middle">PyTorch</text>

        <rect x="110" y="0" width="102" height="32" rx="8" fill="rgba(124, 92, 255, 0.15)" stroke="rgba(124, 92, 255, 0.3)"/>
        <text x="161" y="20" fill="#B28DFF" font-weight="600" text-anchor="middle">TensorFlow</text>

        <rect x="0" y="40" width="100" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="50" y="60" fill="#F8FAFC" text-anchor="middle">LangChain</text>

        <rect x="110" y="40" width="102" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="161" y="60" fill="#F8FAFC" text-anchor="middle">LangGraph</text>

        <rect x="0" y="80" width="100" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="50" y="100" fill="#F8FAFC" text-anchor="middle">CrewAI</text>

        <rect x="110" y="80" width="102" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="161" y="100" fill="#F8FAFC" text-anchor="middle">AutoGen</text>

        <rect x="0" y="120" width="100" height="32" rx="8" fill="rgba(79, 140, 255, 0.15)" stroke="rgba(79, 140, 255, 0.3)"/>
        <text x="50" y="140" fill="#4F8CFF" font-weight="600" text-anchor="middle">OpenAI</text>

        <rect x="110" y="120" width="102" height="32" rx="8" fill="rgba(79, 140, 255, 0.15)" stroke="rgba(79, 140, 255, 0.3)"/>
        <text x="161" y="140" fill="#4F8CFF" font-weight="600" text-anchor="middle">Gemini</text>

        <rect x="0" y="160" width="212" height="30" rx="8" fill="rgba(178, 141, 255, 0.15)" stroke="rgba(178, 141, 255, 0.3)"/>
        <text x="106" y="180" fill="#B28DFF" font-weight="600" text-anchor="middle">Groq &amp; Scikit-Learn</text>
      </g>
    </g>
  </g>

  <!-- Skill Category 3: Backend & Infra -->
  <g transform="translate(605, 80)" style="animation: floatCard 6s ease-in-out infinite 2s;">
    <rect width="260" height="300" rx="18" fill="url(#card-grad)" stroke="rgba(255,255,255,0.1)" stroke-width="1.2"/>
    
    <g transform="translate(24, 30)">
      <text x="0" y="0" fill="#F8FAFC" font-size="18" font-weight="700">Backend &amp; Cloud</text>
      <text x="0" y="18" fill="#94A3B8" font-size="11" class="mono">Scalable Infrastructure</text>
      
      <line x1="0" y1="32" x2="212" y2="32" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

      <g transform="translate(0, 50)" class="mono" font-size="11">
        <rect x="0" y="0" width="100" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="50" y="20" fill="#F8FAFC" text-anchor="middle">FastAPI</text>

        <rect x="110" y="0" width="102" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="161" y="20" fill="#F8FAFC" text-anchor="middle">Flask</text>

        <rect x="0" y="40" width="100" height="32" rx="8" fill="rgba(79, 140, 255, 0.15)" stroke="rgba(79, 140, 255, 0.3)"/>
        <text x="50" y="60" fill="#4F8CFF" font-weight="600" text-anchor="middle">Docker</text>

        <rect x="110" y="40" width="102" height="32" rx="8" fill="rgba(79, 140, 255, 0.15)" stroke="rgba(79, 140, 255, 0.3)"/>
        <text x="161" y="60" fill="#4F8CFF" font-weight="600" text-anchor="middle">Linux</text>

        <rect x="0" y="80" width="100" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="50" y="100" fill="#F8FAFC" text-anchor="middle">Redis</text>

        <rect x="110" y="80" width="102" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="161" y="100" fill="#F8FAFC" text-anchor="middle">Postgres</text>

        <rect x="0" y="120" width="100" height="32" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255,255,255,0.08)"/>
        <text x="50" y="140" fill="#F8FAFC" text-anchor="middle">MongoDB</text>

        <rect x="110" y="120" width="102" height="32" rx="8" fill="rgba(124, 92, 255, 0.15)" stroke="rgba(124, 92, 255, 0.3)"/>
        <text x="161" y="140" fill="#B28DFF" font-weight="600" text-anchor="middle">AWS</text>
      </g>
    </g>
  </g>
</svg>
'''

with open('assets/skills.svg', 'w') as f:
    f.write(skills_svg_content)
print("Generated assets/skills.svg")

# ----------------------------------------------------
# 4. stats.svg (900x320, rx=24)
# ----------------------------------------------------
stats_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 320" width="900" height="320">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;600&amp;display=swap');
      * { box-sizing: border-box; }
      text { font-family: 'Inter', sans-serif; }
      .mono { font-family: 'JetBrains Mono', monospace; }

      @keyframes ringRotate {
        0% { stroke-dashoffset: 280; }
        100% { stroke-dashoffset: 40; }
      }
    </style>

    <linearGradient id="rank-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#4F8CFF"/>
      <stop offset="50%" stop-color="#7C5CFF"/>
      <stop offset="100%" stop-color="#B28DFF"/>
    </linearGradient>
  </defs>

  <rect width="900" height="320" rx="24" fill="#04070E" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(35, 40)">
    <circle cx="8" cy="8" r="4" fill="#7C5CFF"/>
    <text x="22" y="12" fill="#7C5CFF" font-size="12" font-weight="700" class="mono" letter-spacing="2">GITHUB TELEMETRY // AI RESEARCHER PROFILE</text>
  </g>

  <!-- Left: S+ Rank Badge Circle -->
  <g transform="translate(80, 160)">
    <!-- Background Circle Ring -->
    <circle cx="0" cy="0" r="65" fill="none" stroke="rgba(255, 255, 255, 0.08)" stroke-width="10"/>
    <!-- Animated Glowing Ring -->
    <circle cx="0" cy="0" r="65" fill="none" stroke="url(#rank-grad)" stroke-width="10" stroke-dasharray="400" stroke-dashoffset="80" stroke-linecap="round"/>
    
    <text x="0" y="-5" fill="#F8FAFC" font-size="32" font-weight="900" text-anchor="middle">S+</text>
    <text x="0" y="18" fill="#B28DFF" font-size="10" font-weight="600" text-anchor="middle" class="mono">TOP 1% AI BUILDER</text>
  </g>

  <!-- Center-Right Metrics Grid -->
  <g transform="translate(200, 90)">
    <!-- Metric 1: Repos -->
    <g transform="translate(0, 0)">
      <rect width="145" height="90" rx="14" fill="rgba(10, 18, 36, 0.7)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
      <text x="18" y="32" fill="#94A3B8" font-size="10" font-weight="600" class="mono">REPOSITORIES</text>
      <text x="18" y="65" fill="#F8FAFC" font-size="28" font-weight="800">35+</text>
    </g>

    <!-- Metric 2: Commits -->
    <g transform="translate(160, 0)">
      <rect width="155" height="90" rx="14" fill="rgba(10, 18, 36, 0.7)" stroke="rgba(79, 140, 255, 0.25)" stroke-width="1"/>
      <text x="18" y="32" fill="#94A3B8" font-size="10" font-weight="600" class="mono">TOTAL COMMITS</text>
      <text x="18" y="65" fill="#4F8CFF" font-size="28" font-weight="800">2,450+</text>
    </g>

    <!-- Metric 3: Stars -->
    <g transform="translate(330, 0)">
      <rect width="145" height="90" rx="14" fill="rgba(10, 18, 36, 0.7)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
      <text x="18" y="32" fill="#94A3B8" font-size="10" font-weight="600" class="mono">TOTAL STARS</text>
      <text x="18" y="65" fill="#F8FAFC" font-size="28" font-weight="800">180+</text>
    </g>

    <!-- Metric 4: Followers -->
    <g transform="translate(490, 0)">
      <rect width="145" height="90" rx="14" fill="rgba(10, 18, 36, 0.7)" stroke="rgba(178, 141, 255, 0.25)" stroke-width="1"/>
      <text x="18" y="32" fill="#94A3B8" font-size="10" font-weight="600" class="mono">FOLLOWERS</text>
      <text x="18" y="65" fill="#B28DFF" font-size="28" font-weight="800">120+</text>
    </g>

    <!-- Language Distribution Bar -->
    <g transform="translate(0, 115)">
      <text x="0" y="0" fill="#94A3B8" font-size="10" font-weight="600" class="mono">MOST USED LANGUAGES</text>

      <!-- Multi-color bar -->
      <g transform="translate(0, 12)">
        <rect x="0" y="0" width="280" height="10" rx="5" fill="#4F8CFF"/>
        <rect x="284" y="0" width="130" height="10" rx="5" fill="#7C5CFF"/>
        <rect x="418" y="0" width="100" height="10" rx="5" fill="#B28DFF"/>
        <rect x="522" y="0" width="60" height="10" rx="5" fill="#38BDF8"/>
        <rect x="586" y="0" width="49" height="10" rx="5" fill="#94A3B8"/>
      </g>

      <!-- Language Labels -->
      <g transform="translate(0, 38)" font-size="11" class="mono">
        <circle cx="6" cy="-4" r="4" fill="#4F8CFF"/>
        <text x="16" y="0" fill="#F8FAFC">Python 45%</text>

        <circle cx="130" cy="-4" r="4" fill="#7C5CFF"/>
        <text x="140" y="0" fill="#F8FAFC">C++ 20%</text>

        <circle cx="230" cy="-4" r="4" fill="#B28DFF"/>
        <text x="240" y="0" fill="#F8FAFC">JS/TS 15%</text>

        <circle cx="340" cy="-4" r="4" fill="#38BDF8"/>
        <text x="350" y="0" fill="#F8FAFC">SQL 10%</text>

        <circle cx="430" cy="-4" r="4" fill="#94A3B8"/>
        <text x="440" y="0" fill="#F8FAFC">Shell 10%</text>
      </g>
    </g>
  </g>
</svg>
'''

with open('assets/stats.svg', 'w') as f:
    f.write(stats_svg_content)
print("Generated assets/stats.svg")

# ----------------------------------------------------
# 5. lanyard.svg (900x240, rx=20)
# ----------------------------------------------------
lanyard_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 240" width="900" height="240">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;600&amp;display=swap');
      * { box-sizing: border-box; }
      text { font-family: 'Inter', sans-serif; }
      .mono { font-family: 'JetBrains Mono', monospace; }

      @keyframes waveAnim {
        0% { stroke-dashoffset: 0; }
        100% { stroke-dashoffset: -200; }
      }

      @keyframes pulseDot {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.4); opacity: 1; }
      }
    </style>

    <linearGradient id="lanyard-bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="rgba(10, 18, 36, 0.8)"/>
      <stop offset="100%" stop-color="rgba(4, 7, 14, 0.9)"/>
    </linearGradient>
  </defs>

  <rect width="900" height="240" rx="20" fill="url(#lanyard-bg)" stroke="rgba(79, 140, 255, 0.25)" stroke-width="1.5"/>

  <!-- Header Status Bar -->
  <g transform="translate(30, 35)">
    <circle cx="10" cy="10" r="5" fill="#27C93F" style="animation: pulseDot 2s infinite;"/>
    <text x="26" y="14" fill="#27C93F" font-size="12" font-weight="700" class="mono" letter-spacing="1.5">SYSTEM STATUS // ONLINE &amp; ACTIVE</text>
  </g>

  <!-- Content Grid -->
  <g transform="translate(30, 75)">
    <!-- Box 1: Active Model -->
    <rect width="260" height="125" rx="14" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.08)"/>
    <g transform="translate(20, 30)">
      <text x="0" y="0" fill="#94A3B8" font-size="10" font-weight="600" class="mono">PRIMARY MODELS</text>
      <text x="0" y="26" fill="#F8FAFC" font-size="15" font-weight="700">Claude 3.5 Sonnet</text>
      <text x="0" y="48" fill="#4F8CFF" font-size="13" font-weight="600">GPT-4o &amp; Gemini 1.5</text>
      <text x="0" y="70" fill="#94A3B8" font-size="10" class="mono">Autonomous Multi-Agent</text>
    </g>

    <!-- Box 2: Infrastructure -->
    <g transform="translate(280, 0)">
      <rect width="260" height="125" rx="14" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.08)"/>
      <g transform="translate(20, 30)">
        <text x="0" y="0" fill="#94A3B8" font-size="10" font-weight="600" class="mono">COMPUTE ENGINE</text>
        <text x="0" y="26" fill="#F8FAFC" font-size="15" font-weight="700">PyTorch + vLLM</text>
        <text x="0" y="48" fill="#7C5CFF" font-size="13" font-weight="600">Groq LPU Acceleration</text>
        <text x="0" y="70" fill="#94A3B8" font-size="10" class="mono">Sub-10ms Inference</text>
      </g>
    </g>

    <!-- Box 3: Waveform Visualizer -->
    <g transform="translate(560, 0)">
      <rect width="280" height="125" rx="14" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(178, 141, 255, 0.2)"/>
      <g transform="translate(20, 30)">
        <text x="0" y="0" fill="#94A3B8" font-size="10" font-weight="600" class="mono">SIGNAL FREQUENCY</text>
        
        <!-- Animated Wave Sine Line -->
        <path d="M 0 45 Q 20 15, 40 45 T 80 45 T 120 45 T 160 45 T 200 45 T 240 45" fill="none" stroke="#B28DFF" stroke-width="2" stroke-dasharray="10 5" style="animation: waveAnim 4s linear infinite;"/>
        
        <text x="0" y="75" fill="#B28DFF" font-size="12" font-weight="700" class="mono">STABLE // 120 FPS MOTION</text>
      </g>
    </g>
  </g>
</svg>
'''

with open('assets/lanyard.svg', 'w') as f:
    f.write(lanyard_svg_content)
print("Generated assets/lanyard.svg")

# ----------------------------------------------------
# 6. timeline.svg (900x340, rx=24)
# ----------------------------------------------------
timeline_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="900" height="340">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@500;600&amp;display=swap');
      * { box-sizing: border-box; }
      text { font-family: 'Inter', sans-serif; }
      .mono { font-family: 'JetBrains Mono', monospace; }

      @keyframes lineFlow {
        0% { stroke-dashoffset: 1000; }
        100% { stroke-dashoffset: 0; }
      }

      @keyframes nodeGlow {
        0%, 100% { r: 6px; opacity: 0.8; }
        50% { r: 9px; opacity: 1; }
      }
    </style>

    <linearGradient id="timeline-line-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#4F8CFF"/>
      <stop offset="33%" stop-color="#7C5CFF"/>
      <stop offset="66%" stop-color="#B28DFF"/>
      <stop offset="100%" stop-color="#27C93F"/>
    </linearGradient>
  </defs>

  <rect width="900" height="340" rx="24" fill="#04070E" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(35, 40)">
    <circle cx="8" cy="8" r="4" fill="#B28DFF"/>
    <text x="22" y="12" fill="#B28DFF" font-size="12" font-weight="700" class="mono" letter-spacing="2">EVOLUTION TRAJECTORY // CAREER TIMELINE</text>
  </g>

  <!-- Horizontal Connected Line -->
  <g transform="translate(70, 160)">
    <line x1="0" y1="0" x2="760" y2="0" stroke="url(#timeline-line-grad)" stroke-width="4" stroke-linecap="round"/>

    <!-- Step 1: 2024 -->
    <g transform="translate(0, 0)">
      <circle cx="0" cy="0" r="14" fill="#04070E" stroke="#4F8CFF" stroke-width="3"/>
      <circle cx="0" cy="0" r="6" fill="#4F8CFF" style="animation: nodeGlow 3s infinite;"/>
      
      <!-- Top Card -->
      <g transform="translate(-65, -95)">
        <rect width="130" height="70" rx="10" fill="rgba(10, 18, 36, 0.8)" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1"/>
        <text x="65" y="24" fill="#4F8CFF" font-size="14" font-weight="800" text-anchor="middle" class="mono">2024</text>
        <text x="65" y="44" fill="#F8FAFC" font-size="11" font-weight="600" text-anchor="middle">Machine Learning</text>
        <text x="65" y="58" fill="#94A3B8" font-size="9" text-anchor="middle" class="mono">Foundations &amp; Stats</text>
      </g>
    </g>

    <!-- Step 2: 2025 -->
    <g transform="translate(190, 0)">
      <circle cx="0" cy="0" r="14" fill="#04070E" stroke="#7C5CFF" stroke-width="3"/>
      <circle cx="0" cy="0" r="6" fill="#7C5CFF" style="animation: nodeGlow 3s infinite 0.6s;"/>

      <!-- Bottom Card -->
      <g transform="translate(-65, 30)">
        <rect width="130" height="70" rx="10" fill="rgba(10, 18, 36, 0.8)" stroke="rgba(124, 92, 255, 0.3)" stroke-width="1"/>
        <text x="65" y="24" fill="#7C5CFF" font-size="14" font-weight="800" text-anchor="middle" class="mono">2025</text>
        <text x="65" y="44" fill="#F8FAFC" font-size="11" font-weight="600" text-anchor="middle">Deep Learning</text>
        <text x="65" y="58" fill="#94A3B8" font-size="9" text-anchor="middle" class="mono">PyTorch &amp; Neural Nets</text>
      </g>
    </g>

    <!-- Step 3: 2026 -->
    <g transform="translate(380, 0)">
      <circle cx="0" cy="0" r="14" fill="#04070E" stroke="#B28DFF" stroke-width="3"/>
      <circle cx="0" cy="0" r="6" fill="#B28DFF" style="animation: nodeGlow 3s infinite 1.2s;"/>

      <!-- Top Card -->
      <g transform="translate(-65, -95)">
        <rect width="130" height="70" rx="10" fill="rgba(10, 18, 36, 0.8)" stroke="rgba(178, 141, 255, 0.4)" stroke-width="1"/>
        <text x="65" y="24" fill="#B28DFF" font-size="14" font-weight="800" text-anchor="middle" class="mono">2026</text>
        <text x="65" y="44" fill="#F8FAFC" font-size="11" font-weight="600" text-anchor="middle">Generative AI</text>
        <text x="65" y="58" fill="#94A3B8" font-size="9" text-anchor="middle" class="mono">LLMs, RAG &amp; Fine-Tune</text>
      </g>
    </g>

    <!-- Step 4: 2027 -->
    <g transform="translate(570, 0)">
      <circle cx="0" cy="0" r="14" fill="#04070E" stroke="#4F8CFF" stroke-width="3"/>
      <circle cx="0" cy="0" r="6" fill="#4F8CFF" style="animation: nodeGlow 3s infinite 1.8s;"/>

      <!-- Bottom Card -->
      <g transform="translate(-65, 30)">
        <rect width="130" height="70" rx="10" fill="rgba(10, 18, 36, 0.8)" stroke="rgba(79, 140, 255, 0.4)" stroke-width="1"/>
        <text x="65" y="24" fill="#4F8CFF" font-size="14" font-weight="800" text-anchor="middle" class="mono">2027</text>
        <text x="65" y="44" fill="#F8FAFC" font-size="11" font-weight="600" text-anchor="middle">Agentic AI</text>
        <text x="65" y="58" fill="#94A3B8" font-size="9" text-anchor="middle" class="mono">Multi-Agent Networks</text>
      </g>
    </g>

    <!-- Step 5: Future -->
    <g transform="translate(760, 0)">
      <circle cx="0" cy="0" r="14" fill="#04070E" stroke="#27C93F" stroke-width="3"/>
      <circle cx="0" cy="0" r="6" fill="#27C93F" style="animation: nodeGlow 3s infinite 2.4s;"/>

      <!-- Top Card -->
      <g transform="translate(-65, -95)">
        <rect width="130" height="70" rx="10" fill="rgba(10, 18, 36, 0.8)" stroke="rgba(39, 201, 63, 0.4)" stroke-width="1"/>
        <text x="65" y="24" fill="#27C93F" font-size="14" font-weight="800" text-anchor="middle" class="mono">FUTURE</text>
        <text x="65" y="44" fill="#F8FAFC" font-size="11" font-weight="600" text-anchor="middle">AI Engineer</text>
        <text x="65" y="58" fill="#94A3B8" font-size="9" text-anchor="middle" class="mono">Frontier Intelligence</text>
      </g>
    </g>
  </g>
</svg>
'''

with open('assets/timeline.svg', 'w') as f:
    f.write(timeline_svg_content)
print("Generated assets/timeline.svg")

# ----------------------------------------------------
# 7. footer.svg (900x180, rx=20)
# ----------------------------------------------------
footer_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 180" width="900" height="180">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      text { font-family: 'JetBrains Mono', monospace; }

      @keyframes blinkCursor {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
      }
    </style>
  </defs>

  <rect width="900" height="180" rx="20" fill="#04070E" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1.5"/>

  <!-- Terminal Window Controls -->
  <circle cx="35" cy="25" r="5" fill="#FF5F56" opacity="0.85"/>
  <circle cx="52" cy="25" r="5" fill="#FFBD2E" opacity="0.85"/>
  <circle cx="69" cy="25" r="5" fill="#27C93F" opacity="0.85"/>

  <text x="450" y="28" fill="#94A3B8" font-size="11" font-weight="500" text-anchor="middle" letter-spacing="1">infinite-learning-loop.js</text>

  <line x1="0" y1="45" x2="900" y2="45" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>

  <!-- Code Content -->
  <g transform="translate(40, 72)" font-size="14" font-weight="600">
    <text x="0" y="0">
      <tspan fill="#7C5CFF">while</tspan><tspan fill="#F8FAFC"> (</tspan><tspan fill="#4F8CFF">alive</tspan><tspan fill="#F8FAFC">) {</tspan>
    </text>
    <text x="30" y="24">
      <tspan fill="#B28DFF">learn</tspan><tspan fill="#F8FAFC">();</tspan>
    </text>
    <text x="30" y="44">
      <tspan fill="#4F8CFF">build</tspan><tspan fill="#F8FAFC">();</tspan>
    </text>
    <text x="30" y="64">
      <tspan fill="#27C93F">share</tspan><tspan fill="#F8FAFC">();</tspan>
    </text>
    <text x="30" y="84">
      <tspan fill="#7C5CFF">repeat</tspan><tspan fill="#F8FAFC">();</tspan>
    </text>
    <text x="0" y="104">
      <tspan fill="#F8FAFC">}</tspan>
    </text>
    
    <!-- Blinking Cursor -->
    <rect x="20" y="93" width="9" height="16" fill="#4F8CFF" style="animation: blinkCursor 1s step-end infinite;"/>
  </g>
</svg>
'''

with open('assets/footer.svg', 'w') as f:
    f.write(footer_svg_content)
print("Generated assets/footer.svg")

# ----------------------------------------------------
# 8. particles.svg (900x100)
# ----------------------------------------------------
particles_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 100" width="900" height="100">
  <defs>
    <style>
      @keyframes pMove {
        0%, 100% { transform: translateY(0px); opacity: 0.3; }
        50% { transform: translateY(-20px); opacity: 0.8; }
      }
    </style>
  </defs>
  <rect width="900" height="100" fill="transparent"/>
  <circle cx="100" cy="50" r="2" fill="#4F8CFF" style="animation: pMove 4s ease-in-out infinite;"/>
  <circle cx="250" cy="70" r="1.5" fill="#7C5CFF" style="animation: pMove 6s ease-in-out infinite 1s;"/>
  <circle cx="450" cy="30" r="2" fill="#B28DFF" style="animation: pMove 5s ease-in-out infinite 0.5s;"/>
  <circle cx="650" cy="60" r="1.8" fill="#4F8CFF" style="animation: pMove 7s ease-in-out infinite 2s;"/>
  <circle cx="800" cy="40" r="1.2" fill="#F8FAFC" style="animation: pMove 4.5s ease-in-out infinite 1.5s;"/>
</svg>
'''

with open('assets/particles.svg', 'w') as f:
    f.write(particles_svg_content)
print("Generated assets/particles.svg")

# ----------------------------------------------------
# 9. loading.svg (400x100)
# ----------------------------------------------------
loading_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 100" width="400" height="100">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600&amp;display=swap');
      text { font-family: 'JetBrains Mono', monospace; }
      @keyframes loadBar {
        0% { width: 0%; }
        100% { width: 100%; }
      }
    </style>
  </defs>
  <rect width="400" height="100" rx="16" fill="#04070E" stroke="rgba(255,255,255,0.1)"/>
  <text x="200" y="38" fill="#4F8CFF" font-size="12" text-anchor="middle" letter-spacing="2">INITIALIZING AI SYSTEM...</text>
  <rect x="50" y="55" width="300" height="8" rx="4" fill="rgba(255,255,255,0.08)"/>
  <rect x="50" y="55" width="300" height="8" rx="4" fill="url(#load-grad)">
    <animate attributeName="width" from="0" to="300" dur="2.5s" repeatCount="indefinite"/>
  </rect>
  <linearGradient id="load-grad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#4F8CFF"/>
    <stop offset="50%" stop-color="#7C5CFF"/>
    <stop offset="100%" stop-color="#B28DFF"/>
  </linearGradient>
</svg>
'''

with open('assets/loading.svg', 'w') as f:
    f.write(loading_svg_content)
print("Generated assets/loading.svg")

# ----------------------------------------------------
# 10. .github/workflows/snake.yml
# ----------------------------------------------------
snake_yml_content = '''name: Generate Contribution Snake

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
  push:
    branches:
      - main
      - master

jobs:
  generate:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Generate Snake SVG
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            assets/github-contribution-grid-snake.svg?color_snake=#4F8CFF&color_dots=#0A1224,#1E293B,#334155,#475569,#7C5CFF
            assets/github-contribution-grid-snake-dark.svg?color_snake=#B28DFF&color_dots=#04070E,#0A1224,#1E293B,#4F8CFF,#7C5CFF

      - name: Commit and Push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add assets/
          git diff --quiet && git diff --staged --quiet || (git commit -m "chore: update contribution snake animation" && git push)
'''

with open('.github/workflows/snake.yml', 'w') as f:
    f.write(snake_yml_content)
print("Generated .github/workflows/snake.yml")

# ----------------------------------------------------
# 11. .github/workflows/stats.yml
# ----------------------------------------------------
stats_yml_content = '''name: Profile Sync & Telemetry

on:
  schedule:
    - cron: "0 12 * * *"
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Log Sync
        run: echo "Profile telemetry verified active."
'''

with open('.github/workflows/stats.yml', 'w') as f:
    f.write(stats_yml_content)
print("Generated .github/workflows/stats.yml")

# ----------------------------------------------------
# 12. README.md
# ----------------------------------------------------
readme_md_content = '''<div align="center">

<!-- Hero Banner with Dark/Light Mode Theme Switching -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg?v=1">
  <img alt="Vishal Rathod - AI Engineer Profile Banner" src="assets/banner-dark.svg?v=1" width="100%">
</picture>

<br/><br/>

<!-- Telemetry Dashboard -->
<img src="assets/lanyard.svg?v=1" alt="Live AI Telemetry Dashboard" width="100%">

</div>

<br/>

## ❖ ABOUT THE LAB

```yaml
Architect: Vishal Rathod
Specialization: Artificial Intelligence & Autonomous Agentic Systems
Location: India 🇮🇳
Current Focus: Frontier LLM Fine-Tuning, Multi-Agent Orchestration & vLLM Inference
Mission: "Building high-impact, production-grade AI systems that transform complex problems into elegant autonomous solutions."
```

---

## ⚡ TECHNICAL MATRIX & CAPABILITIES

<div align="center">
  <img src="assets/skills.svg?v=1" alt="Skill Matrix" width="100%">
</div>

---

## 🚀 FEATURED AI RESEARCH & PROJECTS

<br/>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🌐 InterviewAI</h3>
      <p align="center"><b>Multi-Agent AI Interview Platform</b></p>
      <p>An autonomous multi-agent platform designed to conduct dynamic technical interviews, analyze voice &amp; text responses in real-time, and generate objective candidate evaluation reports using LLMs.</p>
      <p align="center">
        <code>Python</code> • <code>LangChain</code> • <code>LangGraph</code> • <code>FastAPI</code> • <code>OpenAI</code>
      </p>
      <p align="center">
        <a href="https://github.com/VishalRathod21/InterviewAI"><img src="https://img.shields.io/badge/GitHub-Repository-4F8CFF?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
        <a href="#"><img src="https://img.shields.io/badge/Live-Demo-7C5CFF?style=for-the-badge&logo=vercel&logoColor=white" alt="Demo"></a>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🎙️ AI Voice Assistant</h3>
      <p align="center"><b>Ultra-Low Latency Conversational AI</b></p>
      <p>Real-time speech-to-speech assistant powered by Groq LPU inference, Whisper STT, and ElevenLabs TTS. Features context retention, tool calling, and streaming audio WebSocket pipeline.</p>
      <p align="center">
        <code>Python</code> • <code>Groq</code> • <code>Whisper</code> • <code>FastAPI</code> • <code>WebSockets</code>
      </p>
      <p align="center">
        <a href="https://github.com/VishalRathod21"><img src="https://img.shields.io/badge/GitHub-Repository-4F8CFF?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
        <a href="#"><img src="https://img.shields.io/badge/Live-Demo-7C5CFF?style=for-the-badge&logo=streamlit&logoColor=white" alt="Demo"></a>
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🧠 Enterprise RAG Chatbot</h3>
      <p align="center"><b>Hybrid Neural Search & Retrieval</b></p>
      <p>Production RAG engine leveraging dense (FAISS/Qdrant) and sparse vector retrieval with re-ranking. Supports multi-format document ingestion, semantic chunking, and hallucination guardrails.</p>
      <p align="center">
        <code>PyTorch</code> • <code>Qdrant</code> • <code>LangChain</code> • <code>LlamaIndex</code> • <code>Docker</code>
      </p>
      <p align="center">
        <a href="https://github.com/VishalRathod21"><img src="https://img.shields.io/badge/GitHub-Repository-4F8CFF?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
        <a href="#"><img src="https://img.shields.io/badge/Live-Demo-7C5CFF?style=for-the-badge&logo=huggingface&logoColor=white" alt="Demo"></a>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🎬 Movie Recommendation System</h3>
      <p align="center"><b>Collaborative & Neural Filtering Engine</b></p>
      <p>Deep learning recommendation system utilizing matrix factorization and content embeddings to deliver hyper-personalized movie suggestions with sub-5ms lookup speeds.</p>
      <p align="center">
        <code>Python</code> • <code>Scikit-Learn</code> • <code>TensorFlow</code> • <code>Flask</code> • <code>Redis</code>
      </p>
      <p align="center">
        <a href="https://github.com/VishalRathod21"><img src="https://img.shields.io/badge/GitHub-Repository-4F8CFF?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
        <a href="#"><img src="https://img.shields.io/badge/Live-Demo-7C5CFF?style=for-the-badge&logo=streamlit&logoColor=white" alt="Demo"></a>
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">📈 House Price Prediction</h3>
      <p align="center"><b>Advanced Gradient Boosting Regressor</b></p>
      <p>End-to-end ML pipeline engineered with XGBoost, LightGBM, and automated feature selection for precise real-estate valuation with feature importance interpretability.</p>
      <p align="center">
        <code>Python</code> • <code>XGBoost</code> • <code>Scikit-Learn</code> • <code>Pandas</code> • <code>FastAPI</code>
      </p>
      <p align="center">
        <a href="https://github.com/VishalRathod21"><img src="https://img.shields.io/badge/GitHub-Repository-4F8CFF?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
        <a href="#"><img src="https://img.shields.io/badge/Live-Demo-7C5CFF?style=for-the-badge&logo=render&logoColor=white" alt="Demo"></a>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🛡️ Auto Insurance Prediction</h3>
      <p align="center"><b>Risk Assessment & Claim Modeling</b></p>
      <p>Predictive analytics platform for insurance risk assessment, fraud probability scoring, and automated claim cost estimation using ensemble ML algorithms.</p>
      <p align="center">
        <code>Python</code> • <code>CatBoost</code> • <code>Scikit-Learn</code> • <code>Docker</code> • <code>AWS</code>
      </p>
      <p align="center">
        <a href="https://github.com/VishalRathod21"><img src="https://img.shields.io/badge/GitHub-Repository-4F8CFF?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
        <a href="#"><img src="https://img.shields.io/badge/Live-Demo-7C5CFF?style=for-the-badge&logo=aws&logoColor=white" alt="Demo"></a>
      </p>
    </td>
  </tr>
</table>

---

## 📈 CAREER & AI EVOLUTION TIMELINE

<div align="center">
  <img src="assets/timeline.svg?v=1" alt="AI Career Evolution Timeline" width="100%">
</div>

---

## 📊 GITHUB TELEMETRY & STATS

<div align="center">
  <img src="assets/stats.svg?v=1" alt="GitHub Stats & Telemetry" width="100%">
</div>

---

## 🐍 CONTRIBUTION ACTIVITY

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/github-contribution-grid-snake-dark.svg?v=1">
    <source media="(prefers-color-scheme: light)" srcset="assets/github-contribution-grid-snake.svg?v=1">
    <img alt="Vishal's Contribution Snake" src="assets/github-contribution-grid-snake-dark.svg?v=1" width="100%">
  </picture>
</div>

---

## 📬 CONNECT & COLLABORATE

<div align="center">

  <a href="mailto:vishalrathod.ai@gmail.com">
    <img src="https://img.shields.io/badge/Email-vishalrathod.ai--gmail-4F8CFF?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  &nbsp;
  <a href="https://linkedin.com/in/vishalrathod">
    <img src="https://img.shields.io/badge/LinkedIn-Vishal_Rathod-7C5CFF?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  &nbsp;
  <a href="https://github.com/VishalRathod21">
    <img src="https://img.shields.io/badge/GitHub-VishalRathod21-B28DFF?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>

</div>

<br/>

<!-- Footer Terminal Window -->
<div align="center">
  <img src="assets/footer.svg?v=1" alt="Footer Code Loop" width="100%">
</div>
'''

with open('README.md', 'w') as f:
    f.write(readme_md_content)
print("Generated README.md")

print("All profile files build script completed successfully!")
