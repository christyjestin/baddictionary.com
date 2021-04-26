from flask import Flask, render_template, request, jsonify, redirect

from flask_cors import CORS, cross_origin

import functions as f

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/browse', methods=['POST', 'GET'])
def redirect_to_display():
    query=request.form.get("query")
    query=query.split()
    query="%20".join(query)
    return redirect("/browse/" + query)

@app.route('/browse/<query>', methods=['POST', 'GET'])
def show_result(query):
    query = query.split("%20")
    query = " ".join(query)
    header, pos, definition = f.page(query)
    return render_template("display.html", header = str(header), pos = str(pos), definition = str(definition))

if __name__ == '__main__':
    app.run(debug=True)
