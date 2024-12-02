
def equals(word_one, word_two):
    if len(word_one) != len(word_two):  #cant be the same word if the dont have the same length
        return False
    if len(word_one) == 0 and len(word_two) == 0:
        return True
    elif len(word_one) == 0 and len(word_two) != 0:
        return False
    elif len(word_one) != 0 and len(word_two) == 0:
        return False
    
    else:
        if word_one[0] == word_two[0]:
            return equals(word_one[1:], word_two[1:])  #check the next characters in the word
        else:
            return False
        
        
def query(pattern, word):
     #if len(pattern) != len(word):
        #return False
    if len(pattern) == 0 and len(word) == 0:
        return True
    if len(pattern) == 0 or len(word) == 0:
        return False
    if pattern[0] == "?":
        return query(pattern[1:], word[1:])
    else:
        if pattern[0] == word[0]:
            return query(pattern[1:], word[1:])
        else:
            return False
        
        
def match(pattern, word):
    if len(pattern) == 0 and len(word) == 0:
        return True
    if len(pattern) == 0:
        return False    
    if len(word) == 0: 
        return pattern == "*" * len(pattern)
    
    if pattern[0] == "*":
        return match(pattern[1:], word) or match(pattern, word[1:])
    
    if pattern[0] == "?":   #just like query() function
        return query(pattern[1:], word[1:])
    
    if pattern[0] == word[0]:
        return match(pattern[1:], word[1:])
    
    return False