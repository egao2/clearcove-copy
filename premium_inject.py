import re

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# 1. index.html - Fix Hero Copy, CTA, and Case Study
index_html = read_file('index.html')

# Hero Copy
index_html = index_html.replace('>Customer Experience &amp; Operations<', '>AI automation consultancy<')
index_html = re.sub(r'>Architecting intelligent customer experiences<', '>Agentic AI.<br/><span style=\"color: #007E76;\">Mid-market pricing.</span><', index_html)
index_html = index_html.replace('We engineer bespoke AI strategies that eliminate manual bottlenecks, streamline your operations, and deliver flawless, zero-wait experiences to your customers at scale.', 'ClearCove deploys AI agents and custom workflows that cut cost and grow revenue — without forcing you through an enterprise procurement cycle.')

# CTA
primary_cta = """<a target="_blank" rel="noopener noreferrer" data-slot="button" label="Book a Free Strategy Call" style="--bg-color:#007E76;--hover-bg-color:#00766f;color:#fcfcfc" class="inline-flex shrink-0 cursor-pointer items-center justify-center bg-(--bg-color) whitespace-nowrap transition-all outline-none hover:bg-(--hover-bg-color) focus-visible:border-primary-border focus-visible:ring-[3px] focus-visible:ring-primary-interactive-bg disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-error-border aria-invalid:ring-error-interactive-bg [&amp;_svg]:pointer-events-none [&amp;_svg]:shrink-0 [&amp;_svg:not([class*=&#x27;size-&#x27;])]:size-4 border border-(--bg-color) hover:border-(--hover-bg-color) gap-2 px-5 py-2.5 has-[&gt;svg:first-child]:pr-4 has-[&gt;svg:last-child]:pl-4 has-[&gt;svg:only-child]:px-2.5 rounded-3xl" href="https://calendar.app.google/mCDenTF29rv4Zzb18"><span class="min-w-0 overflow-hidden text-ellipsis [font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)" style="--typography-font-size:var(--typography-body-sm-em-font-size);--typography-font-weight:var(--typography-body-sm-em-font-weight);--typography-line-height:var(--typography-body-sm-em-line-height);--typography-letter-spacing:var(--typography-body-sm-em-letter-spacing);--typography-font-family:var(--typography-body-sm-em-font-family);color:#fcfcfc">Book a Free Strategy Call</span></a>"""
secondary_cta_style = """
<style>
.cc-sec-cta {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: transparent;
    color: #ffffff;
    font-weight: 500;
    font-size: 0.875rem;
    padding: 10px 20px;
    border-radius: 9999px;
    border: 1px solid #6b7280;
    text-decoration: none;
    transition: all 0.2s;
    margin-left: 16px;
    font-family: var(--typography-font-family, sans-serif);
}
.cc-sec-cta:hover { border-color: #ffffff; background-color: rgba(255,255,255,0.1); }
@media (max-width: 640px) { .cc-sec-cta { margin-left: 0; margin-top: 16px; } }
</style>
"""
secondary_cta = secondary_cta_style + """<a class="cc-sec-cta" href="mailto:hello@clearcove.pro?subject=AI Readiness Checklist Request&body=Hi ClearCove Team,%0D%0A%0D%0AI'd like to receive the free AI Readiness Checklist to see if our operations are ready for automation.%0D%0A%0D%0AThank you!">Get AI Readiness Checklist</a>"""

if "cc-sec-cta" not in index_html:
    index_html = index_html.replace(primary_cta, primary_cta + secondary_cta)

