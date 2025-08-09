### Setup Python Virtual Environment (Optional but Recommended)

1. **Create a virtual environment** (run this in your backend folder):

```bash
python -m venv env

.\env\Scripts\Activate

```




# RuralEdu Course Platform

This project provides a platform to browse free online courses from multiple platforms.  
It uses a Flask backend with MongoDB to serve course data and a React frontend built with Vite to display the courses.

---

## Prerequisites

- Python 3.x installed  
- Node.js and npm installed  
- MongoDB installed and running locally (default port 27017)

---

## Setup Instructions

### 1. Import Course Data

You should have a JSON file (e.g., `courses_export.json`) containing all courses.

Import this data into your local MongoDB database:

```bash
mongoimport --db Rural --collection Courses --file courses_export.json --jsonArray

```

### 2. Install Dependencies

**Backend:**
```Bash
pip install -r requirements.txt

npm install
```


### 3.Run

```Bash
npm start



