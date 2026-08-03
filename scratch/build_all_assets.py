import base64
import os

# Read profile.png and convert to base64
profile_img_path = "assets/profile.png"
if os.path.exists(profile_img_path):
    with open(profile_img_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
        img_data_uri = f"data:image/png;base64,{img_b64}"
else:
    img_data_uri = ""

print(f"Base64 image size: {len(img_data_uri)} chars")

# ==========================================
# 1. BANNER DARK SVG
# ==========================================
banner_dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1400 700" width="100%" height="100%">
  <defs>
    <!-- Dark AI Lab Gradients -->
    <radialGradient id="bgGrad" cx="50%" cy="30%" r="80%" fx="50%" fy="30%">
      <stop offset="0%" stop-color="#0E1A35"/>
      <stop offset="50%" stop-color="#0A1224"/>
      <stop offset="100%" stop-color="#04070E"/>
    </radialGradient>

    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F8CFF"/>
      <stop offset="50%" stop-color="#7C5CFF"/>
      <stop offset="100%" stop-color="#B28DFF"/>
    </linearGradient>

    <linearGradient id="textShimmer" x1="0%" y1="0%" x2="200%" y2="0%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="25%" stop-color="#4F8CFF"/>
      <stop offset="50%" stop-color="#B28DFF"/>
      <stop offset="75%" stop-color="#7C5CFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
      <animate attributeName="x1" values="0%; -100%" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="200%; 100%" dur="6s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="glassBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.25)"/>
      <stop offset="50%" stop-color="rgba(79,140,255,0.15)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0.05)"/>
    </linearGradient>

    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(79, 140, 255, 0)"/>
      <stop offset="50%" stop-color="rgba(79, 140, 255, 0.8)"/>
      <stop offset="75%" stop-color="rgba(178, 141, 255, 0.9)"/>
      <stop offset="100%" stop-color="rgba(79, 140, 255, 0)"/>
    </linearGradient>

    <radialGradient id="lightBeam" cx="80%" cy="20%" r="50%">
      <stop offset="0%" stop-color="rgba(124, 92, 255, 0.25)"/>
      <stop offset="60%" stop-color="rgba(79, 140, 255, 0.08)"/>
      <stop offset="100%" stop-color="rgba(4, 7, 14, 0)"/>
    </radialGradient>

    <!-- Glow Filters -->
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="laserGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <!-- Clip Paths -->
    <clipPath id="avatarClip">
      <rect x="910" y="80" width="420" height="540" rx="24"/>
    </clipPath>
    <clipPath id="bannerClip">
      <rect x="0" y="0" width="1400" height="700" rx="40"/>
    </clipPath>
  </defs>

  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    
    @keyframes pulseParticle {{
      0%, 100% {{ opacity: 0.2; transform: translateY(0px) scale(1); }}
      50% {{ opacity: 0.8; transform: translateY(-15px) scale(1.3); }}
    }}
    @keyframes typeLine1 {{ 0% {{ opacity: 0; }} 10% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
    @keyframes typeLine2 {{ 0%, 15% {{ opacity: 0; }} 25% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
    @keyframes typeLine3 {{ 0%, 30% {{ opacity: 0; }} 40% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
    @keyframes typeLine4 {{ 0%, 45% {{ opacity: 0; }} 55% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
    @keyframes typeLine5 {{ 0%, 60% {{ opacity: 0; }} 70% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
    @keyframes typeLine6 {{ 0%, 75% {{ opacity: 0; }} 85% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}

    @keyframes cursorBlink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    @keyframes scanMotion {{
      0% {{ transform: translateY(-40px); }}
      50% {{ transform: translateY(520px); }}
      100% {{ transform: translateY(-40px); }}
    }}
    @keyframes floatHud {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-8px); }}
    }}
    .p1 {{ animation: pulseParticle 4s infinite ease-in-out; }}
    .p2 {{ animation: pulseParticle 6s infinite ease-in-out 1s; }}
    .p3 {{ animation: pulseParticle 5s infinite ease-in-out 2s; }}
  </style>

  <g clip-path="url(#bannerClip)">
    <!-- Canvas Base -->
    <rect width="1400" height="700" fill="url(#bgGrad)"/>
    <rect width="1400" height="700" fill="url(#lightBeam)"/>

    <!-- Grid Lines (Subtle AI Network) -->
    <g opacity="0.07" stroke="#4F8CFF" stroke-width="1">
      <path d="M0 100 H1400 M0 200 H1400 M0 300 H1400 M0 400 H1400 M0 500 H1400 M0 600 H1400"/>
      <path d="M100 0 V700 M200 0 V700 M300 0 V700 M400 0 V700 M500 0 V700 M600 0 V700 M700 0 V700 M800 0 V700 M900 0 V700 M1000 0 V700 M1100 0 V700 M1200 0 V700 M1300 0 V700"/>
    </g>

    <!-- Floating Particles -->
    <circle cx="150" cy="120" r="2" fill="#4F8CFF" class="p1"/>
    <circle cx="380" cy="450" r="1.5" fill="#B28DFF" class="p2"/>
    <circle cx="720" cy="180" r="2" fill="#7C5CFF" class="p3"/>
    <circle cx="840" cy="520" r="1.5" fill="#4F8CFF" class="p1"/>
    <circle cx="520" cy="610" r="2.5" fill="#B28DFF" class="p2"/>
    <circle cx="1250" cy="140" r="2" fill="#4F8CFF" class="p3"/>

    <!-- Ambient Glow Orbs -->
    <circle cx="1100" cy="350" r="260" fill="#7C5CFF" opacity="0.12" filter="url(#softGlow)"/>
    <circle cx="250" cy="250" r="200" fill="#4F8CFF" opacity="0.08" filter="url(#softGlow)"/>

    <!-- Banner Outer Border Glass -->
    <rect x="2" y="2" width="1396" height="696" rx="38" fill="none" stroke="url(#glassBorder)" stroke-width="2"/>

    <!-- ================= LEFT SIDE: TERMINAL ================= -->
    <g transform="translate(60, 70)">
      <!-- Terminal Glass Container -->
      <rect width="440" height="560" rx="20" fill="rgba(10, 18, 36, 0.75)" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
      <rect width="440" height="40" rx="20" fill="rgba(255,255,255,0.03)"/>
      <!-- Window Controls -->
      <circle cx="25" cy="20" r="5.5" fill="#FF5F56" opacity="0.8"/>
      <circle cx="43" cy="20" r="5.5" fill="#FFBD2E" opacity="0.8"/>
      <circle cx="61" cy="20" r="5.5" fill="#27C93F" opacity="0.8"/>
      <text x="220" y="24" fill="#94A3B8" font-size="12" class="mono" text-anchor="middle" opacity="0.7">ai_core_kernel.sh</text>

      <!-- Terminal Logs -->
      <g transform="translate(25, 70)" class="mono" font-size="13">
        <!-- Sequence Lines -->
        <g style="animation: typeLine1 1s forwards;">
          <text fill="#4F8CFF" y="0">&gt; <tspan fill="#F8FAFC">Initializing AI Core...</tspan></text>
        </g>
        <g style="animation: typeLine2 1s forwards;">
          <text fill="#4F8CFF" y="30">&gt; <tspan fill="#94A3B8">Loading Neural Network...</tspan></text>
        </g>
        <g style="animation: typeLine3 1s forwards;">
          <text fill="#4F8CFF" y="60">&gt; <tspan fill="#94A3B8">Loading Memory Modules...</tspan></text>
        </g>
        <g style="animation: typeLine4 1s forwards;">
          <text fill="#4F8CFF" y="90">&gt; <tspan fill="#94A3B8">Loading Autonomous Agents...</tspan></text>
        </g>
        <g style="animation: typeLine5 1s forwards;">
          <text fill="#4F8CFF" y="120">&gt; <tspan fill="#B28DFF">Loading LLM Models...</tspan></text>
        </g>
        <g style="animation: typeLine6 1s forwards;">
          <text fill="#27C93F" y="150">[OK] AI Engine Status: Ready.</text>
        </g>

        <!-- Divider Line -->
        <line x1="0" y1="180" x2="390" y2="180" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>

        <!-- Whoami Section -->
        <g transform="translate(0, 215)">
          <text fill="#7C5CFF" font-weight="bold">$ whoami</text>
          
          <rect x="0" y="15" width="390" height="110" rx="12" fill="rgba(79, 140, 255, 0.05)" stroke="rgba(79, 140, 255, 0.2)" stroke-width="1"/>
          
          <text x="15" y="42" fill="#F8FAFC" font-size="16" class="sans" font-weight="bold">Vishal Rathod</text>
          <text x="15" y="66" fill="#4F8CFF" font-size="13" class="sans">AI Engineer &amp; ML Specialist</text>
          <text x="15" y="88" fill="#94A3B8" font-size="12" class="mono">GenAI • Agentic AI • LLMs • MLOps</text>
          <text x="15" y="108" fill="#B28DFF" font-size="11" class="mono">📍 India</text>
        </g>

        <!-- Mission Section -->
        <g transform="translate(0, 370)">
          <text fill="#94A3B8" font-size="11" class="mono">// CURRENT MISSION</text>
          <rect x="0" y="12" width="390" height="55" rx="10" fill="rgba(124, 92, 255, 0.08)" stroke="rgba(124, 92, 255, 0.25)"/>
          <text x="12" y="34" fill="#F8FAFC" font-size="12" class="sans">"Building intelligent AI products that</text>
          <text x="12" y="52" fill="#4F8CFF" font-size="12" class="sans">positively impact millions of people."</text>
        </g>

        <!-- Blinking Prompt -->
        <g transform="translate(0, 465)">
          <text fill="#4F8CFF" font-weight="bold">$ <tspan fill="#F8FAFC">exec agent.run()</tspan></text>
          <rect x="165" y="-12" width="8" height="15" fill="#4F8CFF" style="animation: cursorBlink 1s infinite;"/>
        </g>
      </g>
    </g>

    <!-- ================= CENTER SIDE: NAME & BRANDING ================= -->
    <g transform="translate(540, 310)">
      <!-- Background Soft Glow -->
      <ellipse cx="170" cy="30" rx="180" ry="70" fill="#4F8CFF" opacity="0.15" filter="url(#softGlow)"/>
      
      <!-- Sub-tag badge -->
      <g transform="translate(0, -100)">
        <rect width="210" height="30" rx="15" fill="rgba(79, 140, 255, 0.1)" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1"/>
        <circle cx="18" cy="15" r="4" fill="#27C93F"/>
        <text x="32" y="20" fill="#4F8CFF" font-size="11" class="mono" font-weight="bold" letter-spacing="1">AI RESEARCH LAB</text>
      </g>

      <!-- Main Name -->
      <text x="0" y="-30" fill="url(#textShimmer)" font-size="52" class="sans" font-weight="900" letter-spacing="4" filter="url(#softGlow)">VISHAL RATHOD</text>
      <text x="0" y="-30" fill="url(#textShimmer)" font-size="52" class="sans" font-weight="900" letter-spacing="4">VISHAL RATHOD</text>

      <!-- Title Subtitle -->
      <text x="4" y="15" fill="#94A3B8" font-size="18" class="sans" font-weight="500" letter-spacing="6">AI ENGINEER &amp; ARCHITECT</text>

      <!-- Minimal Divider Line -->
      <line x1="4" y1="35" x2="330" y2="35" stroke="url(#primaryGrad)" stroke-width="2" stroke-linecap="round"/>

      <!-- Tags Pill Row -->
      <g transform="translate(4, 55)">
        <!-- Tag 1 -->
        <rect width="105" height="26" rx="13" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)"/>
        <text x="52.5" y="17" fill="#F8FAFC" font-size="11" class="mono" text-anchor="middle">Deep Learning</text>
        
        <!-- Tag 2 -->
        <rect x="115" width="95" height="26" rx="13" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)"/>
        <text x="162.5" y="17" fill="#F8FAFC" font-size="11" class="mono" text-anchor="middle">Agentic AI</text>

        <!-- Tag 3 -->
        <rect x="220" width="85" height="26" rx="13" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)"/>
        <text x="262.5" y="17" fill="#F8FAFC" font-size="11" class="mono" text-anchor="middle">LLMs/RAG</text>
      </g>
    </g>

    <!-- ================= RIGHT SIDE: HOLOGRAM CHARACTER ================= -->
    <g transform="translate(920, 70)">
      <!-- Avatar Frame Backing & Glow -->
      <rect width="410" height="560" rx="24" fill="rgba(10, 18, 36, 0.6)" stroke="url(#glassBorder)" stroke-width="1.5"/>
      <ellipse cx="205" cy="280" rx="160" ry="200" fill="#7C5CFF" opacity="0.15" filter="url(#softGlow)"/>

      <!-- Embedded Image with Hologram Clipping -->
      <g clip-path="url(#avatarClip)">
        <image href="{img_data_uri}" x="910" y="80" width="420" height="540" preserveAspectRatio="xMidYMid slice" opacity="0.92"/>
        
        <!-- Subtle Hologram Mesh Lines -->
        <rect x="910" y="80" width="420" height="540" fill="none" stroke="rgba(79, 140, 255, 0.15)" stroke-width="1"/>
        <path d="M910 180 H1330 M910 280 H1330 M910 380 H1330 M910 480 H1330" stroke="rgba(79,140,255,0.08)" stroke-dasharray="4 4"/>
      </g>

      <!-- Laser Scanner Line (Moving Top to Bottom) -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="410" height="8" fill="url(#scanlineGrad)" filter="url(#laserGlow)" style="animation: scanMotion 4s infinite ease-in-out;"/>
        <line x1="0" y1="4" x2="410" y2="4" stroke="#4F8CFF" stroke-width="2" style="animation: scanMotion 4s infinite ease-in-out;"/>
      </g>

      <!-- Floating Holographic HUD Overlay Elements -->
      <g transform="translate(20, 20)" style="animation: floatHud 4s infinite ease-in-out;" class="mono">
        <rect width="130" height="40" rx="8" fill="rgba(4, 7, 14, 0.7)" stroke="rgba(79, 140, 255, 0.4)" stroke-width="1"/>
        <text x="12" y="17" fill="#4F8CFF" font-size="9" font-weight="bold">SYSTEM STATUS</text>
        <text x="12" y="30" fill="#27C93F" font-size="10">● NEURAL CORE ONLINE</text>
      </g>

      <g transform="translate(250, 480)" style="animation: floatHud 5s infinite ease-in-out 1s;" class="mono">
        <rect width="140" height="45" rx="8" fill="rgba(4, 7, 14, 0.7)" stroke="rgba(178, 141, 255, 0.4)" stroke-width="1"/>
        <text x="12" y="18" fill="#B28DFF" font-size="9" font-weight="bold">HOLOGRAM MATRIX</text>
        <text x="12" y="32" fill="#F8FAFC" font-size="10">v4.8 • SCANNING</text>
      </g>

      <!-- Decorative HUD Target Corners -->
      <path d="M 10 30 L 10 10 L 30 10" fill="none" stroke="#4F8CFF" stroke-width="2"/>
      <path d="M 400 30 L 400 10 L 380 10" fill="none" stroke="#4F8CFF" stroke-width="2"/>
      <path d="M 10 530 L 10 550 L 30 550" fill="none" stroke="#4F8CFF" stroke-width="2"/>
      <path d="M 400 530 L 400 550 L 380 550" fill="none" stroke="#4F8CFF" stroke-width="2"/>
    </g>
  </g>
</svg>'''

# Save banner-dark.svg
with open("assets/banner-dark.svg", "w") as f:
    f.write(banner_dark_svg)

print("Created assets/banner-dark.svg")

# ==========================================
# 2. BANNER LIGHT SVG
# ==========================================
banner_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1400 700" width="100%" height="100%">
  <defs>
    <!-- Light AI Lab Gradients -->
    <radialGradient id="bgGradLight" cx="50%" cy="30%" r="80%" fx="50%" fy="30%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F1F5F9"/>
      <stop offset="100%" stop-color="#E2E8F0"/>
    </radialGradient>

    <linearGradient id="primaryGradLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="50%" stop-color="#6D28D9"/>
      <stop offset="100%" stop-color="#9333EA"/>
    </linearGradient>

    <linearGradient id="textShimmerLight" x1="0%" y1="0%" x2="200%" y2="0%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="25%" stop-color="#2563EB"/>
      <stop offset="50%" stop-color="#7C3AED"/>
      <stop offset="75%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#0F172A"/>
      <animate attributeName="x1" values="0%; -100%" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="200%; 100%" dur="6s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="glassBorderLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(15, 23, 42, 0.15)"/>
      <stop offset="50%" stop-color="rgba(37, 99, 235, 0.2)"/>
      <stop offset="100%" stop-color="rgba(15, 23, 42, 0.05)"/>
    </linearGradient>

    <linearGradient id="scanlineGradLight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(37, 99, 235, 0)"/>
      <stop offset="50%" stop-color="rgba(37, 99, 235, 0.8)"/>
      <stop offset="75%" stop-color="rgba(124, 58, 237, 0.9)"/>
      <stop offset="100%" stop-color="rgba(37, 99, 235, 0)"/>
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="softGlowLight" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <clipPath id="avatarClipLight">
      <rect x="910" y="80" width="420" height="540" rx="24"/>
    </clipPath>
    <clipPath id="bannerClipLight">
      <rect x="0" y="0" width="1400" height="700" rx="40"/>
    </clipPath>
  </defs>

  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    
    @keyframes cursorBlinkLight {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    @keyframes scanMotionLight {{
      0% {{ transform: translateY(-40px); }}
      50% {{ transform: translateY(520px); }}
      100% {{ transform: translateY(-40px); }}
    }}
  </style>

  <g clip-path="url(#bannerClipLight)">
    <!-- Canvas Base -->
    <rect width="1400" height="700" fill="url(#bgGradLight)"/>

    <!-- Grid Lines -->
    <g opacity="0.08" stroke="#2563EB" stroke-width="1">
      <path d="M0 100 H1400 M0 200 H1400 M0 300 H1400 M0 400 H1400 M0 500 H1400 M0 600 H1400"/>
      <path d="M100 0 V700 M200 0 V700 M300 0 V700 M400 0 V700 M500 0 V700 M600 0 V700 M700 0 V700 M800 0 V700 M900 0 V700 M1000 0 V700 M1100 0 V700 M1200 0 V700 M1300 0 V700"/>
    </g>

    <!-- Banner Outer Border -->
    <rect x="2" y="2" width="1396" height="696" rx="38" fill="none" stroke="url(#glassBorderLight)" stroke-width="2"/>

    <!-- ================= LEFT SIDE: TERMINAL (LIGHT) ================= -->
    <g transform="translate(60, 70)">
      <rect width="440" height="560" rx="20" fill="rgba(255, 255, 255, 0.85)" stroke="rgba(15, 23, 42, 0.12)" stroke-width="1.5"/>
      <rect width="440" height="40" rx="20" fill="rgba(15, 23, 42, 0.04)"/>
      <circle cx="25" cy="20" r="5.5" fill="#FF5F56"/>
      <circle cx="43" cy="20" r="5.5" fill="#FFBD2E"/>
      <circle cx="61" cy="20" r="5.5" fill="#27C93F"/>
      <text x="220" y="24" fill="#64748B" font-size="12" class="mono" text-anchor="middle">ai_core_kernel.sh</text>

      <g transform="translate(25, 70)" class="mono" font-size="13">
        <text fill="#2563EB" y="0">&gt; <tspan fill="#0F172A">Initializing AI Core...</tspan></text>
        <text fill="#2563EB" y="30">&gt; <tspan fill="#475569">Loading Neural Network...</tspan></text>
        <text fill="#2563EB" y="60">&gt; <tspan fill="#475569">Loading Memory Modules...</tspan></text>
        <text fill="#2563EB" y="90">&gt; <tspan fill="#475569">Loading Autonomous Agents...</tspan></text>
        <text fill="#2563EB" y="120">&gt; <tspan fill="#7C3AED">Loading LLM Models...</tspan></text>
        <text fill="#16A34A" y="150">[OK] AI Engine Status: Ready.</text>

        <line x1="0" y1="180" x2="390" y2="180" stroke="rgba(15,23,42,0.1)" stroke-width="1"/>

        <g transform="translate(0, 215)">
          <text fill="#6D28D9" font-weight="bold">$ whoami</text>
          <rect x="0" y="15" width="390" height="110" rx="12" fill="rgba(37, 99, 235, 0.05)" stroke="rgba(37, 99, 235, 0.2)" stroke-width="1"/>
          <text x="15" y="42" fill="#0F172A" font-size="16" class="sans" font-weight="bold">Vishal Rathod</text>
          <text x="15" y="66" fill="#2563EB" font-size="13" class="sans">AI Engineer &amp; ML Specialist</text>
          <text x="15" y="88" fill="#475569" font-size="12" class="mono">GenAI • Agentic AI • LLMs • MLOps</text>
          <text x="15" y="108" fill="#7C3AED" font-size="11" class="mono">📍 India</text>
        </g>

        <g transform="translate(0, 370)">
          <text fill="#64748B" font-size="11" class="mono">// CURRENT MISSION</text>
          <rect x="0" y="12" width="390" height="55" rx="10" fill="rgba(109, 40, 217, 0.06)" stroke="rgba(109, 40, 217, 0.2)"/>
          <text x="12" y="34" fill="#0F172A" font-size="12" class="sans">"Building intelligent AI products that</text>
          <text x="12" y="52" fill="#2563EB" font-size="12" class="sans">positively impact millions of people."</text>
        </g>

        <g transform="translate(0, 465)">
          <text fill="#2563EB" font-weight="bold">$ <tspan fill="#0F172A">exec agent.run()</tspan></text>
          <rect x="165" y="-12" width="8" height="15" fill="#2563EB" style="animation: cursorBlinkLight 1s infinite;"/>
        </g>
      </g>
    </g>

    <!-- ================= CENTER SIDE: NAME & BRANDING (LIGHT) ================= -->
    <g transform="translate(540, 310)">
      <g transform="translate(0, -100)">
        <rect width="210" height="30" rx="15" fill="rgba(37, 99, 235, 0.08)" stroke="rgba(37, 99, 235, 0.25)" stroke-width="1"/>
        <circle cx="18" cy="15" r="4" fill="#16A34A"/>
        <text x="32" y="20" fill="#2563EB" font-size="11" class="mono" font-weight="bold" letter-spacing="1">AI RESEARCH LAB</text>
      </g>

      <text x="0" y="-30" fill="url(#textShimmerLight)" font-size="52" class="sans" font-weight="900" letter-spacing="4">VISHAL RATHOD</text>
      <text x="4" y="15" fill="#475569" font-size="18" class="sans" font-weight="500" letter-spacing="6">AI ENGINEER &amp; ARCHITECT</text>
      <line x1="4" y1="35" x2="330" y2="35" stroke="url(#primaryGradLight)" stroke-width="2" stroke-linecap="round"/>

      <g transform="translate(4, 55)">
        <rect width="105" height="26" rx="13" fill="rgba(15, 23, 42, 0.05)" stroke="rgba(15, 23, 42, 0.1)"/>
        <text x="52.5" y="17" fill="#0F172A" font-size="11" class="mono" text-anchor="middle">Deep Learning</text>
        <rect x="115" width="95" height="26" rx="13" fill="rgba(15, 23, 42, 0.05)" stroke="rgba(15, 23, 42, 0.1)"/>
        <text x="162.5" y="17" fill="#0F172A" font-size="11" class="mono" text-anchor="middle">Agentic AI</text>
        <rect x="220" width="85" height="26" rx="13" fill="rgba(15, 23, 42, 0.05)" stroke="rgba(15, 23, 42, 0.1)"/>
        <text x="262.5" y="17" fill="#0F172A" font-size="11" class="mono" text-anchor="middle">LLMs/RAG</text>
      </g>
    </g>

    <!-- ================= RIGHT SIDE: HOLOGRAM CHARACTER (LIGHT) ================= -->
    <g transform="translate(920, 70)">
      <rect width="410" height="560" rx="24" fill="rgba(255, 255, 255, 0.75)" stroke="url(#glassBorderLight)" stroke-width="1.5"/>
      <g clip-path="url(#avatarClipLight)">
        <image href="{img_data_uri}" x="910" y="80" width="420" height="540" preserveAspectRatio="xMidYMid slice" opacity="0.95"/>
      </g>
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="410" height="8" fill="url(#scanlineGradLight)" style="animation: scanMotionLight 4s infinite ease-in-out;"/>
        <line x1="0" y1="4" x2="410" y2="4" stroke="#2563EB" stroke-width="2" style="animation: scanMotionLight 4s infinite ease-in-out;"/>
      </g>
    </g>
  </g>
</svg>'''

with open("assets/banner-light.svg", "w") as f:
    f.write(banner_light_svg)

print("Created assets/banner-light.svg")

# ==========================================
# 3. SKILLS SVG
# ==========================================
skills_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradSkills" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E1A35"/>
      <stop offset="100%" stop-color="#04070E"/>
    </linearGradient>

    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(79, 140, 255, 0.4)"/>
      <stop offset="50%" stop-color="rgba(124, 92, 255, 0.2)"/>
      <stop offset="100%" stop-color="rgba(255, 255, 255, 0.05)"/>
    </linearGradient>

    <linearGradient id="badgeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(79, 140, 255, 0.15)"/>
      <stop offset="100%" stop-color="rgba(124, 92, 255, 0.15)"/>
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .sans { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
    .mono { font-family: 'JetBrains Mono', monospace; }
    
    @keyframes floatCard {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-6px); }
    }
    .c1 { animation: floatCard 6s infinite ease-in-out; }
    .c2 { animation: floatCard 6s infinite ease-in-out 1.5s; }
    .c3 { animation: floatCard 6s infinite ease-in-out 3s; }
  </style>

  <rect width="900" height="520" rx="24" fill="url(#bgGradSkills)" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>

  <!-- Title Header -->
  <g transform="translate(40, 45)">
    <text fill="#F8FAFC" font-size="22" class="sans" font-weight="800" letter-spacing="1">AI &amp; ENGINEERING TECH STACK</text>
    <text fill="#94A3B8" font-size="13" class="mono" y="24">System Architecture &amp; Core Competencies</text>
  </g>

  <!-- CARD 1: LANGUAGES -->
  <g transform="translate(40, 100)" class="c1">
    <rect width="820" height="100" rx="16" fill="rgba(10, 18, 36, 0.65)" stroke="url(#cardBorder)" stroke-width="1"/>
    <rect width="4" height="100" rx="2" fill="#4F8CFF"/>
    
    <text x="24" y="32" fill="#4F8CFF" font-size="14" class="sans" font-weight="bold">⚡ LANGUAGES &amp; CORE</text>

    <!-- Badges Row -->
    <g transform="translate(24, 48)">
      <!-- Python -->
      <rect width="110" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(79, 140, 255, 0.3)"/>
      <circle cx="16" cy="16" r="4" fill="#3776AB"/>
      <text x="28" y="21" fill="#F8FAFC" font-size="12" class="mono">Python</text>

      <!-- C++ -->
      <rect x="122" width="90" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(79, 140, 255, 0.3)"/>
      <circle cx="138" cy="16" r="4" fill="#00599C"/>
      <text x="150" y="21" fill="#F8FAFC" font-size="12" class="mono">C++</text>

      <!-- SQL -->
      <rect x="224" width="90" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(79, 140, 255, 0.3)"/>
      <circle cx="240" cy="16" r="4" fill="#F29111"/>
      <text x="252" y="21" fill="#F8FAFC" font-size="12" class="mono">SQL</text>

      <!-- JavaScript -->
      <rect x="326" width="120" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(79, 140, 255, 0.3)"/>
      <circle cx="342" cy="16" r="4" fill="#F7DF1E"/>
      <text x="354" y="21" fill="#F8FAFC" font-size="12" class="mono">JavaScript</text>
    </g>
  </g>

  <!-- CARD 2: AI / ML / LLM -->
  <g transform="translate(40, 220)" class="c2">
    <rect width="820" height="150" rx="16" fill="rgba(10, 18, 36, 0.65)" stroke="url(#cardBorder)" stroke-width="1"/>
    <rect width="4" height="150" rx="2" fill="#7C5CFF"/>
    
    <text x="24" y="30" fill="#7C5CFF" font-size="14" class="sans" font-weight="bold">🧠 AI, DEEP LEARNING &amp; AGENTIC FRAMEWORKS</text>

    <g transform="translate(24, 45)">
      <!-- Row 1 -->
      <g transform="translate(0,0)">
        <rect width="110" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="16" cy="16" r="4" fill="#EE4C2C"/>
        <text x="28" y="21" fill="#F8FAFC" font-size="12" class="mono">PyTorch</text>

        <rect x="122" width="130" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="138" cy="16" r="4" fill="#FF6F00"/>
        <text x="150" y="21" fill="#F8FAFC" font-size="12" class="mono">TensorFlow</text>

        <rect x="264" width="135" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="280" cy="16" r="4" fill="#F7931E"/>
        <text x="292" y="21" fill="#F8FAFC" font-size="12" class="mono">Scikit-Learn</text>

        <rect x="411" width="125" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="427" cy="16" r="4" fill="#1C3C3C"/>
        <text x="439" y="21" fill="#F8FAFC" font-size="12" class="mono">LangChain</text>

        <rect x="548" width="125" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="564" cy="16" r="4" fill="#7C5CFF"/>
        <text x="576" y="21" fill="#F8FAFC" font-size="12" class="mono">LangGraph</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 46)">
        <rect width="105" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="16" cy="16" r="4" fill="#B28DFF"/>
        <text x="28" y="21" fill="#F8FAFC" font-size="12" class="mono">CrewAI</text>

        <rect x="117" width="110" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="133" cy="16" r="4" fill="#4F8CFF"/>
        <text x="145" y="21" fill="#F8FAFC" font-size="12" class="mono">AutoGen</text>

        <rect x="239" width="105" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="255" cy="16" r="4" fill="#10A37F"/>
        <text x="267" y="21" fill="#F8FAFC" font-size="12" class="mono">OpenAI</text>

        <rect x="356" width="105" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="372" cy="16" r="4" fill="#8E75FF"/>
        <text x="384" y="21" fill="#F8FAFC" font-size="12" class="mono">Gemini</text>

        <rect x="473" width="95" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(124, 92, 255, 0.3)"/>
        <circle cx="489" cy="16" r="4" fill="#F55036"/>
        <text x="501" y="21" fill="#F8FAFC" font-size="12" class="mono">Groq</text>
      </g>
    </g>
  </g>

  <!-- CARD 3: BACKEND & CLOUD -->
  <g transform="translate(40, 390)" class="c3">
    <rect width="820" height="100" rx="16" fill="rgba(10, 18, 36, 0.65)" stroke="url(#cardBorder)" stroke-width="1"/>
    <rect width="4" height="100" rx="2" fill="#B28DFF"/>
    
    <text x="24" y="32" fill="#B28DFF" font-size="14" class="sans" font-weight="bold">⚙️ BACKEND, INFRASTRUCTURE &amp; MLOPS</text>

    <g transform="translate(24, 48)">
      <rect width="105" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(178, 141, 255, 0.3)"/>
      <circle cx="16" cy="16" r="4" fill="#059669"/>
      <text x="28" y="21" fill="#F8FAFC" font-size="12" class="mono">FastAPI</text>

      <rect x="117" width="90" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(178, 141, 255, 0.3)"/>
      <circle cx="133" cy="16" r="4" fill="#94A3B8"/>
      <text x="145" y="21" fill="#F8FAFC" font-size="12" class="mono">Flask</text>

      <rect x="219" width="100" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(178, 141, 255, 0.3)"/>
      <circle cx="235" cy="16" r="4" fill="#2496ED"/>
      <text x="247" y="21" fill="#F8FAFC" font-size="12" class="mono">Docker</text>

      <rect x="331" width="90" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(178, 141, 255, 0.3)"/>
      <circle cx="347" cy="16" r="4" fill="#FCC624"/>
      <text x="359" y="21" fill="#F8FAFC" font-size="12" class="mono">Linux</text>

      <rect x="433" width="90" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(178, 141, 255, 0.3)"/>
      <circle cx="449" cy="16" r="4" fill="#DC382D"/>
      <text x="461" y="21" fill="#F8FAFC" font-size="12" class="mono">Redis</text>

      <rect x="535" width="110" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(178, 141, 255, 0.3)"/>
      <circle cx="551" cy="16" r="4" fill="#4169E1"/>
      <text x="563" y="21" fill="#F8FAFC" font-size="12" class="mono">Postgres</text>

      <rect x="657" width="90" height="32" rx="8" fill="url(#badgeGrad)" stroke="rgba(178, 141, 255, 0.3)"/>
      <circle cx="673" cy="16" r="4" fill="#FF9900"/>
      <text x="685" y="21" fill="#F8FAFC" font-size="12" class="mono">AWS</text>
    </g>
  </g>
</svg>'''

with open("assets/skills.svg", "w") as f:
    f.write(skills_svg)

print("Created assets/skills.svg")

# ==========================================
# 4. STATS SVG
# ==========================================
stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradStats" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E1A35"/>
      <stop offset="100%" stop-color="#04070E"/>
    </linearGradient>

    <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F8CFF"/>
      <stop offset="50%" stop-color="#7C5CFF"/>
      <stop offset="100%" stop-color="#B28DFF"/>
    </linearGradient>

    <filter id="glowStats" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .sans { font-family: 'Inter', -apple-system, sans-serif; }
    .mono { font-family: 'JetBrains Mono', monospace; }

    @keyframes spinRing {
      0% { stroke-dashoffset: 440; }
      100% { stroke-dashoffset: 65; }
    }
    @keyframes barGrow {
      0% { width: 0px; }
    }
  </style>

  <rect width="900" height="450" rx="24" fill="url(#bgGradStats)" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(40, 45)">
    <text fill="#F8FAFC" font-size="22" class="sans" font-weight="800" letter-spacing="1">AI METRICS &amp; GITHUB DASHBOARD</text>
    <text fill="#94A3B8" font-size="13" class="mono" y="24">Real-time Performance &amp; Repository Telemetry</text>
  </g>

  <!-- Left: Circular Rank Ring -->
  <g transform="translate(160, 240)">
    <circle cx="0" cy="0" r="85" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="12"/>
    <circle cx="0" cy="0" r="85" fill="none" stroke="url(#ringGrad)" stroke-width="12" stroke-dasharray="534" stroke-linecap="round" filter="url(#glowStats)" style="animation: spinRing 2.5s ease-out forwards;"/>
    
    <text text-anchor="middle" y="-10" fill="#F8FAFC" font-size="34" class="sans" font-weight="900">S+</text>
    <text text-anchor="middle" y="18" fill="#4F8CFF" font-size="12" class="mono" font-weight="bold">TOP 1% RANK</text>
    <text text-anchor="middle" y="36" fill="#94A3B8" font-size="10" class="mono">AI ARCHITECT</text>
  </g>

  <!-- Middle: Key Metrics Cards -->
  <g transform="translate(340, 110)">
    <!-- Metric 1 -->
    <g transform="translate(0, 0)">
      <rect width="230" height="90" rx="14" fill="rgba(10, 18, 36, 0.65)" stroke="rgba(79, 140, 255, 0.2)" stroke-width="1"/>
      <text x="20" y="34" fill="#94A3B8" font-size="12" class="mono">REPOSITORIES</text>
      <text x="20" y="68" fill="#F8FAFC" font-size="28" class="sans" font-weight="800">35+</text>
      <circle cx="195" cy="45" r="14" fill="rgba(79,140,255,0.15)"/>
      <path d="M190 45 L194 49 L200 41" fill="none" stroke="#4F8CFF" stroke-width="2"/>
    </g>

    <!-- Metric 2 -->
    <g transform="translate(250, 0)">
      <rect width="230" height="90" rx="14" fill="rgba(10, 18, 36, 0.65)" stroke="rgba(124, 92, 255, 0.2)" stroke-width="1"/>
      <text x="20" y="34" fill="#94A3B8" font-size="12" class="mono">TOTAL COMMITS</text>
      <text x="20" y="68" fill="#F8FAFC" font-size="28" class="sans" font-weight="800">1,250+</text>
      <circle cx="195" cy="45" r="14" fill="rgba(124,92,255,0.15)"/>
      <path d="M190 45 L194 49 L200 41" fill="none" stroke="#7C5CFF" stroke-width="2"/>
    </g>

    <!-- Metric 3 -->
    <g transform="translate(0, 110)">
      <rect width="230" height="90" rx="14" fill="rgba(10, 18, 36, 0.65)" stroke="rgba(178, 141, 255, 0.2)" stroke-width="1"/>
      <text x="20" y="34" fill="#94A3B8" font-size="12" class="mono">STARS EARNED</text>
      <text x="20" y="68" fill="#F8FAFC" font-size="28" class="sans" font-weight="800">480+</text>
      <circle cx="195" cy="45" r="14" fill="rgba(178,141,255,0.15)"/>
      <path d="M190 45 L194 49 L200 41" fill="none" stroke="#B28DFF" stroke-width="2"/>
    </g>

    <!-- Metric 4 -->
    <g transform="translate(250, 110)">
      <rect width="230" height="90" rx="14" fill="rgba(10, 18, 36, 0.65)" stroke="rgba(79, 140, 255, 0.2)" stroke-width="1"/>
      <text x="20" y="34" fill="#94A3B8" font-size="12" class="mono">FOLLOWERS</text>
      <text x="20" y="68" fill="#F8FAFC" font-size="28" class="sans" font-weight="800">120+</text>
      <circle cx="195" cy="45" r="14" fill="rgba(79,140,255,0.15)"/>
      <path d="M190 45 L194 49 L200 41" fill="none" stroke="#4F8CFF" stroke-width="2"/>
    </g>
  </g>

  <!-- Bottom: Language Breakdown Progress Bar -->
  <g transform="translate(40, 345)">
    <rect width="820" height="65" rx="14" fill="rgba(10, 18, 36, 0.65)" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    
    <text x="20" y="24" fill="#94A3B8" font-size="11" class="mono">PRIMARY STACK DISTRIBUTION</text>
    
    <!-- Multi-color bar -->
    <g transform="translate(20, 34)">
      <rect width="780" height="12" rx="6" fill="rgba(255,255,255,0.08)"/>
      
      <!-- Python (65%) -->
      <rect width="507" height="12" rx="6" fill="#4F8CFF" style="animation: barGrow 1.5s ease-out;"/>
      <!-- C++ (15%) -->
      <rect x="511" width="117" height="12" rx="6" fill="#7C5CFF" style="animation: barGrow 1.8s ease-out;"/>
      <!-- SQL (10%) -->
      <rect x="632" width="78" height="12" rx="6" fill="#B28DFF" style="animation: barGrow 2.1s ease-out;"/>
      <!-- JS (10%) -->
      <rect x="714" width="78" height="12" rx="6" fill="#27C93F" style="animation: barGrow 2.4s ease-out;"/>
    </g>
  </g>
</svg>'''

with open("assets/stats.svg", "w") as f:
    f.write(stats_svg)

print("Created assets/stats.svg")

# ==========================================
# 5. TIMELINE SVG
# ==========================================
timeline_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradTimeline" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E1A35"/>
      <stop offset="100%" stop-color="#04070E"/>
    </linearGradient>

    <linearGradient id="timelineLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F8CFF"/>
      <stop offset="35%" stop-color="#7C5CFF"/>
      <stop offset="70%" stop-color="#B28DFF"/>
      <stop offset="100%" stop-color="#27C93F"/>
    </linearGradient>

    <filter id="glowNode" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .sans { font-family: 'Inter', -apple-system, sans-serif; }
    .mono { font-family: 'JetBrains Mono', monospace; }
    
    @keyframes pulseNode {
      0%, 100% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.3); opacity: 1; }
    }
  </style>

  <rect width="900" height="360" rx="24" fill="url(#bgGradTimeline)" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>

  <!-- Title -->
  <g transform="translate(40, 45)">
    <text fill="#F8FAFC" font-size="22" class="sans" font-weight="800" letter-spacing="1">EVOLUTION &amp; MILESTONES</text>
    <text fill="#94A3B8" font-size="13" class="mono" y="24">Engineering Trajectory &amp; Technical Specialization</text>
  </g>

  <!-- Horizontal Timeline Line -->
  <line x1="80" y1="180" x2="820" y2="180" stroke="url(#timelineLine)" stroke-width="4" stroke-linecap="round"/>

  <!-- STEP 1: 2024 -->
  <g transform="translate(100, 180)">
    <circle cx="0" cy="0" r="10" fill="#0A1224" stroke="#4F8CFF" stroke-width="4" filter="url(#glowNode)"/>
    <circle cx="0" cy="0" r="4" fill="#4F8CFF"/>
    
    <!-- Top Box -->
    <g transform="translate(-65, -110)">
      <rect width="130" height="80" rx="12" fill="rgba(10, 18, 36, 0.75)" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1"/>
      <text x="15" y="28" fill="#4F8CFF" font-size="16" class="sans" font-weight="bold">2024</text>
      <text x="15" y="48" fill="#F8FAFC" font-size="12" class="sans" font-weight="600">Machine Learning</text>
      <text x="15" y="65" fill="#94A3B8" font-size="10" class="mono">Foundations &amp; Math</text>
    </g>
  </g>

  <!-- STEP 2: 2025 -->
  <g transform="translate(280, 180)">
    <circle cx="0" cy="0" r="10" fill="#0A1224" stroke="#7C5CFF" stroke-width="4" filter="url(#glowNode)"/>
    <circle cx="0" cy="0" r="4" fill="#7C5CFF"/>
    
    <!-- Bottom Box -->
    <g transform="translate(-65, 30)">
      <rect width="130" height="80" rx="12" fill="rgba(10, 18, 36, 0.75)" stroke="rgba(124, 92, 255, 0.3)" stroke-width="1"/>
      <text x="15" y="28" fill="#7C5CFF" font-size="16" class="sans" font-weight="bold">2025</text>
      <text x="15" y="48" fill="#F8FAFC" font-size="12" class="sans" font-weight="600">Deep Learning</text>
      <text x="15" y="65" fill="#94A3B8" font-size="10" class="mono">PyTorch &amp; CV</text>
    </g>
  </g>

  <!-- STEP 3: 2026 -->
  <g transform="translate(460, 180)">
    <circle cx="0" cy="0" r="10" fill="#0A1224" stroke="#B28DFF" stroke-width="4" filter="url(#glowNode)"/>
    <circle cx="0" cy="0" r="4" fill="#B28DFF"/>
    
    <!-- Top Box -->
    <g transform="translate(-65, -110)">
      <rect width="130" height="80" rx="12" fill="rgba(10, 18, 36, 0.75)" stroke="rgba(178, 141, 255, 0.3)" stroke-width="1"/>
      <text x="15" y="28" fill="#B28DFF" font-size="16" class="sans" font-weight="bold">2026</text>
      <text x="15" y="48" fill="#F8FAFC" font-size="12" class="sans" font-weight="600">Generative AI</text>
      <text x="15" y="65" fill="#94A3B8" font-size="10" class="mono">LLMs &amp; RAG</text>
    </g>
  </g>

  <!-- STEP 4: 2027 -->
  <g transform="translate(640, 180)">
    <circle cx="0" cy="0" r="10" fill="#0A1224" stroke="#4F8CFF" stroke-width="4" filter="url(#glowNode)"/>
    <circle cx="0" cy="0" r="4" fill="#4F8CFF"/>
    
    <!-- Bottom Box -->
    <g transform="translate(-65, 30)">
      <rect width="130" height="80" rx="12" fill="rgba(10, 18, 36, 0.75)" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1"/>
      <text x="15" y="28" fill="#4F8CFF" font-size="16" class="sans" font-weight="bold">2027</text>
      <text x="15" y="48" fill="#F8FAFC" font-size="12" class="sans" font-weight="600">Agentic AI</text>
      <text x="15" y="65" fill="#94A3B8" font-size="10" class="mono">Autonomous Multi-Agent</text>
    </g>
  </g>

  <!-- STEP 5: FUTURE -->
  <g transform="translate(800, 180)">
    <circle cx="0" cy="0" r="12" fill="#27C93F" opacity="0.3" filter="url(#glowNode)"/>
    <circle cx="0" cy="0" r="8" fill="#0A1224" stroke="#27C93F" stroke-width="3"/>
    <circle cx="0" cy="0" r="3" fill="#27C93F"/>
    
    <!-- Top Box -->
    <g transform="translate(-65, -110)">
      <rect width="130" height="80" rx="12" fill="rgba(10, 18, 36, 0.85)" stroke="rgba(39, 201, 63, 0.4)" stroke-width="1.5"/>
      <text x="15" y="28" fill="#27C93F" font-size="16" class="sans" font-weight="bold">FUTURE</text>
      <text x="15" y="48" fill="#F8FAFC" font-size="12" class="sans" font-weight="600">AI Product Lead</text>
      <text x="15" y="65" fill="#94A3B8" font-size="10" class="mono">Scaling Global AI</text>
    </g>
  </g>