# Case Study
case_study_html = """
<style>
.cc-case-study-sec { padding: 100px 24px; background-color: #0b1120; position: relative; z-index: 10; font-family: var(--typography-font-family, system-ui, sans-serif); }
.cc-case-study-container { max-width: 900px; margin: 0 auto; text-align: center; background: #111827; border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 24px; padding: 60px 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
.cc-case-study-eyebrow { color: #007E76; font-weight: 700; letter-spacing: 0.1em; font-size: 0.875rem; text-transform: uppercase; margin-bottom: 1rem; }
.cc-case-study-title { font-size: 3rem; font-weight: 800; color: #fcfcfc; line-height: 1.2; margin-bottom: 2rem; }
.cc-case-study-quote { font-size: 1.25rem; line-height: 1.8; color: #d1d5db; margin-bottom: 2.5rem; font-style: italic; }
.cc-btn { display: inline-block; background-color: #007E76; color: #ffffff; font-weight: 500; padding: 14px 36px; border-radius: 9999px; text-decoration: none; transition: background-color 0.2s; font-size: 1rem;}
.cc-btn:hover { background-color: #00665f; }
@media (min-width: 768px) { .cc-case-study-title { font-size: 4rem; } .cc-case-study-quote { font-size: 1.5rem; padding: 0 40px;} }
</style>
<section class="cc-case-study-sec">
    <div class="cc-case-study-container">
        <p class="cc-case-study-eyebrow">Case Study: Series A FinTech</p>
        <h2 class="cc-case-study-title">60% Reduction in Support Costs</h2>
        <p class="cc-case-study-quote">"ClearCove automated our support intake process, reducing first-response time from 4 hours to under 2 minutes. We scaled our user base 3x without adding a single headcount."</p>
        <a href="https://calendar.app.google/mCDenTF29rv4Zzb18" target="_blank" class="cc-btn">See how we did it</a>
    </div>
</section>
"""
testimonials_match = re.search(r'(<section[^>]*>.*?Organizations trust ClearCove.*?</section>)', index_html, re.DOTALL)
if testimonials_match and "cc-case-study-sec" not in index_html:
    testimonials_html = testimonials_match.group(1)
    index_html = index_html.replace(testimonials_html, case_study_html + "\n" + testimonials_html)
write_file('index.html', index_html)

# 2. services.html
services_html = read_file('services.html')
services_match = re.search(r'(<section[^>]*>.*?Workflow Automation.*?</section>)', services_html, re.DOTALL)
if services_match:
    new_services_html = """
<style>
.cc-srv-sec { padding: 100px 24px; max-width: 1000px; margin: 60px auto 0; font-family: var(--typography-font-family, sans-serif); }
.cc-srv-eyebrow { color: #007E76; font-weight: 700; letter-spacing: 0.1em; font-size: 0.875rem; text-transform: uppercase; margin-bottom: 1rem; text-align: center; }
.cc-srv-title { font-size: 2.5rem; font-weight: 800; color: #fcfcfc; text-align: center; margin-bottom: 4rem; }
.cc-srv-card { background: #111827; border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 24px; padding: 40px; margin-bottom: 30px; transition: border-color 0.3s; }
.cc-srv-card:hover { border-color: rgba(156, 163, 175, 0.8); }
.cc-srv-header { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; margin-bottom: 24px; }
.cc-srv-num { font-size: 3rem; font-weight: 800; color: #007E76; opacity: 0.8; line-height: 1;}
.cc-srv-card-title { font-size: 1.8rem; font-weight: 800; color: #fcfcfc; line-height: 1.3; margin: 0;}
.cc-srv-desc { font-size: 1.125rem; line-height: 1.7; color: #d1d5db; margin-bottom: 30px; }
.cc-srv-list { list-style: none; padding: 0; margin: 0; }
.cc-srv-list li { display: flex; align-items: flex-start; gap: 12px; color: #9ca3af; margin-bottom: 16px; font-size: 1rem; line-height: 1.5; }
.cc-srv-list li span { color: #007E76; font-weight: bold; }
@media (min-width: 768px) {
    .cc-srv-title { font-size: 3.5rem; }
    .cc-srv-header { flex-direction: row; align-items: center; gap: 24px; }
}
</style>
<section class="cc-srv-sec">
    <p class="cc-srv-eyebrow">Three Service Pillars</p>
    <h2 class="cc-srv-title">What we actually deliver.</h2>
    
    <div class="cc-srv-grid">
        <div class="cc-srv-card">
            <div class="cc-srv-header">
                <span class="cc-srv-num">01</span>
                <h3 class="cc-srv-card-title">Intelligent CX Strategy & Business Operations</h3>
            </div>
            <p class="cc-srv-desc">Translate customer experience briefs and back-office processes into measurable, AI-native operating models — not slides that age on a shelf.</p>
            <ul class="cc-srv-list">
                <li><span>&rarr;</span> Customer journey mapping scored against automatable moments</li>
                <li><span>&rarr;</span> Back-office workflow audit and ROI modeling before a line is written</li>
                <li><span>&rarr;</span> Voice, chat, email, and case-management agents on one operating plane</li>
            </ul>
        </div>
        
        <div class="cc-srv-card">
            <div class="cc-srv-header">
                <span class="cc-srv-num">02</span>
                <h3 class="cc-srv-card-title">AI Agent Configuration & Orchestration</h3>
            </div>
            <p class="cc-srv-desc">We design, configure, and orchestrate multi-agent systems that plug into the tools you already run — Salesforce, HubSpot, NetSuite, and the legacy database nobody has the mandate to retire.</p>
            <ul class="cc-srv-list">
                <li><span>&rarr;</span> Tool-using agents grounded on your real data, not a demo dataset</li>
                <li><span>&rarr;</span> Orchestration across LLM, retrieval, and human-in-the-loop checkpoints</li>
                <li><span>&rarr;</span> Production-grade observability, evals, and safe-fail rails</li>
            </ul>
        </div>

        <div class="cc-srv-card">
            <div class="cc-srv-header">
                <span class="cc-srv-num">03</span>
                <h3 class="cc-srv-card-title">Marketing Systems & Brand Strategy Advisory</h3>
            </div>
            <p class="cc-srv-desc">Tie AI outputs to a brand strategy that compounds — pipeline-attribution, lifecycle messaging, and content engines that respect the voice of the business.</p>
            <ul class="cc-srv-list">
                <li><span>&rarr;</span> Attribution and lifecycle modeling built around your funnel reality</li>
                <li><span>&rarr;</span> Brand voice encoded into every generated asset, not just the copy</li>
                <li><span>&rarr;</span> Always-on content engines with human editorial oversight</li>
            </ul>
        </div>
    </div>
</section>
"""
    services_html = services_html.replace(services_match.group(1), new_services_html)
    write_file('services.html', services_html)

