# AI-Enabled Recommendation Engine - Group 1

## Milestone 1: Data Preparation
**Status:** Completed
**Deadline:** Jan 8

### Objective
Prepare clean, structured datasets and build a user-item interaction matrix for model development.

### Work Completed
- **Data Collection:** Collected user reviews and product data from the Amazon dataset.
- **Data Cleaning:** Handled inconsistencies by removing missing values and renaming columns for standardization.
- **Matrix Generation:** Successfully built a User-Item Interaction Matrix.
  - **Result:** 836 Users x 66 Products.

### Files in this Milestone
- `Milestone1_Prep.ipynb`: Python code for data processing.
- `user_item_matrix.csv`: The final structured matrix ready for training.

## Milestone 2: Model Building
- **Objective:** Developed and trained the core recommendation engine.
- **Algorithm:** Used Cosine Similarity to identify user-to-user rating patterns.
- **Benchmark:** Achieved an initial Average User Similarity Score of 0.3973.