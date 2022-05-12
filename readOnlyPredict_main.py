import csv
from sklearn.tree import DecisionTreeClassifier
import numpy as np


# main prediction (use decision tree)
def load_train_test(file_id, train_path, test_path):
    train_x = list()
    train_y = list()
    test_x = list()

    with open(train_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            train_x.append((
                int(row[1]), int(row[2]), int(row[3]), float(row[8])))
            train_y.append(int(row[9]))

    with open(test_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if int(row[0]) == int(file_id):
                file_type = int(row[1])
                file_uid = int(row[2])
                file_gid = int(row[3])
                file_access = int(row[4])
                file_write = int(row[5])
                file_gap_time = (file_access - file_write) / 86400
                test_x.append((
                    file_type, file_uid, file_gid, float(file_gap_time)))
                break
    train_x = np.array(train_x)
    train_y = np.array(train_y)
    test_x = np.array(test_x)
    return (train_x, train_y, test_x)


def decision_test(train_x, train_y, test_x):
    clf = DecisionTreeClassifier()
    clf.fit(train_x, train_y)
    pre = clf.predict(X=[test_x[0]])
    return pre[0]


if __name__ == "__main__":
    temp_fid = set()
    datasets_path = " "  # datasets(have label)
    test_path = " "  # test path (use readTraces to get)
    with open(test_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        x = 0
        y = 0
        for row in reader:
            train_x, train_y, test_x = load_train_test(row[0], datasets_path, test_path)
            ifrom = decision_test(train_x, train_y, test_x)
            fid = int(row[0])
            if fid not in temp_fid:
                x = x + int(ifrom)
                y = y + 1
                temp_fid.add(fid)
        ifrom_rate = x / y
        print("read-only rate：%.2f" % ((ifrom_rate) * 100) + "%")
