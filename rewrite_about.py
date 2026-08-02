import re

with open('about.html', 'r') as f:
    html = f.read()

# 1. Remove "former" from the JSON schema
html = html.replace('Led by a former Senior Platform Architect', 'Led by a Senior Platform Architect')

# 2. Rewrite Hero Text
old_hero = 'ClearCove is a technology consulting firm based in New York City that is currently just starting out.'
new_hero = 'We bridge the gap between bleeding-edge AI models and practical, ROI-driven business operations. No hype. Just execution.'
html = html.replace(old_hero, new_hero)

# 3. Rewrite "How it Works" Steps
# Old Step 1
old_step1_title = 'Define the Challenge'
new_step1_title = '1. Process Diagnostics'
html = html.replace(old_step1_title, new_step1_title)

old_step1_desc = 'We start by understanding your specific business needs, operational bottlenecks, and long-term goals to identify the highest-impact areas for AI integration.'
new_step1_desc = 'We deep-dive into your existing architecture and workflows, identifying exactly where manual processes are bottlenecking revenue.'
html = html.replace(old_step1_desc, new_step1_desc)

# Old Step 2
old_step2_title = 'Architect the Solution'
new_step2_title = '2. AI Tool-chaining'
html = html.replace(old_step2_title, new_step2_title)

old_step2_desc = 'Our team designs a tailored strategy, selecting the right technologies and configuring custom AI agents to seamlessly integrate with your existing workflows.'
new_step2_desc = 'We architect robust, scalable integrations that connect advanced LLMs directly to your CRM, support ticketing, or marketing databases.'
html = html.replace(old_step2_desc, new_step2_desc)

# Old Step 3
old_step3_title = 'Deploy and Scale'
new_step3_title = '3. Human-in-the-loop Handoff'
html = html.replace(old_step3_title, new_step3_title)

old_step3_desc = 'We implement the solution with a focus on smooth adoption, providing ongoing support and optimization to ensure your systems scale efficiently as your business grows.'
new_step3_desc = 'We deploy the agents with strict guardrails, ensuring that AI handles the heavy lifting while seamlessly escalating high-value decisions back to your human team.'
html = html.replace(old_step3_desc, new_step3_desc)

# 4. Inject Founder's Note
# We will inject this right before the "How it Works" section.
# The "How it Works" section has an id like id="how-it-works" or similar. We can search for the text "How it Works".
founder_css = """
<style>
.cc-founder-sec {
    padding: 100px 24px;
    background-color: #0b1120;
    color: #fcfcfc;
    font-family: var(--typography-font-family, system-ui, sans-serif);
    text-align: center;
}
.cc-founder-container {
    max-width: 800px;
    margin: 0 auto;
    background-color: #111827;
    padding: 60px 40px;
    border-radius: 24px;
    border: 1px solid rgba(0, 126, 118, 0.3);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    position: relative;
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
</style>
"""

founder_html = founder_css + """
<section class="cc-founder-sec">
    <div class="cc-founder-container">
        <p class="cc-founder-quote">"Enterprise software used to take months to build. With modern AI orchestration, what used to take teams of engineers can now be deployed in weeks. But scaling it requires deep architectural discipline. That's why ClearCove exists."</p>
        <div class="cc-founder-author">Founder</div>
        <div class="cc-founder-title">Senior Platform Architect, Zendesk</div>
    </div>
</section>
"""

# Find "How it works" or something before it to inject.
# Let's search for the start of the section that contains "1. Process Diagnostics" (formerly "Define the Challenge")
step_idx = html.find('1. Process Diagnostics')
if step_idx != -1:
    div_idx = html.rfind('<div class="w-full"', 0, step_idx)
    if div_idx != -1:
        html = html[:div_idx] + founder_html + "\n" + html[div_idx:]
        print("Injected Founder Note")
    else:
        print("Could not find div for founder note")
else:
    print("Could not find step 1")

with open('about.html', 'w') as f:
    f.write(html)
print("Updated about.html")
