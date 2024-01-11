from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers.db'
db = SQLAlchemy(app)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)

# Create database tables
db.create_all()

# CRUD Routes
@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    new_teacher = Teacher(name=data['name'], subject=data['subject'])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({"message": "Teacher added successfully"})

@app.route('/update_teacher/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if teacher:
        data = request.get_json()
        teacher.name = data['name']
        teacher.subject = data['subject']
        db.session.commit()
        return jsonify({"message": f"Teacher {teacher_id} updated successfully"})
    else:
        return jsonify({"message": f"Teacher {teacher_id} not found"}), 404

@app.route('/delete_teacher/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()
        return jsonify({"message": f"Teacher {teacher_id} deleted successfully"})
    else:
        return jsonify({"message": f"Teacher {teacher_id} not found"}), 404

@app.route('/get_teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    teachers_list = [{"id": teacher.id, "name": teacher.name, "subject": teacher.subject} for teacher in teachers]
    return jsonify(teachers_list)

if __name__ == '__main__':
    app.run(debug=True)
