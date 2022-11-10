import json 

f = open("student_score.json")
data = json.load(f)
print("-------生徒一人目-------")
print(data["students"][3]["japanese"])
print(data["students"][2]["japanese"])
print(data["students"][1]["japanese"])
f.close()