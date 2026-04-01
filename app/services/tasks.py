from app.db import get_connection
from flask_jwt_extended import get_jwt_identity

def get_all_tasks():
    current_user_id = get_jwt_identity() #Se obtiene el id desde el token

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (current_user_id,))
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for row in rows:
        tasks.append({
            "id" : row["id"],
            "title": row["title"],
            "done" : bool(row["done"])
        })
    return tasks

def create_task(title):
    current_user_id = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, done, user_id) VALUES (?, ?, ?)",
        (title, False, current_user_id)
    )

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return {
        "id" : new_id,
        "title" : title,
        "done" : False
    }

def update_task(task_id, data):
    current_user_id = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ? AND user_id = ?", (task_id, current_user_id))
    task = cursor.fetchone()

    if not task:
        conn.close()
        return None

    new_title = data.get("title", task["title"])
    new_done = data.get("done", task["done"])

    cursor.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ? AND user_id = ?",
        (new_title, new_done, task_id, current_user_id)
    )
    
    conn.commit()
    conn.close()

    return{
        "id" : task_id,
        "title" : new_title,
        "done": new_done
    }

def delete_task(task_id):
    current_user_id = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", (task_id, current_user_id))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return False

    conn.close()
    return True
    

