import re

with open('premium.js', 'r') as f:
    js = f.read()

# Fix Logo Link
if "// Fix Logo Link" not in js:
    js = js.replace("});\n\n    // 6. Route legal links", "});\n\n    // Fix Logo Link\n    document.querySelectorAll('header a').forEach(a => {\n        if (a.textContent.trim() === 'ClearCove') {\n            a.setAttribute('href', '/');\n        }\n    });\n\n    // 6. Route legal links")

# Fix Case Study logic
old_case_study = """    // 9. Case Study Injection (Homepage)
    if (window.location.pathname === '/' || window.location.pathname.endsWith('index.html')) {
        const testimonials = document.getElementById('testimonials') || document.querySelector('section:nth-of-type(4)');
        if (testimonials && !document.getElementById('injected-case-study')) {"""

new_case_study = """    // 9. Case Study Injection (Homepage)
    if (window.location.pathname === '/' || window.location.pathname === '' || window.location.pathname.endsWith('index.html')) {
        let testimonials = null;
        document.querySelectorAll('section').forEach(s => {
            if (s.textContent.includes('Organizations trust ClearCove')) testimonials = s;
        });
        if (testimonials && !document.getElementById('injected-case-study')) {"""

js = js.replace(old_case_study, new_case_study)

# Fix CTA button logic
old_cta = """    // 10. Secondary CTA (Lead Magnet)
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

new_cta = """    // 10. Secondary CTA (Lead Magnet)
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
    }"""

js = js.replace(old_cta, new_cta)

with open('premium.js', 'w') as f:
    f.write(js)
print("premium.js fixed")
