import re

with open('pricing.html', 'r') as f:
    html = f.read()

# Replace tier 3 title
html = html.replace('Flexible AI Advisory', 'Marketing &amp; Brand Systems')
# Replace tier 3 description
old_desc = 'Ongoing, high-level technical strategy and architectural oversight for organizations scaling custom AI applications.'
new_desc = 'Ongoing lifecycle modeling, attribution tracking, and brand-encoded content engines to drive pipeline.'
html = html.replace(old_desc, new_desc)

# Replace tier 3 bullets
old_bullet_1 = 'Dedicated monthly architectural review hours'
new_bullet_1 = 'Attribution and lifecycle modeling'
html = html.replace(old_bullet_1, new_bullet_1)

old_bullet_2 = 'Technical feasibility studies and MVP prototyping'
new_bullet_2 = 'Brand voice encoded into every asset'
html = html.replace(old_bullet_2, new_bullet_2)

old_bullet_3 = 'Scalability, security, and performance guidance'
new_bullet_3 = 'Always-on human-reviewed content engines'
html = html.replace(old_bullet_3, new_bullet_3)

old_bullet_4 = 'Priority access to our Lead Architect'
new_bullet_4 = 'Priority access to our Lead Strategist'
html = html.replace(old_bullet_4, new_bullet_4)

with open('pricing.html', 'w') as f:
    f.write(html)
print("Updated pricing.html")
