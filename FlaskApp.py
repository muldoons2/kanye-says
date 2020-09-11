import os
import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
    ye_quote= requests.get("https://api.kanye.rest").json()['quote']
    return render_template('kanye.html',value=ye_quote)

# @app.route("/kanye")
# def home():
#     ye_quote= requests.get("https://api.kanye.rest").json()['quote']
#     return render_template('kanye.html',value=ye_quote)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# Credits: https://kanye.rest/
