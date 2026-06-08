import re
import json

with open('site_services.html', 'r') as f:
    text = f.read()

# Find the JSON part
match = re.search(r'Integrated CX Strategy.*?("image":\{"src":"[^"]+")', text)
if match:
    print("Found JSON match:", match.group(1))

# Find the next image URL directly after the text
idx = text.find('Integrated CX Strategy')
if idx != -1:
    img_idx = text.find('http', idx-200)
    print("Found URL around text:", text[img_idx:img_idx+150])
