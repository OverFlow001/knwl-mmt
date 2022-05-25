#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# NOTICE FILE in the root directory of this source tree.
#


"""
Example: python data/vocab.txt data/train.txt
vocab.txt: 1stline=word, 2ndline=count
"""

import os
import sys

from src.logger import create_logger
from src.data.dictionary import Dictionary, KnowledgeDictionary


if __name__ == '__main__':

    logger = create_logger(None, 0)

    print(sys.argv)

    voc_path = sys.argv[1]
    txt_path = sys.argv[2]
    bin_path = sys.argv[2] + '.pth'
    use_k = len(sys.argv) == 4
    if use_k:
        name2id_path = sys.argv[3]
        print('k will be used')
    else:
        print('k will not be used')
    assert os.path.isfile(voc_path)
    assert os.path.isfile(txt_path)
    assert (not use_k) or (os.path.isfile(name2id_path) and name2id_path.endswith('.pkl'))

    if use_k:
        dico = Dictionary.read_vocab(voc_path, name2id_path)
        k_dico = KnowledgeDictionary.read_knowledge(name2id_path)
    else:
        dico = Dictionary.read_vocab(voc_path)

    logger.info("")

    data = Dictionary.index_data(txt_path, bin_path, dico, k_dico if use_k else None)
    logger.info("%i words (%i unique) in %i sentences." % (
        len(data['sentences']) - len(data['positions']),
        len(data['dico']),
        len(data['positions'])
    ))
    if len(data['unk_words']) > 0:
        logger.info("%i unknown words (%i unique), covering %.2f%% of the data." % (
            sum(data['unk_words'].values()),
            len(data['unk_words']),
            sum(data['unk_words'].values()) * 100. / (len(data['sentences']) - len(data['positions']))
        ))
        if len(data['unk_words']) < 30:
            for w, c in sorted(data['unk_words'].items(), key=lambda x: x[1])[::-1]:
                logger.info("%s: %i" % (w, c))
