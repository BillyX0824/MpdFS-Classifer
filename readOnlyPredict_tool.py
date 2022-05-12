from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, accuracy_score, roc_auc_score
from time import *


def logistic_test(train_x, train_y, test_x, test_y):
    clf = LogisticRegression(tol=1e-2, max_iter=5000)

    train_time_begin = time()
    clf.fit(train_x, train_y)
    train_time_end = time()

    predict = list()
    predict_time_begin = time()
    for i in range(len(test_x)):
        pre = clf.predict(X=[test_x[i]])
        predict.append(pre[0])
    predict_time_end = time()

    precision = precision_score(test_y, predict)
    recall = recall_score(test_y, predict)
    accuracy = accuracy_score(test_y, predict)
    roc = roc_auc_score(test_y, predict)
    train_time = int((train_time_end - train_time_begin) * 1e6)
    predict_time = int((predict_time_end - predict_time_begin) * 1e6 / len(test_y))
    print(
        "{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(precision * 100,
                                                                                            accuracy * 100,
                                                                                            recall * 100,
                                                                                            roc * 100, train_time,
                                                                                            predict_time))


def bayes_test(train_x, train_y, test_x, test_y):
    clf = GaussianNB()

    train_time_begin = time()
    clf.fit(train_x, train_y)
    train_time_end = time()

    predict = list()
    predict_time_begin = time()
    for i in range(len(test_x)):
        pre = clf.predict(X=[test_x[i]])
        predict.append(pre[0])
    predict_time_end = time()

    precision = precision_score(test_y, predict)
    recall = recall_score(test_y, predict)
    accuracy = accuracy_score(test_y, predict)
    roc = roc_auc_score(test_y, predict)
    train_time = int((train_time_end - train_time_begin) * 1e6)
    predict_time = int((predict_time_end - predict_time_begin) * 1e6 / len(test_y))
    print(
        "{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(precision*100, accuracy*100, recall*100,
                                                                                            roc*100, train_time,
                                                                                            predict_time))


def decision_test(train_x, train_y, test_x, test_y):
    clf = DecisionTreeClassifier()

    train_time_begin = time()
    clf.fit(train_x, train_y)
    train_time_end = time()

    predict = list()
    predict_time_begin = time()
    for i in range(len(test_x)):
        pre = clf.predict(X=[test_x[i]])
        predict.append(pre[0])
    predict_time_end = time()

    precision = precision_score(test_y, predict)
    recall = recall_score(test_y, predict)
    accuracy = accuracy_score(test_y, predict)
    roc = roc_auc_score(test_y, predict)
    train_time = int((train_time_end - train_time_begin) * 1e6)
    predict_time = int((predict_time_end - predict_time_begin) * 1e6 / len(test_y))
    print(
        "{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(precision * 100,
                                                                                            accuracy * 100,
                                                                                            recall * 100,
                                                                                            roc * 100, train_time,
                                                                                            predict_time))


def adaboost_test(train_x, train_y, test_x, test_y):
    clf = AdaBoostClassifier()

    train_time_begin = time()
    clf.fit(train_x, train_y)
    train_time_end = time()

    predict = list()
    predict_time_begin = time()
    for i in range(len(test_x)):
        pre = clf.predict(X=[test_x[i]])
        predict.append(pre[0])
    predict_time_end = time()

    precision = precision_score(test_y, predict)
    recall = recall_score(test_y, predict)
    accuracy = accuracy_score(test_y, predict)
    roc = roc_auc_score(test_y, predict)
    train_time = int((train_time_end - train_time_begin) * 1e6)
    predict_time = int((predict_time_end - predict_time_begin) * 1e6 / len(test_y))
    print(
        "{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(precision * 100,
                                                                                            accuracy * 100,
                                                                                            recall * 100,
                                                                                            roc * 100, train_time,
                                                                                            predict_time))


def randomforest_test(train_x, train_y, test_x, test_y):
    clf = RandomForestClassifier()

    train_time_begin = time()
    clf.fit(train_x, train_y)
    train_time_end = time()

    predict = list()
    predict_time_begin = time()
    for i in range(len(test_x)):
        pre = clf.predict(X=[test_x[i]])
        predict.append(pre[0])
    predict_time_end = time()

    precision = precision_score(test_y, predict)
    recall = recall_score(test_y, predict)
    accuracy = accuracy_score(test_y, predict)
    roc = roc_auc_score(test_y, predict)
    train_time = int((train_time_end - train_time_begin) * 1e6)
    predict_time = int((predict_time_end - predict_time_begin) * 1e6 / len(test_y))
    print(
        "{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(precision * 100,
                                                                                            accuracy * 100,
                                                                                            recall * 100,
                                                                                            roc * 100, train_time,
                                                                                            predict_time))


