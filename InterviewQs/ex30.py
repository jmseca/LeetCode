def ex30(words, s):
    
    def find_and_increment(seen, substring):
        found_indx = -1
        for i,n in enumerate(seen):
            if n[0]==substring:
                if n[1] == 0:
                    n[1] += 1
                    return True
                else:
                    found_indx = i
        if found_indx>-1:
            seen[found_indx][1]+=1
        return False

    def all_seen(seen):
        return all(map(lambda x:x[1]==1, seen))

    def reset_seen(seen):
        return [[w,0] for w in words]

    
    length_words_i = len(words[0])
    length_words = len(words)*length_words_i
    length_s = len(s)
    seen = [[w,0] for w in words]
    output = []
    for i in range(0, length_s):

        if len(s[i:]) >= length_words:
            
            for n in range(i, i+length_words, length_words_i):
                substring = s[n:(n+length_words_i)]
                if not(find_and_increment(seen, substring)):
                    break

            # Check if every sub word exists only once in the current substring
            if all_seen(seen):
                output += [i]
    return output



s = "lingmindrabofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]

print(ex30(words,s))