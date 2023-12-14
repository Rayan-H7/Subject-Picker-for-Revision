import random

def picker():
  choice = random.choice(["Humanities", "Sciences"])
  if  choice == "Humanities":
    subject = random.choice(["English Language", "English Literature", "Mandarin", "History", "R.E"])
  else:
    subject = random.choice(["Biology", "Chemistry", "Computer Science", "Mathematics", "Physics"])
  return subject + " -> " + choice
print(picker())