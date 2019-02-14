import json

import jieba
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression


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
    return vector, data_set[1]


def split_data_set(data_set, training_rate=0.7):
    train_index = int(training_rate * len(data_set[1]))
    train_x = data_set[0][:train_index]
    train_y = data_set[1][:train_index]

    test_x = data_set[0][train_index:]
    test_y = data_set[1][train_index:]
    return train_x, train_y, test_x, test_y


def train_by_lr(train_x, train_y):
    lr = LinearRegression()
    lr.fit(train_x, train_y)
    return lr


def train(method_func, train_x, train_y):
    method_func.fit(train_x, train_y)
    return method_func


def predict(method_func, test_x):
    return method_func.predict(test_x)
