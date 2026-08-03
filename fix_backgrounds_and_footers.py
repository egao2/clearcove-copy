import glob
import re

def hex_to_rgba(hex_code, opacity=0.6):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) == 3:
        hex_code = ''.join([c*2 for c in hex_code])
    if len(hex_code) != 6:
        # If something weird like an 8-char hex with alpha, just return original but try to parse
        return hex_code
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return f"rgba({r}, {g}, {b}, {opacity})"

def convert_background_to_glass(match):
    full_style = match.group(0)
    hex_color = match.group(1)
    
    # Exclude if it's not a standard hex (e.g. if it has alpha already or is something else)
    if len(hex_color) not in [4, 7]:
        return full_style
        
    rgba_color = hex_to_rgba(hex_color, 0.6)
    
    # Replace the hex color with rgba
    new_style = full_style.replace(f"background:{hex_color}", f"background:{rgba_color}")
    new_style = new_style.replace(f"background-color:{hex_color}", f"background-color:{rgba_color}")
    
    # Add backdrop filter
    if "backdrop-filter" not in new_style:
        new_style = new_style[:-1] + "; backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);\""
        
    return new_style

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
        
    # 1. Remove redundant strategy footer blocks if they appear right before cc-prefooter-sec
    # A safe way is to split by <section and if the second to last contains 'build your AI strategy together' or 'Ready to transform your operations' or similar CTA text?
    # Wait, the redundant footer always seems to be the section IMMEDIATELY PRECEDING `<section class="cc-prefooter-sec">`.
    # Let's check if the section immediately preceding it has a CTA like "Let’s build" or if it's the last native Durable block.
    # Actually, we can just remove the specific section by finding it.
    
    # Let's remove the second to last section in blog.html and services.html ONLY if it's the CTA block.
    # We can do this reliably by regex matching the entire section before cc-prefooter-sec that contains an image with _next/img or "strategy together"
    if file in ['blog.html', 'services.html']:
        # Find the cc-prefooter-sec
        prefooter_idx = html.find('<section class="cc-prefooter-sec">')
        if prefooter_idx != -1:
            # Find the start of the section immediately before it
            # To do this safely, we reverse search for '<section' starting from prefooter_idx - 1
            prev_sec_idx = html.rfind('<section', 0, prefooter_idx - 1)
            if prev_sec_idx != -1:
                # Get that section
                prev_section = html[prev_sec_idx:prefooter_idx]
                # Is it the CTA? (Let's build... or has the isometric image)
                if 'strategy together' in prev_section or 'Isometric 3D visualization' in prev_section or 'Let’s build' in prev_section or 'Let\'s build' in prev_section:
                    html = html[:prev_sec_idx] + html[prefooter_idx:]
                    print(f"Removed redundant footer CTA from {file}")

    # 2. Fix solid backgrounds that block the geometric grid
    # Some sections use `style="...background:#19212B..."` instead of `--bg-color`
    html = re.sub(r'style="[^"]*?background(?:-color)?:\s*(#[A-Fa-f0-9]{3,6})[^"]*?"', convert_background_to_glass, html)
    
    with open(file, 'w') as f:
        f.write(html)

print("Fixed solid backgrounds and redundant footers.")
