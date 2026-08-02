import re

with open('about.html', 'r') as f:
    html = f.read()

# Replace the testimonials section in about.html with the new framework
about_hero_match = re.search(r'(<section[^>]*>.*?Trusted by forward-thinking organizations.*?</section>)', html, re.DOTALL)
if about_hero_match:
    new_about_hero = """
    <section class="py-24 px-6 sm:px-8 max-w-6xl mx-auto relative z-10" style="margin-top: 60px;">
        <p class="text-[var(--primary-color)] font-bold tracking-widest text-sm uppercase mb-4" style="color: #007E76; text-align: center;">How we work</p>
        <h2 class="text-4xl md:text-5xl font-bold mb-6" style="color: #fcfcfc; text-align: center;">From diagnosis to operating system in weeks, not quarters.</h2>
        <p class="text-xl text-center max-w-3xl mx-auto mb-16" style="color: #d1d5db;">Most consultancies hand you a deck. We hand you a working production system you can defend in front of your board — and hand back the keys when you are ready.</p>
        
        <div class="grid grid-cols-1 gap-8">
            <!-- 01 -->
            <div class="flex flex-col md:flex-row gap-8 items-start border-b border-gray-700 pb-8">
                <span class="text-5xl font-bold md:w-24 text-right" style="color: #007E76; opacity: 0.8;">01</span>
                <div>
                    <h3 class="text-2xl font-bold mb-3" style="color: #fcfcfc;">Diagnose</h3>
                    <p class="text-lg leading-relaxed" style="color: #d1d5db;">Two weeks of structured interviews with operators, CX leads, and IT. We walk out with a delivery backlog ranked by ROI, risk, and time-to-first-value.</p>
                </div>
            </div>
            
            <!-- 02 -->
            <div class="flex flex-col md:flex-row gap-8 items-start border-b border-gray-700 pb-8">
                <span class="text-5xl font-bold md:w-24 text-right" style="color: #007E76; opacity: 0.8;">02</span>
                <div>
                    <h3 class="text-2xl font-bold mb-3" style="color: #fcfcfc;">Architect</h3>
                    <p class="text-lg leading-relaxed" style="color: #d1d5db;">A target architecture and a sequencing plan: what ships first, what integrates last, what legacy systems stay. You sign off on the blueprint before any code lands.</p>
                </div>
            </div>
            
            <!-- 03 -->
            <div class="flex flex-col md:flex-row gap-8 items-start border-b border-gray-700 pb-8">
                <span class="text-5xl font-bold md:w-24 text-right" style="color: #007E76; opacity: 0.8;">03</span>
                <div>
                    <h3 class="text-2xl font-bold mb-3" style="color: #fcfcfc;">Build</h3>
                    <p class="text-lg leading-relaxed" style="color: #d1d5db;">A senior engineering team ships the first agentic workflow end-to-end in weeks, not quarters. You see progress weekly; every increment is production-grade, not a prototype.</p>
                </div>
            </div>
            
            <!-- 04 -->
            <div class="flex flex-col md:flex-row gap-8 items-start pb-8">
                <span class="text-5xl font-bold md:w-24 text-right" style="color: #007E76; opacity: 0.8;">04</span>
                <div>
                    <h3 class="text-2xl font-bold mb-3" style="color: #fcfcfc;">Operate</h3>
                    <p class="text-lg leading-relaxed" style="color: #d1d5db;">Continuous monitoring, eval-driven iteration, and quarterly business reviews. We hand the keys back when you want them — your stack, your institutional knowledge.</p>
                </div>
            </div>
        </div>
    </section>
    """
    html = html.replace(about_hero_match.group(1), new_about_hero)
    with open('about.html', 'w') as f:
        f.write(html)
    print('About page updated with framework!')
else:
    print('Could not find section')
