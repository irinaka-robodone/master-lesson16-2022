from pprint import pprint
import json

f = open("student_score.json")
data = json.load(f)
# print("-------生徒1人目-------")
# p\rint(data["students"])


scores = data["students"]
# a = scores[0]["math"]
# b = scores[0]["Science"]
# c = scores[0]["japanese"]
# d = scores[0]["Social"]
# avg = a+b+c+d
# avg /= 4
avg =0
for i in range(len(scores)):
     avg += scores[i]["math"]
avg/= len(scores)

print(avg)
f.close()
