import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Move Case Study
case_study_match = re.search(r'(<style>\s*\.cc-case-study-sec.*?</style>\s*<section class="cc-case-study-sec">.*?</section>)', html, re.DOTALL)
if case_study_match:
    case_study_html = case_study_match.group(1)
    
    # Remove it from its current location
    html = html.replace(case_study_html, '')
    
    # The hero section ends shortly after the secondary CTA.
    cta_index = html.find('Get AI Readiness Checklist</a>')
    if cta_index != -1:
        end_section_index = html.find('</section>', cta_index)
        if end_section_index != -1:
            insertion_point = end_section_index + len('</section>')
            html = html[:insertion_point] + "\n" + case_study_html + html[insertion_point:]
            print("Moved case study successfully")
        else:
            print("Could not find end of hero section")
    else:
        print("Could not find CTA")
else:
    print("Could not find case study")


# 2. Inject Pre-Footer CTA
footer_match = re.search(r'(<footer.*?>.*?</footer>)', html, re.DOTALL)
if footer_match:
    pre_footer_html = """
    <style>
    .cc-prefooter-sec {
        padding: 120px 24px;
        background-color: #0c1312; /* Very dark background */
        text-align: center;
        font-family: var(--typography-font-family, system-ui, sans-serif);
        position: relative;
        overflow: hidden;
    }
    .cc-prefooter-eyebrow {
        color: #007E76;
        font-weight: 700;
        letter-spacing: 0.1em;
        font-size: 0.875rem;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .cc-prefooter-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #fcfcfc;
        line-height: 1.2;
        margin-bottom: 1.5rem;
        letter-spacing: -0.02em;
    }
    .cc-prefooter-desc {
        font-size: 1.25rem;
        line-height: 1.7;
        color: #9ca3af;
        max-width: 700px;
        margin: 0 auto 3rem;
    }
    .cc-prefooter-btn-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 16px;
        flex-wrap: wrap;
    }
    .cc-btn-primary {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background-color: #007E76;
        color: #ffffff;
        font-weight: 500;
        padding: 14px 32px;
        border-radius: 8px;
        text-decoration: none;
        transition: background-color 0.2s;
    }
    .cc-btn-primary:hover { background-color: #00665f; }
    
    .cc-btn-outline {
        display: inline-flex;
        align-items: center;
        background-color: transparent;
        color: #d1d5db;
        font-weight: 500;
        padding: 14px 32px;
        border-radius: 8px;
        border: 1px solid rgba(156, 163, 175, 0.4);
        text-decoration: none;
        transition: all 0.2s;
    }
    .cc-btn-outline:hover { 
        border-color: #fcfcfc;
        color: #fcfcfc;
    }
    .cc-prefooter-meta {
        margin-top: 3rem;
        font-size: 0.875rem;
        color: #6b7280;
    }
    @media (min-width: 768px) {
        .cc-prefooter-title { font-size: 4.5rem; }
    }
    </style>
    <section class="cc-prefooter-sec">
        <p class="cc-prefooter-eyebrow">Ready when you are</p>
        <h2 class="cc-prefooter-title">Bring the noise. We'll clear the cove.</h2>
        <p class="cc-prefooter-desc">Send us your operation, your backlog, or the workflow everyone else has written off. We'll come back with a delivery plan ranked by ROI — within a week.</p>
        
        <div class="cc-prefooter-btn-container">
            <a href="https://calendar.app.google/mCDenTF29rv4Zzb18" class="cc-btn-primary">
                Start a project
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
            <a href="mailto:hello@clearcove.pro" class="cc-btn-outline">hello@clearcove.pro</a>
        </div>
        
        <p class="cc-prefooter-meta">Founder-led. Senior architecture team. Fully remote, US-wide.</p>
    </section>
    """
    html = html.replace(footer_match.group(1), pre_footer_html + "\n" + footer_match.group(1))
    print("Injected pre-footer successfully")
else:
    print("Could not find footer")

with open('index.html', 'w') as f:
    f.write(html)
