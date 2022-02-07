def anagrams(word, words):
    #your code here
    temp = []
    word = [char for char in word]
    for i in range(len(words)):
        if len(word) == len(words[i]):
            checker = [char for char in words[i]]
            if set(word) == set(checker):
                tes = ''.join(checker)
                temp.append(tes) 
    return temp       
    

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))