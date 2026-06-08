with open('services.html', 'r') as f:
    text = f.read()

idx = text.find('Integrated CX Strategy')
img_idx = text.rfind('<img', 0, idx)
end_img = text.find('>', img_idx)
print("IMG TAG FOR INTEGRATED CX STRATEGY:")
print(text[img_idx:end_img+1])

print("\nAll occurrences of Integrated CX Strategy:")
current = 0
while True:
    current = text.find('Integrated CX Strategy', current)
    if current == -1:
        break
    print("Found at:", current)
    img_idx = text.rfind('<img', 0, current)
    end_img = text.find('>', img_idx)
    print("IMG:", text[img_idx:end_img+1])
    current += 1
