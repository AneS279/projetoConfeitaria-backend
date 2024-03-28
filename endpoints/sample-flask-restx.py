from flask import Flask, request
from flask_restx import Api, Resource, fields
from werkzeug.exceptions import NotFound

app = Flask(__name__)
api = Api(app)

# Mock database for storing todos
todos = {}

# Define data model for Todo object
todo_model = api.model('Todo', {
    'task': fields.String(required=True, description='The task details')
})

# API Routes
@api.route('/todos')
class TodoList(Resource):
    @api.marshal_with(todo_model, envelope='data')
    def get(self):
        """Get all todos"""
        return todos

    @api.expect(todo_model)
    @api.marshal_with(todo_model, envelope='data')
    def post(self):
        """Create a new todo"""
        todo = api.payload
        task = todo['task']
        todo_id = len(todos) + 1
        todos[todo_id] = {'id': todo_id, 'task': task}
        return todos[todo_id], 201

@api.route('/todos/<int:todo_id>')
class Todo(Resource):
    @api.marshal_with(todo_model, envelope='data')
    def get(self, todo_id):
        """Get a todo by ID"""
        if todo_id not in todos:
            raise NotFound(f'Todo with id {todo_id} not found')
        return todos[todo_id]

    @api.expect(todo_model)
    @api.marshal_with(todo_model, envelope='data')
    def put(self, todo_id):
        """Update a todo by ID"""
        if todo_id not in todos:
            raise NotFound(f'Todo with id {todo_id} not found')
        todo = api.payload
        todos[todo_id] = {'id': todo_id, 'task': todo['task']}
        return todos[todo_id]

    @api.doc(responses={204: 'Todo deleted'})
    def delete(self, todo_id):
        """Delete a todo by ID"""
        if todo_id not in todos:
            raise NotFound(f'Todo with id {todo_id} not found')
        del todos[todo_id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
