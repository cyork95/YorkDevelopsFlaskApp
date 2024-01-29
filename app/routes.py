from app import app
from flask import render_template
import json
import os


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/portfolio')
def portfolio():
    base_dir = os.path.abspath(os.path.dirname(__file__))

    projects_path = os.path.join(base_dir, 'resources', 'json', 'projects.json')
    with open(projects_path, 'r') as file:
        projects = json.load(file)

    work_history_path = os.path.join(base_dir, 'resources', 'json', 'work_history.json')
    with open(work_history_path, 'r') as file:
        work_history = json.load(file)

    courses_path = os.path.join(base_dir, 'resources', 'json', 'courses.json')
    with open(courses_path, 'r') as file:
        courses = json.load(file)

    education_path = os.path.join(base_dir, 'resources', 'json', 'education.json')
    with open(education_path, 'r') as file:
        education = json.load(file)

    licenses_certifications_path = os.path.join(base_dir, 'resources', 'json', 'licenses_certifications.json')
    with open(licenses_certifications_path, 'r') as file:
        licenses_certifications = json.load(file)

    return render_template('portfolio.html', projects=projects, work_history=work_history,
                           courses=courses, education=education, licenses_certifications=licenses_certifications)

