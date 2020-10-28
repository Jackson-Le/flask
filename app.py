from flask import Flask, request, render_template, jsonify
from ShortestPath import *

app = Flask(__name__)

def do_something(origin, dest):
    o = int(origin)
    d = int(dest)
    print(get_shortest_path_to(o, d)[0])
    return get_shortest_path_to(o, d)[0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    combine = do_something(text1,text2)
    result = {"output": combine}
    result = {str(key): value for key, value in result.items()}
    print(combine)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
