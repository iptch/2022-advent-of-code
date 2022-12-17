from timeit import default_timer as timer
import re


def puzzle_1():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    valves = {}
    for line in lines:
        groups = [group for group in re.match(r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line).groups()]
        valves[groups[0]] = {"rate": int(groups[1]), "connections": {v: 1 for v in groups[2].split(", ")}}

    full_connections = False
    while not full_connections:
        full_connections = True
        for name in valves:
            valve = valves[name]
            for possible_valve in valves:
                for connection in list(valve["connections"]):
                    if possible_valve in valves[connection]["connections"]:
                        distance = valve["connections"][connection] + valves[connection]["connections"][possible_valve]
                        if possible_valve not in valve["connections"] or valve["connections"][possible_valve] > distance:
                            full_connections = False
                            valve["connections"][possible_valve] = distance

    for key in list(valves):
        if valves[key]["rate"] > 0:
            continue
        if key != "AA":
            del valves[key]
        for other in valves:
            del valves[other]["connections"][key]

    options = list(valves)
    options.remove("AA")
    return find_highest_release(valves, "AA", 30, options)


def find_highest_release(valves, position, minutes, options):
    if minutes <= 0:
        return 0
    max_released = 0
    for i in range(len(options)):
        if options[i] not in valves[position]["connections"]:
            continue
        released = find_highest_release(valves, options[i], minutes - valves[position]["connections"][options[i]] - 1, options[:i] + options[i+1:])
        if released > max_released:
            max_released = released

    return minutes * valves[position]["rate"] + max_released


def puzzle_2():
    return "ich gib uuf"


if __name__ == '__main__':
    start1 = timer()
    print(f"Puzzle 1: {puzzle_1()} (in {timer()-start1}sec)")
    start2 = timer()
    print(f"Puzzle 2: {puzzle_2()} (in {timer()-start2}sec)")
