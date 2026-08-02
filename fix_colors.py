import glob
import re

# 1. Fix the premium.js footer blog link issue
with open('premium.js', 'r') as f:
    js = f.read()

# Replace textContent = 'Blog' with innerHTML replace to preserve styling spans
js = js.replace("blogLink.textContent = 'Blog';", "blogLink.innerHTML = blogLink.innerHTML.replace('About', 'Blog');")

with open('premium.js', 'w') as f:
    f.write(js)

# 2. Fix the font colors on the newly generated HTML pages
new_pages = ['privacy.html', 'terms.html', 'blog-support-automation.html', 'blog-ai-readiness.html']

for page in new_pages:
    with open(page, 'r') as f:
        html = f.read()
    
    # The generated pages have a section wrapper. Let's force text-white and colors.
    # The Tailwind classes like text-gray-300 were stripped because they weren't in the original build.
    # We will inject raw CSS styles into the tags to guarantee they render correctly.
    
    # Fix the main wrapper text color
    html = html.replace('text-[var(--secondary-text)]"', 'text-[var(--secondary-text)]" style="color: #d1d5db;"')
    
    # Fix all paragraphs
    html = re.sub(r'<p class="(.*?)"', r'<p class="\1" style="color: #d1d5db;"', html)
    
    # Fix all h2s
    html = re.sub(r'<h2 class="(.*?)"', r'<h2 class="\1" style="color: #fcfcfc;"', html)
    
    # Fix list items
    html = html.replace('<li>', '<li style="color: #d1d5db;">')
    html = html.replace('<li class="', '<li style="color: #d1d5db;" class="')
    
    # Fix the specific h1
    html = html.replace('<h1 class="', '<h1 style="color: #fcfcfc;" class="')

    # Fix the blog publish dates
    html = html.replace('style="color: #d1d5db;">Published on', 'style="color: #9ca3af;">Published on')
    
    with open(page, 'w') as f:
        f.write(html)

print("Applied color fixes to premium.js and all 4 new HTML pages.")
