import random

grammar_str = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article => 一个 | 这个 | 那个
noun => 女人 | 篮球 | 桌子 | 小猫 | 小可爱
verb => 看着 | 坐在 | 听着 | 看见
Adj => 蓝色的 | 好看的 | 小小的 | 有趣的
"""

def parse_grammar():
    grammar_dict = {}
    for line in grammar_str.split('\n'):
        if not line: continue
        index, terms = line.split("=>")
        grammar_dict[index.strip()] = [term.split() for term in terms.split('|')]
    return grammar_dict

def generate(grammar, target):
    if target == "null": return ""
    if target not in grammar: return target
    terms = random.choice(grammar[target])
    if terms.count == 1: return generate(grammar, terms)
    return "".join([generate(grammar, term) for term in terms])

print(generate(parse_grammar(),'sentence'))