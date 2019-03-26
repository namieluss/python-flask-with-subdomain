__author__ = 'Suleiman'

from urllib.parse import urlparse

from flask import Flask, g, session, request, render_template, redirect, url_for
from helper import login_required
from model import users

app = Flask(__name__)

""" server configurations """
app.config.from_object('config.DevConfig')

""" add static file route to allow loading of static files irrespective of which subdomain """
app.add_url_rule('/static/<path:filename>', endpoint='static', subdomain='<user>', view_func=app.send_static_file)


@app.errorhandler(404)
def error_404(error):
    return "Oops, page not found !!!!"


@app.url_value_preprocessor
def before_route(endpoint, values):
    """
    do some more logic here, prevent certain sub-domains etc.
    """
    if endpoint is not 'login' and values is not None:
        values.pop('user', None)
    pass


@app.before_request
def start():
    """
    init globals and set the schema search path for the current request.
    """
    g.user = session.get('user', None)
    current_url = urlparse(request.url)
    subdomain = current_url.hostname.split('.')

    if subdomain.__len__() > 2:
        """
        redirect to home page
        """
        if current_url.path == "/":
            return redirect(url_for('index'))
        pass
    pass


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'], subdomain='<user>')
def login(user):
    if request.method == 'POST':
        """
        do some stuffs i.e. authenticate user
        """
        username = request.form.get('user_name')
        userpass = request.form.get('user_pass')

        if users.get(username, {}).get('site', '') == user and users[username]['pass'] == userpass:
            """
            set new login user to current session
            """
            session['user'] = users[username].get("site")
            return redirect('/profile')

        return render_template('login.html', data={"msg": "Oops, invalid credentials, failed to login !!!"}, user=user)

    if g.user == user:
        """
        redirect to user page if user already logged in
        """
        return redirect(url_for('profile', user=user))

    return render_template('login.html', data={}, user=user)


@app.route('/logout', subdomain='<user>')
def logout():
    session.pop('user', 0)
    return redirect(url_for('index'))


@app.route('/profile', methods=['POST', 'GET'], subdomain='<user>')
@login_required
def profile():
    user = session.get('user')
    return render_template('profile.html', user=session.get('user'))


if __name__ == '__main__':
    app.run(debug=True)
