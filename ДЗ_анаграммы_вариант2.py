def anagrams(s, p):
    letters_p = {}
    ind = set()
    k = 0
    for letter in p:
        letters_p[letter] = p.count(letter)
    for i in range(len(s) - len(p)):
        string = s[i: i + len(p)]
        for letter in string:
            if letter in letters_p:
                if letters_p[letter] == string.count(letter):
                    k += 1
        if k == len(string):
            ind.add(i)
        k = 0
    return list(ind)


s = "cbaebabacd"
p = "abc"
print(anagrams(s, p))
