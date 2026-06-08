import urllib.request
import re

html = urllib.request.urlopen('https://clearcove.durable.site').read().decode('utf-8')
services_html = urllib.request.urlopen('https://clearcove.durable.site/services').read().decode('utf-8')

def find_images(text, pattern):
    matches = list(re.finditer(pattern, text))
    if not matches:
        return
    for match in matches:
        idx = match.start()
        # Find the previous <img> tag
        img_idx = text.rfind('<img', 0, idx)
        if img_idx != -1:
            end_img = text.find('>', img_idx)
            print("Found image for", pattern, ":", text[img_idx:end_img+1])

find_images(html, r"AI Agent Configuration")
find_images(services_html, r"Integrated CX")
find_images(services_html, r"Intelligent CX")
find_images(services_html, r"CX Strategy")
