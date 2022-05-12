import csv
import random


def createGroup(group_num):
    group = dict()
    temp = set()
    for i in range(group_num):
        user_num = random.randint(40, 60)
        group[i + 1] = list()
        while len(group[i + 1]) != user_num:
            user_id = random.randint(1, 60 * group_num)
            if not user_id in temp:
                group[i + 1].append(user_id)
                temp.add(user_id)
    return group


def writeUserCSV(file_path, group):
    with open(file_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, dialect="excel")
        for gid in group:
            line = list()
            line.append(gid)
            line.extend(group[gid])
            writer.writerow(line)


if __name__ == "__main__":
    user_csv_path = " "  # a csv file to write user we created
    writeUserCSV(user_csv_path, createGroup(20))  # 20 groups id and UserId
