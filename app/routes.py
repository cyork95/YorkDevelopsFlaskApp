import json
import os

import requests
from flask import render_template, request, jsonify

from app import app

from bs4 import BeautifulSoup


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


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


@app.route('/horoscope')
def horoscope():
    return render_template('horoscope.html')


@app.route('/get_horoscope', methods=['GET'])
def get_horoscope():
    sign = request.args.get('sign')
    if not sign:
        return jsonify({"error": "No sign provided"}), 400

    # URLs for main and love horoscopes
    main_url = f"https://www.astrology.com/horoscope/daily/{sign}.html"
    love_url = f"https://www.astrology.com/horoscope/daily-love/{sign}.html"
    work_url = f"https://www.astrology.com/horoscope/daily-work/{sign}.html"
    dating_url = f"https://www.astrology.com/horoscope/daily-dating/{sign}.html"

    main_response = requests.get(main_url)
    love_response = requests.get(love_url)
    work_response = requests.get(work_url)
    dating_response = requests.get(dating_url)

    if (main_response.status_code == 200 and love_response.status_code == 200 and work_response.status_code == 200 and
            dating_response.status_code == 200):
        main_soup = BeautifulSoup(main_response.content, 'html.parser')
        love_soup = BeautifulSoup(love_response.content, 'html.parser')
        work_soup = BeautifulSoup(work_response.content, 'html.parser')
        dating_soup = BeautifulSoup(dating_response.content, 'html.parser')

        # Extracting the main daily horoscope
        main_content_div = main_soup.find('div', id='content')
        date_span = main_soup.find('span', id='content-date')

        # Initialize all variables to None or a default value
        main_horoscope_text = None
        love_horoscope_text = None
        work_horoscope_text = None
        dating_horoscope_text = None
        singles_horoscope_text = None
        beauty_horoscope_text = None
        food_horoscope_text = None
        home_horoscope_text = None
        cat_horoscope_text = None
        bonus_horoscope_text = None

        full_text = ""
        if main_content_div and main_content_div.p and date_span:
            date_text = date_span.get_text(strip=True)
            main_horoscope_text = main_content_div.p.get_text(strip=True)
            full_text = f"{date_text}: {main_horoscope_text}\n\n"

            sections = [('content-food', 'Daily Food Horoscope'),
                        ('content-home', 'Daily Home Horoscope'),
                        ('content-cat', 'Daily Cat Horoscope'),
                        ('content-bonus', 'Daily Bonus Horoscope')]

            for section_id, section_title in sections:
                section_div = main_soup.find('div', id=section_id)
                if section_div:
                    section_text = section_div.get_text(strip=True)
                    if section_id == 'content-food':
                        food_horoscope_text = f"{section_title}: {section_text}\n\n"
                    elif section_id == 'content-home':
                        home_horoscope_text = f"{section_title}: {section_text}\n\n"
                    elif section_id == 'content-cat':
                        cat_horoscope_text = f"{section_title}: {section_text}\n\n"
                    else:
                        bonus_horoscope_text = f"{section_title}: {section_text}\n\n"
                    full_text += f"{section_title}: {section_text}\n\n"

            # Extracting the love horoscope
            love_content_div = love_soup.find('div', id='content')
            if love_content_div and love_content_div.p:
                love_horoscope_text = love_content_div.p.get_text(strip=True)
                full_text += f"Daily Love Horoscope: {love_horoscope_text}\n\n"

            # Extracting the couples horoscope
            couples_content_div = love_soup.find('div', id='content-couples')
            if couples_content_div:
                couples_horoscope_text = couples_content_div.get_text(strip=True)
                full_text += f"Daily Couples Horoscope: {couples_horoscope_text}\n\n"

            # Extracting the work horoscope
            work_content_div = work_soup.find('div', id='content')
            if work_content_div and work_content_div.p:
                work_horoscope_text = work_content_div.p.get_text(strip=True)
                full_text += f"Daily Work Horoscope: {work_horoscope_text}\n\n"

            # Extracting the finances horoscope
            finances_content_div = work_soup.find('div', id='content-finances')
            if finances_content_div:
                finances_horoscope_text = finances_content_div.get_text(strip=True)
                full_text += f"Daily Finances Horoscope: {finances_horoscope_text}\n\n"

            # Extracting the dating horoscope
            dating_content_div = dating_soup.find('div', id='content')
            if dating_content_div:
                dating_horoscope_text = dating_content_div.get_text(strip=True)
                full_text += f"Daily Dating Horoscope: {dating_horoscope_text}\n\n"

            # Extracting the singles horoscope
            singles_content_div = dating_soup.find('div', id='content-singles')
            if singles_content_div:
                singles_horoscope_text = singles_content_div.get_text(strip=True)
                full_text += f"Daily Singles Horoscope: {singles_horoscope_text}\n\n"

            # Extracting the beauty horoscope
            beauty_content_div = dating_soup.find('div', id='content-beauty')
            if beauty_content_div:
                beauty_horoscope_text = beauty_content_div.get_text(strip=True)
                full_text += f"Daily Beauty Horoscope: {beauty_horoscope_text}\n\n"

            # Adding credit for the source
            full_text += "Horoscope source: astrology.com"

            return jsonify({
                "daily": main_horoscope_text,
                "love": love_horoscope_text,
                "work": work_horoscope_text,
                "dating": dating_horoscope_text,
                "singles": singles_horoscope_text,
                "beauty": beauty_horoscope_text,
                "food": food_horoscope_text,
                "home": home_horoscope_text,
                "cat": cat_horoscope_text,
                "bonus": bonus_horoscope_text
            })
        else:
            return jsonify({"error": "Horoscope content not found"}), 404
    else:
        return jsonify({"error": "Error fetching horoscope"}), 500


def fetch_horoscope(sign):
    # Placeholder for fetching horoscope data
    # In reality, this would fetch data from an API or database
    return f"Today's horoscope for {sign.capitalize()} is ..."
