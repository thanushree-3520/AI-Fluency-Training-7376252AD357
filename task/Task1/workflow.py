# System 2: Rule-Based Workflow
# No LLM is used.

student = {
    "name": "Arun",
    "course": "AI & DS",
    "attendance": 82,
    "internal_mark": 76
}

def workflow(question):
    text = question.lower()

    if "attendance" in text:
        return f"Attendance of Arun: {student['attendance']}%"

    if "eligible" in text or "end-semester" in text:
        if student["attendance"] >= 75 and student["internal_mark"] >= 40:
            return "Arun is eligible for the end-semester examination."
        else:
            return "Arun is not eligible for the end-semester examination."

    return "Sorry, I do not have a rule for this type of question."


questions = [
    "What is Arun's attendance percentage?",
    "Is Arun eligible to attend the end-semester examination?",
    "What is Arun's internal mark and course?",
    "Write a welcome message for Arun."
]

print("\n=== SYSTEM 2: RULE-BASED WORKFLOW (no LLM) ===\n")

for question in questions:
    print("Q:", question)
    print("A:", workflow(question))
    print("-" * 70)