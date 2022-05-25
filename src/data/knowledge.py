from nltk.corpus import wordnet as wn

"""
attach_knowledge_bpe
bpe: space splitted bpe tokens
e.g.
input: a fo@@ untain and co@@ bbled walk@@ way in the fore@@ ground , a pink and white bu@@ id@@ ling with many ar@@ ches in the background ; trees on the right ;
output: [[[31924, 39409, 35303, 34803], [6693], 'InWord', [], [36742, 24559], 'InWord', [3150], 'InWord', [10236, 31119, 4809], [], [32602, 4480], 'InWord', [], [31924, 39409, 35303, 34803], [21835, 25296, 18456, 33883], [], [8121, 14679, 20780, 32952, 33163, 13939, 2366], [], 'InWord', 'InWord', [], [], [35985, 14895, 16000, 14896], 'InWord', [10236, 31119, 4809], [], [38460, 40615, 11659, 33958, 18966, 11658], [], [2497, 38008, 11754, 13459], [], [], [4707, 22383, 30190, 37132, 4706, 8293, 221, 5213], []]]
"""
def attach_wordnet_bpe(bpe: str, name2id: dict, in_word_policy='same', lang='en'):
    # if name2id is None:
        # import pickle, os
        # filename = os.path.dirname(__file__) + '/wn_name2id.pkl'
        # with open(filename, 'rb') as n2i_file:
            # name2id = pickle.load(n2i_file)
    lang = {
        'en': 'eng',
        'de': 'ger',
        'fr': 'fra'
    }[lang]
    result = []
    if lang == 'ger':
        result = [[] for _ in bpe.split('\n')]
    else:
        for line in bpe.split('\n'):
            knowledge_line = []
            token_length = 0
            word = ''
            for token in line.split():
                token_length += 1
                if token.endswith('@@'):
                    word += token[:-2]
                else:
                    word += token

                    # a word is made
                    synsets = wn.synsets(word, lang=lang)
                    names = [s.name() for s in synsets]
                    ids = [name2id[n] for n in names if n in name2id]
                    knowledge_line.append(ids)
                    if in_word_policy == 'mark':
                        knowledge_line.extend(['InWord'] * (token_length-1))
                    elif in_word_policy == 'same':
                        knowledge_line.extend([ids] * (token_length - 1))
                    elif in_word_policy == 'empty_list':
                        knowledge_line.extend([[]] * (token_length - 1))

                    # reset
                    word = ''
                    token_length = 0
            result.append(knowledge_line)
    return result[:-1] if bpe.endswith('\n') else result


def generate_entity2id():
    i = 0
    content = ''
    for synset in wn.all_synsets():
        content += synset.name()
        content += '\t'
        content += str(i)
        content += '\n'
        i += 1
    with open('entity2id', 'w') as f:
        f.write(content)
