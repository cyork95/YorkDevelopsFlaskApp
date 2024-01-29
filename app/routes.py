from app import app


@app.route('/about')
def about():
    return 'About Page'
