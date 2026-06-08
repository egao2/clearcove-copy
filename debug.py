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

with open('index.html', 'r') as f:
    content = f.read()

pattern = re.compile(r'/?_next/image(?:\?|%3F)[^"\'\s\),]+')
matches = pattern.findall(content)
print("Found", len(matches), "matches in HTML.")

if matches:
    full_match = matches[0]
    print("Match:", full_match)
    if '%3F' in full_match:
        qs = full_match.split('%3F', 1)[1]
    else:
        qs = full_match.split('?', 1)[1]
        
    qs = qs.replace('&amp;', '&')
    print("QS:", qs)
    parsed_qs = urllib.parse.parse_qs(qs)
    print("Parsed QS:", parsed_qs)
    
    url_param = parsed_qs.get('url', [''])[0]
    w_param = parsed_qs.get('w', [''])[0]
    q_param = parsed_qs.get('q', [''])[0]
    
    decoded_url = deep_unquote(url_param)
    print("Decoded URL:", decoded_url, "w:", w_param, "q:", q_param)
