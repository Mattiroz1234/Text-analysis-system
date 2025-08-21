def get_weapons(file):
    weapons = []
    with open(file, "r", encoding='utf-8-sig') as f:
        while True:
            line = f.readline().strip("\n")
            if line == "":
                break
            weapons.append(line)

    return weapons

