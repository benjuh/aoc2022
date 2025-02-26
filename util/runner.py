import config as config
import util.colors as colors

NS = [1000000000, "ns"]
MiS = [1000000, "µs"]
MS = [1000, "ms"]
S = [1, "s"]



def RunDay(day, part1, part2, time1, time2):
    color1 = colors.BAD
    color2 = colors.BAD

    time_unit_1 = MS
    time_unit_2 = MS

    check_time1 = time1 * time_unit_1[0]
    check_time2 = time2 * time_unit_2[0]

    if check_time1 < config.BLAZING_TIME:
        color1 = colors.BLAZING
        time_unit_1 = MiS
        time1 = time1 * time_unit_1[0]
    elif check_time1 < config.GOOD_TIME:
        color1 = colors.GOOD
        time_unit_1 = MS
        time1 = time1 * time_unit_1[0]
    elif check_time1 < config.OKAY_TIME:
        color1 = colors.OKAY
        time_unit_1 = MS
        time1 = time1 * time_unit_1[0]
    else:
        time_unit_1 = S
        time1 = time1 * time_unit_1[0]

    if check_time2 < config.BLAZING_TIME:
        color2 = colors.BLAZING
        time_unit_2 = MiS
        time2 = time2 * time_unit_2[0]
    elif check_time2 < config.GOOD_TIME:
        color2 = colors.GOOD
        time_unit_2 = MS
        time2 = time2 * time_unit_2[0]
    elif check_time2 < config.OKAY_TIME:
        color2 = colors.OKAY
        time_unit_2 = MS
        time2 = time2 * time_unit_2[0]
    else:
        time_unit_2 = S
        time2 = time2 * time_unit_2[0]


    print(f"\n[Day {day}]")
    t1 = f"{time1:.4f}{time_unit_1[1]}"
    t2 = f"{time2:.4f}{time_unit_2[1]}"
    print(f"{color1}{t1:<14}\t{colors.RESET} part_1={part1}")
    print(f"{color2}{t2:<14}\t{colors.RESET} part_2={part2}\n")
