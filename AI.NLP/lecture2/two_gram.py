import unigram as ug

def get_n_gram_words(phrase,n):
    return [phrase[i:i + n] for i in range(len(phrase) - n)]

from collections import Counter

from functools import reduce
from operator import mul

# 2 gram 概率模型
def get_2_gram_prob(phrase):
    phrase_2_gram_words = get_n_gram_words(phrase,2)
    all_content = ug.read_tokenized_file_content()
    all_chars_countered = Counter(all_content)
    SUM2 = sum(all_chars_countered.values())

    simple_2_gram_prob = reduce(mul,[(1 if all_chars_countered[term] else all_chars_countered[term])/SUM2 for term in phrase_2_gram_words])
    last_char_prob = ug.get_unigram_prob(phrase[-1:][0])
    return simple_2_gram_prob * last_char_prob / reduce(mul,[ug.get_unigram_prob(char_) for char_ in phrase])

print(get_2_gram_prob("中华名族伟大复兴"))
