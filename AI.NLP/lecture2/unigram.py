import re

def read_file(filename='10k_articles.txt'):
    file = open(filename,encoding='utf-8')
    return file.read()

def tokenize(content):
    return ''.join(re.findall(r'[\w|\d]+', content))

def read_tokenized_file_content():
    return tokenize(read_file())

from collections import Counter

def get_char_prob_func(all_content):
    all_chars_countered = Counter(all_content)
    SUM = sum(all_chars_countered.values())
    def get_char_prob_in(char_):
        return all_chars_countered[char_] / SUM
    return get_char_prob_in

get_char_prob = get_char_prob_func(read_tokenized_file_content())

from functools import reduce
from operator import mul

# 1 gram 概率模型
def get_unigram_prob(phrase):
    return reduce(mul,[get_char_prob(char_) for char_ in phrase])

print(get_unigram_prob("中华名族伟大复兴"))
