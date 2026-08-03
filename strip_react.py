import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    # Remove all self.__next_f scripts
    html = re.sub(r'<script>self\.__next_f.*?<\/script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script>\(self\.__next_f=self\.__next_f\|\|\[\]\)\.push\(\[0\]\)<\/script>', '', html, flags=re.DOTALL)
    
    # Remove Next.js chunks in <head>
    html = re.sub(r'<script src=\"_next\/static\/chunks\/.*?<\/script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<link rel=\"preload\" href=\"_next\/static\/chunks\/.*?/>', '', html, flags=re.DOTALL)
    
    with open(file, 'w') as f:
        f.write(html)

print("Removed React hydration from all HTML files.")
