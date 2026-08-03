import re

def update_about_page():
    with open('about.html', 'r') as f:
        html = f.read()

    # Section 1: Impact & Metrics
    metrics_html = """
    <section class="website-container cc-metrics-sec" style="padding: 60px 24px;">
        <div class="mx-auto max-w-[1200px]">
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
    
    # Insert after founder quote section
    html = re.sub(
        r'(<section[^>]*cc-founder-sec.*?</section>)',
        r'\1\n' + metrics_html,
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Section 2: Core Principles
    principles_html = """
    <section class="website-container cc-principles-sec" style="padding: 100px 24px; background: rgba(11, 17, 32, 0.3);">
        <div class="mx-auto max-w-[1200px]">
            <div class="text-center mb-16 reveal-hidden">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-6">Core Engineering Principles</h2>
                <p class="text-xl text-gray-400 max-w-2xl mx-auto">We don't build standard corporate values. We adhere to aggressive, elite standards that match our "no hype" branding.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Principle 1 -->
                <div class="p-8 rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl hover-lift reveal-hidden">
                    <div class="w-12 h-12 rounded-full bg-[#007E76]/20 flex items-center justify-center mb-6">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#007E76" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">Systems Over Band-Aids</h3>
                    <p class="text-gray-400 leading-relaxed">We don't build temporary fixes or fragile integrations. We architect resilient, self-healing infrastructure that scales.</p>
                </div>
                <!-- Principle 2 -->
                <div class="p-8 rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl hover-lift reveal-hidden" style="transition-delay: 150ms;">
                    <div class="w-12 h-12 rounded-full bg-[#007E76]/20 flex items-center justify-center mb-6">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#007E76" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">Radical Transparency</h3>
                    <p class="text-gray-400 leading-relaxed">No black-box algorithms or vendor lock-in. You own the IP, the systems, and the data architecture.</p>
                </div>
                <!-- Principle 3 -->
                <div class="p-8 rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl hover-lift reveal-hidden" style="transition-delay: 300ms;">
                    <div class="w-12 h-12 rounded-full bg-[#007E76]/20 flex items-center justify-center mb-6">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#007E76" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-4">Execution Is Everything</h3>
                    <p class="text-gray-400 leading-relaxed">Strategy without deployment is just a slide deck. We build, deploy, and monitor what we design.</p>
                </div>
            </div>
        </div>
    </section>
    """
    
    # Insert after methodology section
    html = re.sub(
        r'(<section[^>]*cc-methodology.*?</section>)',
        r'\1\n' + principles_html,
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Section 3: Tech Stack Abstraction
    tech_html = """
    <section class="website-container cc-tech-sec" style="padding: 80px 24px; border-top: 1px solid rgba(255,255,255,0.05); overflow: hidden;">
        <div class="mx-auto max-w-[1200px] text-center">
            <p class="text-[#007E76] font-bold tracking-widest uppercase text-sm mb-8 reveal-hidden">Technologies We Orchestrate</p>
            <div class="flex flex-wrap justify-center gap-4 reveal-hidden">
                <span class="px-6 py-3 rounded-full border border-white/20 bg-white/5 text-gray-300 backdrop-blur-md text-sm hover:bg-white/10 hover:border-white/40 hover:-translate-y-1 transition-all cursor-default shadow-[0_0_15px_rgba(255,255,255,0.05)] hover:shadow-[0_0_20px_rgba(0,126,118,0.3)]">LLM Orchestration</span>
                <span class="px-6 py-3 rounded-full border border-white/20 bg-white/5 text-gray-300 backdrop-blur-md text-sm hover:bg-white/10 hover:border-white/40 hover:-translate-y-1 transition-all cursor-default shadow-[0_0_15px_rgba(255,255,255,0.05)] hover:shadow-[0_0_20px_rgba(0,126,118,0.3)]" style="transition-delay: 50ms;">Vector Databases</span>
                <span class="px-6 py-3 rounded-full border border-white/20 bg-white/5 text-gray-300 backdrop-blur-md text-sm hover:bg-white/10 hover:border-white/40 hover:-translate-y-1 transition-all cursor-default shadow-[0_0_15px_rgba(255,255,255,0.05)] hover:shadow-[0_0_20px_rgba(0,126,118,0.3)]" style="transition-delay: 100ms;">Autonomous Agents</span>
                <span class="px-6 py-3 rounded-full border border-white/20 bg-white/5 text-gray-300 backdrop-blur-md text-sm hover:bg-white/10 hover:border-white/40 hover:-translate-y-1 transition-all cursor-default shadow-[0_0_15px_rgba(255,255,255,0.05)] hover:shadow-[0_0_20px_rgba(0,126,118,0.3)]" style="transition-delay: 150ms;">Edge AI</span>
                <span class="px-6 py-3 rounded-full border border-white/20 bg-white/5 text-gray-300 backdrop-blur-md text-sm hover:bg-white/10 hover:border-white/40 hover:-translate-y-1 transition-all cursor-default shadow-[0_0_15px_rgba(255,255,255,0.05)] hover:shadow-[0_0_20px_rgba(0,126,118,0.3)]" style="transition-delay: 200ms;">Data Pipelines</span>
                <span class="px-6 py-3 rounded-full border border-white/20 bg-white/5 text-gray-300 backdrop-blur-md text-sm hover:bg-white/10 hover:border-white/40 hover:-translate-y-1 transition-all cursor-default shadow-[0_0_15px_rgba(255,255,255,0.05)] hover:shadow-[0_0_20px_rgba(0,126,118,0.3)]" style="transition-delay: 250ms;">Event-Driven Architecture</span>
                <span class="px-6 py-3 rounded-full border border-white/20 bg-white/5 text-gray-300 backdrop-blur-md text-sm hover:bg-white/10 hover:border-white/40 hover:-translate-y-1 transition-all cursor-default shadow-[0_0_15px_rgba(255,255,255,0.05)] hover:shadow-[0_0_20px_rgba(0,126,118,0.3)]" style="transition-delay: 300ms;">High-Availability Systems</span>
            </div>
        </div>
    </section>
    """
    
    # Insert before the prefooter section
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
/* About Page Metrics Grid */
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
"""
    with open('premium.css', 'a') as f:
        f.write("\n" + css_append)
    print("Updated premium.css")

if __name__ == '__main__':
    update_about_page()
    update_css()
