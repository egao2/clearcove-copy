import re
import urllib.parse

with open('site_services.html', 'r') as f:
    text = f.read()

# Find the string "Integrated CX Strategy"
idx = text.find('Integrated CX Strategy')
# Search around it for the nearest image src. Since it's in HTML, we should find the `<img>` tag before it.
img_idx = text.rfind('<img', 0, idx)
end_img = text.find('>', img_idx)
img_tag = text[img_idx:end_img+1]

# Extract src
src_match = re.search(r'src="([^"]+)"', img_tag)
if src_match:
    src = src_match.group(1)
    if '_next/image?url=' in src:
        url_encoded = src.split('url=')[1].split('&')[0]
        url = urllib.parse.unquote(url_encoded)
        print("Integrated CX Strategy image URL:", url)

# Now do the same for "AI Agent Configuration" in index.html
with open('site_index.html', 'r') as f:
    text2 = f.read()
idx2 = text2.find('AI Agent Configuration')
img_idx2 = text2.rfind('<img', 0, idx2)
end_img2 = text2.find('>', img_idx2)
img_tag2 = text2[img_idx2:end_img2+1]

src_match2 = re.search(r'src="([^"]+)"', img_tag2)
if src_match2:
    src2 = src_match2.group(1)
    if '_next/image?url=' in src2:
        url_encoded2 = src2.split('url=')[1].split('&')[0]
        url2 = urllib.parse.unquote(url_encoded2)
        print("AI Agent Configuration image URL:", url2)

