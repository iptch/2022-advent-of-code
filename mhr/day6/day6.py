from common import load_lines


def find_marker(signal: str, offset: int):
    for idx in range(len(signal)):
        if len(set([signal[idx+i] for i in range(offset)])) == offset:
            return idx + offset


if __name__ == '__main__':
    signal_ = load_lines(day=6)[0]
    print(f'Task1: {find_marker(signal_, offset=4)}')
    print(f'Task2: {find_marker(signal_, offset=14)}')
