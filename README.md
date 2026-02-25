# ShopSense AI — Product Recommendation Engine

> An AI-powered shopping intelligence platform built on User-Based Collaborative Filtering, delivering personalized product recommendations from a 9,600-item electronics catalog.

---

## 🚀 Project Overview

ShopSense AI solves the *Paradox of Choice* in e-commerce by analyzing behavioral patterns across 836 unique shopper vectors to surface high-fidelity, personalized product suggestions. The system combines a collaborative filtering engine with a fully redesigned production-grade frontend — featuring user authentication, wishlist management, trending analytics, and real-time match scoring.

---

## 🛠️ Technical Stack

| Layer | Technology |
|---|---|
| Backend Logic | Python, Pandas (vectorized matrix operations) |
| Frontend | Streamlit + custom CSS injection (Zero-Block architecture) |
| Fonts | Fraunces (display) + Plus Jakarta Sans (body) via Google Fonts |
| Data Layer | CSV-based metadata — 9,600 product nodes |
| Algorithm | User-Based Collaborative Filtering with cosine similarity |

---

## ✨ Features (Milestone 4 — Current)

### 🔐 Authentication System
- **Sign In** — credential-based login with session state persistence
- **Sign Up** — full registration flow (name, email, username, password validation)
- Accounts persist across the session; supports multiple users

### 🛍️ Recommendation Hub
- Dropdown product selector across the full 9,600-item catalog
- AI-powered recommendations via user neighborhood clustering
- **Match Score %** — each recommendation shows a compatibility percentage derived from the ratio of similar users who highly rated that product
- Save any product to wishlist with one click

### 🔥 Trending Now
- Dedicated page ranking top 8 products by mean rating across all user sessions
- Live stats: average rating, total interactions, 5-star count, active users

### ❤️ My Wishlist
- Personal saved items list, persistent across pages
- Add/remove products from any page

### 🕘 Recently Viewed
- Sidebar tracker showing last 4 browsed products with thumbnail and price
- Auto-updates as you browse

### ⚙️ System Info
- Model diagnostics: benchmark score, node count, user vectors
- Visual explanation of how the collaborative filtering engine works

---

## 📈 Development Milestones

### Milestone 1 — Data Preparation
- **Goal:** Dataset cleaning and initial matrix generation
- **Result:** Clean ETL pipeline for raw Amazon metadata; established 9,600-node product catalog

### Milestone 2 — Model Building
- **Goal:** Core recommendation engine using cosine similarity
- **Benchmark:** Initial Average User Similarity Score of **0.3973**

### Milestone 3 — Model Refinement & Validation
- **Goal:** Optimize neighborhood clusters and similarity logic
- **Benchmark:** Final accuracy score of **0.6821**

### Milestone 4 — Deployment & UI Overhaul *(Current)*
- **Goal:** Full-stack integration with production-ready UI
- Complete frontend redesign under **ShopSense AI** branding
- Bright animated gradient background with floating blob effects
- Light-theme dropdown fix (overriding Streamlit's default dark popover)
- Added Sign Up page, Wishlist, Trending Now, Recently Viewed, Match Score
- Removed live search input to streamline UX
- Removed eyebrow labels for cleaner page headers
- Normal, readable typography — normalized font sizes throughout

---

## ⚙️ Engineering Challenges Solved

- **Dark Dropdown Override** — Streamlit's `[data-baseweb="popover"]` defaults to dark theme; fixed using targeted CSS injection forcing white background and navy text across all dropdown states
- **UI Artifacting** — Eliminated Streamlit block containers using proprietary CSS engine with `!important` overrides
- **Logic Loop Sync** — Resolved repeating product image errors via dynamic primary key lookups
- **Typography Normalization** — Controlled font size explosion across Streamlit's nested `div`/`p`/`label` elements using scoped CSS resets
- **Session State Management** — Wishlist, recently viewed, and user accounts all managed via `st.session_state` without external database

---

## 🗂️ Project Structure

```
amazon_recommendation_engine/
├── app.py                          # Main Streamlit application
├── amazon_product.csv              # Product metadata (9,600 items)
├── user_item_matrix.csv            # User-item rating matrix (836 users)
├── user_similarity_model.csv       # Precomputed similarity scores
├── fix_images.py                   # Image URL normalization utility
├── Milestone2_Model.ipynb          # Model building notebook
├── Milestone_1_Files.csv/          # Data preparation files
│   ├── Milestone1_Prep.ipynb
│   ├── amazon_product.csv
│   └── user_item_matrix.csv
├── Agile_Template_v0.1.xls         # Project management tracker
└── README.md
```

---

## ▶️ Running Locally

```bash
# Install dependencies
pip install streamlit pandas numpy

# Run the app
streamlit run app.py
```

Default login: `admin` / `kiit123`

---

## ⚖️ License

This project is licensed under the MIT License — see the `LICENSE` file for details.  
Copyright © 2025 Vidzai Digital.