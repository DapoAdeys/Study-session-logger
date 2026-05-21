# session logger for students to log their study sessions, subjects, time spent, and notes.
import json

session_logger = {
    "study_session": input("add a name for the study session: "),
    "student_subject": input("what subject did student study? "),
    "time_studied": None,
    "notes_added": None
}

try:
    session_logger["time_studied"] = int(
        input("how long the student studied (in minutes): ")
    )
except ValueError:
    print("that wasnt a number! please type digits only")
    exit()

session_logger["notes_added"] = input(
    "add notes about the study session: "
)

# SAVE TO JSON FILE
with open("study_session.json", "w") as file:
    json.dump(session_logger, file, indent=4)

print("\nSession saved to study_session.json")


with open("study_session.json", "r") as file:
    data = json.load(file)

print(data)