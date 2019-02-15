import json

import jieba
import pandas as pd
from sklearn import svm
from sklearn import tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier


def cut(content):
    return ' '.join(jieba.cut(content))


def get_top_corpus_source(n, filename='../data/sqlResult_1558435.csv', encoding='gb18030'):
    data_csv = pd.read_csv(filename, header=0, encoding=encoding)
    corpus, sources = [], []
    for i in range(n):
        if isinstance(data_csv['content'][i], float):  # 排除float型空行
            corpus.append('')
            sources.append('x')
            continue

        corpus.append(cut(data_csv['content'][i].replace('\r\n', '').replace(u'\u3000', '')))
        if 'site' in data_csv['feature'][i]:
            sources.append(json.loads(data_csv['feature'][i])['site'])
        else:
            sources.append("x")
    return corpus, sources


def tf_idf(data_set):
    vectorizer = TfidfVectorizer()
    vector = vectorizer.fit_transform(data_set[0])
    return vector.toarray(), data_set[1]


def split_data_set(data_set, training_rate=0.7):
    train_index = int(training_rate * len(data_set[1]))
    train_x = data_set[0][:train_index]
    train_y = data_set[1][:train_index]

    test_x = data_set[0][train_index:]
    test_y = data_set[1][train_index:]
    return train_x, train_y, test_x, test_y


def train(method_name, train_x, train_y):
    method_func = {
        'LogisticRegression': LogisticRegression(),
        'KNeighborsClassifier': KNeighborsClassifier(),
        'SVM': svm.SVC(),
        'NaiveBayes': GaussianNB(),
        'DecisionTree': tree.DecisionTreeClassifier()
    }[method_name]
    method_func.fit(train_x, train_y)
    return method_func


def accuracy(t, p):
    tpc = 0
    for i in range(len(t)):
        if t[i] == p[i]:
            tpc = tpc + 1
    return float(tpc / len(t))


method_names = ['LogisticRegression', 'KNeighborsClassifier', 'SVM', 'NaiveBayes', 'DecisionTree']
corpus_source = get_top_corpus_source(1000)
ds = tf_idf(corpus_source)
tt_data = split_data_set(ds)
for method in method_names:
    recognizer = train(method, tt_data[0], tt_data[1])
    predict_rs = recognizer.predict(tt_data[2])
    print(method + " accuracy:" + str(accuracy(tt_data[3], predict_rs)))
