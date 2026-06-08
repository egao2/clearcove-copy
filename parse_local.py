import re

with open('services.html', 'r') as f:
    text = f.read()

idx = text.find('Integrated CX Strategy')
img_idx = text.rfind('<img', 0, idx)
end_img = text.find('>', img_idx)
img_tag = text[img_idx:end_img+1]

# Find all src and srcset in this img tag
local_imgs_cx = re.findall(r'_next/img_\d+\.(?:png|jpg|jpeg|webp)', img_tag)

with open('index.html', 'r') as f:
    text2 = f.read()

idx2 = text2.find('AI Agent Configuration')
img_idx2 = text2.rfind('<img', 0, idx2)
end_img2 = text2.find('>', img_idx2)
img_tag2 = text2[img_idx2:end_img2+1]

local_imgs_ai = re.findall(r'_next/img_\d+\.(?:png|jpg|jpeg|webp)', img_tag2)

print("Local CX Strategy images to replace:", set(local_imgs_cx))
print("Local AI Agent images to replace:", set(local_imgs_ai))

