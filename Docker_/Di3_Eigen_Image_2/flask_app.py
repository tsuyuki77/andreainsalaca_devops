from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_FILE = "app.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            body TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/health")
def health():
    return "OK"

@app.route("/posts", methods=["POST"])
def add_post():
    data = request.get_json()

    title = data["title"]
    body = data["body"]

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO posts (title, body) VALUES (?, ?)", (title, body))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()

    return jsonify({"id": new_id, "title": title, "body": body})

@app.route("/posts", methods=["GET"])
def list_posts():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, title, body FROM posts")
    rows = cur.fetchall()
    conn.close()

    posts = []
    for r in rows:
        posts.append({"id": r[0], "title": r[1], "body": r[2]})

    return jsonify(posts)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5555)
