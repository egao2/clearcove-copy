import re

with open('services.html', 'r') as f:
    html = f.read()

# Find the section containing the services (look for Workflow Automation)
services_section_match = re.search(r'(<section[^>]*>.*?Workflow Automation.*?</section>)', html, re.DOTALL)
if services_section_match:
    new_services_section = """
    <section class="py-24 px-6 sm:px-8 max-w-6xl mx-auto relative z-10" style="margin-top: 60px;">
        <p class="text-[var(--primary-color)] font-bold tracking-widest text-sm uppercase mb-4" style="color: #007E76; text-align: center;">Three Service Pillars</p>
        <h2 class="text-4xl md:text-5xl font-bold mb-16" style="color: #fcfcfc; text-align: center;">What we actually deliver.</h2>
        
        <div class="grid grid-cols-1 gap-12">
            <!-- Pillar 1 -->
            <div class="p-10 rounded-3xl border border-gray-700/50 hover:border-gray-500 transition-colors bg-[var(--bg-color-alt)]" style="background-color: #111827;">
                <div class="flex items-center gap-6 mb-6">
                    <span class="text-5xl font-bold" style="color: #007E76; opacity: 0.8;">01</span>
                    <h3 class="text-3xl font-bold" style="color: #fcfcfc;">Intelligent CX Strategy & Business Operations</h3>
                </div>
                <p class="leading-relaxed mb-8 text-lg" style="color: #d1d5db;">Translate customer experience briefs and back-office processes into measurable, AI-native operating models — not slides that age on a shelf.</p>
                <ul class="space-y-4" style="color: #9ca3af;">
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Customer journey mapping scored against automatable moments</li>
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Back-office workflow audit and ROI modeling before a line is written</li>
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Voice, chat, email, and case-management agents on one operating plane</li>
                </ul>
            </div>
            
            <!-- Pillar 2 -->
            <div class="p-10 rounded-3xl border border-gray-700/50 hover:border-gray-500 transition-colors bg-[var(--bg-color-alt)]" style="background-color: #111827;">
                <div class="flex items-center gap-6 mb-6">
                    <span class="text-5xl font-bold" style="color: #007E76; opacity: 0.8;">02</span>
                    <h3 class="text-3xl font-bold" style="color: #fcfcfc;">AI Agent Configuration & Orchestration</h3>
                </div>
                <p class="leading-relaxed mb-8 text-lg" style="color: #d1d5db;">We design, configure, and orchestrate multi-agent systems that plug into the tools you already run — Salesforce, HubSpot, NetSuite, and the legacy database nobody has the mandate to retire.</p>
                <ul class="space-y-4" style="color: #9ca3af;">
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Tool-using agents grounded on your real data, not a demo dataset</li>
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Orchestration across LLM, retrieval, and human-in-the-loop checkpoints</li>
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Production-grade observability, evals, and safe-fail rails</li>
                </ul>
            </div>

            <!-- Pillar 3 -->
            <div class="p-10 rounded-3xl border border-gray-700/50 hover:border-gray-500 transition-colors bg-[var(--bg-color-alt)]" style="background-color: #111827;">
                <div class="flex items-center gap-6 mb-6">
                    <span class="text-5xl font-bold" style="color: #007E76; opacity: 0.8;">03</span>
                    <h3 class="text-3xl font-bold" style="color: #fcfcfc;">Marketing Systems & Brand Strategy Advisory</h3>
                </div>
                <p class="leading-relaxed mb-8 text-lg" style="color: #d1d5db;">Tie AI outputs to a brand strategy that compounds — pipeline-attribution, lifecycle messaging, and content engines that respect the voice of the business.</p>
                <ul class="space-y-4" style="color: #9ca3af;">
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Attribution and lifecycle modeling built around your funnel reality</li>
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Brand voice encoded into every generated asset, not just the copy</li>
                    <li class="flex items-start gap-3"><span style="color: #007E76;">&rarr;</span> Always-on content engines with human editorial oversight</li>
                </ul>
            </div>
        </div>
    </section>
    """
    html = html.replace(services_section_match.group(1), new_services_section)
    with open('services.html', 'w') as f:
        f.write(html)
    print("Services page updated!")
else:
    print("Could not find services section")
