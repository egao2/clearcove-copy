import re

with open('index.html', 'r') as f:
    html = f.read()

# The current case study section is:
# <style>
# .cc-case-study-sec { ...
# ...
# </section>

new_case_study_html = """
<style>
.cc-case-study-sec {
    padding: 80px 24px;
    background-color: #0b1120;
    position: relative;
    z-index: 10;
    font-family: var(--typography-font-family, system-ui, sans-serif);
}
.cc-case-study-grid {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr;
    gap: 24px;
}
@media (min-width: 1024px) {
    .cc-case-study-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
.cc-case-study-card {
    background-color: #111827;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 32px 24px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.2);
    display: flex;
    flex-direction: column;
}
.cc-case-study-eyebrow {
    color: #007E76;
    font-weight: 700;
    font-size: 0.75rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 16px;
}
.cc-case-study-title {
    font-size: 1.75rem;
    font-weight: 800;
    color: #fcfcfc;
    line-height: 1.2;
    margin-bottom: 16px;
    letter-spacing: -0.02em;
}
.cc-case-study-quote {
    font-size: 1rem;
    line-height: 1.6;
    color: #9ca3af;
    font-style: italic;
    flex-grow: 1;
}
</style>
<section class="cc-case-study-sec">
    <div class="cc-case-study-grid">
        <!-- Card 1 -->
        <div class="cc-case-study-card">
            <div class="cc-case-study-eyebrow">Case Study: Series A Fintech</div>
            <h2 class="cc-case-study-title">60% Reduction in Support Costs</h2>
            <p class="cc-case-study-quote">"ClearCove automated our support intake process, reducing first-response time from 4 hours to under 2 minutes. We scaled our user base 3x without adding a single headcount."</p>
        </div>
        
        <!-- Card 2 -->
        <div class="cc-case-study-card">
            <div class="cc-case-study-eyebrow">Case Study: Enterprise SaaS</div>
            <h2 class="cc-case-study-title">4x Faster Sales Cycles</h2>
            <p class="cc-case-study-quote">"By implementing their AI lead orchestration agents, our sales team no longer wastes time on manual qualification. High-intent prospects are engaged immediately, completely transforming our pipeline velocity."</p>
        </div>

        <!-- Card 3 -->
        <div class="cc-case-study-card">
            <div class="cc-case-study-eyebrow">Case Study: Healthcare Tech</div>
            <h2 class="cc-case-study-title">200% Inbound Pipeline Growth</h2>
            <p class="cc-case-study-quote">"ClearCove built an always-on content engine that perfectly matched our brand voice. The output volume and quality allowed us to dominate our niche SEO rankings within months."</p>
        </div>
    </div>
</section>
"""

# We need to replace the old one
old_match = re.search(r'(<style>\s*\.cc-case-study-sec.*?</style>\s*<section class="cc-case-study-sec">.*?</section>)', html, re.DOTALL)
if old_match:
    html = html.replace(old_match.group(1), new_case_study_html)
    with open('index.html', 'w') as f:
        f.write(html)
    print("Successfully replaced case study section")
else:
    print("Could not find the old case study section")
