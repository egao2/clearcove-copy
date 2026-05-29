import os
import re
import urllib.parse

def deep_unquote(url):
    while '%' in url:
        decoded = urllib.parse.unquote(url)
        if decoded == url:
            break
        url = decoded
    return url

def main():
    root_dir = "."
    next_dir = os.path.join(root_dir, "_next")
    if not os.path.exists(next_dir):
        print("No _next dir found")
        return

    # 1. Rename files and build mapping
    mapping = {} # (decoded_url, w, q) -> new_filename
    
    files = [f for f in os.listdir(next_dir) if f.startswith("image?")]
    for i, f in enumerate(files):
        ext = ".png"
        if ".jpg" in f or ".jpeg" in f: ext = ".jpg"
        if ".webp" in f: ext = ".webp"
        
        new_name = f"img_{i}{ext}"
        
        qs = f[len("image?"):]
        parsed_qs = urllib.parse.parse_qs(qs)
        
        url_param = parsed_qs.get('url', [''])[0]
        w_param = parsed_qs.get('w', [''])[0]
        q_param = parsed_qs.get('q', [''])[0]
        
        decoded_url = deep_unquote(url_param)
        mapping[(decoded_url, w_param, q_param)] = new_name
        
        os.rename(os.path.join(next_dir, f), os.path.join(next_dir, new_name))
        
    print(f"Renamed {len(mapping)} images.")

    # 2. Replace in all HTML/CSS/JS files
    def replacer(match):
        full_match = match.group(0)
        if '%3F' in full_match:
            qs = full_match.split('%3F', 1)[1]
        else:
            qs = full_match.split('?', 1)[1]
            
        qs = qs.replace('&amp;', '&')
        parsed_qs = urllib.parse.parse_qs(qs)
        
        url_param = parsed_qs.get('url', [''])[0]
        w_param = parsed_qs.get('w', [''])[0]
        q_param = parsed_qs.get('q', [''])[0]
        
        decoded_url = deep_unquote(url_param)
        
        key = (decoded_url, w_param, q_param)
        if key in mapping:
            prefix = "/" if full_match.startswith("/") else ""
            return f"{prefix}_next/{mapping[key]}"
        
        # If not found, try without w and q (fallback)
        for k, v in mapping.items():
            if k[0] == decoded_url:
                prefix = "/" if full_match.startswith("/") else ""
                return f"{prefix}_next/{v}"
                
        return full_match

    pattern = re.compile(r'/?_next/image(?:\?|%3F)[^"\'\s\),]+')

    for root, dirs, files in os.walk(root_dir):
        if ".git" in root or "node_modules" in root: continue
        for f in files:
            if f.endswith((".html", ".css", ".js")):
                filepath = os.path.join(root, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                new_content = pattern.sub(replacer, content)
                
                new_content = new_content.replace('icon?size=32', 'icon_32.png')
                new_content = new_content.replace('icon?size=apple', 'icon_apple.png')
                new_content = new_content.replace('icon%3Fsize=32', 'icon_32.png')
                new_content = new_content.replace('icon%3Fsize=apple', 'icon_apple.png')
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Updated {filepath}")
                    
    # Rename icons
    if os.path.exists("icon?size=32"): os.rename("icon?size=32", "icon_32.png")
    if os.path.exists("icon?size=apple"): os.rename("icon?size=apple", "icon_apple.png")

if __name__ == "__main__":
    main()
