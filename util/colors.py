def GetANSIColor(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

BLAZING = GetANSIColor(0, 255, 0)
GOOD = GetANSIColor(100, 255, 100)
OKAY = GetANSIColor(255, 225, 0)
BAD = GetANSIColor(255, 100, 100)
RESET = "\033[0m"