</svg>'''

with open("assets/timeline.svg", "w") as f:
    f.write(timeline_svg)

print("Created assets/timeline.svg")

# ==========================================
# 6. FOOTER SVG
# ==========================================
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 180" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradFooter" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E1A35"/>
      <stop offset="100%" stop-color="#04070E"/>
    </linearGradient>

    <linearGradient id="borderGradFooter" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(79, 140, 255, 0.3)"/>
      <stop offset="50%" stop-color="rgba(124, 92, 255, 0.2)"/>
      <stop offset="100%" stop-color="rgba(178, 141, 255, 0.3)"/>
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', monospace; }
    @keyframes blinkCursor { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
  </style>

  <rect width="900" height="180" rx="20" fill="url(#bgGradFooter)" stroke="url(#borderGradFooter)" stroke-width="1.5"/>

  <!-- Top Bar -->
  <rect width="900" height="35" rx="20" fill="rgba(255,255,255,0.03)"/>
  <circle cx="20" cy="18" r="5" fill="#FF5F56"/>
  <circle cx="36" cy="18" r="5" fill="#FFBD2E"/>
  <circle cx="52" cy="18" r="5" fill="#27C93F"/>
  <text x="450" y="22" fill="#94A3B8" font-size="11" class="mono" text-anchor="middle">life_loop.py</text>

  <!-- Loop Content -->
  <g transform="translate(30, 65)" class="mono" font-size="14">
    <text fill="#4F8CFF" y="0"><tspan fill="#7C5CFF" font-weight="bold">while</tspan> (<tspan fill="#27C93F">alive</tspan>) {</text>
    <text fill="#94A3B8" y="24" x="25">learn();</text>
    <text fill="#94A3B8" y="44" x="25">build();</text>
    <text fill="#94A3B8" y="64" x="25">share();</text>
    <text fill="#B28DFF" y="84" x="25">repeat();</text>
    <text fill="#4F8CFF" y="104">}</text>

    <!-- Blinking Cursor -->
    <rect x="20" y="92" width="8" height="16" fill="#4F8CFF" style="animation: blinkCursor 1s infinite;"/>
  </g>

  <!-- Right Watermark -->
  <g transform="translate(860, 150)" class="mono" text-anchor="end">
    <text fill="#94A3B8" font-size="10" opacity="0.6">VISHAL RATHOD // AI LAB v2026</text>
  </g>
</svg>'''

