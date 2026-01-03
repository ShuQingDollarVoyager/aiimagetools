# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Image Tools Hub - A Flask-powered web application that serves as a directory for discovering and comparing AI image processing tools. The site catalogs 30+ tools across 6 categories (AI Art, Background Removal, Enhancement, Avatars, Design, Professional).

## Running the Application

```bash
# Start Flask server (runs at http://localhost:5000)
python server.py

# Alternative: Windows batch script
start_server.bat

# Alternative: PowerShell
.\start_server.ps1
```

The frontend can also be opened directly via `index.html` for static-only usage, but API features require the Flask server.

## Architecture

**Backend (Flask):** `server.py` handles all routing and API endpoints:
- Static file serving for HTML/CSS/JS/images
- REST API endpoints under `/api/`:
  - `GET /api/tools` - Filtered/sorted/paginated tool listing
  - `GET /api/search?q=` - Weighted search (name > description > tags > category)
  - `GET /api/categories` - Category statistics
  - `GET /api/stats` - Site-wide statistics
  - `POST /api/subscribe` - Email subscriptions

**Frontend:** Vanilla JavaScript (ES6+) with Tailwind CSS (CDN)
- `js/main.js` - Search autocomplete, lazy image loading (IntersectionObserver), mobile menu, category filtering
- `css/custom.css` - Custom animations, gradients, component styles

**Data:** `data/tools.json` contains all tool metadata (name, URL, description, category, tags, pricing, ratings, logos)

## Adding New Tools

1. Edit `data/tools.json` - add entry to the `tools` array with required fields: `id`, `name`, `url`, `shortDescription`, `fullDescription`, `category`, `tags`, `pricingModel`, `rating`, `reviewCount`, `logo`
2. Add logo image to `images/logos/`
3. Optionally set `featured: true` and `popularityScore` for homepage visibility

## Key Files

- `server.py` - Flask backend with all API logic
- `data/tools.json` - Tool database (source of truth)
- `js/main.js` - Frontend interactivity
- `index.html` - Homepage with featured tools
- `tools.html` - Full tool listing with filters
- `tool-detail.html` - Individual tool detail page

## Deployment

GitHub Actions workflow (`.github/workflows/deploy.yml`) auto-deploys to GitHub Pages on push to main/master branch.
