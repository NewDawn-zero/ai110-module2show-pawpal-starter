from dataclasses import dataclass, field
from datetime import timedelta


@dataclass
class Task:
    title: str
    time: str
    duration: int
    priority: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def next_occurrence(self):
        if self.frequency == "daily":
            delta = timedelta(days=1)
        elif self.frequency == "weekly":
            delta = timedelta(weeks=1)
        else:
            return None
        return Task(self.title, self.time, self.duration, self.priority, self.frequency)


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        return [(pet.name, task) for pet in self.pets for task in pet.tasks]


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def sort_by_time(self):
        return sorted(self.owner.get_all_tasks(), key=lambda x: x[1].time)

    def filter_tasks(self, pet_name=None, completed=None):
        tasks = self.owner.get_all_tasks()
        if pet_name:
            tasks = [(p, t) for p, t in tasks if p.lower() == pet_name.lower()]
        if completed is not None:
            tasks = [(p, t) for p, t in tasks if t.completed == completed]
        return tasks

    def detect_conflicts(self):
        seen = {}
        conflicts = []
        for pet, task in self.sort_by_time():
            if task.time in seen:
                conflicts.append(f"Conflict at {task.time}: {task.title} ({pet}) vs {seen[task.time][1].title} ({seen[task.time][0]})")
            else:
                seen[task.time] = (pet, task)
        return conflicts

    def complete_task(self, pet_name, task_title):
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                for task in pet.tasks:
                    if task.title.lower() == task_title.lower() and not task.completed:
                        task.mark_complete()
                        next_task = task.next_occurrence()
                        if next_task:
                            pet.add_task(next_task)
                        return True
        return False

    def daily_schedule(self):
        tasks = self.sort_by_time()
        if not tasks:
            return "No tasks scheduled."
        lines = ["Today's Schedule", "-" * 30]
        for pet, task in tasks:
            icon = "✅" if task.completed else "⬜"
            lines.append(f"{icon} [{task.time}] {task.title} ({pet}) - {task.duration}min | {task.priority}")
        return "\n".join(lines)