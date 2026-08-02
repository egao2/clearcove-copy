import re

with open('index.html', 'r') as f:
    html = f.read()

# Find the case study
case_study_match = re.search(r'(<style>\s*\.cc-case-study-sec.*?</style>\s*<section class="cc-case-study-sec">.*?</section>)', html, re.DOTALL)
if case_study_match:
    case_study_html = case_study_match.group(1)
    
    # Remove from current location
    html = html.replace(case_study_html, '')
    
    # Find testimonial section (id="44ead0ce-9a25-4d04-b400-b3f2c2e7dc41" or "Organizations trust ClearCove")
    testimonial_match = re.search(r'(<div class="w-full" id="[^"]*">\s*<section[^>]*>.*?Organizations trust ClearCove.*?</section>)', html, re.DOTALL)
    if not testimonial_match:
        # Fallback search
        testimonial_match = re.search(r'(<div[^>]*>.*?Organizations trust ClearCove.*?</section>\s*</div>)', html, re.DOTALL)
        
    if testimonial_match:
        # We need to find the START of the testimonial section. The match group starts with <div class="w-full" ...
        # Let's just find the index of "Organizations trust ClearCove" and then find the preceding <div class="w-full"
        idx = html.find('Organizations trust ClearCove')
        if idx != -1:
            # Find the preceding <div class="w-full"
            div_idx = html.rfind('<div class="w-full"', 0, idx)
            if div_idx != -1:
                # Inject case study right before this div
                html = html[:div_idx] + case_study_html + "\n" + html[div_idx:]
                print("Successfully moved case study")
            else:
                print("Could not find preceding div")
        else:
            print("Could not find text 'Organizations trust ClearCove'")
    else:
        print("Could not find testimonial match")
else:
    print("Could not find case study")

with open('index.html', 'w') as f:
    f.write(html)
