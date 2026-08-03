import re

avatar_dark = """        <!-- Base Viewport Box -->
        <rect width="300" height="320" rx="16" fill="#070D1B" stroke="rgba(124, 92, 255, 0.35)" stroke-width="1.5" />

        <!-- Ambient Volumetric Glow behind Avatar -->
        <circle cx="150" cy="140" r="100" fill="url(#volumetricLight2)" opacity="0.6" />
        <circle cx="150" cy="130" r="85" fill="none" stroke="#4F8CFF" stroke-width="1.5" stroke-dasharray="6 4" class="circuit-line" />
        <circle cx="150" cy="130" r="65" fill="none" stroke="#7C5CFF" stroke-width="1" opacity="0.5" />

        <!-- Vector Sci-Fi AI Silhouette & Neural Mesh -->
        <g transform="translate(0, 10)">
          <!-- Shoulders & Torso -->
          <path d="M 45,300 C 60,225 105,200 150,200 C 195,200 240,225 255,300 Z" fill="url(#primaryGradient)" opacity="0.75" />
          <path d="M 75,300 L 150,220 L 225,300" fill="none" stroke="#B28DFF" stroke-width="1.5" opacity="0.6" />

          <!-- Neck -->
          <path d="M 132,170 L 168,170 L 164,200 L 136,200 Z" fill="#0A1224" stroke="#7C5CFF" stroke-width="1.5" />

          <!-- Head Structure -->
          <path d="M 105,125 C 105,70 195,70 195,125 C 195,175 105,175 105,125 Z" fill="#091020" stroke="#4F8CFF" stroke-width="2" />
          
          <!-- Glowing Futuristic AI Visor -->
          <path d="M 112,118 Q 150,106 188,118 Q 188,136 150,140 Q 112,136 112,118 Z" fill="#4F8CFF" filter="url(#softGlow)" opacity="0.95" />
          <path d="M 118,124 Q 150,116 182,124" fill="none" stroke="#F8FAFC" stroke-width="2.5" stroke-linecap="round" />

          <!-- Facial Neural Mesh Points -->
          <circle cx="130" cy="100" r="2.5" fill="#B28DFF" />
          <circle cx="170" cy="100" r="2.5" fill="#B28DFF" />
          <circle cx="150" cy="90" r="3" fill="#4F8CFF" />
          <circle cx="150" cy="155" r="2.5" fill="#7C5CFF" />

          <line x1="130" y1="100" x2="150" y2="90" stroke="#7C5CFF" stroke-width="1" opacity="0.5" />
          <line x1="170" y1="100" x2="150" y2="90" stroke="#7C5CFF" stroke-width="1" opacity="0.5" />
          <line x1="130" y1="100" x2="112" y2="118" stroke="#4F8CFF" stroke-width="1" opacity="0.5" />
          <line x1="170" y1="100" x2="188" y2="118" stroke="#4F8CFF" stroke-width="1" opacity="0.5" />
        </g>

        <!-- Holographic Top-to-Bottom Scanline Beam -->
        <rect width="300" height="45" fill="url(#scanlineGrad)" class="scanner-line" clip-path="url(#avatarClip)" />
        
        <!-- Tech Viewport Corner Accents -->
        <path d="M 0,20 L 0,0 L 20,0" fill="none" stroke="#4F8CFF" stroke-width="2.5" />
        <path d="M 280,0 L 300,0 L 300,20" fill="none" stroke="#4F8CFF" stroke-width="2.5" />
        <path d="M 0,300 L 0,320 L 20,320" fill="none" stroke="#7C5CFF" stroke-width="2.5" />
        <path d="M 280,320 L 300,320 L 300,300" fill="none" stroke="#7C5CFF" stroke-width="2.5" />"""

avatar_light = """        <!-- Base Viewport Box -->
        <rect width="300" height="320" rx="16" fill="#F1F5F9" stroke="rgba(37, 99, 235, 0.35)" stroke-width="1.5" />

        <circle cx="150" cy="140" r="100" fill="url(#volumetricLightLight2)" opacity="0.6" />
        <circle cx="150" cy="130" r="85" fill="none" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="6 4" />
        <circle cx="150" cy="130" r="65" fill="none" stroke="#6366F1" stroke-width="1" opacity="0.5" />

        <g transform="translate(0, 10)">
          <path d="M 45,300 C 60,225 105,200 150,200 C 195,200 240,225 255,300 Z" fill="url(#primaryGradientLight)" opacity="0.75" />
          <path d="M 75,300 L 150,220 L 225,300" fill="none" stroke="#7C3AED" stroke-width="1.5" opacity="0.6" />

          <path d="M 132,170 L 168,170 L 164,200 L 136,200 Z" fill="#E2E8F0" stroke="#6366F1" stroke-width="1.5" />
          <path d="M 105,125 C 105,70 195,70 195,125 C 195,175 105,175 105,125 Z" fill="#CBD5E1" stroke="#2563EB" stroke-width="2" />
          
          <path d="M 112,118 Q 150,106 188,118 Q 188,136 150,140 Q 112,136 112,118 Z" fill="#2563EB" opacity="0.95" />
          <path d="M 118,124 Q 150,116 182,124" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" />

          <circle cx="130" cy="100" r="2.5" fill="#7C3AED" />
          <circle cx="170" cy="100" r="2.5" fill="#7C3AED" />
          <circle cx="150" cy="90" r="3" fill="#2563EB" />
        </g>

        <rect width="300" height="45" fill="url(#scanlineGradLight)" class="scanner-line" clip-path="url(#avatarClipLight)" />
        
        <path d="M 0,20 L 0,0 L 20,0" fill="none" stroke="#2563EB" stroke-width="2.5" />
        <path d="M 280,0 L 300,0 L 300,20" fill="none" stroke="#2563EB" stroke-width="2.5" />
        <path d="M 0,300 L 0,320 L 20,320" fill="none" stroke="#6366F1" stroke-width="2.5" />
        <path d="M 280,320 L 300,320 L 300,300" fill="none" stroke="#6366F1" stroke-width="2.5" />"""

with open('assets/banner-dark.svg', 'r', encoding='utf-8') as f:
    content = f.read()

new_content_dark = re.sub(r'<g transform="translate\(20, 20\)">(.*?)</g>\n\n      <!-- Subtitle Stats', f'<g transform="translate(20, 20)">\n{avatar_dark}\n      </g>\n\n      <!-- Subtitle Stats', content, flags=re.DOTALL)

with open('assets/banner-dark.svg', 'w', encoding='utf-8') as f:
    f.write(new_content_dark)

with open('assets/banner-light.svg', 'r', encoding='utf-8') as f:
    content_light = f.read()

new_content_light = re.sub(r'<g transform="translate\(20, 20\)">(.*?)</g>\n\n      <!-- Subtitle Stats', f'<g transform="translate(20, 20)">\n{avatar_light}\n      </g>\n\n      <!-- Subtitle Stats', content_light, flags=re.DOTALL)

with open('assets/banner-light.svg', 'w', encoding='utf-8') as f:
    f.write(new_content_light)

print("Updated banner SVGs with pure vector AI avatars successfully!")
