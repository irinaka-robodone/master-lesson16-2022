import json
math_1 = 0
all = []
zero = 0
one = 0
two = 0
three = 0


f=open("student_score.json")
data=json.load(f)
print("len of data",len(data))
print("len of students",len(data["students"]))
data_=data["students"]


for i in range(len(data_)):
    print("---------生徒",i+1,"人目---------")
    print(data_["students"][i]["math"]["japanese"]["Science"]["Social"])


# math_1 += data_[i]["math"]
# math_1 /= 4
print(math_1)

avg = 50
all.append(avg)
print(all)

f.close()