// premium.js

document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Glassmorphism Nav
    const header = document.querySelector('header');
    if (header) {
        header.classList.add('glass-nav');
    }

    // 2. Scroll Reveals
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-visible');
                // Optional: stop observing once revealed
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    // Apply reveal to sections, headings, images
    const elementsToReveal = document.querySelectorAll('section, h2, h3, img');
    elementsToReveal.forEach(el => {
        // Skip small icons or specific elements
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

    // 6. Fix broken footer legal links (Privacy Policy / Terms of Service)
    // These link to index.html which is incorrect — remove the href so they don't mislead
    document.querySelectorAll('a').forEach(a => {
        const text = a.textContent.trim();
        if ((text === 'Privacy Policy' || text === 'Terms of Service') && 
            (a.getAttribute('href') === 'index.html' || a.getAttribute('href') === '/')) {
            a.removeAttribute('href');
            a.style.cursor = 'default';
            a.style.opacity = '0.5';
        }
    });

    // 7. Remove Blog from header nav (no real content yet)
    document.querySelectorAll('header a, nav a').forEach(a => {
        if (a.textContent.trim() === 'Blog' && a.getAttribute('href') === 'blog.html') {
            a.style.display = 'none';
        }
    });

});