with open("assets/footer.svg", "w") as f:
    f.write(footer_svg)

print("Created assets/footer.svg")

# ==========================================
# 7. LANYARD SVG
# ==========================================
lanyard_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 70" width="100%" height="100%">
  <defs>
    <linearGradient id="bgLanyard" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0A1224"/>
      <stop offset="100%" stop-color="#0E1A35"/>
    </linearGradient>
  </defs>

  <style>
    .sans { font-family: 'Inter', sans-serif; }
    .mono { font-family: 'JetBrains Mono', monospace; }
    @keyframes pulseOnline { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }
  </style>

  <rect width="500" height="70" rx="35" fill="url(#bgLanyard)" stroke="rgba(79, 140, 255, 0.3)" stroke-width="1.5"/>

  <g transform="translate(25, 38)">
    <circle cx="15" cy="0" r="6" fill="#27C93F" style="animation: pulseOnline 2s infinite;"/>
    <text x="32" y="5" fill="#F8FAFC" font-size="13" class="sans" font-weight="bold">SYSTEM STATUS:</text>
    <text x="160" y="5" fill="#27C93F" font-size="13" class="mono">ONLINE</text>
    <text x="235" y="5" fill="#94A3B8" font-size="12" class="mono">| Latency: 12ms | India 🇮🇳</text>
  </g>
