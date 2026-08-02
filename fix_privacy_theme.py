import glob

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    # 1. Update JSON schema globally
    old_schema_text = "Led by a Senior Platform Architect at Zendesk"
    new_schema_text = "Founded by a veteran enterprise architect"
    if old_schema_text in html:
        html = html.replace(old_schema_text, new_schema_text)
    
    # 2. Update about.html specifically for the Founder note and colors
    if file == 'about.html':
        # Remove hardcoded background colors to inherit theme
        html = html.replace('background-color: #0b1120;', 'background-color: transparent;')
        
        # Change card background to match Durable theme (#19212B or transparent)
        html = html.replace('background-color: #111827;', 'background-color: rgba(25, 33, 43, 0.6);')
        
        # Change the founder title
        html = html.replace('<div class="cc-founder-title">Senior Platform Architect, Zendesk</div>', '')
        
        # Maybe change author to "Founder & Principal Architect"
        html = html.replace('<div class="cc-founder-author">Founder</div>', '<div class="cc-founder-author">Founder & Principal Architect</div>')
        
    with open(file, 'w') as f:
        f.write(html)

print("Updated schema and about.html theme + privacy settings.")
