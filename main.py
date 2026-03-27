from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner(name="Jordan")

mochi = Pet(name="Mochi", species="cat")
rex = Pet(name="Rex", species="dog")

mochi.add_task(Task(title="Medication", time="08:30", duration=5, priority="high", frequency="daily"))
mochi.add_task(Task(title="Playtime", time="12:00", duration=20, priority="medium", frequency="daily"))
rex.add_task(Task(title="Morning walk", time="07:00", duration=30, priority="high", frequency="daily"))
rex.add_task(Task(title="Grooming", time="12:00", duration=45, priority="low", frequency="weekly"))

owner.add_pet(mochi)
owner.add_pet(rex)

scheduler = Scheduler(owner)

print(scheduler.daily_schedule())
print()

conflicts = scheduler.detect_conflicts()
if conflicts:
    print("Conflicts:")
    for c in conflicts:
        print(" ", c)

print()
scheduler.complete_task("Mochi", "Medication")
print("Mochi's medication marked complete, next occurrence scheduled.")
print()
print(scheduler.daily_schedule())