# 3. about.html
about_html = read_file('about.html')
about_match = re.search(r'(<section[^>]*>.*?Trusted by forward-thinking organizations.*?</section>)', about_html, re.DOTALL)
if about_match:
    new_about_html = """
<style>
.cc-abt-sec { padding: 100px 24px; max-width: 1000px; margin: 60px auto 0; font-family: var(--typography-font-family, sans-serif); }
.cc-abt-eyebrow { color: #007E76; font-weight: 700; letter-spacing: 0.1em; font-size: 0.875rem; text-transform: uppercase; margin-bottom: 1rem; text-align: center; }
.cc-abt-title { font-size: 2.5rem; font-weight: 800; color: #fcfcfc; text-align: center; margin-bottom: 1.5rem; line-height: 1.2; }
.cc-abt-subtitle { font-size: 1.25rem; color: #d1d5db; text-align: center; max-width: 800px; margin: 0 auto 4rem; line-height: 1.6; }
.cc-abt-step { display: flex; flex-direction: column; gap: 16px; border-bottom: 1px solid rgba(75, 85, 99, 0.4); padding-bottom: 40px; margin-bottom: 40px; }
.cc-abt-step:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0;}
.cc-abt-num { font-size: 3rem; font-weight: 800; color: #007E76; opacity: 0.8; line-height: 1;}
.cc-abt-step-title { font-size: 1.8rem; font-weight: 800; color: #fcfcfc; margin: 0 0 12px 0; }
.cc-abt-step-desc { font-size: 1.125rem; line-height: 1.7; color: #d1d5db; margin: 0;}
@media (min-width: 768px) {
    .cc-abt-title { font-size: 3.5rem; }
    .cc-abt-step { flex-direction: row; align-items: flex-start; gap: 40px; }
    .cc-abt-num { width: 80px; text-align: right; }
    .cc-abt-content { flex: 1; }
}
</style>
<section class="cc-abt-sec">
    <p class="cc-abt-eyebrow">How we work</p>
    <h2 class="cc-abt-title">From diagnosis to operating system in weeks, not quarters.</h2>
    <p class="cc-abt-subtitle">Most consultancies hand you a deck. We hand you a working production system you can defend in front of your board — and hand back the keys when you are ready.</p>
    
    <div>
        <div class="cc-abt-step">
            <span class="cc-abt-num">01</span>
            <div class="cc-abt-content">
                <h3 class="cc-abt-step-title">Diagnose</h3>
                <p class="cc-abt-step-desc">Two weeks of structured interviews with operators, CX leads, and IT. We walk out with a delivery backlog ranked by ROI, risk, and time-to-first-value.</p>
            </div>
        </div>
        
        <div class="cc-abt-step">
            <span class="cc-abt-num">02</span>
            <div class="cc-abt-content">
                <h3 class="cc-abt-step-title">Architect</h3>
                <p class="cc-abt-step-desc">A target architecture and a sequencing plan: what ships first, what integrates last, what legacy systems stay. You sign off on the blueprint before any code lands.</p>
            </div>
        </div>
        
        <div class="cc-abt-step">
            <span class="cc-abt-num">03</span>
            <div class="cc-abt-content">
                <h3 class="cc-abt-step-title">Build</h3>
                <p class="cc-abt-step-desc">A senior engineering team ships the first agentic workflow end-to-end in weeks, not quarters. You see progress weekly; every increment is production-grade, not a prototype.</p>
            </div>
        </div>
        
        <div class="cc-abt-step">
            <span class="cc-abt-num">04</span>
            <div class="cc-abt-content">
                <h3 class="cc-abt-step-title">Operate</h3>
                <p class="cc-abt-step-desc">Continuous monitoring, eval-driven iteration, and quarterly business reviews. We hand the keys back when you want them — your stack, your institutional knowledge.</p>
            </div>
        </div>
    </div>
</section>
"""
    about_html = about_html.replace(about_match.group(1), new_about_html)
    write_file('about.html', about_html)

