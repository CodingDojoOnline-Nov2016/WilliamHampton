from flask import Flask, render_template, request, redirect,session,flash
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/result', methods = ['post'])
def results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(name) <1:
        return render_template('results.html',name = "Name Can not be empty", location = location, language = language, comment = comment)
    if len(location) <1:
        return render_template('results.html',name = name, location ="Location Can not be empty", language = language, comment = comment)
    if len(language) <1:
        return render_template('results.html',name = name, location = location, language = "Language Can not be empty", comment = comment)
    if len(comment) <1:
        return render_template('results.html',name = name, location = location, language = language, comment = "Comment can not be empty")
    if len(comment) >120:
        return render_template('results.html',name = name, location = location, language = language, comment = "Comment is to long to display")
    else:
        return render_template('results.html',name = name, location = location, language = language, comment = comment)
app.run(debug=True)
