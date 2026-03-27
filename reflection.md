# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

Owner — holds the owner's name and their list of pets
Pet — holds pet info and a list of tasks
Task — represents one care activity with a time, duration, and priority
Scheduler — sorts, filters, and manages all tasks across pets

**b. Design changes**

No major changes and the initial design matched the final implementation.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

The conflict detection only checks for exact time matches, not overlapping durations. Two tasks at 08:00 and 08:10 with 30 minute durations would not be flagged.

---

## 3. AI Collaboration

**a. How you used AI**

Used AI for brainstorming the class structure and generating test cases. Asking specific questions like "how should Scheduler access Owner's pets" was most helpful.

**b. Judgment and verification**

AI added extra methods I didn't need. I reviewed everything manually and removed anything that wasn't part of the original design.

---

## 4. Testing and Verification

**a. What you tested**

Tested task completion, chronological sorting, recurring task scheduling, and conflict detection, the core behaviors of the scheduler.

**b. Confidence**

4/5. Edge cases like empty pet lists or two pets with identical task names could use more coverage.

---

## 5. Reflection

**a. What went well**

The UML design phase made implementation straightforward. Having a clear blueprint before coding saved a lot of time.

**b. What you would improve**

Add the ability to mark tasks complete directly in the Streamlit UI.

**c. Key takeaway**

Designing the system before writing code made collaboration with AI much more effective and I knew exactly what to ask for.