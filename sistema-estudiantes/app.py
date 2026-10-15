from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "cambia-esta-clave-antes-de-publicar"
DB_PATH = Path(__file__).with_name("estudiantes.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                rut TEXT NOT NULL UNIQUE,
                curso TEXT NOT NULL
            )
        """)

@app.route("/")
def index():
    with get_db() as conn:
        estudiantes = conn.execute(
            "SELECT id, nombre, rut, curso FROM estudiantes ORDER BY id DESC"
        ).fetchall()
    return render_template("index.html", estudiantes=estudiantes)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre", "").strip()
    rut = request.form.get("rut", "").strip()
    curso = request.form.get("curso", "").strip()

    if not nombre or not rut or not curso:
        flash("Completa todos los campos.", "error")
        return redirect(url_for("index"))

    try:
        with get_db() as conn:
            conn.execute(
                "INSERT INTO estudiantes (nombre, rut, curso) VALUES (?, ?, ?)",
                (nombre, rut, curso)
            )
        flash("Estudiante agregado correctamente.", "success")
    except sqlite3.IntegrityError:
        flash("Ya existe un estudiante con ese RUT.", "error")
    return redirect(url_for("index"))

@app.route("/eliminar/<int:estudiante_id>", methods=["POST"])
def eliminar(estudiante_id):
    with get_db() as conn:
        conn.execute("DELETE FROM estudiantes WHERE id = ?", (estudiante_id,))
    flash("Estudiante eliminado.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
