# Introduction to Flask

Source code for the Introduction to Flask presentation given at Swisscom Digital Lab
[meetup](https://www.meetup.com/Swisscom-Digital-Lab/events/237521928/).

[Create a Facebook App and Page](https://developers.facebook.com/docs/messenger-platform/guides/setup#app_and_page_setup) and generate a [Page Access Token](https://developers.facebook.com/docs/messenger-platform/guides/setup#page_access_token).

Open a terminal window and run the chatbot using the aforementioned Page Access
Token:

    $ export FLASK_APP=app.y
    $ export FB_VERIFY_TOKEN=<SECRET>
    $ export FB_PAGE_TOKEN=<PAGE_ACCES_TOKEN>
    $ flask run
     * Serving Flask app "app"
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Ensure [nrgok](https://ngrok.com/download) is installed, open a new terminal
window and create an HTTP(S) tunneling on port `5000`::

    $ ngrok http 5000
    ...
    Forwarding                    https://ca31e2d2.ngrok.io -> localhost:5000
    ...

Then, [setup a Webhook](https://developers.facebook.com/docs/messenger-platform/guides/setup#webhook_setup) with the resulted HTTPS forwarding address and the previously defined `SECRET`.

Chat with the bot either through the Messages tab of your Facebook Page or via
Messenger App on your smartphone.
