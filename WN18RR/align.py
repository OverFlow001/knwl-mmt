with open('names.txt') as names_file:
    name_lines = names_file.readlines()
with open('ids.txt') as ids_file:
    id_lines = ids_file.readlines()
assert len(name_lines) == len(id_lines)

e2i = dict()
with open('entity2id.txt') as e2i_file:
    count = int(e2i_file.readline())
    for line in e2i_file.readlines():
        e, i = map(lambda s: s.strip(), line.split('\t'))
        e2i[e] = int(i)
    assert len(e2i) == count

alignment = dict()
# rev = dict()
for name_line, id_line in zip(name_lines, id_lines):
    # print(name_line, id_line)
    name_tuple = name_line.split('\t')
    id_tuple = id_line.split('\t')
    assert len(name_tuple) == 3
    assert len(id_tuple) == 3
    assert name_tuple[1] == id_tuple[1]
    n1 = name_tuple[0].strip()
    i1 = id_tuple[0].strip()
    n2 = name_tuple[2].strip()
    i2 = id_tuple[2].strip()
    
    assert i1 in e2i
    if n1 in alignment:
        assert alignment[n1] == e2i[i1]
    elif i1 in e2i:
        alignment[n1] = e2i[i1]
    # if e2i[i1] in rev:
        # if rev[e2i[i1]] != n1:
            # print(f'o: {rev[e2i[i1]]}\nn: {n1}\n')
    # else:
        # rev[e2i[i1]] = n1
    
    assert i2 in e2i
    if n2 in alignment:
        assert alignment[n2] == e2i[i2]
    elif i2 in e2i:
        alignment[n2] = e2i[i2]
    # if e2i[i2] in rev:
        # if rev[e2i[i2]] != n2:
            # print(f'o: {rev[e2i[i2]]}\nn: {n2}\n')
    # else:
        # rev[e2i[i2]] = n2
print(len(alignment))
# assert len(alignment) == count

# special words
specials = ['<s>', '</s>', '<pad>']
len_special = len(specials)
# insert <pad>
for key in alignment:
    alignment[key] += len_special
for i, s in enumerate(specials):
    alignment[s] = i

output = '\n'.join(f'{k}\t{v}' for k, v in alignment.items())
with open('name2id.txt', 'w') as f:
    f.write(output)
with open('name2id.pkl', 'wb') as f:
    import pickle
    pickle.dump(alignment, f)
