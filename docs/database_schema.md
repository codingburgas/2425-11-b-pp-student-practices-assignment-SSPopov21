# Database Schema (ERD)

This project uses SQLAlchemy ORM with the following main tables:

---

## User
- **id** (Integer, PK)
- **username** (String, unique, not null)
- **email** (String, unique, not null)
- **password_hash** (String)
- **role** (String, not null, default: 'worker')  // 'worker', 'employer', or 'admin'
- **created_at** (DateTime, default: now)
- **is_admin** (Boolean, default: False)

**Relationships:**
- One-to-many: User → Survey (user.surveys)
- One-to-many: User → JobOffer (if employer)

---

## Survey
- **id** (Integer, PK)
- **user_id** (Integer, FK to User.id, not null)
- **created_at** (DateTime, default: now)
- **is_public** (Boolean, default: False)
- **success** (Boolean) // Target variable
- **years_experience** (Float, not null)
- **education_level** (Integer, not null) // 1: High School, 2: Bachelor's, 3: Master's, 4: PhD
- **num_skills** (Integer, not null)
- **industry_type** (String, not null)
- **prev_job_changes** (Integer, not null)
- **certifications** (Integer, not null)
- **language_proficiency** (Float, not null, 0-1)
- **interview_prep_score** (Float, not null, 0-1)

**Relationships:**
- Many-to-one: Survey → User

---

## JobOffer
- **id** (Integer, PK)
- **employer_id** (Integer, FK to User.id, not null)
- **title** (String, not null)
- **description** (Text, not null)
- **requirements** (Text, not null)
- **location** (String, not null)
- **salary_range** (String)
- **industry_type** (String, not null)
- **required_experience** (Float, not null)
- **education_level** (Integer, not null) // 1: High School, 2: Bachelor's, 3: Master's, 4: PhD
- **created_at** (DateTime, default: now)
- **is_active** (Boolean, default: True)

**Relationships:**
- Many-to-one: JobOffer → User (employer)

---

## Relationships Diagram (Text)

- User (1) ────< Survey (many)
- User (1) ────< JobOffer (many)

---

**Note:**
- All tables use SQLAlchemy's default autoincrementing primary keys.
- Foreign keys enforce referential integrity.
- See `app/models/` for full model definitions. 