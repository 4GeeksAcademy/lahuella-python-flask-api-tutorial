from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False }, { "label": "My second task", "done": False }, { "label": "My third task", "done": False } ]

@app.route('/todos', methods=['GET'])
def my_todos():
    json_text = jsonify(todos)

    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    todos.append(request_body)

    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)