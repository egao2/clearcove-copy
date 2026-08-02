import os

with open('template_base.html', 'r') as f:
    template = f.read()

def create_page(filename, title, content_html):
    page = template.replace('<title>Get in Touch with ClearCove</title>', f'<title>{title} | ClearCove</title>')
    
    section_wrapper = f"""
    <section class="py-20 px-6 sm:px-8 max-w-4xl mx-auto text-[var(--secondary-text)]" style="margin-top: 100px; min-height: 60vh;">
        <h1 class="text-4xl font-bold text-gradient-premium mb-8 text-[var(--primary-text)]">{title}</h1>
        <div class="prose prose-invert max-w-none text-lg leading-relaxed text-gray-300">
            {content_html}
        </div>
    </section>
    """
    page = page.replace('<!-- CONTENT GOES HERE -->', section_wrapper)
    with open(filename, 'w') as out:
        out.write(page)

privacy_content = """
<p class="mb-4">Last updated: August 2, 2026</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">1. Information We Collect</h2>
<p class="mb-4">We collect information you provide directly to us, such as when you fill out a contact form, request a consultation, or communicate with us via email. This may include your name, email address, phone number, and any other information you choose to provide.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">2. How We Use Your Information</h2>
<p class="mb-4">We use the information we collect to provide, maintain, and improve our consulting services, to communicate with you, and to personalize your experience. We do not sell or rent your personal information to third parties.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">3. Data Security</h2>
<p class="mb-4">We implement appropriate technical and organizational measures to protect the security of your personal information. However, please note that no method of transmission over the Internet is 100% secure.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">4. Contact Us</h2>
<p class="mb-4">If you have any questions about this Privacy Policy, please contact us at <a href="mailto:hello@clearcove.pro" class="text-teal-400 hover:underline">hello@clearcove.pro</a>.</p>
"""
create_page('privacy.html', 'Privacy Policy', privacy_content)

terms_content = """
<p class="mb-4">Last updated: August 2, 2026</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">1. Acceptance of Terms</h2>
<p class="mb-4">By accessing or using the ClearCove website and services, you agree to be bound by these Terms of Service. If you disagree with any part of the terms, you may not access our services.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">2. Services Description</h2>
<p class="mb-4">ClearCove provides AI strategy consulting, agent configuration, and workflow automation advisory services. The specific scope, deliverables, and timeline of any consulting engagement will be defined in a separate Statement of Work (SOW) or consulting agreement.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">3. Intellectual Property</h2>
<p class="mb-4">Unless otherwise specified in a consulting agreement, all materials, methodologies, and content provided by ClearCove remain the intellectual property of ClearCove.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">4. Limitation of Liability</h2>
<p class="mb-4">ClearCove shall not be liable for any indirect, incidental, special, consequential, or punitive damages resulting from your use of or inability to use our services.</p>
"""
create_page('terms.html', 'Terms of Service', terms_content)

