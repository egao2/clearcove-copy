import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the old premium.css with a versioned one
    # Also handle if it already has ?v=1 or something
    import re
    new_content = re.sub(r'premium\.css(\?v=\d+)?', 'premium.css?v=2', content)
    new_content = re.sub(r'premium\.js(\?v=\d+)?', 'premium.js?v=2', new_content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
