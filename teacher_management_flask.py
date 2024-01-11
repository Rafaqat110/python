# teacher_management_flask.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/teacher_management'
mongo = PyMongo(app)

@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    teachers = mongo.db.teachers
    teacher_id = teachers.insert_one(data).inserted_id
    return jsonify({"message": f"Teacher added successfully with ID: {teacher_id}"}), 201

@app.route('/update_teacher/<teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    data = request.get_json()
    teachers = mongo.db.teachers
    result = teachers.update_one({'_id': teacher_id}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({"message": f"Teacher {teacher_id} updated successfully"})
    else:
        return jsonify({"message": f"Teacher {teacher_id} not found"}), 404

@app.route('/delete_teacher/<teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    teachers = mongo.db.teachers
    result = teachers.delete_one({'_id': teacher_id})
    if result.deleted_count > 0:
        return jsonify({"message": f"Teacher {teacher_id} deleted successfully"})
    else:
        return jsonify({"message": f"Teacher {teacher_id} not found"}), 404

@app.route('/get_teachers', methods=['GET'])
def get_teachers():
    teachers = mongo.db.teachers.find()
    teachers_list = [{"id": str(teacher['_id']), "name": teacher['name'], "subject": teacher['subject']} for teacher in teachers]
    return jsonify(teachers_list)

if __name__ == '__main__':
    app.run(debug=True)
