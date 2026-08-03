import re

def update_buttons():
    files = ['blog-support-automation.html', 'blog-ai-readiness.html']
    for f_name in files:
        with open(f_name, 'r') as f:
            content = f.read()
        
        # Replace the broken tailwind classes with our standard cc-btn-primary
        old_classes = 'class="inline-block bg-[var(--primary-color)] hover:bg-[var(--primary-color-hover)] text-white font-medium py-3 px-8 rounded-full transition-colors button-glow"'
        new_classes = 'class="cc-btn-primary"'
        
        content = content.replace(old_classes, new_classes)
        
        with open(f_name, 'w') as f:
            f.write(content)
        print(f"Updated buttons in {f_name}")

def update_tech_tags():
    with open('about.html', 'r') as f:
        html = f.read()

    # The new generalized 12 tags
    tags = [
        "LLM Orchestration",
        "Vector Databases",
        "Autonomous Agents",
        "RAG Pipelines",
        "Data Engineering",
        "Event-Driven Architecture",
        "High-Availability Systems",
        "Modern Frontend Architecture",
        "Cross-Platform Mobile",
        "Real-Time Databases",
        "Serverless Infrastructure",
        "Automated DevOps"
    ]
    
    tags_html = '\\n                '.join(
        [f'<span class="cc-tech-tag" style="transition-delay: {i * 50}ms;">{tag}</span>' for i, tag in enumerate(tags)]
    )
    
    new_tech_grid = f'<div class="cc-tech-grid reveal-hidden">\n                {tags_html}\n            </div>'
    
    html = re.sub(
        r'<div class="cc-tech-grid reveal-hidden">.*?</div>',
        new_tech_grid,
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open('about.html', 'w') as f:
        f.write(html)
    print("Updated tech tags in about.html")

if __name__ == '__main__':
    update_buttons()
    update_tech_tags()
