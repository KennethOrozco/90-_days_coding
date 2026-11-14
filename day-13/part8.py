from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    completed: bool = False




@dataclass
class Project:
    name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, title:str)-> None:
        self.tasks.append(Task(title))

    def completion_rate(self) -> float:
        if not self.tasks:
            return 0.0
        
        completed = 0
        
        for task in self.tasks:
        
            if task.completed:
                completed += 1

        return completed / len(self.tasks) * 100

    def incomplete_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]

project = Project("AI Assistant")

project.add_task("Build interface")
project.add_task("Connect API")
project.add_task("Write tests")

project.tasks[0].completed = True

print(project.completion_rate())

for task in project.incomplete_tasks():
    print(task.title)



