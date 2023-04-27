# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: AspectClassification
@file   : loadEmbedding.py
@version: 1.0
@time   : 2018-05-31
@author : Jianzhang Zhang, <jianzhang.zhang@foxmail.com>

为了快速加载和节省内存, 将fastText的文本embedding
用dict保存word2idx, 用numpy array保存词向量dict中的idx对应numpy array中的行索引
word2idx用json格式保存到本地, 词向量用numpy二进制格式npy保存到本地
分别保存为word2idx字典和embeddingArray
"""

import io
import numpy as np
from utils.fileUtils import dumpToFile
import gensim
from gensim.models import KeyedVectors

# # ----- 重要参数 -----
# embeddingDir = "/home/zjz/PycharmProjects/AspectClassification/embeddings/"
# embeddingName = "wiki-news-300d-1M"
#
#
# embeddingText = embeddingDir + embeddingName + ".vec"
# embeddingNpy = embeddingDir + embeddingName + "npy"
# word2idxPkl = embeddingDir + embeddingName + ".word2idx.pkl"
# fin = io.open(embeddingText, 'r', encoding='utf-8', newline='\n', errors='ignore')
# # n表示词个数, d表示向量维度
# n, d = map(int, fin.readline().split())
# embeddingMatrix = np.empty((n,d),dtype=float)
# word2idx = {}
# for idx,line in enumerate(fin):
# 	tokens = line.rstrip().split(' ')
# 	word = tokens[0]
# 	word2idx[word] = idx
# 	vec = np.asarray(tokens[1:],dtype=float)
# 	embeddingMatrix[idx] = vec
# fin.close()
# # 将word2idx和embeddingMatrix保存到本地
# np.save(embeddingNpy,embeddingMatrix)
# dumpToFile(word2idxPkl,word2idx)

# m = gensim.models.KeyedVectors.load_word2vec_format(
# 	"/home/zjz/PycharmProjects/AspectClassification/embeddings/wiki-news-300d-1M.vec")
# m = KeyedVectors.load("/home/zjz/PycharmProjects/AspectClassification/embeddings/fastText.bin"
# )

m = gensim.models.KeyedVectors.load_word2vec_format("/home/zjz/PycharmProjects/RE2019/issueExtraction/wiki-news-300d-1M-subword.txt")
# fin = io.open("/home/zjz/sgns.target.word-character.char1-2.dynwin5.thr10.neg5.dim300.iter5", 'r', encoding='utf-8', newline='\n', errors='ignore')
print "done."

