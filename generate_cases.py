import re

with open('about.html', 'r') as f:
    about_html = f.read()

# The header is everything before <main> (or <div class="w-full" id="our-story">)
# The footer is from <footer> to the end of the file.

# Find <main>
main_match = re.search(r'(.*?<main>)', about_html, re.DOTALL)
if main_match:
    header_html = main_match.group(1)
else:
    print("Could not find <main>")
    header_html = ""

# Find footer
footer_match = re.search(r'(<footer.*)', about_html, re.DOTALL)
if footer_match:
    footer_html = "</main>" + footer_match.group(1)
else:
    print("Could not find <footer>")
    footer_html = ""

def build_case_study(title, eyebrow, stats, challenge, solution, result):
    css = """
    <style>
    .cc-cs-page {
        padding: 120px 24px 60px;
        background-color: #0b1120;
        color: #fcfcfc;
        font-family: var(--typography-font-family, system-ui, sans-serif);
        min-height: 100vh;
    }
    .cc-cs-container {
        max-width: 800px;
        margin: 0 auto;
    }
    .cc-cs-eyebrow {
        color: #007E76;
        font-weight: 700;
        font-size: 0.875rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 24px;
        display: block;
    }
    .cc-cs-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 40px;
        letter-spacing: -0.02em;
    }
    .cc-cs-stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        background-color: #111827;
        padding: 32px;
        border-radius: 16px;
        margin-bottom: 60px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .cc-cs-stat-item {
        display: flex;
        flex-direction: column;
    }
    .cc-cs-stat-val {
        font-size: 2.5rem;
        font-weight: 800;
        color: #007E76;
        line-height: 1;
        margin-bottom: 8px;
    }
    .cc-cs-stat-label {
        font-size: 0.875rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .cc-cs-content h2 {
        font-size: 1.75rem;
        font-weight: 700;
        margin-top: 48px;
        margin-bottom: 24px;
        color: #fcfcfc;
    }
    .cc-cs-content p {
        font-size: 1.125rem;
        line-height: 1.8;
        color: #d1d5db;
        margin-bottom: 24px;
    }
    .cc-cs-cta-box {
        margin-top: 80px;
        padding: 48px;
        background-color: #007E76;
        border-radius: 16px;
        text-align: center;
    }
    .cc-cs-cta-box h3 {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 16px;
        color: #ffffff;
    }
    .cc-cs-cta-box p {
        font-size: 1.125rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: 32px;
    }
    .cc-cs-cta-btn {
        display: inline-flex;
        background-color: #ffffff;
        color: #007E76;
        font-weight: 600;
        padding: 16px 32px;
        border-radius: 8px;
        text-decoration: none;
        transition: background-color 0.2s;
    }
    .cc-cs-cta-btn:hover {
        background-color: #f3f4f6;
    }
    @media (max-width: 768px) {
        .cc-cs-title { font-size: 2.25rem; }
        .cc-cs-stats { grid-template-columns: 1fr; gap: 32px; text-align: center; }
    }
    </style>
    """
    
    stats_html = "".join([f'<div class="cc-cs-stat-item"><div class="cc-cs-stat-val">{s[0]}</div><div class="cc-cs-stat-label">{s[1]}</div></div>' for s in stats])
    
    body = f"""
    <section class="cc-cs-page">
        <div class="cc-cs-container">
            <span class="cc-cs-eyebrow">{eyebrow}</span>
            <h1 class="cc-cs-title">{title}</h1>
            
            <div class="cc-cs-stats">
                {stats_html}
            </div>
            
            <div class="cc-cs-content">
                <h2>The Challenge</h2>
                <p>{challenge}</p>
                
                <h2>The Solution</h2>
                <p>{solution}</p>
                
                <h2>The Results</h2>
                <p>{result}</p>
            </div>
            
            <div class="cc-cs-cta-box">
                <h3>Want similar results?</h3>
                <p>Let's discuss how AI can transform your operations.</p>
                <a href="mailto:hello@clearcove.pro" class="cc-cs-cta-btn">Book a Strategy Call</a>
            </div>
        </div>
    </section>
    """
    
    return header_html + css + body + footer_html


