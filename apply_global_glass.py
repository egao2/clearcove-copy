import glob
import re

def hex_to_rgba(hex_code, opacity=0.6):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) == 3:
        hex_code = ''.join([c*2 for c in hex_code])
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return f"rgba({r}, {g}, {b}, {opacity})"

def add_glass_to_style(match):
    full_style = match.group(0)
    hex_color = match.group(1)
    
    rgba_color = hex_to_rgba(hex_color, 0.6)
    
    # Replace the hex color with rgba
    new_style = full_style.replace(f"--bg-color:{hex_color}", f"--bg-color:{rgba_color}")
    
    # Add backdrop filter
    if "backdrop-filter" not in new_style:
        # insert before the closing quote
        new_style = new_style[:-1] + "; backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);\""
        
    return new_style

# Append CSS to premium.css
global_css = """
/* Global Animated Background */
.website-container {
    background-color: transparent !important;
}

body {
    background-color: #0d1117 !important;
    background-image: 
        radial-gradient(circle at 15% 30%, rgba(0, 126, 118, 0.15), transparent 40%),
        radial-gradient(circle at 85% 70%, rgba(0, 126, 118, 0.12), transparent 40%),
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 60px 60px, 60px 60px !important;
    background-position: center !important;
    background-attachment: fixed !important;
    animation: bgPulse 10s infinite alternate;
}

@keyframes bgPulse {
    0% { background-position: 0% 0%; }
    100% { background-position: 5% 5%; }
}

/* Global Animations */
.cc-fade-up {
    opacity: 0;
    transform: translateY(30px);
    animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fadeUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
"""

with open('premium.css', 'a') as f:
    f.write(global_css)

# Apply glassmorphism to all HTML files
for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    # Find all style attributes that contain --bg-color:#XXXXXX
    # style="...--bg-color:#19212B..."
    html = re.sub(r'style="[^"]*?--bg-color:(#[A-Fa-f0-9]{3,6})[^"]*?"', add_glass_to_style, html)
    
    # Add cc-fade-up to all sections that don't already have it
    # We target `<section class="w-full"` which is Durable's standard section wrapper
    # We will replace `class="w-full"` with `class="w-full cc-fade-up"`
    html = html.replace('class="w-full"', 'class="w-full cc-fade-up"')
    html = html.replace('class="w-full relative"', 'class="w-full relative cc-fade-up"')
    
    with open(file, 'w') as f:
        f.write(html)

print("Applied global glassmorphism and animations.")
