import re

with open('about.html', 'r') as f:
    html = f.read()

# The hero section is: We bridge the gap between bleeding-edge AI models...
# We will just replace everything between <main> and the footer with our custom sections.

new_main_content = """<main>
<style>
.cc-about-page {
    background-color: #0b1120;
    color: #fcfcfc;
    font-family: var(--typography-font-family, system-ui, sans-serif);
}
.cc-hero {
    padding: 140px 24px 80px;
    text-align: center;
    max-width: 900px;
    margin: 0 auto;
}
.cc-hero h1 {
    font-size: 4rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 24px;
    letter-spacing: -0.02em;
}
.cc-hero p {
    font-size: 1.25rem;
    line-height: 1.6;
    color: #9ca3af;
    max-width: 700px;
    margin: 0 auto;
}
.cc-founder-sec {
    padding: 80px 24px;
}
.cc-founder-container {
    max-width: 800px;
    margin: 0 auto;
    background-color: #111827;
    padding: 60px 40px;
    border-radius: 24px;
    border: 1px solid rgba(0, 126, 118, 0.3);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    text-align: center;
}
.cc-founder-quote {
    font-size: 1.5rem;
    line-height: 1.6;
    font-style: italic;
    color: #fcfcfc;
    margin-bottom: 32px;
}
.cc-founder-author {
    font-weight: 800;
    font-size: 1.25rem;
    color: #007E76;
}
.cc-founder-title {
    font-size: 0.875rem;
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
}
.cc-methodology {
    padding: 80px 24px 120px;
    max-width: 1200px;
    margin: 0 auto;
}
.cc-method-header {
    text-align: center;
    margin-bottom: 60px;
}
.cc-method-header h2 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 16px;
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
    background-color: #111827;
    padding: 40px 32px;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}
.cc-method-num {
    font-size: 3rem;
    font-weight: 900;
    color: rgba(0, 126, 118, 0.2);
    line-height: 1;
    margin-bottom: 16px;
}
.cc-method-card h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #fcfcfc;
}
.cc-method-card p {
    color: #9ca3af;
    line-height: 1.6;
}
</style>
<div class="cc-about-page">
    <section class="cc-hero">
        <h1>No hype.<br/><span style="color: #007E76;">Just execution.</span></h1>
        <p>We bridge the gap between bleeding-edge AI models and practical, ROI-driven business operations. We build resilient, self-healing systems that slash overhead and accelerate growth.</p>
    </section>

    <section class="cc-founder-sec">
        <div class="cc-founder-container">
            <p class="cc-founder-quote">"Enterprise software used to take months to build. With modern AI orchestration, what used to take teams of engineers can now be deployed in weeks. But scaling it requires deep architectural discipline. That's why ClearCove exists."</p>
            <div style="color: #fcfcfc; font-weight: 700; font-size: 1.25rem; margin-bottom: 0.25rem;">Eric G.</div>
            <div class="cc-founder-author">Founder & Principal Architect</div>
            <div class="cc-founder-title">Senior Platform Architect, Zendesk</div>
        </div>
    </section>

    <section class="cc-methodology">
        <div class="cc-method-header">
            <h2>Our Methodology</h2>
        </div>
        <div class="cc-method-grid">
            <div class="cc-method-card">
                <div class="cc-method-num">01</div>
                <h3>Process Diagnostics</h3>
                <p>We deep-dive into your existing architecture and workflows, identifying exactly where manual processes are bottlenecking revenue.</p>
            </div>
            <div class="cc-method-card">
                <div class="cc-method-num">02</div>
                <h3>AI Tool-chaining</h3>
                <p>We architect robust, scalable integrations that connect advanced LLMs directly to your CRM, support ticketing, or marketing databases.</p>
            </div>
            <div class="cc-method-card">
                <div class="cc-method-num">03</div>
                <h3>Human Handoff</h3>
                <p>We deploy the agents with strict guardrails, ensuring that AI handles the heavy lifting while seamlessly escalating high-value decisions back to your human team.</p>
            </div>
        </div>
    </section>
</div>
"""

# Find <main>...</main> and replace
main_match = re.search(r'(<main>.*?</main>)', html, re.DOTALL)
if main_match:
    html = html.replace(main_match.group(1), new_main_content + "</main>")
    with open('about.html', 'w') as f:
        f.write(html)
    print("Rebuilt about.html successfully")
else:
    # If no closing </main>, try finding footer and replace up to there
    print("Could not find <main> block")
    
