from functools import cache

PATH = 'input.txt'


def load():
    res = {}
    valve_counter, valve_mapping = 0, {}
    with open(PATH) as f:
        for line in f:
            valve = line[6:8]  # process the lines
            fl, cv = line.split('to valve')
            cv = cv.replace('\n', '')
            flow_rate = int(fl.split(';')[0][23:])
            if cv[0] == 's':
                cv = cv[2:]
            else:
                cv = cv[1:]
            connecting_valves = cv.split(', ')

            if valve not in valve_mapping:
                valve_mapping[valve] = valve_counter
                valve_counter += 1

            for v in connecting_valves:
                if v not in valve_mapping:
                    valve_mapping[v] = valve_counter
                    valve_counter += 1

            res[valve_mapping[valve]] = (flow_rate, [valve_mapping[v] for v in connecting_valves])
    return res, valve_mapping


class Solution:

    def __init__(self, valves, valve_mapping):
        self.valves = valves
        self.valve_mapping = valve_mapping

    @cache
    def max_flow(self, timestamp, current_valve, current_flow, open_valves):
        if timestamp == 30:
            return 0

        res = 0
        #  open current if not open and flow > 0
        if self.valves[current_valve][0] > 0 and not (1 << current_valve & open_valves):
            res = self.max_flow(timestamp + 1, current_valve, current_flow + self.valves[current_valve][0],
                                open_valves | 1 << current_valve) + current_flow

        #  walk to all other valves
        for neighbor in self.valves[current_valve][1]:
            res = max(res, self.max_flow(timestamp + 1, neighbor, current_flow, open_valves) + current_flow)

        return res

    @cache
    def max_flow_elephant_v2(self, timestamp, current_valve, current_flow, open_valves, turn):
        """turn false: my turn. turn true: elephant turn"""
        if timestamp == 26:
            if not turn:
                return self.max_flow_elephant_v2(0, self.valve_mapping['AA'], 0, open_valves, True)
            else:
                return 0

        res = 0
        #  open current if not open and flow > 0
        if self.valves[current_valve][0] > 0 and not (1 << current_valve & open_valves):
            res = self.max_flow_elephant_v2(timestamp + 1, current_valve, current_flow + self.valves[current_valve][0],
                                            open_valves | 1 << current_valve, turn) + current_flow

        #  walk to all other valves
        for neighbor in self.valves[current_valve][1]:
            res = max(res, self.max_flow_elephant_v2(timestamp + 1, neighbor, current_flow, open_valves,
                                                     turn) + current_flow)

        return res

    @cache
    def max_flow_elephant(self, timestamp, current_valve_me, current_valve_elephant, current_temp_flow, current_flow,
                          open_valves, turn):
        """
        turn false: my turn. turn true: elephant turn. Start with my turn
        edit: too slow, need something faster
        """
        if timestamp == 26:
            return 0

        res = 0

        if not turn:
            #  my turn
            #  open current if not open and flow > 0
            if self.valves[current_valve_me][0] > 0 and not (1 << current_valve_me & open_valves):
                res = self.max_flow_elephant(timestamp, current_valve_me, current_valve_elephant, current_temp_flow,
                                             current_flow + self.valves[current_valve_me][0],
                                             open_valves | 1 << current_valve_me, True)

            #  walk to all other valves
            for neighbor in self.valves[current_valve_me][1]:
                res = max(res, self.max_flow_elephant(timestamp, neighbor, current_valve_elephant, current_temp_flow,
                                                      current_flow, open_valves, True))

            return res

        else:
            #  elephant turn
            #  open current if not open and flow > 0
            if self.valves[current_valve_elephant][0] > 0 and not (1 << current_valve_elephant & open_valves):
                res = self.max_flow_elephant(timestamp + 1, current_valve_me, current_valve_elephant,
                                             current_flow + self.valves[current_valve_elephant][0],
                                             current_flow + self.valves[current_valve_elephant][0],
                                             open_valves | 1 << current_valve_elephant, False) + current_temp_flow

            #  walk to all other valves
            for neighbor in self.valves[current_valve_elephant][1]:
                res = max(res,
                          self.max_flow_elephant(timestamp + 1, current_valve_me, neighbor, current_flow, current_flow,
                                                 open_valves, False) + current_temp_flow)

            return res


def part1():
    valves, valve_mapping = load()
    sol = Solution(valves, valve_mapping)
    print(sol.max_flow(0, valve_mapping['AA'], 0, 0))


def part2():
    valves, valve_mapping = load()
    sol = Solution(valves, valve_mapping)
    open_valves = 0
    for i in valves:
        if valves[i][0] == 0:
            open_valves = open_valves | 1 << i
    # print(sol.max_flow_elephant(0, valve_mapping['AA'], valve_mapping['AA'], 0, 0, 0, False))
    print(sol.max_flow_elephant_v2(0, valve_mapping['AA'], 0, open_valves, False))


if __name__ == '__main__':
    part1()
    part2()
