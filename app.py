from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Simples armazenamento em memória (lista de dicionários)
# Estrutura de cada tarefa: { "id": int, "title": str, "description": str, "done": bool, "priority": int }
tasks = []
next_id = 1

def find_task(tid):
    return next((t for t in tasks if t["id"] == tid), None)

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks), 200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    t = find_task(task_id)
    if not t:
        return jsonify({"error":"Tarefa não encontrada"}), 404
    return jsonify(t), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json() or {}
    title = data.get("title")
    if not title or not isinstance(title, str):
        return jsonify({"error":"Campo 'title' é obrigatório e deve ser string"}), 400
    description = data.get("description","")
    priority = data.get("priority", 3)
    try:
        priority = int(priority)
    except:
        priority = 3
    task = {"id": next_id, "title": title, "description": description, "done": False, "priority": priority}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    t = find_task(task_id)
    if not t:
        return jsonify({"error":"Tarefa não encontrada"}), 404
    data = request.get_json() or {}
    if "title" in data:
        if not isinstance(data["title"], str):
            return jsonify({"error":"Campo 'title' deve ser string"}), 400
        t["title"] = data["title"]
    if "description" in data:
        t["description"] = data["description"]
    if "done" in data:
        t["done"] = bool(data["done"])
    if "priority" in data:
        try:
            t["priority"] = int(data["priority"])
        except:
            pass
    return jsonify(t), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    t = find_task(task_id)
    if not t:
        return jsonify({"error":"Tarefa não encontrada"}), 404
    tasks.remove(t)
    return jsonify({"message":"Removida"}), 200

# helper for tests to reset state
@app.route("/_test/reset", methods=["POST"])
def _reset():
    global tasks, next_id
    tasks = []
    next_id = 1
    return jsonify({"ok":True}), 200

if __name__ == "__main__":
    app.run()
