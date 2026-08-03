import re
import glob

# 1. Update cc-case-study-sec to use glassmorphism
with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('background-color: #0b1120;', 'background-color: rgba(11, 17, 32, 0.4); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);')
with open('index.html', 'w') as f:
    f.write(html)
print("Updated case study background in index.html")

# 2. Remove cc-fade-up hardcoded classes from ALL HTML files
# Because cc-fade-up forces an immediate animation on page load, breaking scroll reveals
for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        content = f.read()
    
    # We remove cc-fade-up and any cc-delay-X classes
    content = re.sub(r'\s*cc-fade-up\s*', ' ', content)
    content = re.sub(r'\s*cc-delay-\d+\s*', ' ', content)
    
    with open(file, 'w') as f:
        f.write(content)
print("Removed hardcoded cc-fade-up animations globally to rely on JS scroll reveals.")

# 3. Update premium.js to handle staggered scroll reveals
with open('premium.js', 'r') as f:
    js = f.read()

new_observer_logic = """
    // 2. Scroll Reveals with Staggering
    let staggerTimeout;
    let revealQueue = [];
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                revealQueue.push(entry.target);
                observer.unobserve(entry.target);
            }
        });
        
        if (revealQueue.length > 0) {
            clearTimeout(staggerTimeout);
            staggerTimeout = setTimeout(() => {
                // Sort by vertical position to ensure top-to-bottom staggering
                revealQueue.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
                
                revealQueue.forEach((el, index) => {
                    // Apply a staggered transition delay based on their index in the batch
                    el.style.transitionDelay = `${index * 150}ms`;
                    el.classList.add('reveal-visible');
                    
                    // Clean up the inline delay after the transition finishes so hover effects aren't delayed later
                    setTimeout(() => {
                        el.style.transitionDelay = '';
                    }, 1000 + (index * 150));
                });
                revealQueue = [];
            }, 50);
        }
    }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    // Apply reveal to sections, headings, images, and paragraphs
    const elementsToReveal = document.querySelectorAll('section, h1, h2, h3, img, p');
    elementsToReveal.forEach(el => {
"""

# Replace the old observer logic
# Find the block from "// 2. Scroll Reveals" to "elementsToReveal.forEach(el => {"
old_observer_logic = re.search(r'// 2\. Scroll Reveals.*?const elementsToReveal = document\.querySelectorAll\([^\)]+\);\s*elementsToReveal\.forEach\(el => \{', js, re.DOTALL)
if old_observer_logic:
    js = js.replace(old_observer_logic.group(0), new_observer_logic.strip())
    with open('premium.js', 'w') as f:
        f.write(js)
    print("Updated premium.js to support staggered scroll reveals.")

