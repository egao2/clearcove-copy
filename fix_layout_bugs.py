import re

# 1. Fix about.html missing </style> tag
with open('about.html', 'r') as f:
    about_html = f.read()

# Check if </style> is missing before <div class="cc-about-page">
if '</style>\n<div class="cc-about-page">' not in about_html:
    about_html = about_html.replace('<div class="cc-about-page">', '</style>\n<div class="cc-about-page">')
    with open('about.html', 'w') as f:
        f.write(about_html)
    print("Fixed missing </style> in about.html")
else:
    print("</style> was already present in about.html")

# 2. Fix index.html button size
with open('index.html', 'r') as f:
    index_html = f.read()

# The second button has padding: 12px 26px; ... font-size: 1rem;
# Let's just do a string replace to match the first button
old_btn = 'padding: 12px 26px; border-radius: 9999px; font-weight: 700; text-decoration: none; font-size: 1rem;'
new_btn = 'padding: 14px 28px; border-radius: 9999px; font-weight: 700; text-decoration: none; font-size: 1.125rem;'
if old_btn in index_html:
    index_html = index_html.replace(old_btn, new_btn)
    with open('index.html', 'w') as f:
        f.write(index_html)
    print("Fixed button size in index.html")
else:
    print("Could not find old button CSS string in index.html")

