#백준 10808: 알파벳 개수

x = list(str(input()))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet)):
    y = x.count(alphabet[i])
    print(y,end=' ')

