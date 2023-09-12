count = 0
find = False
dict_alpha = ['A','E','I','O','U']
def dictionary(word, dict_word):
    global count, find
    if word == dict_word and not find:
        find = True
    elif len(dict_word) <= 4 and not find:
        for i in dict_alpha:
            count += 1
            dictionary(word, dict_word + i)
            if find:
                break
                
        
    
def solution(word):
    dictionary(word, '')
    return count
