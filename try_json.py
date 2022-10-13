import json

f=open("student_score.json")
data=json.load(f)
print("---------生徒一人目---------")
print(data["students"][0])

f.close()