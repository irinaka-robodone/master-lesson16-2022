import json 

f = open("student_score.json")
data = json.load(f)
data = data["students"]
goukei=0
heikin=0

#平均点　for文を使う
for i in range(4):
        pass

print("-------生徒一人目-------")

f.close()



for i in range(len(data)):
        print(data[i]["math"])
        print(data[i]["japanese"])
        goukei+=data[i]["math"]
        goukei+=data[i]["japanese"]
        print(data[i]["math"])
        print(data[i]["japanese"])
#heikin=goukei/len(data)
print(goukei)