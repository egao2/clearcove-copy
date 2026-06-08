import os
import glob

html_files = glob.glob('*.html')
skip_files = ['site_index.html', 'site_services.html']

for file in html_files:
    if file in skip_files:
        continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already injected
    if 'premium.css' in content:
        continue

    # Inject CSS before </head>
    head_tag = '</head>'
    if head_tag in content:
        content = content.replace(head_tag, '<link rel="stylesheet" href="premium.css">\n</head>')
    
    # Inject JS before </body>
    body_tag = '</body>'
    if body_tag in content:
        content = content.replace(body_tag, '<script src="premium.js"></script>\n</body>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Injected premium styles and scripts into {file}")

