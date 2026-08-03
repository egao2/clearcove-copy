import re

def update_content():
    with open('about.html', 'r') as f:
        html = f.read()

    # Update KPI
    html = html.replace(
        '<div class="cc-metric-value text-gradient-premium">100%</div>\n                    <div class="cc-metric-label">US-Based Architecture Team</div>',
        '<div class="cc-metric-value text-gradient-premium">100%</div>\n                    <div class="cc-metric-label">Code & IP Ownership Retained</div>'
    )

    # Update Technologies
    tags = [
        "LLM Orchestration",
        "Vector Databases",
        "Autonomous Agents",
        "RAG Pipelines",
        "Data Engineering",
        "Event-Driven Architecture",
        "High-Availability Systems",
        "React & Next.js",
        "Flutter & Dart",
        "Firebase & Firestore",
        "Serverless Infrastructure",
        "CI/CD Automation",
        "Edge AI"
    ]
    
    tags_html = '\\n                '.join(
        [f'<span class="cc-tech-tag" style="transition-delay: {i * 50}ms;">{tag}</span>' for i, tag in enumerate(tags)]
    )
    
    new_tech_grid = f'<div class="cc-tech-grid reveal-hidden">\n                {tags_html}\n            </div>'
    
    # Replace the old grid
    html = re.sub(
        r'<div class="cc-tech-grid reveal-hidden">.*?</div>',
        new_tech_grid,
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open('about.html', 'w') as f:
        f.write(html)
    print("Content updated successfully.")

if __name__ == '__main__':
    update_content()
