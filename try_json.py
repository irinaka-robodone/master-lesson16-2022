from pprint import pprint
import json

f = open("student_score.json")
data = json.load(f)
f.close()
# print("-------生徒1人目-------")
# p\rint(data["students"])


scores = data["students"]

avgs =[]
# for i in range(len(scores)):
#      avg += scores[i]["math"]
# avg/= len(scores)
for i in range(len(scores)):
    a = scores[i]["math"]
    b = scores[i]["Science"]
    c = scores[i]["japanese"]
    d = scores[i]["Social"]
    avg = a+b+c+d
    avg /= 4
    avgs.append(avg)
print(avgs)
