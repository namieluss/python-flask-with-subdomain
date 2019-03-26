## Python Flask with subdomain


### Setup
The project requires Flask to run.
```
pip install -r requirements.txt
```


### Run
The application is compatible with Python 3.4 upwards.

To test using python 3:
```
python3 app.py
```


### Setup a Testing in a Development Environment
Flask does not support subdomains on localhost or on host names without a top-level domain (TLD) identifier. For the example app below, I added the following entry to `/etc/hosts`:
```
127.0.0.1 flask-subdomain.com
127.0.0.1 user1.flask-subdomain.com
127.0.0.1 user2.flask-subdomain.com
.
.
127.0.0.1 usern.flask-subdomain.com
```



## License
- Author is [`Suleiman`](http://namieluss.com)
- This repository uses the [MIT License](/LICENSE).