#백준 11944: NN

A,B = map(int,input().split())

print(str(A)*A if A<B else (str(A)*A)[:B])


