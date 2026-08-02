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
    # We will find the secondary CTA, and then find the next </section> tag.
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

with open('index.html', 'w') as f:
    f.write(html)
