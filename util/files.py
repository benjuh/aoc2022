import config
def GetRawInput(day):
    file = open(f"{config.DATA_LOCATION}day{day}.txt", "r")
    return file.read()
def GetLines(day):
    lines = []
    file = open(f"{config.DATA_LOCATION}day{day}.txt", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines
def PrintLines(lines):
    for line in lines:
        print(line)
