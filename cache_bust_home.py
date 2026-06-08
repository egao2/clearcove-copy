import os

files_to_bust = {
    '_next/img_219.png': '_next/img_219_v2.png',
    '_next/img_40.png': '_next/img_40_v2.png'
}

for old, new in files_to_bust.items():
    if os.path.exists(old):
        os.rename(old, new)
        print(f"Renamed {old} to {new}")
    else:
        print(f"Warning: {old} not found")

with open('index.html', 'r') as f:
    text = f.read()

for old, new in files_to_bust.items():
    text = text.replace(old, new)

with open('index.html', 'w') as f:
    f.write(text)
