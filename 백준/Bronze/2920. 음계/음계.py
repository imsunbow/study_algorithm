#백준 2920 음계

a,b,c,d,e,f,g,h  = map(int,input().split())

if a<b<c<d<e<f<g<h:
    print("ascending")
elif a>b>c>d>e>f>g>h:
    print("descending")
else:
    print("mixed")