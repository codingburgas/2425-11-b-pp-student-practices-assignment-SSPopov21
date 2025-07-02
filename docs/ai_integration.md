# AI/ML Integration

This project integrates a custom machine learning model to predict job application success. Below is an overview of how AI is used and where to find the relevant code.

---

## 1. Model Definition & Training (Backend)
- **File:** `app/ml/model.py`
- **Class:** `JobSuccessPredictor`
- **Algorithm:** Logistic Regression (scikit-learn)
- **Features Used:**
  - Years of experience
  - Education level
  - Number of skills
  - Previous job changes
  - Certifications
  - Language proficiency
  - Interview preparation score
- **Training:**
  - Model is trained on survey data (`Survey` table).
  - Training can be triggered via admin or automatically if no model exists.
  - Model and scaler are saved as `.pkl` files for reuse.

---

## 2. Prediction Usage (Backend)
- **Prediction:**
  - The model predicts the probability of job application success for a given survey or job application.
  - Used in user dashboards, job application forms, and quick prediction endpoints.
- **Key Files:**
  - `app/routes/job_offers.py`:
    - `/job-offers/<id>/apply` — Predicts success for a job application.
    - `/quick-predict/<job_id>` — Quick prediction based on minimal data.
    - `/predict` — API endpoint for frontend to get predictions based on skills.
  - `app/routes/main.py`:
    - `/dashboard` — Shows predictions for user and public surveys.
  - `app/routes/survey.py`:
    - Handles survey submission, which is used for model training.

---

## 3. Frontend Integration
- **File:** `src/utils/mlModel.ts`
  - Contains a TypeScript class (`JobSuccessModel`) that mimics backend logic for instant UI feedback.
  - Used for local predictions and visualizations.
- **File:** `src/pages/PredictionsPage.tsx`
  - Calls backend API (`/job-offers/predict`) to get real ML predictions.
  - Displays probability, key factors, and recommendations to the user.
- **Workflow:**
  - User submits job application or survey.
  - Frontend may show instant prediction (mocked or real).
  - For real predictions, frontend sends data to backend API, receives probability and recommendations, and displays them.

---

## 4. Model Workflow Summary
1. **Data Collection:** Users fill surveys and job applications.
2. **Model Training:** Admin or system trains the model on survey data.
3. **Prediction:**
   - Backend: Predicts success probability for applications and surveys.
   - Frontend: Requests predictions via API and displays results.
4. **Feedback:** Users see their predicted probability and key factors for success.

---

**See also:**
- `app/ml/model.py` for model code
- `app/routes/` for API endpoints
- `src/utils/mlModel.ts` and `src/pages/PredictionsPage.tsx` for frontend integration 