vowel_list = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()

    if word == "end":
        break  # exit loop

    is_acceptable = True  # initialize 

    # case 1 )  at least one vowel
    if not any(char in vowel_list for char in word):
        is_acceptable = False 

    vowel_cnt, conso_cnt = 0, 0

    # count consecutive vowels or consonants to check case 2
    for char in word:
        if char in vowel_list:
            vowel_cnt += 1
            conso_cnt = 0
        else:
            conso_cnt += 1
            vowel_cnt = 0

        # case 2 )  three consecutive vowels or consonants
        if vowel_cnt == 3 or conso_cnt == 3:
            is_acceptable = False
            break

    # case 3 )  same letter twice in a row (except e or o)
    for i in range(1, len(word)):
        if word[i] == word[i - 1] and word[i] not in ['e', 'o']:
            is_acceptable = False
            break

    print(f"<{word}> is {'acceptable' if is_acceptable else 'not acceptable'}.")
            