def get_seconds(time):
    hours, minutes, seconds = map(int, time.split(":"))

    return (hours * 3600) + (minutes * 60) + seconds


def get_time(seconds):
    return str(seconds // 3600).zfill(2) + ":" + str(seconds // 60 % 60).zfill(2) + ":" + str(seconds % 60).zfill(2)


def solution(play_time, adv_time, logs):
    answer = []
    play_time, adv_time = get_seconds(play_time), get_seconds(adv_time)

    for i in range(len(logs)):
        logs[i] = list(map(get_seconds, logs[i].split("-")))

    if adv_time >= play_time:
        return get_time(0)

    for i in range(len(logs)):
        count = 1
        start_seconds, end_seconds = logs[i]

        for j in range(len(logs)):
            if i == j:
                continue

            target_start_seconds, target_end_seconds = logs[j]

            if target_start_seconds <= start_seconds <= target_end_seconds:
                count += 1
            elif target_start_seconds <= end_seconds <= target_start_seconds + adv_time:
                count += 1
            elif end_seconds <= target_end_seconds or start_seconds >= target_start_seconds:
                count += 1

        answer.append((count, get_time(start_seconds)))

    return answer


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))  # "01:30:59"
print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))  # "01:00:00"
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))  # "00:00:00"
