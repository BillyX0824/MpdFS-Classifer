import csv
import random


def createSchemes(file_path):
    users = dict()
    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            gid = 0
            for i in range(len(row)):
                if i == 0:
                    gid = int(row[i])
                else:
                    wp = random.randint(1, 100)
                    if 1 <= wp <= 15:
                        scheme = 1  # corresponding type of strategy
                    if 16 <= wp <= 45:
                        scheme = 2  # corresponding type of strategy
                    if 46 <= wp <= 70:
                        scheme = 3  # corresponding type of strategy
                    if 71 <= wp <= 90:
                        scheme = 4  # corresponding type of strategy
                    if 91 <= wp <= 100:
                        scheme = 5  # corresponding type of strategy
                    users[int(row[i])] = {"gid": gid, "scheme": scheme}
    return users


def writeSchemesCSV(file_path, users):
    with open(file_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, dialect="excel")
        for uid in users:
            line = [uid, users[uid]["gid"], users[uid]["scheme"]]
            writer.writerow(line)


if __name__ == "__main__":
    user_csv_path = " "  # user csv file path
    schemes_csv_path = " "  # a csv file to write schemes we created
    writeSchemesCSV(schemes_csv_path, createSchemes(user_csv_path))
