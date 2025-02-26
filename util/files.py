import config
def GetRawInput(day):
    file = open(f"{config.DATA_LOCATION}day{day}.txt", "r")
    return file.read()
def GetLines(day, test=False):
    lines = []
    path = f"{config.DATA_LOCATION}day{day}.txt"
    if test:
        path = f"{config.TEST_DATA_LOCATION}day{day}.txt"
    file = open(path, "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines
def GetLinesNoStrip(day, test=False):
    lines = []
    path = f"{config.DATA_LOCATION}day{day}.txt"
    if test:
        path = f"{config.TEST_DATA_LOCATION}day{day}.txt"
    file = open(path, "r")
    for line in file:
        lines.append(line.split("\n")[0])
    file.close()
    return lines
def PrintLines(lines):
    longest = 0
    for line in lines:
        if len(line) > longest:
            longest = len(line)

    sep = ""
    for _ in range((longest//2)-1):
        sep += "~"
    sep += "DATA"
    for _ in range((longest//2)-1):
        sep += "~"
    print(sep)
    for line in lines:
        print(line)
    sep_bott = ""
    for _ in range(len(sep)):
        sep_bott += "~"
    print(sep_bott)