</svg>'''

with open("assets/lanyard.svg", "w") as f:
    f.write(lanyard_svg)

print("Created assets/lanyard.svg")

# ==========================================
# 8. LOADING & PARTICLES SVG
# ==========================================
loading_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 60" width="100%" height="100%">
  <style>
    .mono { font-family: 'JetBrains Mono', monospace; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
  </style>
  <g transform="translate(20, 30)">
    <circle cx="15" cy="0" r="10" fill="none" stroke="rgba(79,140,255,0.2)" stroke-width="3"/>
    <circle cx="15" cy="0" r="10" fill="none" stroke="#4F8CFF" stroke-width="3" stroke-dasharray="25 40" style="transform-origin: 15px 0px; animation: spin 1s linear infinite;"/>
    <text x="40" y="4" fill="#94A3B8" font-size="12" class="mono">Initializing AI Neural Engine...</text>
  </g>
</svg>'''

with open("assets/loading.svg", "w") as f:
    f.write(loading_svg)

particles_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="100%">
  <style>
    @keyframes floatP { 0%, 100% { transform: translateY(0px); opacity: 0.3; } 50% { transform: translateY(-20px); opacity: 0.9; } }
  </style>
  <circle cx="100" cy="150" r="2" fill="#4F8CFF" style="animation: floatP 4s infinite;"/>
  <circle cx="300" cy="80" r="1.5" fill="#7C5CFF" style="animation: floatP 6s infinite 1s;"/>
  <circle cx="500" cy="120" r="2.5" fill="#B28DFF" style="animation: floatP 5s infinite 2s;"/>
  <circle cx="700" cy="60" r="2" fill="#4F8CFF" style="animation: floatP 7s infinite 0.5s;"/>
</svg>'''

with open("assets/particles.svg", "w") as f:
    f.write(particles_svg)

print("All assets generated successfully!")
