# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:53:39 2020

@author: lucifelex
"""


"""
import jieba
text1="我去過清華大學和交通大學。"
test2="小明來到了航研大廈"
seg_list = jieba.cut(text1, cut_all=True, HMM=False)        #
# 對於詞庫內沒有的詞使用 HMM Hidden Markov Model 隱馬可夫模型 及 Viterbi算法辨識出來
print("Full Mode: " + "/ ".join(seg_list))      # .join 陣列分隔符號


seg_list = jieba.cut(text1, cut_all=False, HMM=True)        #系統預設分割設定
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

print(", ".join(jieba.cut(test2, HMM=True)))
print(", ".join(jieba.cut(test2, HMM=False)))
print(", ".join(jieba.cut(test2)))
print(", ".join(jieba.cut_for_search(test2) ))      #透過網路資料分詞
"""


"""
# load_userdict 輸入使用者定義字典
# posseg  取得詞性
# extract_tags  算出關鍵字權重
# textrank  算出關鍵字權重
import sys
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)      #取得現在的路徑

text = open(path.join(d, 'test.txt'),'r',encoding='utf-8').read()

text=text.replace(" ", "")
text=text.replace("「", "")
text=text.replace("」", "")
text=text.replace("，", "")
text=text.replace("。", "")
print('/'.join(jieba.cut(text)))        #預設模式
print("1 ====================")
jieba.load_userdict(path.join(d, 'userdict.txt'))   #輸入使用者定義字典
print('/'.join(jieba.cut(text)))
print("2 ====================")
words =jieba.posseg.cut(text)       #取得詞性
for word, flag in words:
    print('%s, %s' % (word, flag))
print("3 ====================")
if (sys.version_info > (3, 0)):
  content=text
else:
  content = text.decode('utf_8')    #使用unicode編碼 python 2.0
keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
for item in keywords:
    if (sys.version_info > (3, 0)):
        print(" %s =  %f "  %  (item[0], item[1]))
    else:
        print(" %s =  %f " % (item[0].encode('utf_8'), item[1]))
        # item[0] 分詞陣列
        # item[1] 權重
print("4 ====================")
keywords = jieba.analyse.textrank(content, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# 取得 topK(前20個)關鍵字   allowPOS 只截取地名、名詞、動名詞、動詞
for item in keywords:
    print(" %s =  %f " % (item[0].encode('utf_8'), item[1])) 
    # item[0] 關鍵字
    # item[1] 權重
"""
    


"""
# suggest_freq 自定義分詞
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
text ="post部落格中將出错，台中的名產中太陽餅是台中特產最出名"
#text="如果放到post中将出错。"
text=text.replace("，", "")
print('/'.join(jieba.cut(text)))
jieba.suggest_freq('台中', True)      #非讀取自定義字典, 定義自定義詞的用法
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('名產'), True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('部落格'), True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('太陽餅'), True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('中', '將'), True)
print('/'.join(jieba.cut(text)))
"""


"""
# tokenize 取得斷詞位置
import sys
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
text = "柯博文老師，喜歡去「甜心一點DIY烘焙坊」做蛋糕。"
jieba.load_userdict(path.join(d, 'userdict.txt'))
# 字符串前面加u表示使用unicode编码
if (sys.version_info > (3, 0)):
  content = text
else:
  content = text.decode('utf_8')  # 使用unicode編碼 
print(' default'+'-'*40)
result = jieba.tokenize(content)        #取得斷詞位置
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
# tk[0] 分詞陣列
# tk[1] 文字起始位置
# tk[2] 文字終止位置

print(' tokenize search'+'-'*40)

result = jieba.tokenize(content, mode='search')     #取得網路搜尋用斷詞
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))         
"""
    


"""
# set_stop_words  移除用詞
# set_idf_path  自定義權重
import sys
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
text = "柯博文老師和我們喜歡去甜心一點DIY烘焙坊做蛋糕"
jieba.load_userdict(path.join(d, 'userdict.txt'))
if (sys.version_info > (3, 0)):
  content = text
else:
  content = text.decode('utf_8')
print(",".join(jieba.analyse.extract_tags(text, topK=10)))
jieba.analyse.set_stop_words("stop_words.txt")      #移除用詞
print(",".join(jieba.analyse.extract_tags(text, topK=10)))


print(' default idf'+'-'*40)
keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=True, allowPOS=()) #topK=TF/IDF 
print(" topK=TF/IDF , TF=%d" % len(keywords))
for item in keywords:
    if (sys.version_info > (3, 0)):
        print(" %s =  %f "  %  (item[0], item[1]))      # 分別為關鍵詞和相應的權重
    else:
        print(" %s =  %f " % (item[0].encode('utf_8'), item[1]))     # 關鍵詞和權重


print('set_idf_path'+'-'*40)
jieba.analyse.set_idf_path("idf.txt")       #自定義分詞權重
keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=True, allowPOS=())
for item in keywords:
    if (sys.version_info > (3, 0)):
        print("  %s   TF=%f , IDF=%f  topK=%f" % (item[0], item[1], len(keywords)*item[1], item[1]*len(keywords)*item[1]))      # 分別為關鍵詞和相應的權重
    else:
        print(" %s   TF=%f , IDF=%f  topK=%f" % (item[0].encode('utf_8'), item[1],len(keywords)*item[1], item[1]*len(keywords)*item[1]))     # 關鍵詞和權重
"""



"""
# 排列最常出現的分詞
import sys
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
if (sys.version_info > (3, 0)):
	text = open(path.join(d, 'test.txt'),'r',encoding='utf-8').read()
else:
	text = open(path.join(d, 'test.txt'),'r').read()

text=text.replace('\n', '')
jieba.analyse.set_stop_words("stop_words.txt")
print('/'.join(jieba.cut(text)))
print("====================")
jieba.load_userdict(path.join(d, 'userdict.txt'))
dic={}
for ele in jieba.cut(text):
    if ele not in dic:
        dic[ele]=1
    else:
        dic[ele]=dic[ele]+1

for w in sorted(dic, key=dic.get, reverse=True):
    print("%s  %i " % (w, dic[w]))
"""



# ERROR
import sys
import jieba
import jieba.analyse
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

try:
    url="http://www.powenko.com/wordpress/"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:
            contents=reponse.read()
        #print(contents)

        #print(",".join(jieba.analyse.extract_tags(contents, topK=1000)))
        jieba.analyse.set_stop_words("stop_words.txt")
        #print(",".join(jieba.analyse.extract_tags(contents, topK=1000)))

        dic = {}
        #keywords = jieba.analyse.extract_tags(contents, topK=40, withWeight=True, allowPOS=())
        keywords = jieba.analyse.extract_tags(contents, topK=100, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
        for item in keywords:
            if (sys.version_info > (3, 0)):
                print(" %s =  %f  %s "  %  (item[0], item[1],flag))
            else:
                print(" %s =  %f  " % (item[0].encode('utf_8'), item[1] ))
        print("="*40)
        words =jieba.posseg.cut(contents)
        for word, flag in words:
            if flag=="ns" or flag=="n" or flag=='vn' or flag=='n':
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] = dic[word] + 1
        for w in sorted(dic, key=dic.get, reverse=True):
            if dic[w]>1:
               print("%s  %i " % (w, dic[w]))

except:
    print("error")














