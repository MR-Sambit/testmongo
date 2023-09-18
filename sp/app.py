from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/project_data.projectdata"
mongo = PyMongo(app)

# Define a project schema (if needed)
# project_schema = ...

# Endpoint to save project data
@app.route('/student_project', methods=['POST'])
def add_project():
    project_data = request.get_json()
    # Create a new project document (you may want to add validation and error handling)
    project_id = mongo.db.projects.insert_one(project_data).inserted_id
    return jsonify({"message": "Project added successfully", "project_id": str(project_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)
