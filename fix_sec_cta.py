import os

css_append = """
/* Standardized Secondary CTA Button Styling */
/* Matches the exact dimensions, padding, and typography of Durable's primary buttons */
.cc-sec-cta {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.625rem 1.25rem; /* Matches Tailwind py-2.5 px-5 */
    border-radius: 1.5rem; /* Matches Tailwind rounded-3xl */
    border: 1px solid rgba(255, 255, 255, 0.3);
    background-color: rgba(255, 255, 255, 0.05);
    color: #fcfcfc !important;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.2s ease-in-out;
    text-decoration: none;
    white-space: nowrap;
    
    /* Matches Durable's typography-body-sm-em scale */
    font-size: var(--typography-body-sm-em-font-size, clamp(0.8333rem, 0.7681rem + 0.2899cqi, 1.0000rem));
    font-weight: var(--typography-body-sm-em-font-weight, 500);
    line-height: var(--typography-body-sm-em-line-height, 1.5);
    letter-spacing: var(--typography-body-sm-em-letter-spacing, 0em);
    font-family: var(--typography-body-sm-em-font-family, var(--font-space-grotesk, "Space Grotesk", sans-serif));
}

.cc-sec-cta:hover {
    background-color: rgba(255, 255, 255, 0.15);
    border-color: rgba(255, 255, 255, 0.6);
}
"""

with open('premium.css', 'a') as f:
    f.write("\n" + css_append)

print("Appended standardized .cc-sec-cta CSS to premium.css")
