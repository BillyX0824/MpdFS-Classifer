import csv
import random


def createTrainSets(schemes_csv_path, file_csv_path):
    # Load user group information
    group = dict()
    temp = set()
    with open(schemes_csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not int(row[1]) in temp:
                temp.add(row[1])
            if not int(row[1]) in group:
                group[int(row[1])] = dict()
            group[int(row[1])][int(row[0])] = dict()
            group[int(row[1])][int(row[0])] = int(row[2])
    # Load all files
    trains = list()
    with open(file_csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        p = 10
        for row in reader:
            temp_gid = random.sample(temp, 1)
            gid = temp_gid[0]
            uid = random.choice(list(group[int(gid)].keys()))
            view = 3
            if (float(row[5])) < 0:
                label = 0
                ratio = random.uniform(0.300, 0.800)
                trains.append((int(row[0]), int(row[1]), int(row[2]),
                               int(row[3]), uid, gid, view, "{:.3f}".format(ratio), float(row[5]), label))
            else:
                if (float(row[5])) == 0:
                    wp = random.randint(1, 100)
                    label = 0
                    if wp <= 20:
                        label = 1
                    ratio = random.uniform(0.300, 0.800)
                    trains.append((int(row[0]), int(row[1]), int(row[2]),
                                   int(row[3]), uid, gid, view,
                                   "{:.3f}".format(ratio), float(row[5]), label))
                else:
                    if group[int(gid)][uid] == 1:
                        label = 0
                        if (float(row[5])) >= 365:
                            label = 1
                        ratio = random.uniform(0.050, 0.150)
                        trains.append((int(row[0]), int(row[1]), int(row[2]),
                                       int(row[3]), uid, gid, view,
                                       "{:.3f}".format(ratio), float(row[5]), label))
                    elif group[int(gid)][uid] == 2:
                        label = 0
                        if (float(row[5])) >= 7:
                            label = 1
                        ratio = random.uniform(0.150, 0.300)
                        trains.append((int(row[0]), int(row[1]), int(row[2]),
                                       int(row[3]), uid, gid, view,
                                       "{:.3f}".format(ratio), float(row[5]), label))
                    elif group[int(gid)][uid] == 3:
                        label = 0
                        if (float(row[5])) >= 1 / 24:
                            label = 1
                        ratio = random.uniform(0.300, 0.450)
                        trains.append((int(row[0]), int(row[1]), int(row[2]),
                                       int(row[3]), uid, gid, view,
                                       "{:.3f}".format(ratio), float(row[5]), label))
                    elif group[int(gid)][uid] == 4:
                        label = 0
                        if (float(row[5])) >= 1 / 24 / 6:
                            label = 1
                        ratio = random.uniform(0.450, 0.600)
                        trains.append((int(row[0]), int(row[1]), int(row[2]),
                                       int(row[3]), uid, gid, view,
                                       "{:.3f}".format(ratio), float(row[5]), label))
                    elif group[int(gid)][uid] == 5:
                        label = 0
                        if (float(row[5])) >= 1 / 24 / 60:
                            label = 1
                        ratio = random.uniform(0.600, 0.800)
                        trains.append((int(row[0]), int(row[1]), int(row[2]),
                                       int(row[3]), uid, gid, view,
                                       "{:.3f}".format(ratio), float(row[5]), label))
    return trains


def writeTrainCSV(datasets_csv_path, train_csv_path, trains):
    with open(datasets_csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, dialect="excel")
        for item in trains:
            writer.writerow(item)

    with open(train_csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, dialect="excel")
        for item in trains:
            writer.writerow((item[1], item[2], item[3], item[8], item[9]))


if __name__ == "__main__":
    schemes_csv_path = " "  # schemes csv
    file_csv_path = " "  # file csv
    datasets_csv_path = " "  # a csv file to write train datasets we created
    train_csv_path = " "  # a csv file to write train data we created
    writeTrainCSV(datasets_csv_path, train_csv_path, createTrainSets(schemes_csv_path, file_csv_path))
