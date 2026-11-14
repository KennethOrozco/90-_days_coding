import json

def load_tasks():
    try:
        file_path = "tasks.json"
        with open(file_path, "r") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        content = []
        return content

def save_tasks(tasks):
  file_path = "tasks.json"
  with open(file_path, "w") as file:
        json.dump(tasks, file)


def display_tasks(tasks):
    if tasks:
        for task in tasks:
            if task['completed']:
                status = "Complete"
            else:
                status = "Incomplete"
            print(f"{task['id']}. {task['task']} [{status}]")
    else:
        print("There are no tasks to display.")
        

def add_task(tasks):
    while True:
        user_task = input("Describe your task: ")
        if  user_task.strip():
            break
        print("Please describe your task!")

    if tasks:
        id_ = tasks[-1]['id'] + 1
    else:
        id_ =  1
    user_data = {
        "id": id_, 
        "task": user_task,
        "completed": False
        }      
    tasks.append(user_data)  
    save_tasks(tasks)
    
def complete_task(tasks):
    if tasks:
        display_tasks(tasks)
        while True:
            try:
                user_id = int(input("Choose task ID: "))
                found = False
                for task in tasks:
                    if user_id == task['id']:
                        task['completed'] = True
                        found = True
                        break
                if found:
                    break
                else:
                    print("Not Valid ID")
            except ValueError:
                print("Type a number!")
        save_tasks(tasks)
    else:
        print("There are no tasks to complete.")
        

def delete_task(tasks):
    
    if tasks:
        display_tasks(tasks)
        while True:
            try:
                delete_id = int(input("Choose the ID of the task you would like to delete: "))
                found = False
                for task in tasks:
                    if delete_id == task['id']:
                        tasks.remove(task)
                        found = True
                        break
                if found:
                    break
                if not found:
                    print("Not Valid ID")
            except ValueError:
                print("Type a number!")
    else:
        print("There are no tasks to delete.")
    save_tasks(tasks)

def main():
    tasks = load_tasks()
    options = {
        1: "View Tasks",
        2: "Add Task",
        3: "Complete Task",
        4: "Delete Task",
        5: "Exit"
        }
    while True:
        for key,value in options.items():
            print(f"{key}. {value}")
        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks(tasks)
                    
        elif choice == "2":
            add_task(tasks)
                    
        elif choice == "3":
            complete_task(tasks)
                    
        elif choice == "4":
            delete_task(tasks)
        elif choice =="5":
            break
        else:
            print("Invalid option.")
                   
           

main()















#task_list = [
   # {"id": 1, "task": "Learn Python", "completed": False},
    #{"id": 2, "task": "Practice JSON", "completed": True}
    #]


#tasks = load_tasks()

#delete_task(tasks)

#display_tasks(tasks)












