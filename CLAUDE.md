# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Pages static website for Chokmah LLC (chokmah.me), a professional services company specializing in cybersecurity and AI engineering solutions. The site is built with vanilla HTML/CSS using Tailwind CSS for styling.

## Site Architecture

### Core Pages Structure
- **index.html** - Main landing page featuring services, company background, and contact information
- **ai-ciso-training/index.html** - Dedicated training curriculum page with structured JSON-LD schema markup
- **theme.html** - Brand color palette reference and Tailwind config documentation

### Key Design Elements
- **Color Scheme** (Sovereign Competence Theme):
  - Deep Anthracite (#0f172a) - Primary background
  - Slate Armor (#1e293b) - Cards and panels
  - Signal Amber (#d97706) - Accents and buttons
  - Active Amber (#f59e0b) - Hover states
  - Titanium White (#f8fafc) - Primary text
  - Cadet Grey (#cbd5e1) - Secondary text

- **CSS Framework**: Tailwind CSS via CDN
- **Typography**: Inter font family (Google Fonts)
- **Responsive**: Mobile-first design with breakpoints at 600px, 640px, 768px, 1024px

### SEO & Schema Markup
Both main pages include comprehensive structured data:
- **Schema.org JSON-LD** for Organization, Person, ProfessionalService, Course, Product
- **Open Graph** meta tags with social card images
- **Twitter Card** meta tags with large image preview
- Canonical URLs and multiple favicon formats (ICO, PNG, Apple Touch Icon)

## Common Development Tasks

### Local Development
```bash
# Serve locally (Python 3)
python -m http.server 8000

# Or with Node.js
npx http-server -p 8000
```

View at: http://localhost:8000

### Deployment
This is a GitHub Pages site. Changes pushed to the `main` branch automatically deploy to https://chokmah.me

```bash
# Standard deployment workflow
git add .
git commit -m "Description of changes"
git push origin main
```

### Updating Content

#### Modify Service Offerings
Services are in `index.html` in multiple locations:
1. **Quick Services Grid** (lines ~227-246): Two-column grid with emoji icons for compact overview
2. **Detailed Services Section**: Full descriptions within the `<section>` containing "Core Service Offerings". Each service uses `<h3>` for titles.

When updating services, maintain consistency between both locations.

#### Update Training Curriculum
Training details are in `ai-ciso-training/index.html`. Session content uses `<details>` elements for expand/collapse functionality. Update both:
1. HTML content in the sessions section
2. JSON-LD schema at lines 30-96 to maintain SEO accuracy

#### Color Scheme Changes
1. Update CSS variables in both `index.html` (lines 137-144) and `theme.html` (lines 13-20)
2. Update Tailwind config snippet in `theme.html` (lines 136-154)
3. Verify color references in palette grid section

### SEO Maintenance

#### Update Sitemap
Edit `sitemap.xml` when adding/removing pages. Current structure:
- Main pages: priority 1.0 (homepage), 0.9 (training page)
- Only includes direct site pages (not external GitHub repositories)
- Update `<lastmod>` dates in YYYY-MM-DD format when making content changes

#### robots.txt Configuration
Currently blocks GPTBot while allowing general crawling. Modify `robots.txt` to adjust crawler permissions.

## Important Constraints

### Content Philosophy
- **Professional tone**: No emojis in body content (emojis allowed only in headers/highlights as currently used)
- **No-nonsense approach**: Clarity, evidence, and results-focused messaging
- **Sovereign-grade competence**: Maintain technical credibility and precision

### Brand Consistency
- Always use the official color palette defined in `theme.html`
- Maintain the dark-mode-first aesthetic
- Keep typography limited to Inter font family or system fallbacks
- Preserve the structured, card-based layout pattern

### Technical Standards
- **No build process**: Keep vanilla HTML/CSS for simplicity
- **CDN dependencies only**: Tailwind CSS and Google Fonts via CDN
- **Inline styles preferred**: Keep critical CSS in `<style>` blocks for performance
- **Minimal JavaScript**: Only essential interactivity (expand/collapse, copy email)

### UI Components & Interactive Elements

**Homepage (index.html)**:
- **GitHub Button Style** (`.github-btn`): Pill-shaped buttons with hover effects for repository links
- **Quick Services Grid**: Responsive two-column grid (collapses to single column on mobile)
- **Card Components**: Slate armor background with subtle borders and hover effects
- **CTA Buttons**: Amber-colored with glow effects on hover

**Training Page (ai-ciso-training/index.html)**:
- **Sticky Navigation**: Backdrop-blur nav bar with smooth scroll anchors
- **Expand/Collapse Details**: JavaScript functions `openAllDetails()` and `closeAllDetails()` for session sections
- **Email Copy Function**: `copyEmail()` JavaScript function with clipboard API and temporary success message
- **Responsive Time-Saved Cards**: Grid layout with card-hover effects and gradient backgrounds
- **Mobile Optimizations**: Responsive text sizes, hyphenation, and word-breaking for narrow viewports

## Domain & Contact Configuration

- **Primary domain**: chokmah.me (configured in CNAME file)
- **GitHub Pages**: chokmah-me.github.io redirects to chokmah.me
- **Email**: info@chokmah.me (public-facing contact in schema markup and UI)
- **Email Implementation**: Contact forms use `mailto:info@chokmah.me` with pre-filled subject lines and fallback copy-to-clipboard functionality

## Assets & Images

The `assets/` directory contains:
- **social-card.png** (948KB): Main Open Graph image for homepage
- **ciso-training-card.png** (1.3MB): Social card for AI CISO training page
- **dummy.png**: Placeholder file

Root-level icons:
- **favicon.ico** (15KB): Browser favicon
- **favicon-32x32.png** (389 bytes): PNG favicon
- **apple-touch-icon.png** (5KB): Apple device icon
- **icon.svg**: Simple SVG logo with `>_` terminal prompt in brand colors

When adding/updating assets:
- Optimize images before upload (consider WebP for better compression)
- Update meta tag references in both `index.html` and `ai-ciso-training/index.html`
- Maintain consistent branding with the color palette
- Keep file sizes reasonable for page performance
