
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0319Mon_LA.txt","r")
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0320Tue_LA.txt","r")
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0321Wed_LA.txt","r")
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0322Thu_LA.txt","r")
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0323Fri_LA.txt","r")
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0324Sat_LA.txt","r")
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0325Sun_LA.txt","r")
#f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0326Mon_LA.txt","r")
f = open("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/LA/beer_LA/beer_0327Tue_LA.txt","r")

it = 0
T,P,N =0,0,0
List = []

for line in f:    ####### can not transfer value???!?!?!?!?
    if(it==0):
        it = 1
        continue
    lis = []
    TOTAL, pos, neg = line.split()
    lis.append(int(TOTAL))
    lis.append(int(pos))
    lis.append(int(neg))
    List.append(lis)

for ii in range(len(List)):
    T = T + List[ii][0]
    P = P + List[ii][1]
    N = N + List[ii][2]

print(T,P,N)

f.close()
