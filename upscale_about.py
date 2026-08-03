import re

with open('about.html', 'r') as f:
    html = f.read()

# Define the new enhanced CSS
new_css = """
.cc-about-page {
    background-color: transparent;
    background-image: 
        radial-gradient(circle at 15% 30%, rgba(0, 126, 118, 0.15), transparent 40%),
        radial-gradient(circle at 85% 70%, rgba(0, 126, 118, 0.12), transparent 40%),
        linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 60px 60px, 60px 60px;
    background-position: center;
    color: #fcfcfc;
    font-family: var(--typography-font-family, system-ui, sans-serif);
    animation: bgPulse 10s infinite alternate;
}
@keyframes bgPulse {
    0% { background-position: 0% 0%; }
    100% { background-position: 5% 5%; }
}

/* Animations */
.cc-fade-up {
    opacity: 0;
    transform: translateY(30px);
    animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.cc-delay-1 { animation-delay: 0.2s; }
.cc-delay-2 { animation-delay: 0.4s; }
.cc-delay-3 { animation-delay: 0.6s; }

@keyframes fadeUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.cc-hero {
    padding: 160px 24px 80px;
    text-align: center;
    max-width: 1000px;
    margin: 0 auto;
}
.cc-hero h1 {
    font-size: 4.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 32px;
    letter-spacing: -0.03em;
}
.cc-hero p {
    font-size: 1.5rem; /* Increased font size */
    line-height: 1.6;
    color: #d1d5db;
    max-width: 800px;
    margin: 0 auto;
}

.cc-founder-sec {
    padding: 80px 24px;
}
.cc-founder-container {
    max-width: 800px;
    margin: 0 auto;
    background-color: rgba(17, 24, 39, 0.6); /* Glassmorphism */
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    padding: 80px 60px;
    border-radius: 24px;
    border: 1px solid rgba(0, 126, 118, 0.4);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(0, 126, 118, 0.05);
    text-align: center;
}
.cc-founder-quote {
    font-size: 1.75rem; /* Increased font size */
    line-height: 1.6;
    font-style: italic;
    color: #fcfcfc;
    margin-bottom: 40px;
}
.cc-founder-author {
    font-weight: 800;
    font-size: 1.25rem;
    color: #007E76;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

.cc-methodology {
    padding: 80px 24px 140px;
    max-width: 1200px;
    margin: 0 auto;
}
.cc-method-header {
    text-align: center;
    margin-bottom: 80px;
}
.cc-method-header h2 {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 16px;
    letter-spacing: -0.02em;
}
.cc-method-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 32px;
}
@media (min-width: 768px) {
    .cc-method-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
.cc-method-card {
    background-color: rgba(17, 24, 39, 0.6); /* Glassmorphism */
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 48px 40px;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.cc-method-card:hover {
    transform: translateY(-8px);
    border-color: rgba(0, 126, 118, 0.5);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(0, 126, 118, 0.15);
}
.cc-method-num {
    font-size: 3.5rem;
    font-weight: 900;
    color: rgba(0, 126, 118, 0.3);
    line-height: 1;
    margin-bottom: 24px;
    transition: color 0.4s;
}
.cc-method-card:hover .cc-method-num {
    color: rgba(0, 126, 118, 0.8);
}
.cc-method-card h3 {
    font-size: 1.75rem;
    font-weight: 700;
    margin-bottom: 20px;
    color: #fcfcfc;
}
.cc-method-card p {
    color: #9ca3af;
    line-height: 1.7;
    font-size: 1.25rem; /* Increased font size */
}
"""

# We need to extract the existing custom style block and replace it.
# The custom block starts with .cc-about-page { and ends right before <div class="cc-about-page">
match = re.search(r'(\.cc-about-page\s*{.*?)<div class="cc-about-page">', html, re.DOTALL)
if match:
    old_css = match.group(1)
    html = html.replace(old_css, new_css + "\n")
    
    # Also add the cc-fade-up classes to the HTML tags
    # 1. Hero
    html = html.replace('<section class="cc-hero">', '<section class="cc-hero cc-fade-up">')
    # 2. Founder Note
    html = html.replace('<section class="cc-founder-sec">', '<section class="cc-founder-sec cc-fade-up cc-delay-1">')
    # 3. Methodology Header
    html = html.replace('<div class="cc-method-header">', '<div class="cc-method-header cc-fade-up cc-delay-2">')
    # 4. Methodology Cards
    html = html.replace('<div class="cc-method-card">', '<div class="cc-method-card cc-fade-up cc-delay-3">')
    
    with open('about.html', 'w') as f:
        f.write(html)
    print("Successfully replaced CSS and injected animation classes!")
else:
    print("Failed to find custom CSS block.")
