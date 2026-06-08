import re
import urllib.parse
import os

with open('site_services.html', 'r') as f:
    text = f.read()

# 1. Digital globe (corresponds to img_11.jpg and img_202.jpg)
globe_match = re.search(r'alt="Digital globe visualization[^>]+srcSet="/_next/image\?url=([^&]+)', text)
if globe_match:
    globe_url = urllib.parse.unquote(globe_match.group(1))
    print("Globe URL:", globe_url)
    os.system(f'curl -s -o _next/img_11.jpg "{globe_url}"')
    os.system(f'cp _next/img_11.jpg _next/img_202.jpg')

# 2. Isometric 3D (corresponds to img_114.png and img_41.png)
iso_match = re.search(r'alt="Isometric 3D visualization[^>]+srcSet="/_next/image\?url=([^&]+)', text)
if iso_match:
    iso_url = urllib.parse.unquote(iso_match.group(1))
    print("Isometric URL:", iso_url)
    os.system(f'curl -s -o _next/img_114.png "{iso_url}"')
    os.system(f'cp _next/img_114.png _next/img_41.png')

