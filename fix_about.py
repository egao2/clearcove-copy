with open('about.html', 'r') as f:
    html = f.read()

# Replace "former Senior Platform Architect" with "Senior Platform Architect"
html = html.replace('former Senior Platform Architect', 'Senior Platform Architect')

with open('about.html', 'w') as f:
    f.write(html)
print("Removed 'former' from about.html")
