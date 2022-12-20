from functools import cache

PATH = 'input.txt'


def load():
    res = []
    p2 = ': Each ore robot costs '
    p3 = ' ore. Each clay robot costs '
    p4 = ' ore. Each obsidian robot costs '
    p5 = ' clay. Each geode robot costs '
    with open(PATH) as f:
        for line in f:
            index, line = line.split(p2)
            ore, line = line.split(p3)
            clay, line = line.split(p4)
            obsidian, geode = line.split(p5)

            index = int(index[10:])
            ore = int(ore)
            clay = int(clay)
            obsidian_ore, obsidian_clay = obsidian.split(' ore and ')
            geode_ore, geode_obsidian = geode.split(' ore and ')

            obsidian_ore, obsidian_clay = int(obsidian_ore), int(obsidian_clay)
            geode_ore, geode_obsidian = int(geode_ore), int(geode_obsidian.replace(' obsidian.', ''))

            res.append((index, ore, clay, (obsidian_ore, obsidian_clay), (geode_ore, geode_obsidian)))
    return res


@cache
def max_open_geodes(blueprint, timestamp, ore, clay, obsidian, ore_robot, clay_robot, obsidian_robot, geode_robot):
    """
    blueprint: (index, ore, clay, (obsidian_ore, obsidian_clay), (geode_ore, geode_obsidian))
    return: geodes
    """

    if timestamp == 0:
        return 0

    new_ore = ore + ore_robot
    new_clay = clay + clay_robot
    new_obsidian = obsidian + obsidian_robot

    res = 0
    geode_robot_built = False

    if ore >= blueprint[4][0] and obsidian >= blueprint[4][1]:  # build geode robot
        res = max(res, geode_robot + max_open_geodes(blueprint, timestamp - 1, new_ore - blueprint[4][0], new_clay,
                                                     new_obsidian - blueprint[4][1], ore_robot, clay_robot,
                                                     obsidian_robot, geode_robot + 1))
        geode_robot_built = True

    if not geode_robot_built:
        res = max(res,
                  geode_robot + max_open_geodes(blueprint, timestamp - 1, new_ore, new_clay, new_obsidian, ore_robot,
                                                clay_robot, obsidian_robot, geode_robot))

    if not geode_robot_built and ore >= blueprint[1] and \
            ore_robot < max(blueprint[1], blueprint[2], blueprint[3][0], blueprint[4][0]) and timestamp > 1 and \
            ore - ore_robot <= blueprint[1]:  # build ore robot
        res = max(res,
                  geode_robot + max_open_geodes(blueprint, timestamp - 1, new_ore - blueprint[1], new_clay,
                                                new_obsidian,
                                                ore_robot + 1, clay_robot, obsidian_robot, geode_robot))

    if not geode_robot_built and ore >= blueprint[2] and clay_robot < blueprint[3][1] and \
            obsidian_robot < blueprint[4][1] and timestamp > 1 and ore - ore_robot <= blueprint[2]:  # build clay robot
        res = max(res,
                  geode_robot + max_open_geodes(blueprint, timestamp - 1, new_ore - blueprint[2], new_clay,
                                                new_obsidian,
                                                ore_robot, clay_robot + 1, obsidian_robot, geode_robot))

    if not geode_robot_built and ore >= blueprint[3][0] and clay >= blueprint[3][1] and \
            obsidian_robot < blueprint[4][1] and timestamp > 1:  # build obsidian robot
        res = max(res, geode_robot + max_open_geodes(blueprint, timestamp - 1, new_ore - blueprint[3][0],
                                                     new_clay - blueprint[3][1], new_obsidian, ore_robot, clay_robot,
                                                     obsidian_robot + 1, geode_robot))

    return res


def part1():
    blueprints = load()
    res = 0
    for b in blueprints:
        score = max_open_geodes(b, 24, 0, 0, 0, 1, 0, 0, 0)
        res += b[0] * score
    print(res)


def part2():
    blueprints = load()
    res = 1
    for b in blueprints[0:3]:
        res *= max_open_geodes(b, 32, 0, 0, 0, 1, 0, 0, 0)
    print(res)


if __name__ == '__main__':
    part1()
    part2()
