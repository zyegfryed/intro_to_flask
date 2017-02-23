# Introduction to Flask

Source code for the Introduction to Flask presentation given at Swisscom Digital Lab
[meetup](https://www.meetup.com/Swisscom-Digital-Lab/events/237521928/).


## Installation

    $ pip install -r requirements.txt


## Usage

Run it with:

    $ export FLASK_APP=app.y
    $ flask run
     * Serving Flask app "app"
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Verify it's working:

    $ curl http://127.0.0.1:5000/
    Hello, World!
