from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    completed: bool = False

    def complete(self) -> None:
        if not self.completed:
            self.completed = True


@dataclass
class Project:
    name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, title: str) -> None:
        self.tasks.append(Task(title))

    def find_task(self, title: str) -> Task | None:
        for task in self.tasks:
            if title.lower() == task.title.lower():
                return task
        return None

    def complete_task(self, title: str) -> None:
        found = self.find_task(title)
        if found is None:
            raise ValueError("Task not found")
        found.complete()

    
    def completion_rate(self) -> float:
        if not self.tasks:
            return 0.0
        completed = 0
        for task in self.tasks:
            if task.completed:
                completed += 1
        return completed / len(self.tasks) * 100
        


@dataclass
class Developer:
    name: str
    projects: list[Project] = field(default_factory=list)

    def find_project(self, name: str) -> Project | None:
        for project in self.projects:
            if name.lower() == project.name.lower():
                return project
        return None

    def add_project(self, name: str) -> None:
        found = self.find_project(name)
        if found is not None:
            raise ValueError("Project already exists")
        self.projects.append(Project(name))

    
    def overall_completion_rate(self) -> float:
        completed = 0.
        total = 0.
        for project in self.projects:
            for task in project.tasks:
                if task.completed:
                    completed += 1
                total +=1
        if total == 0:
            return 0.0
        return completed / total * 100


