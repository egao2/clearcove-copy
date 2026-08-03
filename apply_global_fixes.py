import glob
import re

with open('prefooter.txt', 'r') as f:
    prefooter_html = f.read()

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    # Fix the logo links
    html = html.replace('href="index.html"', 'href="https://clearcove.pro/"')
    html = html.replace('href="/index.html"', 'href="https://clearcove.pro/"')
    
    # Inject prefooter (skip index.html since it already has it)
    if file != 'index.html':
        # check if it already has it to be safe
        if 'cc-prefooter-sec' not in html:
            # inject right before <footer>
            html = html.replace('<footer', prefooter_html + '\n<footer')
            
    # Apply about.html specific tweaks
    if file == 'about.html':
        # Increase font size for method cards
        html = html.replace('.cc-method-card p {\n    color: #9ca3af;\n    line-height: 1.6;\n}', 
                            '.cc-method-card p {\n    color: #9ca3af;\n    line-height: 1.7;\n    font-size: 1.125rem;\n}')
        
        # Add abstract glowing backgrounds to the page container
        # Since I replaced background-color: #0b1120; with transparent previously, let's target the wrapper or the transparent class
        # Wait, the previous script did: html = html.replace('background-color: #0b1120;', 'background-color: transparent;')
        
        old_css = '.cc-about-page {\n    background-color: transparent;\n    color: #fcfcfc;\n    font-family: var(--typography-font-family, system-ui, sans-serif);\n}'
        
        new_css = """.cc-about-page {
    background-color: transparent;
    background-image: 
        radial-gradient(circle at 15% 30%, rgba(0, 126, 118, 0.12), transparent 40%),
        radial-gradient(circle at 85% 70%, rgba(0, 126, 118, 0.08), transparent 40%),
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    background-position: center;
    color: #fcfcfc;
    font-family: var(--typography-font-family, system-ui, sans-serif);
}"""
        html = html.replace(old_css, new_css)
        
    with open(file, 'w') as f:
        f.write(html)

print("Applied global fixes and about.html styling.")
