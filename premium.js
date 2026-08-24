// premium.js

document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Glassmorphism Nav
    const header = document.querySelector('header');
    if (header) {
        header.classList.add('glass-nav');
    }

    // 2. Scroll Reveals with Staggering
    let staggerTimeout;
    let revealQueue = [];
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                revealQueue.push(entry.target);
                observer.unobserve(entry.target);
            }
        });
        
        if (revealQueue.length > 0) {
            clearTimeout(staggerTimeout);
            staggerTimeout = setTimeout(() => {
                // Sort by vertical position to ensure top-to-bottom staggering
                revealQueue.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
                
                revealQueue.forEach((el, index) => {
                    // Apply a staggered transition delay based on their index in the batch
                    el.style.transitionDelay = `${index * 150}ms`;
                    el.classList.add('reveal-visible');
                    
                    // Clean up the inline delay after the transition finishes so hover effects aren't delayed later
                    setTimeout(() => {
                        el.style.transitionDelay = '';
                    }, 1000 + (index * 150));
                });
                revealQueue = [];
            }, 50);
        }
    }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    // Apply reveal to sections, headings, images, and paragraphs
    const elementsToReveal = document.querySelectorAll('section, h1, h2, h3, img, p, .reveal-hidden');
    elementsToReveal.forEach(el => {
        // Skip small icons or specific elements
        if (el.classList.contains('reveal-hidden')) {
            observer.observe(el);
            return;
        }
        if (el.tagName.toLowerCase() === 'img' && el.width < 100) return;
        
        el.classList.add('reveal-hidden');
        observer.observe(el);
    });

    // 3. Hover Micro-Interactions
    // Apply hover-lift to cards (divs containing text, images, having rounded corners)
    const cards = document.querySelectorAll('.rounded-3xl');
    cards.forEach(card => {
        // Only apply to cards that look like content blocks, not just layout wrappers
        if (card.classList.contains('bg-(--bg-color)') || card.innerHTML.includes('<h3')) {
            card.classList.add('hover-lift');
        }
    });

    // Button Glows
    const buttons = document.querySelectorAll('a[data-slot="button"]');
    buttons.forEach(btn => {
        if (btn.style.getPropertyValue('--bg-color') !== 'transparent') {
            btn.classList.add('button-glow');
        }
    });

    // 4. Gradient Text
    const largeHeadings = document.querySelectorAll('h1, h2');
    largeHeadings.forEach(h => {
        // Apply gradient text selectively so it's not overwhelming
        h.classList.add('text-gradient-premium');
    });

    // 5. Infinite Marquee for Reviews
    // Look for the columns containing review cards
    const columns = document.querySelectorAll('.h-dvh > .flex.flex-col');
    columns.forEach((col, index) => {
        // Verify it contains review cards (min-h-80)
        if (col.querySelector('.min-h-80')) {
            // Clone the children to create an infinite loop effect
            const children = Array.from(col.children);
            children.forEach(child => {
                const clone = child.cloneNode(true);
                col.appendChild(clone);
            });
            // Double it again to be safe for tall screens
            children.forEach(child => {
                const clone = child.cloneNode(true);
                col.appendChild(clone);
            });

            col.classList.add('marquee-column');
            if (index % 2 !== 0) {
                col.classList.add('reverse');
            }
        }
    });

    // Fix Logo Link
    document.querySelectorAll('header a').forEach(a => {
        if (a.textContent.trim() === 'ClearCove') {
            a.setAttribute('href', '/');
        }
    });

    // 6. Route legal links to new pages
    document.querySelectorAll('a').forEach(a => {
        const text = a.textContent.trim();
        if (text === 'Privacy Policy') {
            a.setAttribute('href', 'privacy.html');
            a.style.cursor = 'pointer';
            a.style.opacity = '1';
        }
        if (text === 'Terms of Service') {
            a.setAttribute('href', 'terms.html');
            a.style.cursor = 'pointer';
            a.style.opacity = '1';
        }
    });

    // 7. Footer Blog Nav Consistency
    // Find the footer nav links, duplicate "About", change text to "Blog" and href to "blog.html"
    const footerLinks = document.querySelectorAll('footer a');
    let aboutLink = null;
    let blogExists = false;
    footerLinks.forEach(a => {
        if (a.textContent.trim() === 'About') aboutLink = a;
        if (a.textContent.trim() === 'Blog') blogExists = true;
    });
    if (aboutLink && !blogExists) {
        const blogLink = aboutLink.cloneNode(true);
        blogLink.innerHTML = blogLink.innerHTML.replace('About', 'Blog');
        blogLink.setAttribute('href', 'blog.html');
        aboutLink.parentNode.insertBefore(blogLink, aboutLink.nextSibling);
    }

    
});

// ClearCove AI Solutions Advisor Widget
(function() {
    var s = document.createElement('script');
    s.src = 'https://clearcove-backend-production.up.railway.app/web/cc-widget.js';
    s.async = true;
    document.body.appendChild(s);
})();
