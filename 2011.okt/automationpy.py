list = ["januar", "februar", "marcius", "aprilis", "majus", "junius", "julius", "agusztus", "szeptember", "oktober", "november", "december"]

for i in list:
    string = f"if honap == '{i}':\n   {i} += nap\nelse:\n    pass"
    print(string)