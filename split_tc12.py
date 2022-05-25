import random
import re

matcher = re.compile(r'<DESCRIPTION>(.*)</DESCRIPTION>', re.S)
def extract_desc(fn: str):
    with open(fn, encoding='iso-8859-1') as f:
        text = f.read()
    match = matcher.findall(text)
    assert len(match) == 1, f'{len(match)} match in {text}'
    desc = match[0].strip()
    desc.replace('\n', ' ')
    # print(desc)
    return desc

indices = list(range(19999))
random.shuffle(indices)
train_en_idx = sorted(indices[:9000])
train_de_idx = sorted(indices[9000:18000])
valid_en_idx = sorted(indices[18000:18500])
valid_de_idx = sorted(indices[18500:19000])
test_idx = sorted(indices[19000:])
with open('eng_list') as fe, open('ger_list') as fd, open('img_list') as fi:
    en_files = fe.readlines()
    de_files = fd.readlines()
    im_files = fi.readlines()
files = {'en': en_files, 'de': de_files}
splits = [train_de_idx, train_en_idx, valid_de_idx, valid_en_idx, test_idx, test_idx]
split_names = ['all.de', 'all.en', 'val.de', 'val.en', 'test.en', 'test.de']
for split, sn in zip(splits, split_names):
    descs = []
    lang = 'en' if 'en' in sn else 'de'
    for i in split:
        fn = files[lang][i].strip()
        # print(fn)
        desc = extract_desc(fn)
        descs.append(desc)
    print('descs length: ' + str(len(descs)))
    joined = '\n'.join(descs)
    with open(sn, 'w') as f:
        f.write(joined)
idx_names = ['idx.de', 'idx.en']
for split, in_ in zip(splits, idx_names):
    joined = '\n'.join(map(str, split))
    with open(in_, 'w') as f:
        f.write(joined)

