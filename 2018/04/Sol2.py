from collections import defaultdict
import re


def solve(records):
    record_re = re.compile(r"\[(\d\d\d\d)\-(\d\d)\-(\d\d) (\d\d)\:(\d\d)\] (.+)")
    action_re = re.compile(r"Guard #(\d+) begins shift")
    ordered_records = []
    for record in records:
        year, month, day, _, min, action = record_re.match(record).groups()
        ordered_records.append((int(year), int(month), int(day), int(min), action))
    ordered_records.sort()

    date = None
    prev_min = None
    guard_id = None
    guard_history = defaultdict(lambda: defaultdict(lambda: [0] * 60))

    for record in ordered_records:
        year, month, day, min, action = record
        id = action_re.match(action)
        if id:
            date = (year, month, day)
            guard_id = int(id.groups()[0])
        elif action == "wakes up":
            for i in range(prev_min, min):
                guard_history[guard_id][date][i] = 1
            prev_min = None
        elif action == "falls asleep":
            prev_min = min

    max_id  = max(guard_history.keys(), key=lambda k: max(sum(cal[i] for cal in guard_history[k].values()) for i in range(60)))
    max_min = max(range(60), key=lambda i: sum(cal[i] for cal in guard_history[max_id].values()))

    return max_id * max_min


if __name__ == "__main__":
    records = [record.strip() for record in open("input.txt", "r").readlines()]
    print(solve(records))