def all_perms(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp

word1 = input("Enter the first string: ")
word2 = input("Enter the second string: ")
if word2.lower() in list(all_perms(word1.lower())):
    print(f"{word1} and {word2} are anagrams")
