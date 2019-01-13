from flask import Flask, redirect, url_for, request, render_template, jsonify
from inputProblemData import get_problem_text
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/problem',methods = ['GET'])
def get_input_problem():
    op = request.args.get('op')
    print(op)
    problem_text = get_problem_text(op)
    print (problem_text)
    return jsonify({'problem':problem_text})


app.debug = True
if __name__ == '__main__':
    app.run()
