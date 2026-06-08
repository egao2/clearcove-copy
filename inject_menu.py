import os
import glob

html_files = glob.glob('*.html')

snippet = """
<style>
  #mobile-menu-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: #19212B;
    z-index: 9999;
    display: none;
    flex-direction: column;
    padding: 24px;
    color: #fcfcfc;
    font-family: var(--typography-font-family, sans-serif);
  }
  #mobile-menu-overlay.open {
    display: flex;
  }
  .mobile-menu-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
  }
  .mobile-menu-title {
    font-size: 24px;
    font-weight: bold;
    text-decoration: none;
    color: #fcfcfc;
  }
  .mobile-menu-close {
    background: transparent;
    border: none;
    color: #fcfcfc;
    cursor: pointer;
    padding: 8px;
  }
  .mobile-menu-nav {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  .mobile-menu-nav a {
    color: #fcfcfc;
    text-decoration: none;
    font-size: 20px;
  }
  .mobile-menu-contact {
    background-color: #007E76;
    color: #fcfcfc !important;
    padding: 12px 24px;
    border-radius: 999px;
    text-align: center;
    margin-top: 16px;
    font-size: 16px !important;
  }
</style>
<div id="mobile-menu-overlay">
  <div class="mobile-menu-header">
    <a href="index.html" class="mobile-menu-title">ClearCove</a>
    <button id="close-menu-btn" class="mobile-menu-close">
      <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
    </button>
  </div>
  <nav class="mobile-menu-nav">
    <a href="services.html">Services</a>
    <a href="pricing.html">Pricing</a>
    <a href="about.html">About</a>
    <a href="blog.html">Blog</a>
    <a href="contact.html" class="mobile-menu-contact">Contact Us</a>
  </nav>
</div>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var openBtn = document.querySelector('button[aria-label="Open navigation menu"]');
    var overlay = document.getElementById('mobile-menu-overlay');
    var closeBtn = document.getElementById('close-menu-btn');
    if(openBtn && overlay && closeBtn) {
      openBtn.addEventListener('click', function() {
        overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
      });
      closeBtn.addEventListener('click', function() {
        overlay.classList.remove('open');
        document.body.style.overflow = '';
      });
    }
  });
</script>
</body>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '#mobile-menu-overlay' in content:
        print(f"Skipping {file}, already injected.")
        continue
        
    new_content = content.replace('</body>', snippet)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
