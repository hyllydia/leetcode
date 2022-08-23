def mostCommonWord(paragraph, banned):
    hash_map = {}
    words = paragraph.split(" ")
    words=[word.lower() for word in words]
    print(words)
    for word in words:
        hash_map[word] = hash_map.get(word, 0) + 1
    d = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
    print(d)
    key_list = d.keys()
    print(key_list)
    for k in key_list:
        while k not in banned:
            return k
        break

if __name__=="__main__":
    paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
    banned=["hit"]
    print(mostCommonWord(paragraph,banned))