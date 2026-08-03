import re
import glob

# 1. Update premium.css to make the geometric background punchier and re-add the animation
with open('premium.css', 'r') as f:
    css = f.read()

old_block = r'''/\* Global Geometric Background \(Applied ONLY to body to prevent stacking\) \*/
body \{
    background-color: #0d1117 !important;
    background-image: 
        radial-gradient\(circle at 15% 30%, rgba\(0, 126, 118, 0\.15\), transparent 40%\),
        radial-gradient\(circle at 85% 70%, rgba\(0, 126, 118, 0\.12\), transparent 40%\),
        linear-gradient\(to right, rgba\(255, 255, 255, 0\.02\) 1px, transparent 1px\),
        linear-gradient\(to bottom, rgba\(255, 255, 255, 0\.02\) 1px, transparent 1px\) !important;
    background-size: 100% 100%, 100% 100%, 60px 60px, 60px 60px !important;
    background-position: center !important;
    background-attachment: fixed !important;
\}'''

new_block = '''/* Global Geometric Background (Applied ONLY to body to prevent stacking) */
body {
    background-color: #0d1117 !important;
    background-image: 
        radial-gradient(circle at 15% 30%, rgba(0, 126, 118, 0.25), transparent 40%),
        radial-gradient(circle at 85% 70%, rgba(0, 126, 118, 0.20), transparent 40%),
        linear-gradient(to right, rgba(255, 255, 255, 0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.05) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 60px 60px, 60px 60px !important;
    background-position: center !important;
    background-attachment: fixed !important;
    animation: bgPulse 15s ease-in-out infinite alternate !important;
}'''

new_css = re.sub(old_block, new_block, css)
with open('premium.css', 'w') as f:
    f.write(new_css)
print('Updated premium.css with stronger background and animation.')

# 2. Strip the isolated .cc-about-page inline style from about.html so it inherits globally without conflict
with open('about.html', 'r') as f:
    about_html = f.read()

# Remove the entire block inside <style> that defines .cc-about-page
about_html = re.sub(r'\.cc-about-page\s*\{[^}]+\}', '', about_html)
# Remove empty style tags if any
about_html = re.sub(r'<style>\s*</style>', '', about_html)

with open('about.html', 'w') as f:
    f.write(about_html)
print('Cleaned about.html inline styles.')

