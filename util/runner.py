import config as config
import util.colors as colors

def RunDay(day, part1, part2, time1, time2):
    color1 = colors.BAD
    color2 = colors.BAD

    time1 = time1 / 10000000
    time2 = time2 / 10000000

    if time1 < config.BLAZING_TIME:
        color1 = colors.BLAZING
    elif time1 < config.GOOD_TIME:
        color1 = colors.GOOD
    elif time1 < config.OKAY_TIME:
        color1 = colors.OKAY

    if time2 < config.BLAZING_TIME:
        color2 = colors.BLAZING
    elif time2 < config.GOOD_TIME:
        color2 = colors.GOOD
    elif time2 < config.OKAY_TIME:
        color2 = colors.OKAY


    print(f"\n[Day {day}]")
    print(f"{color1}{time1:.4f}ms\t{colors.RESET} part_1={part1}")
    print(f"{color2}{time2:.4f}ms\t{colors.RESET} part_2={part2}\n")
