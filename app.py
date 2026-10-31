from flask import Flask, request, jsonify

class Task:
    def __init__(self, title, priority, task_id):
        self.title = title
        self.priority = priority
        self.task_id = task_id
        self.done = False
        
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        
    def add_task(self, title, priority):
        new_task = Task(title, priority, self.next_id)
        
        self.tasks.append(new_task)
        self.next_id += 1
        
    def get_tasks(self):
        return sorted(self.tasks, key=lambda task: task.priority)
    
    def toggle_done(self, task_id):
        for i in self.tasks:
            if i.task_id == task_id:
                i.done = not i.done
                return i
            
    def delete_task(self, task_id):
        self.tasks = [x for x in self.tasks if task_id != x.task_id]
        return self.tasks
    
manager = TaskManager()    

app = Flask(__name__)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    title = data["title"]
    priority = data["priority"]
    
    result = manager.add_task(title, priority)
    return jsonify({"Message": "Task added"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    getting = manager.get_tasks()
    
    result = [{"title": task.title, "priority": task.priority, "done": task.done, "task_id": task.task_id} for task in getting]
    return jsonify({"result": result})

@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    updated_task = manager.toggle_done(int(task_id))

    if updated_task:
        return jsonify({"Message": "Task updated"})
    
    else:
        return jsonify({"Error": "Task not found"}), 404
    
    
@app.route("/tasks/<task_id>", methods=["DELETE"])
def remove_task(task_id):
    length = len(manager.tasks)
    removed_task = manager.delete_task(int(task_id))
    new_length = len(manager.tasks)
    
    if new_length < length:
        return jsonify({"Message": "Task removed"})
    
    else:
        return jsonify({"Error": "Task not found"}), 404

app.run()