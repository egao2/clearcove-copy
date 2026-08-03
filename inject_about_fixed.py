import re

def update_about_page():
    with open('about.html', 'r') as f:
        html = f.read()

    # Section 1: Impact & Metrics
    metrics_html = """
    <section class="website-container cc-metrics-sec" style="padding: 60px 24px;">
        <div style="margin-left: auto; margin-right: auto; max-width: 1200px;">
            <div class="cc-metrics-grid">
                <div class="cc-metric-card hover-lift reveal-hidden">
                    <div class="cc-metric-value text-gradient-premium">4x</div>
                    <div class="cc-metric-label">Faster Deployment Cycles</div>
                </div>
                <div class="cc-metric-card hover-lift reveal-hidden" style="transition-delay: 150ms;">
                    <div class="cc-metric-value text-gradient-premium">$0</div>
                    <div class="cc-metric-label">Wasted on "Hype" Tech</div>
                </div>
                <div class="cc-metric-card hover-lift reveal-hidden" style="transition-delay: 300ms;">
                    <div class="cc-metric-value text-gradient-premium">100%</div>
                    <div class="cc-metric-label">US-Based Architecture Team</div>
                </div>
            </div>
        </div>
    </section>
    """
    
    html = re.sub(
        r'(<section[^>]*cc-founder-sec.*?</section>)',
        r'\1\n' + metrics_html,
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Section 2: Core Principles
    principles_html = """
    <section class="website-container cc-principles-sec" style="padding: 100px 24px; background: rgba(11, 17, 32, 0.3);">
        <div style="margin-left: auto; margin-right: auto; max-width: 1200px;">
            <div style="text-align: center; margin-bottom: 4rem;" class="reveal-hidden">
                <h2 class="cc-about-title">Core Engineering Principles</h2>
                <p class="cc-about-subtitle">We don't build standard corporate values. We adhere to aggressive, elite standards that match our "no hype" branding.</p>
            </div>
            <div class="cc-principles-grid">
                <!-- Principle 1 -->
                <div class="cc-principle-card hover-lift reveal-hidden">
                    <div class="cc-principle-icon-wrapper">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#007E76" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                    </div>
                    <h3 class="cc-principle-title">Systems Over Band-Aids</h3>
                    <p class="cc-principle-desc">We don't build temporary fixes or fragile integrations. We architect resilient, self-healing infrastructure that scales.</p>
                </div>
                <!-- Principle 2 -->
                <div class="cc-principle-card hover-lift reveal-hidden" style="transition-delay: 150ms;">
                    <div class="cc-principle-icon-wrapper">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#007E76" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                    </div>
                    <h3 class="cc-principle-title">Radical Transparency</h3>
                    <p class="cc-principle-desc">No black-box algorithms or vendor lock-in. You own the IP, the systems, and the data architecture.</p>
                </div>
                <!-- Principle 3 -->
                <div class="cc-principle-card hover-lift reveal-hidden" style="transition-delay: 300ms;">
                    <div class="cc-principle-icon-wrapper">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#007E76" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                    </div>
                    <h3 class="cc-principle-title">Execution Is Everything</h3>
                    <p class="cc-principle-desc">Strategy without deployment is just a slide deck. We build, deploy, and monitor what we design.</p>
                </div>
            </div>
        </div>
    </section>
    """
    
    html = re.sub(
        r'(<section[^>]*cc-methodology.*?</section>)',
        r'\1\n' + principles_html,
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Section 3: Tech Stack
    tech_html = """
    <section class="website-container cc-tech-sec" style="padding: 80px 24px; border-top: 1px solid rgba(255,255,255,0.05); overflow: hidden;">
        <div style="margin-left: auto; margin-right: auto; max-width: 1200px; text-align: center;">
            <p class="cc-tech-eyebrow reveal-hidden">Technologies We Orchestrate</p>
            <div class="cc-tech-grid reveal-hidden">
                <span class="cc-tech-tag">LLM Orchestration</span>
                <span class="cc-tech-tag" style="transition-delay: 50ms;">Vector Databases</span>
                <span class="cc-tech-tag" style="transition-delay: 100ms;">Autonomous Agents</span>
                <span class="cc-tech-tag" style="transition-delay: 150ms;">Edge AI</span>
                <span class="cc-tech-tag" style="transition-delay: 200ms;">Data Pipelines</span>
                <span class="cc-tech-tag" style="transition-delay: 250ms;">Event-Driven Architecture</span>
                <span class="cc-tech-tag" style="transition-delay: 300ms;">High-Availability Systems</span>
            </div>
        </div>
    </section>
    """
    
    html = re.sub(
        r'(<style>\s*\.cc-prefooter-sec|<section[^>]*cc-prefooter-sec)',
        r'\n' + tech_html + r'\n\1',
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open('about.html', 'w') as f:
        f.write(html)
        
    print("Updated about.html")

def update_css():
    css_append = """
/* About Page Custom Styles */
.cc-metrics-grid {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    gap: 2rem;
}
@media (min-width: 768px) {
    .cc-metrics-grid { grid-template-columns: repeat(3, 1fr); }
}
.cc-metric-card {
    background: rgba(25, 33, 43, 0.4);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    padding: 3rem 2rem;
    text-align: center;
}
.cc-metric-value {
    font-size: 4rem;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 1rem;
}
.cc-metric-label {
    font-size: 1.125rem;
    color: #9ca3af;
    font-weight: 500;
}

.cc-about-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1.5rem;
}
@media (min-width: 768px) {
    .cc-about-title { font-size: 3rem; }
}
.cc-about-subtitle {
    font-size: 1.25rem;
    color: #9ca3af;
    max-width: 42rem;
    margin: 0 auto;
    line-height: 1.7;
}
.cc-principles-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
}
@media (min-width: 768px) {
    .cc-principles-grid { grid-template-columns: repeat(3, 1fr); }
}
.cc-principle-card {
    padding: 2rem;
    border-radius: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
}
.cc-principle-icon-wrapper {
    width: 3rem;
    height: 3rem;
    border-radius: 9999px;
    background: rgba(0, 126, 118, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
}
.cc-principle-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1rem;
}
.cc-principle-desc {
    color: #9ca3af;
    line-height: 1.6;
}

.cc-tech-eyebrow {
    color: #007E76;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-size: 0.875rem;
    margin-bottom: 2rem;
}
.cc-tech-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
}
.cc-tech-tag {
    padding: 0.75rem 1.5rem;
    border-radius: 9999px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.05);
    color: #d1d5db;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    font-size: 0.875rem;
    cursor: default;
    transition: all 0.2s;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.05);
}
.cc-tech-tag:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(0, 126, 118, 0.3);
}
"""
    with open('premium.css', 'a') as f:
        f.write("\n" + css_append)
    print("Updated premium.css")

if __name__ == '__main__':
    update_about_page()
    update_css()
