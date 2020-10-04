# student = {
#     "name" : "Neeraj Sharma",
#     "marks" : 96,
#     "sub" : ["maths","science", "eng"]
# }

# print(student["sub"])

marks = {
    "maths" : 89,
    "physics" : {
        "theory" : 60,
        "practical" : 30
    },
    "chemistry" : 92,
    "physical education" : 87,
    "eng" : 87
}

# print(marks)

# del marks["maths"]
marks["maths"] = 80
# marks["home science"] = 82

print(marks)

# print(marks["physics"]["theory"])