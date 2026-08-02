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

    // 8. Blog Page Content Injection
    if (window.location.pathname.includes('blog')) {
        const h3s = document.querySelectorAll('h3');
        if (h3s.length >= 2) {
            // Update Article 1
            h3s[0].textContent = "Support Automation That Doesn't Feel Like a Machine";
            const p1 = h3s[0].nextElementSibling;
            if (p1) p1.textContent = "The rush to implement AI in customer support has led to a predictable problem: terrible customer experiences.";
            const a1 = h3s[0].parentElement.querySelector('a');
            if (a1) a1.setAttribute('href', 'blog-support-automation.html');
            
            // Update Article 2
            h3s[1].textContent = "5 Signs Your Business Is Ready for AI Automation";
            const p2 = h3s[1].nextElementSibling;
            if (p2) p2.textContent = "Artificial Intelligence is no longer just for enterprise tech companies. Mid-market businesses are scaling rapidly with custom AI.";
            const a2 = h3s[1].parentElement.querySelector('a');
            if (a2) a2.setAttribute('href', 'blog-ai-readiness.html');
            
            // Hide the rest of the stub articles
            for (let i = 2; i < h3s.length; i++) {
                let card = h3s[i].closest('div[class*="rounded-"]'); // Find parent card
                if (card) card.style.display = 'none';
            }
        }
    }

    // 9. Case Study Injection (Homepage)
    if (window.location.pathname === '/' || window.location.pathname === '' || window.location.pathname.endsWith('index.html')) {
        let testimonials = null;
        document.querySelectorAll('section').forEach(s => {
            if (s.textContent.includes('Organizations trust ClearCove')) testimonials = s;
        });
        if (testimonials && !document.getElementById('injected-case-study')) {
            const caseStudy = document.createElement('section');
            caseStudy.id = 'injected-case-study';
            caseStudy.className = "py-24 px-6 sm:px-8 bg-[var(--bg-color-alt)] text-center";
            caseStudy.innerHTML = `
                <div class="max-w-4xl mx-auto reveal-hidden">
                    <p class="text-[var(--primary-color)] font-bold tracking-widest text-sm uppercase mb-4">Case Study: Series A FinTech</p>
                    <h2 class="text-3xl md:text-5xl font-bold text-gradient-premium mb-8">60% Reduction in Support Costs</h2>
                    <p class="text-xl leading-relaxed text-[var(--secondary-text)] mb-8">
                        "ClearCove automated our support intake process, reducing first-response time from 4 hours to under 2 minutes. We scaled our user base 3x without adding a single headcount."
                    </p>
                    <a href="https://calendar.app.google/mCDenTF29rv4Zzb18" target="_blank" data-slot="button" class="inline-block bg-[var(--primary-color)] hover:bg-[var(--primary-color-hover)] text-white font-medium py-3 px-8 rounded-full transition-colors button-glow">
                        See how we did it
                    </a>
                </div>
            `;
            testimonials.parentNode.insertBefore(caseStudy, testimonials);
        }
    }

    // 10. Secondary CTA (Lead Magnet)
    const primaryCtas = document.querySelectorAll('a[href*="calendar.app.google"]');
    if (primaryCtas.length > 0) {
        const heroCta = primaryCtas[0];
        if (heroCta && heroCta.parentElement && !heroCta.parentElement.querySelector('.secondary-cta')) {
            const secondary = document.createElement('a');
            secondary.className = "secondary-cta inline-flex shrink-0 cursor-pointer items-center justify-center bg-transparent whitespace-nowrap transition-all outline-none hover:bg-white/10 text-white font-medium px-5 py-2.5 rounded-3xl border border-gray-500 hover:border-white";
            secondary.href = "mailto:hello@clearcove.pro?subject=AI Readiness Checklist Request";
            secondary.textContent = "Get AI Readiness Checklist";
            
            // The container might be a flex column on mobile, so adding margins helps
            secondary.style.marginTop = '10px';
            if (window.innerWidth >= 640) {
                secondary.style.marginTop = '0';
                secondary.style.marginLeft = '16px';
            }
            
            heroCta.parentElement.appendChild(secondary);
        }
    }

});
