import os

files_to_bust = {
    '_next/img_11.jpg': '_next/img_11_v2.jpg',
    '_next/img_202.jpg': '_next/img_202_v2.jpg'
}

for old, new in files_to_bust.items():
    if os.path.exists(old):
        os.rename(old, new)
        print(f"Renamed {old} to {new}")
    else:
        print(f"Warning: {old} not found")

with open('services.html', 'r') as f:
    text = f.read()

for old, new in files_to_bust.items():
    text = text.replace(old, new)

with open('services.html', 'w') as f:
    f.write(text)

