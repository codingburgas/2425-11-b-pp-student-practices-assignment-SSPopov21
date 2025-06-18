# Project Documentation

## Project Overview
This project is a web application that combines a Flask backend (Python) with a React frontend (TypeScript). It features job offers, surveys, and an AI/ML module for predictions and analytics.

## Features
- User registration and login
- Job offer creation and application
- Survey system
- Admin dashboard
- AI/ML predictions

## Installation

### Backend (Flask)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   flask db upgrade
   ```
5. Run the backend server:
   ```bash
   flask run
   ```

### Frontend (React)
1. Navigate to the `src/` directory (if using Vite):
   ```bash
   cd src
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend development server:
   ```bash
   npm run dev
   ```

## Usage
- Access the frontend at `http://localhost:5173` (default Vite port)
- The backend API runs at `http://localhost:5000` (default Flask port)

## Folder Structure
- `app/` - Flask backend
- `src/` - React frontend
- `docs/` - Documentation