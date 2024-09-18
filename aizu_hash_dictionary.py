# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_C
import hashlib
# ハッシュテーブルの作成
# ハッシュ値を返す関数
# 辞書に含まれるか確認

class HashTable():

    def __init__(self,size=10) -> None:
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def hash(self,key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(),base=16) % self.size
    
    def insert(self,key)-> None:
        index = self.hash(key)
        self.table[index].append(key)


hashtable = HashTable()
hashtable.insert("AAA")
hashtable.insert("AAC")