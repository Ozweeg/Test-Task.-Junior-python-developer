import itertools

def appearance(intervals):
    all_intervals = []
    i = -1
    for values in intervals.values():
        for v in values:
            all_intervals.append((v, i))
            if i == -1:
                i = 1
            else:
                i = -1
    all_intervals.sort()
    general_time = calculate_general_time(all_intervals)
    return general_time

def calculate_general_time(sorted_intervals):
    curr = 0
    time_start = 0
    time_delta = 0
    for (secs, type) in sorted_intervals:
        prev = curr
        curr = curr + type
        if curr == -3 and prev == -2:
            time_start = secs
        if curr == -2 and prev == -3:
            time_delta = time_delta + (secs - time_start)
    return time_delta

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                       1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                       1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                       1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3641
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
