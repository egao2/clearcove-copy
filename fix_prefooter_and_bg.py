import re
import glob

# 1. Extract the .cc-prefooter-sec CSS from index.html
with open('index.html', 'r') as f:
    index_html = f.read()

prefooter_css_match = re.search(r'<style>\s*\.cc-prefooter-sec.*?<\/style>', index_html, re.DOTALL)
prefooter_css = ""
if prefooter_css_match:
    full_match = prefooter_css_match.group(0)
    # Strip <style> and </style>
    prefooter_css = full_match.replace('<style>', '').replace('</style>', '').strip()
    
    # Remove it from index.html
    index_html = index_html.replace(full_match, '')
    with open('index.html', 'w') as f:
        f.write(index_html)
    print("Extracted prefooter CSS from index.html")

# 2. Append the prefooter CSS to premium.css
# 3. Force the geometric background on .website-container and [data-live-site-root] 
# to ensure it breaks through any intermediate opaque wrappers in Durable.
force_bg_css = """
/* Force Geometric Background on all root wrappers */
html, body, .website-container, [data-live-site-root], main {
    background-color: #0d1117 !important;
    background-image: 
        radial-gradient(circle at 15% 30%, rgba(0, 126, 118, 0.15), transparent 40%),
        radial-gradient(circle at 85% 70%, rgba(0, 126, 118, 0.12), transparent 40%),
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 60px 60px, 60px 60px !important;
    background-position: center !important;
    background-attachment: fixed !important;
}
"""

with open('premium.css', 'a') as f:
    f.write("\n" + force_bg_css)
    if prefooter_css:
        f.write("\n/* Prefooter Global Styles */\n" + prefooter_css + "\n")
    print("Updated premium.css with forced background and prefooter CSS")

