import glob

old_text = 'ClearCove is a technology consulting firm based in New York City that is currently just starting out. Led by a former Senior Platform Architect at Zendesk'
new_text = 'We bridge the gap between bleeding-edge AI models and practical, ROI-driven business operations. No hype. Just execution. Led by a Senior Platform Architect at Zendesk'

files_updated = 0

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    if old_text in html:
        html = html.replace(old_text, new_text)
        
        # In case there are isolated instances of "former Senior Platform"
        html = html.replace('former Senior Platform Architect', 'Senior Platform Architect')
        
        with open(file, 'w') as f:
            f.write(html)
        files_updated += 1
    else:
        # Fallback: Just replace the 'former' part if the full string didn't match perfectly
        if 'former Senior Platform Architect' in html:
            html = html.replace('former Senior Platform Architect', 'Senior Platform Architect')
            with open(file, 'w') as f:
                f.write(html)
            files_updated += 1

print(f"Updated JSON schema in {files_updated} files.")