# 4. blog.html
blog_html = read_file('blog.html')
blog_match = re.search(r'(<section[^>]*>.*?Know when to hand it off.*?</section>)', blog_html, re.DOTALL)
if blog_match:
    new_blog_html = """
<style>
.cc-blog-sec { padding: 100px 24px; max-width: 1000px; margin: 60px auto 0; font-family: var(--typography-font-family, sans-serif); }
.cc-blog-title { font-size: 2.5rem; font-weight: 800; color: #fcfcfc; text-align: center; margin-bottom: 4rem; }
.cc-blog-grid { display: grid; grid-template-columns: 1fr; gap: 32px; }
.cc-blog-card { display: block; background: #111827; border: 1px solid rgba(75, 85, 99, 0.4); border-radius: 24px; padding: 40px; text-decoration: none; transition: border-color 0.3s; cursor: pointer; }
.cc-blog-card:hover { border-color: rgba(156, 163, 175, 0.8); }
.cc-blog-date { color: #9ca3af; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 16px; display: block;}
.cc-blog-card-title { font-size: 1.8rem; font-weight: 800; color: #fcfcfc; margin: 0 0 16px 0; line-height: 1.3;}
.cc-blog-desc { font-size: 1.125rem; line-height: 1.7; color: #d1d5db; margin: 0 0 24px 0; }
.cc-blog-link { color: #007E76; font-weight: 700; }
@media (min-width: 768px) {
    .cc-blog-title { font-size: 3.5rem; }
    .cc-blog-grid { grid-template-columns: 1fr 1fr; }
}
</style>
<section class="cc-blog-sec">
    <h2 class="cc-blog-title">Insights & Analysis</h2>
    <div class="cc-blog-grid">
        <a href="blog-support-automation.html" class="cc-blog-card">
            <span class="cc-blog-date">August 2, 2026</span>
            <h3 class="cc-blog-card-title">Support Automation That Doesn't Feel Like a Machine</h3>
            <p class="cc-blog-desc">The rush to implement AI in customer support has led to a predictable problem: terrible customer experiences. Effective AI agents are designed for resolution, not deflection.</p>
            <span class="cc-blog-link">Read more &rarr;</span>
        </a>
        
        <a href="blog-ai-readiness.html" class="cc-blog-card">
            <span class="cc-blog-date">August 1, 2026</span>
            <h3 class="cc-blog-card-title">5 Signs Your Business Is Ready for AI Automation</h3>
            <p class="cc-blog-desc">Artificial Intelligence is no longer just for enterprise tech companies. Mid-market businesses are scaling rapidly with custom AI. Here are the 5 signs you are outgrowing manual processes.</p>
            <span class="cc-blog-link">Read more &rarr;</span>
        </a>
    </div>
</section>
"""
    blog_html = blog_html.replace(blog_match.group(1), new_blog_html)
    write_file('blog.html', blog_html)

print("Injections successful with premium styles!")
