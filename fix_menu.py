import glob

html_files = glob.glob('*.html')

old_js = """    var openBtn = document.querySelector('button[aria-label="Open navigation menu"]');
    var overlay = document.getElementById('mobile-menu-overlay');
    var closeBtn = document.getElementById('close-menu-btn');
    if(openBtn && overlay && closeBtn) {
      openBtn.addEventListener('click', function() {
        overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
      });"""

new_js = """    var openBtns = document.querySelectorAll('button[aria-label="Open navigation menu"]');
    var overlay = document.getElementById('mobile-menu-overlay');
    var closeBtn = document.getElementById('close-menu-btn');
    if(openBtns.length > 0 && overlay && closeBtn) {
      openBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          overlay.classList.add('open');
          document.body.style.overflow = 'hidden';
        });
      });"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(old_js, new_js)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
