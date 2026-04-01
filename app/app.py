from flask import Flask, request, jsonify
import json
import os
import sqlite3

app = Flask(__name__)

DB = "tasks.db"

#Conexion DB
def get_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

#Inicializar DB
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done BOOLEAN NOT NULL
    )
    """)
#Crear tarea
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error":"Falta el campo 'title'"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (data["title"],False)
    )

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "id" : new_id,
        "title" : data["title"],
        "done" : False
    }), 201

#Obtener tareas
@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, done FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for row in rows:
        tasks.append({
            "id" : row["id"],
            "title" : row["title"],
            "done" : bool(row["done"])
        })
    return jsonify(tasks)

#Actualizar tarea
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_tasks(id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    task = cursor.fetchone()

    if not task:
        conn.close()
        return jsonify({"error":"Tarea no encontrada"}), 404
    
    new_title = data.get("title", task["title"])
    new_done = data.get("done", task["done"])

    cursor.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (new_title, new_done, id)
    )
    
    conn.commit()
    conn.close()

    return jsonify({
        "id" : id,
        "title" : new_title,
        "done" : bool(new_done)
    })

#Eliminar Tarea
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error" : "Tarea no encontrada"}), 404

    conn.close()
    return jsonify({"message":"Tarea eliminada"})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)









