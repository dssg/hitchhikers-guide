from flask import render_template, request, url_for, jsonify
from webapp import app, model, draw

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        posttext = request.form['posttext']
        if posttext is not "":
            result = model.find_most_similar_topic(posttext, 10)
            labels = list(map(lambda i: i[0], result))
            values = list(map(lambda i: i[1], result))
            script, div = draw.make_bar_plot(labels, values)
            print(result)
            return render_template("index.html", results=result, script=script, div=div)
    return render_template("index.html")

@app.route('/<word>/get_similar/<int:topn>', methods=['GET'])
def get_similar(word, topn):
    try:
        result = model.find_most_similar(word, topn)
        print(result)
        return jsonify(results=result)
    except:
        print('there are some problems')
        return jsonify({"sorry": "Sorry, no results! Please try again."}), 500

