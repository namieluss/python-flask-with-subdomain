__author__ = 'Suleiman'

from functools import wraps
from flask import g, request, redirect, url_for

from urllib.parse import urlparse


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        subdomain = urlparse(request.url).hostname.split('.')[0]
        if g.user != subdomain:
            return redirect(url_for('login', next=request.url, user=subdomain))

        return f(*args, **kwargs)

    return decorated_function
