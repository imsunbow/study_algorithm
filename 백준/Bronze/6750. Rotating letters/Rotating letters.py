#백준 6750: rotating letters

letter = input()
letter_dic = {'I','O','S','H','Z','X','N'}

for i in range(len(letter)):
    if letter[i] not in letter_dic:
        print("NO")
        break
else:
    print("YES")