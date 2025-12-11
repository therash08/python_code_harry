marks = {
    "rash": 100,
    "lolita": 23,
    "rohan": 78,
    0: "rasidul"
}


# print(marks.items())
# print(marks.keys())
# print(marks.values())

marks.update({"rash": 99})
print(marks)

print(marks.get("rash"))
print(marks["rash"])
