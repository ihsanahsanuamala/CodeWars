def spin_words(sentence):
    x = sentence.split()
    str = " "
    for i in range(len(x)):
        if len(x[i])>=5:
            x[i] = x[i][::-1]
    return(str.join(x))        
print(spin_words("letter words words word will with a reversed when or included of the letter"))