from app.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        conn.close()
        return False #El usuario ya existe

    hashed_password = generate_password_hash(password)

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()
    conn.close()
    return True

def check_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = %s", (username,))
    row = cursor.fetchone()
    conn.close()
    if row and check_password_hash(row['password'], password):
        return row['id']
    return None

def update_password(user_id, current_password, new_password):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return False

    if not check_password_hash(row['password'], current_password):
        conn.close()
        return False

    new_hashed = generate_password_hash(new_password)

    cursor.execute(
        "UPDATE users SET password = %s WHERE id = %s",
        (new_hashed, user_id)
    )

    conn.commit()
    conn.close()

    return True
