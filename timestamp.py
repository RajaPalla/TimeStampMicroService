from flask import Flask, render_template
import json
from time import strftime, gmtime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<date>')
def timestamp(date):
    dictTime = {}
    #if isinstance(date, int):
    if type(int(date)) == type(2):
        dictTime['unix'] = str(date)
        dictTime['natural'] = strftime("%d %B %Y", gmtime(int(date)/1000))
    return json.dumps(dictTime)

    # else parse string date, probably time.strptime.


if __name__ == "__main__":
    app.run(debug=True)