blog1_content = """
<p class="text-sm text-gray-400 mb-6 uppercase tracking-wider">Published on August 2, 2026</p>
<p class="mb-6">The rush to implement AI in customer support has led to a predictable problem: terrible customer experiences. We've all been trapped in a loop with a chatbot that doesn't understand context and refuses to escalate to a human.</p>
<p class="mb-6">At ClearCove, we believe that AI should enhance the customer experience, not replace it with a frustrating barrier. The goal isn't to eliminate human interaction; it's to eliminate the <em class="italic">repetitive</em> interactions so your human team can focus on high-value conversations.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">The Core Problem: Deflection vs. Resolution</h2>
<p class="mb-6">Most out-of-the-box AI chatbots are designed for <strong class="text-white">deflection</strong>. They try to keep the customer away from a human agent at all costs. This saves money in the short term but destroys brand loyalty.</p>
<p class="mb-6">Effective AI agents are designed for <strong class="text-white">resolution</strong>. They handle the tasks they are uniquely good at (retrieving order status, updating account details, answering policy questions) and seamlessly hand off complex emotional issues to human agents with full context.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">How We Architect Better Support AI</h2>
<ul class="list-disc pl-6 mb-6 space-y-4">
    <li><strong class="text-white">Context Awareness:</strong> We integrate AI agents deeply with your CRM (Salesforce, Zendesk, HubSpot) so the AI knows who the customer is before they even ask a question.</li>
    <li><strong class="text-white">Graceful Escalation:</strong> If the AI encounters a frustrated customer or a complex issue, it instantly transfers the chat to a human, providing a summary of the conversation so the customer never has to repeat themselves.</li>
    <li><strong class="text-white">Tone Matching:</strong> We train the language models to match your brand's specific voice—whether that's professional and formal, or casual and friendly.</li>
</ul>
<p class="mb-10">Support automation shouldn't feel like a machine. It should feel like your best support agent, available instantly, 24/7.</p>
<div class="mt-12 p-8 bg-[var(--bg-color-alt)] rounded-3xl border border-gray-700/50">
    <h3 class="text-2xl font-semibold mb-3 text-white">Ready to upgrade your CX?</h3>
    <p class="mb-6">Let's discuss how a custom AI agent can streamline your support operations.</p>
    <a href="https://calendar.app.google/mCDenTF29rv4Zzb18" target="_blank" data-slot="button" class="inline-block bg-[var(--primary-color)] hover:bg-[var(--primary-color-hover)] text-white font-medium py-3 px-8 rounded-full transition-colors button-glow">Book a Free Strategy Call</a>
</div>
"""
create_page('blog-support-automation.html', 'Support Automation That Doesn\'t Feel Like a Machine', blog1_content)

blog2_content = """
<p class="text-sm text-gray-400 mb-6 uppercase tracking-wider">Published on August 1, 2026</p>
<p class="mb-6">Artificial Intelligence is no longer just for enterprise tech companies. Today, mid-market businesses and growing startups are leveraging custom AI agents and workflow automation to scale rapidly without bloating their payroll.</p>
<p class="mb-6">But how do you know if your business is actually ready for an AI integration? Here are the top 5 signs that you are outgrowing your manual processes and need an intelligent automation strategy.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">1. Your team spends more than 20% of their time on data entry</h2>
<p class="mb-6">If your highly paid employees are copying and pasting data between your CRM, your billing software, and spreadsheets, you are bleeding money. AI agents can seamlessly parse emails, extract data, and route it to the correct systems instantly.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">2. Customer response times are slipping as you grow</h2>
<p class="mb-6">Growth is great, but if scaling your customer base means response times drop from 2 hours to 24 hours, your CX is suffering. An AI triage agent can instantly categorize incoming requests, resolve Tier 1 issues automatically, and prioritize urgent tickets for your human team.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">3. You have a massive backlog of unstructured data</h2>
<p class="mb-6">Do you have thousands of past customer support transcripts, sales calls, or PDF reports that no one ever looks at? Modern LLMs can ingest this unstructured data and turn it into an instantly searchable knowledge base, providing real-time insights to your sales and support teams.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">4. Processes break down when key employees are on PTO</h2>
<p class="mb-6">If a specific workflow (like onboarding a new client or generating a weekly report) grinds to a halt because "Sarah is on vacation," your business lacks operational resilience. Automating these workflows ensures they run flawlessly 24/7/365.</p>
<h2 class="text-2xl font-semibold mt-8 mb-4 text-[var(--primary-text)]">5. You are hesitant to take on new clients due to capacity constraints</h2>
<p class="mb-6">This is the ultimate sign. If you are turning away revenue because your operations team is maxed out, it's time to automate. AI allows you to decouple revenue growth from headcount growth.</p>
<div class="mt-12 p-8 bg-[var(--bg-color-alt)] rounded-3xl border border-gray-700/50">
    <h3 class="text-2xl font-semibold mb-3 text-white">Recognize any of these signs?</h3>
    <p class="mb-6">Let's discuss where AI can have the highest immediate impact on your operations.</p>
    <a href="https://calendar.app.google/mCDenTF29rv4Zzb18" target="_blank" data-slot="button" class="inline-block bg-[var(--primary-color)] hover:bg-[var(--primary-color-hover)] text-white font-medium py-3 px-8 rounded-full transition-colors button-glow">Book a Free Strategy Call</a>
</div>
"""
create_page('blog-ai-readiness.html', '5 Signs Your Business Is Ready for AI Automation', blog2_content)

print("Created 4 new HTML pages.")
