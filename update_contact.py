import re

with open('contact.html', 'r') as f:
    content = f.read()

# We want to replace the div with id="contact-form" entirely.
# A regex to match id="contact-form" and its balanced div is tricky.
# Let's use a simpler approach. Since we know the HTML, we can find:
# <div class="w-full" id="contact-form"> ... </section></div>
# Wait, let's just find the start of the form section and end of it.

start_str = '<div class="w-full" id="contact-form">'
end_str = '</form></div></div></section></div>'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    end_idx += len(end_str)
    
    new_html = """<div class="w-full" id="contact-form">
    <section class="w-full relative py-20" style="background-color: #19212B;">
      <div class="relative mx-auto max-w-5xl px-6 flex flex-col gap-12 items-center justify-center text-center">
        
        <div class="flex flex-col max-w-3xl items-center gap-6">
            <h2 class="text-4xl md:text-5xl font-bold tracking-tight" style="color: #fcfcfc; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">
                Engage with ClearCove
            </h2>
            <p class="text-lg md:text-xl text-gray-300" style="color: #dfdfdf; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">
                Skip the traditional forms. Connect with our AI Solutions Advisor instantly or schedule a direct consultation with our architects.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 w-full">
            
            <!-- Card 1: AI Agent -->
            <div class="flex flex-col items-center justify-center p-10 rounded-3xl" style="background-color: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);">
                <div class="w-16 h-16 rounded-full flex items-center justify-center mb-6" style="background-color: rgba(47, 163, 154, 0.2);">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#2FA39A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                    </svg>
                </div>
                <h3 class="text-2xl font-semibold mb-4" style="color: #fcfcfc; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">Chat with Alex</h3>
                <p class="text-center mb-8" style="color: #a0a0a0; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">
                    Our AI Concierge is available 24/7 to answer your questions, explain our automation services, and guide you to the right solution.
                </p>
                <button onclick="document.querySelector('#cc-bubble') ? document.querySelector('#cc-bubble').click() : window.dispatchEvent(new CustomEvent('open-cc-widget'))" class="px-8 py-3 rounded-full font-semibold transition-all" style="background-color: #2FA39A; color: #19212B; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif); box-shadow: 0 4px 14px rgba(47, 163, 154, 0.4);">
                    Start Conversation
                </button>
            </div>

            <!-- Card 2: Book Call -->
            <div class="flex flex-col items-center justify-center p-10 rounded-3xl" style="background-color: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);">
                <div class="w-16 h-16 rounded-full flex items-center justify-center mb-6" style="background-color: rgba(255, 255, 255, 0.05);">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#fcfcfc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                </div>
                <h3 class="text-2xl font-semibold mb-4" style="color: #fcfcfc; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">Schedule Consultation</h3>
                <p class="text-center mb-8" style="color: #a0a0a0; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">
                    Ready to architect your AI advantage? Book a direct discovery call with our solutions team to discuss your operational bottlenecks.
                </p>
                <a href="https://calendar.app.google/mCDenTF29rv4Zzb18" target="_blank" rel="noopener noreferrer" class="px-8 py-3 rounded-full font-semibold transition-all hover:bg-white hover:text-black" style="background-color: transparent; border: 1px solid #fcfcfc; color: #fcfcfc; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">
                    View Calendar
                </a>
            </div>

        </div>

        <div class="mt-12 text-center">
            <p class="text-sm" style="color: #646464; font-family: var(--typography-font-family, 'Space Grotesk', sans-serif);">
                Prefer email? Reach us directly at <a href="mailto:hello@clearcove.co" style="color: #2FA39A; text-decoration: none;">hello@clearcove.co</a>
            </p>
        </div>

      </div>
    </section>
</div>"""
    
    new_content = content[:start_idx] + new_html + content[end_idx:]
    with open('contact.html', 'w') as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print("Could not find start/end strings. Form replacement failed.")
