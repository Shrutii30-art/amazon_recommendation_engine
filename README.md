AI-Driven Product Recommendation Engine



🚀 Project Overview
An advanced AI-enabled recommendation engine utilizing User-Based Collaborative Filtering (UBCF) and an N-tier web architecture. The system is designed to solve the "Paradox of Choice" in e-commerce by delivering personalized, high-fidelity product suggestions from a massive catalog.
+2

🛠️ Technical Stack

Backend Logic: Python, Pandas (Vectorized operations for high-speed lookup) 


Frontend Interface: Streamlit with custom Zero-Block CSS injection 
+1


Data Layer: CSV-based metadata optimized for 9,600 product nodes 
+1


Algorithm: User-Based Collaborative Filtering with Matrix Factorization 
+1

📈 Development Milestones
Milestone 1: Data Preparation

Goal: Dataset cleaning and initial matrix generation.


Result: Established a clean ETL pipeline for raw Amazon metadata.

Milestone 2: Model Building

Goal: Developed core engine using Cosine Similarity.

Initial Benchmark: Achieved an initial Average User Similarity Score of 0.3973.

Milestone 3: Model Refinement & Validation

Goal: Optimization of neighborhood clusters and similarity logic.


Final Benchmark: Successfully achieved an accuracy score of 0.6821.
+1

Milestone 4: Deployment & UI Finalization (Current)

Goal: Full-stack integration and production-ready "Shopping Hub".

Key Features:


Catalog Expansion: Now supports 9,600 unique electronics.
+1


User Training: Engine trained on 836 unique shopper vectors.
+1


Dynamic ID Mapping: Real-time lookup for unique, refreshed recommendations.
+2


Visual Consistency: Implemented object-fit scaling to prevent image distortion.

⚙️ Engineering Challenges Solved

UI Artifacting: Eliminated Streamlit "block" containers using a proprietary CSS engine.


Logic Loop Synchronization: Resolved repeating product image errors by implementing dynamic primary key lookups.
+1


Indentation Errors: Fixed critical syntax failures during complex HTML/Python integration.

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.
Copyright (c) 2025 Vidzai Digital.