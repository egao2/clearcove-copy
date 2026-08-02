import re

with open('index.html', 'r') as f:
    html = f.read()

# Add button CSS
css_injection = """
.cc-case-study-quote {
    font-size: 1rem;
    line-height: 1.6;
    color: #9ca3af;
    font-style: italic;
    flex-grow: 1;
    margin-bottom: 24px;
}
.cc-cs-card-btn {
    display: inline-block;
    width: 100%;
    text-align: center;
    background-color: transparent;
    color: #007E76;
    border: 1px solid rgba(0, 126, 118, 0.4);
    font-weight: 600;
    padding: 12px 16px;
    border-radius: 8px;
    text-decoration: none;
    transition: all 0.2s;
    margin-top: auto;
}
.cc-cs-card-btn:hover {
    background-color: rgba(0, 126, 118, 0.1);
    border-color: #007E76;
}
</style>
"""
html = html.replace('.cc-case-study-quote {\n    font-size: 1rem;\n    line-height: 1.6;\n    color: #9ca3af;\n    font-style: italic;\n    flex-grow: 1;\n}\n</style>', css_injection)

# Add buttons to cards
# Card 1
c1 = '<p class="cc-case-study-quote">"ClearCove automated our support intake process, reducing first-response time from 4 hours to under 2 minutes. We scaled our user base 3x without adding a single headcount."</p>'
c1_new = c1 + '\n            <a href="case-study-fintech.html" class="cc-cs-card-btn">Read Case Study</a>'
html = html.replace(c1, c1_new)

# Card 2
c2 = '<p class="cc-case-study-quote">"By implementing their AI lead orchestration agents, our sales team no longer wastes time on manual qualification. High-intent prospects are engaged immediately, completely transforming our pipeline velocity."</p>'
c2_new = c2 + '\n            <a href="case-study-saas.html" class="cc-cs-card-btn">Read Case Study</a>'
html = html.replace(c2, c2_new)

# Card 3
c3 = '<p class="cc-case-study-quote">"ClearCove built an always-on content engine that perfectly matched our brand voice. The output volume and quality allowed us to dominate our niche SEO rankings within months."</p>'
c3_new = c3 + '\n            <a href="case-study-healthtech.html" class="cc-cs-card-btn">Read Case Study</a>'
html = html.replace(c3, c3_new)

with open('index.html', 'w') as f:
    f.write(html)
print("Buttons added to index.html")
