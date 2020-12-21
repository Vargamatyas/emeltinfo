years = [str(x) for x in range(2005, 2021)]
months = ["may", "october"]

tests = list()
for year in years:
    for month in months:
        combination = "{0} {1}".format(year, month)
        tests.append(combination)
print(tests)
with open("tests.txt", "w+") as f:
    for test in tests:
        f.write(test + "\n")
