import re

with open('premium.js', 'r') as f:
    js = f.read()

# Remove the old legal links and blog hiding code block completely
old_code = """    // 6. Fix broken footer legal links (Privacy Policy / Terms of Service)
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
    });"""

new_code = """    // 6. Route legal links to new pages
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
        blogLink.textContent = 'Blog';
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
    if (window.location.pathname === '/' || window.location.pathname.endsWith('index.html')) {
        const testimonials = document.getElementById('testimonials') || document.querySelector('section:nth-of-type(4)');
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
        // Hero CTA is usually the first or second one
        const heroCta = primaryCtas[0];
        // Check if we haven't already injected it
        if (heroCta && heroCta.parentElement && !heroCta.parentElement.querySelector('.secondary-cta')) {
            const wrapper = document.createElement('div');
            wrapper.className = "flex flex-col sm:flex-row gap-4 justify-center sm:justify-start items-center mt-6";
            
            heroCta.parentNode.insertBefore(wrapper, heroCta);
            wrapper.appendChild(heroCta); // Move primary into wrapper
            heroCta.style.marginTop = '0'; // Clean up spacing
            heroCta.classList.remove('mt-6');
            
            const secondary = document.createElement('a');
            secondary.className = "secondary-cta inline-block bg-transparent hover:bg-white/10 text-white font-medium py-3 px-8 rounded-full transition-colors border border-gray-500 hover:border-white";
            secondary.href = "mailto:hello@clearcove.pro?subject=AI Readiness Checklist Request";
            secondary.textContent = "Get AI Readiness Checklist";
            wrapper.appendChild(secondary);
        }
    }"""

js = js.replace(old_code, new_code)
with open('premium.js', 'w') as f:
    f.write(js)
print("Updated premium.js")
