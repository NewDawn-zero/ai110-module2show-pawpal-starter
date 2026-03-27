from pawpal_system import Owner, Pet, Task, Scheduler


def make_scheduler():
    owner = Owner(name="Jordan")
    mochi = Pet(name="Mochi", species="cat")
    rex = Pet(name="Rex", species="dog")
    mochi.add_task(Task(title="Medication", time="08:30", duration=5, priority="high", frequency="daily"))
    mochi.add_task(Task(title="Playtime", time="12:00", duration=20, priority="medium", frequency="daily"))
    rex.add_task(Task(title="Morning walk", time="07:00", duration=30, priority="high", frequency="daily"))
    rex.add_task(Task(title="Grooming", time="12:00", duration=45, priority="low", frequency="weekly"))
    owner.add_pet(mochi)
    owner.add_pet(rex)
    return Scheduler(owner)


def test_mark_complete():
    task = Task(title="Walk", time="09:00", duration=20, priority="medium")
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_count():
    pet = Pet(name="Mochi", species="cat")
    pet.add_task(Task(title="Feed", time="08:00", duration=10, priority="high"))
    assert len(pet.tasks) == 1


def test_sort_by_time():
    scheduler = make_scheduler()
    times = [t.time for _, t in scheduler.sort_by_time()]
    assert times == sorted(times)


def test_recurring_task():
    scheduler = make_scheduler()
    mochi = scheduler.owner.pets[0]
    count = len(mochi.tasks)
    scheduler.complete_task("Mochi", "Medication")
    assert len(mochi.tasks) == count + 1


def test_conflict_detection():
    scheduler = make_scheduler()
    assert len(scheduler.detect_conflicts()) > 0