grammar_str = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article => 一个 | 这个
noun => 女人 | 篮球 | 桌子 | 小猫
verb => 看着 | 坐在 | 听着 | 看见
Adj => 蓝色的 | 好看的 | 小小的
"""

def parse_grammar():
    grammar_dict = {}
    for line in grammar_str.split('\n'):
        if not line: continue
        index, terms = line.split("=>")
        grammar_dict[index.strip()] = [term.split() for term in terms.split('|')]
    print(grammar_dict)
    return grammar_dict

parse_grammar()
def generate(grammar, target):
    if target not in grammar: return target
    terms = random.choice(grammar[target])
    
    #if subtarget not in grammar and not