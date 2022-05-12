import csv
import readOnlyPredict_tool as rop
import numpy as np


def load_train_test(train_path, test_path):
    train_x = list()
    train_y = list()
    test_x = list()
    test_y = list()

    with open(train_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            train_x.append((
                int(row[1]), int(row[2]), int(row[3]), float(row[8])))
            train_y.append(int(row[9]))

    with open(test_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            test_x.append((
                int(row[0]), int(row[1]), int(row[2]), float(row[3])))
            test_y.append(int(row[4]))

    train_x = np.array(train_x)
    train_y = np.array(train_y)
    test_x = np.array(test_x)
    test_y = np.array(test_y)
    return (train_x, train_y, test_x, test_y)


if __name__ == "__main__":
    datasets_csv_path = " "  # datasets
    train_csv_path = " "  # train data
    train_x, train_y, test_x, test_y = load_train_test(datasets_csv_path, train_csv_path)
    print("Train Size: " + str(len(train_y)))
    print("Test Size: " + str(len(test_y)))
    print("Algorithm\t\t\t\t\tprecision\t\t\tAccuracy\t\t\tRecall\t\t\t\troc\t\t\t\tTraining Time(us)"
          "\t\t\tprediction Time(us)")
    print("Logistic Regression:", end="\t\t")
    rop.logistic_test(train_x, train_y, test_x, test_y)
    print("Naive Bayes:", end="\t\t\t\t")
    rop.bayes_test(train_x, train_y, test_x, test_y)
    print("Decision Tree:", end="\t\t\t\t")
    rop.decision_test(train_x, train_y, test_x, test_y)
    print("AdaBoost:", end="\t\t\t\t\t")
    rop.adaboost_test(train_x, train_y, test_x, test_y)
    print("Random Forest:", end="\t\t\t\t")
    rop.randomforest_test(train_x, train_y, test_x, test_y)