# 1. Fintech
fintech = build_case_study(
    title="60% Reduction in Support Costs for a Series A Fintech",
    eyebrow="Case Study: Intelligent CX Strategy",
    stats=[("60%", "Cost Reduction"), ("4hr → 2min", "Response Time"), ("3x", "User Base Scaling")],
    challenge="As the company scaled rapidly after their Series A, their customer support team became a bottleneck. Ticket volumes tripled, and first-response times slipped from 30 minutes to over 4 hours. They were facing a difficult choice: drastically increase headcount and burn rate, or suffer a degraded customer experience.",
    solution="ClearCove architected an intelligent AI-driven intake and routing system. Using advanced LLMs integrated directly into their ticketing platform, we built an agent capable of understanding the intent and sentiment of incoming requests. The agent autonomously resolved Tier 1 issues (like password resets and status checks) and intelligently routed complex issues to the correct human specialized team with full context.",
    result="The impact was immediate. First-response times dropped to under 2 minutes. The system successfully deflected 45% of incoming tickets, allowing the existing support team to handle a 3x increase in user base without adding a single new headcount. Overall support costs were reduced by 60% relative to revenue."
)
with open('case-study-fintech.html', 'w') as f: f.write(fintech)

# 2. SaaS
saas = build_case_study(
    title="4x Faster Sales Cycles for Enterprise SaaS",
    eyebrow="Case Study: AI Agent Configuration",
    stats=[("4x", "Faster Cycles"), ("40%", "Pipeline Conv."), ("24/7", "Lead Engagement")],
    challenge="The sales team at this Enterprise SaaS company was spending hours every week manually qualifying leads from marketing campaigns. High-intent prospects were often left waiting days for an SDR to reach out, while SDRs wasted time on unqualified leads. Pipeline velocity was stagnant.",
    solution="We configured and deployed an AI Lead Orchestration Agent that integrated directly with their CRM and marketing automation platforms. When a new lead entered the system, the AI agent immediately enriched the profile, scored the intent, and engaged the prospect via personalized, context-aware email outreach. Only highly qualified, engaged leads were seamlessly handed off to human Account Executives for closing.",
    result="The time-to-engage dropped to zero. Because Account Executives were only spending time on pre-qualified, warm leads, the overall sales cycle was compressed by 4x. Pipeline conversion rates increased by 40%, and SDRs were repurposed to focus on high-value outbound strategy rather than manual triage."
)
with open('case-study-saas.html', 'w') as f: f.write(saas)

# 3. HealthTech
healthtech = build_case_study(
    title="200% Inbound Pipeline Growth for Healthcare Tech",
    eyebrow="Case Study: Marketing Systems & Brand",
    stats=[("200%", "Pipeline Growth"), ("3x", "Organic Traffic"), ("100%", "Brand Compliance")],
    challenge="A growing healthcare technology firm struggled to rank for highly competitive, niche SEO terms. They lacked the internal resources to produce high-volume, authoritative content, and generic AI tools consistently failed to capture their unique brand voice and adhere to strict medical compliance guidelines.",
    solution="ClearCove engineered a bespoke, always-on Content Engine. We trained customized models exclusively on the company's existing high-performing assets, medical whitepapers, and brand guidelines. This ensured that all generated content was not only structurally optimized for SEO but strictly compliant and perfectly aligned with their authoritative brand tone.",
    result="The marketing team was able to scale content production by 10x without hiring additional writers. Within months, they dominated search rankings for their core niche keywords, leading to a 3x increase in organic inbound traffic and a 200% growth in inbound pipeline."
)
with open('case-study-healthtech.html', 'w') as f: f.write(healthtech)

print("Generated all 3 case study pages.")
