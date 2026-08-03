import os

css_append = """
/* Global Typography Inversion for Dark Theme */
/* Overrides Durable's default dark text to ensure visibility on our dark backgrounds */
h1, h2, h3, h4, h5, h6 {
    color: #fcfcfc !important;
}

p, li, span {
    /* Only apply to spans that don't have explicit cyan styling */
    color: #d1d5db;
}

/* Force paragraph colors except in specific components where we want explicit control */
.website-container p, 
.website-container li {
    color: #d1d5db !important;
}

/* Ensure brand cyan remains intact */
[style*="color: #007E76"], 
[style*="color:#007E76"] {
    color: #007E76 !important;
}

/* Ensure buttons text remain visible */
button, .cc-btn-primary {
    color: #ffffff !important;
}
.cc-btn-outline {
    color: #d1d5db !important;
}
"""

with open('premium.css', 'a') as f:
    f.write("\n" + css_append)

print("Appended typography inversion CSS to premium.css")
