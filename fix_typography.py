with open('contact.html', 'r') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<div class="w-full" id="contact-form">' in line:
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if '</div></main><div class="w-full" id="footer-logo-nav">' in lines[i]:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_html = """<div class="w-full" id="contact-form">
    <section class="w-full relative py-20" style="background-color: #19212B; padding-top: 5rem; padding-bottom: 5rem;">
      <div class="relative mx-auto max-w-[1536px] px-6 flex flex-col gap-12 items-center justify-center text-center">
        
        <div class="flex flex-col max-w-3xl items-center gap-6">
            <h2 class="[font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
style="--typography-font-size: var(--typography-display-sm-font-size);--typography-font-weight: var(--typography-display-sm-font-weight);--typography-line-height: var(--typography-display-sm-line-height);--typography-letter-spacing: var(--typography-display-sm-letter-spacing);--typography-font-family: var(--typography-display-sm-font-family);color: #f9f9f9; margin-bottom: 1.5rem;">
                Engage with ClearCove
            </h2>
            <p class="whitespace-pre-line [font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
style="--typography-font-size: var(--typography-body-lg-font-size);--typography-font-weight: var(--typography-body-lg-font-weight);--typography-line-height: var(--typography-body-lg-line-height);--typography-letter-spacing: var(--typography-body-lg-letter-spacing);--typography-font-family: var(--typography-body-lg-font-family);color: #dfdfdf;">
                Skip the traditional forms. Connect with our AI Solutions Advisor instantly or schedule a direct consultation with our architects.
            </p>
        </div>

        <div class="w-full" style="display: grid; gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 1000px;">
            
            <!-- Card 1: AI Agent -->
            <div class="flex flex-col items-center justify-center p-10 rounded-3xl" style="background-color: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 3rem; border-radius: 1.5rem;">
                <div class="w-16 h-16 rounded-full flex items-center justify-center mb-6" style="background-color: rgba(47, 163, 154, 0.2); width: 4rem; height: 4rem; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#2FA39A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                    </svg>
                </div>
                <h3 class="[font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
style="--typography-font-size: var(--typography-heading-sm-font-size);--typography-font-weight: var(--typography-heading-sm-font-weight);--typography-line-height: var(--typography-heading-sm-line-height);--typography-letter-spacing: var(--typography-heading-sm-letter-spacing);--typography-font-family: var(--typography-heading-sm-font-family);color: #fcfcfc; margin-bottom: 1rem;">Chat with Alex</h3>
                <p class="whitespace-pre-line [font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
style="--typography-font-size: var(--typography-body-md-font-size);--typography-font-weight: var(--typography-body-md-font-weight);--typography-line-height: var(--typography-body-md-line-height);--typography-letter-spacing: var(--typography-body-md-letter-spacing);--typography-font-family: var(--typography-body-md-font-family);color: #a0a0a0; text-align: center; margin-bottom: 2rem;">
                    Our AI Concierge is available 24/7 to answer your questions, explain our automation services, and guide you to the right solution.
                </p>
                
                <button
                  onclick="document.querySelector('#cc-bubble') ? document.querySelector('#cc-bubble').click() : window.dispatchEvent(new CustomEvent('open-cc-widget'))"
                  data-slot="button"
                  style="
                    --bg-color: rgba(0, 126, 118, 0.6);
                    --hover-bg-color: #00766f;
                    color: #fcfcfc;
                    backdrop-filter: blur(16px);
                    -webkit-backdrop-filter: blur(16px);
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 9999px;
                    border: 1px solid rgba(0, 126, 118, 0.6);
                    padding: 0.75rem 2rem;
                    transition: all 0.2s;
                  "
                  class="bg-(--bg-color) hover:bg-(--hover-bg-color)"
                >
                  <span
                    class="[font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
                    style="
                      --typography-font-size: var(--typography-body-sm-em-font-size);
                      --typography-font-weight: var(--typography-body-sm-em-font-weight);
                      --typography-line-height: var(--typography-body-sm-em-line-height);
                      --typography-letter-spacing: var(--typography-body-sm-em-letter-spacing);
                      --typography-font-family: var(--typography-body-sm-em-font-family);
                      color: #fcfcfc;
                    "
                  >Start Conversation</span>
                </button>
            </div>

            <!-- Card 2: Book Call -->
            <div class="flex flex-col items-center justify-center p-10 rounded-3xl" style="background-color: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 3rem; border-radius: 1.5rem;">
                <div class="w-16 h-16 rounded-full flex items-center justify-center mb-6" style="background-color: rgba(255, 255, 255, 0.05); width: 4rem; height: 4rem; border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#fcfcfc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                </div>
                <h3 class="[font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
style="--typography-font-size: var(--typography-heading-sm-font-size);--typography-font-weight: var(--typography-heading-sm-font-weight);--typography-line-height: var(--typography-heading-sm-line-height);--typography-letter-spacing: var(--typography-heading-sm-letter-spacing);--typography-font-family: var(--typography-heading-sm-font-family);color: #fcfcfc; margin-bottom: 1rem;">Schedule Consultation</h3>
                <p class="whitespace-pre-line [font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
style="--typography-font-size: var(--typography-body-md-font-size);--typography-font-weight: var(--typography-body-md-font-weight);--typography-line-height: var(--typography-body-md-line-height);--typography-letter-spacing: var(--typography-body-md-letter-spacing);--typography-font-family: var(--typography-body-md-font-family);color: #a0a0a0; text-align: center; margin-bottom: 2rem;">
                    Ready to architect your AI advantage? Book a direct discovery call with our solutions team to discuss your operational bottlenecks.
                </p>
                
                <a
                  href="https://calendar.app.google/mCDenTF29rv4Zzb18" target="_blank" rel="noopener noreferrer"
                  data-slot="button"
                  style="
                    --bg-color: transparent;
                    --hover-bg-color: rgba(255, 255, 255, 0.1);
                    color: #fcfcfc;
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 9999px;
                    border: 1px solid #fcfcfc;
                    padding: 0.75rem 2rem;
                    text-decoration: none;
                    transition: all 0.2s;
                  "
                  class="bg-(--bg-color) hover:bg-(--hover-bg-color)"
                >
                  <span
                    class="[font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
                    style="
                      --typography-font-size: var(--typography-body-sm-em-font-size);
                      --typography-font-weight: var(--typography-body-sm-em-font-weight);
                      --typography-line-height: var(--typography-body-sm-em-line-height);
                      --typography-letter-spacing: var(--typography-body-sm-em-letter-spacing);
                      --typography-font-family: var(--typography-body-sm-em-font-family);
                      color: #fcfcfc;
                    "
                  >View Calendar</span>
                </a>
            </div>

        </div>

        <div class="mt-12 text-center" style="margin-top: 3rem; text-align: center;">
            <p class="whitespace-pre-line [font-family:var(--typography-font-family)] [font-size:var(--typography-font-size)] leading-(--typography-line-height) font-(--typography-font-weight) tracking-(--typography-letter-spacing)"
style="--typography-font-size: var(--typography-body-sm-font-size);--typography-font-weight: var(--typography-body-sm-font-weight);--typography-line-height: var(--typography-body-sm-line-height);--typography-letter-spacing: var(--typography-body-sm-letter-spacing);--typography-font-family: var(--typography-body-sm-font-family);color: #646464;">
                Prefer email? Reach us directly at <a href="mailto:hello@clearcove.co" style="color: #2FA39A; text-decoration: none;">hello@clearcove.co</a>
            </p>
        </div>

      </div>
    </section>
</div></main>"""

    original_end_line = lines[end_idx] # Contains: </div></main><div class="w-full" id="footer-logo-nav"><style>\n
    # We want to replace from start_idx up to the </div></main> part.
    # We can just split original_end_line at </div></main>
    split_parts = original_end_line.split('</div></main>')
    if len(split_parts) > 1:
        reconstructed_end = split_parts[1]
    else:
        reconstructed_end = original_end_line # fallback

    new_content = "".join(lines[:start_idx]) + new_html + reconstructed_end + "".join(lines[end_idx+1:])
    with open('contact.html', 'w') as f:
        f.write(new_content)
    print("Updated successfully")
else:
    print(f"Failed to find bounds. start: {start_idx}, end: {end_idx}")
