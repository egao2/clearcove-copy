import glob

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    # Revert the naive global replacement
    html = html.replace('class="w-full cc-fade-up"', 'class="w-full"')
    html = html.replace('class="w-full relative cc-fade-up"', 'class="w-full relative"')
    html = html.replace('class="group w-full cc-fade-up"', 'class="group w-full"')
    html = html.replace('class="group w-full relative cc-fade-up"', 'class="group w-full relative"')
    
    # Revert any cc-fade-up cc-fade-up duplicates that might have happened
    html = html.replace('cc-fade-up cc-fade-up', 'cc-fade-up')
    
    # Now specifically target ONLY <section> tags
    html = html.replace('<section class="w-full"', '<section class="w-full cc-fade-up"')
    html = html.replace('<section class="w-full relative"', '<section class="w-full relative cc-fade-up"')
    
    # The header itself should definitely NOT have cc-fade-up to preserve position:fixed
    # If any header got it, remove it
    html = html.replace('<header class="w-full relative z-50 cc-fade-up"', '<header class="w-full relative z-50"')
    html = html.replace('<header class="w-full cc-fade-up"', '<header class="w-full"')
    
    with open(file, 'w') as f:
        f.write(html)

print("Fixed header layout issue by scoping animations only to section tags.")
