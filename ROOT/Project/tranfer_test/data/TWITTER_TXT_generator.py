import os


def read_file_name(filename):             # returning [filename, filename.root, absolute path filename, absolute path filename without root file]
    f = open(filename,"r")

    if(filename[0] == '/'):                 # 'filename' of absoulte location 
        filename = filename
    elif(filename[0] == '~'):
        filename = filename.replace("~",os.environ['HOME'])
    else:
        filename = os.getcwd() + "/" + filename

    loca = len(filename)
    for i in range(1,len(filename)+1):       # find the "/" location
        if(filename[-i] == '/'):
            loca = i-1
            break
    FILENAME = filename.replace(filename[:-loca],"")
    FILE = FILENAME.replace(".txt","")
    filename_NoRoot = filename.replace(filename[len(filename)-loca:len(filename)],"")

    filelist = [FILE, FILENAME, filename, filename_NoRoot]
#    print(filelist)
    return(filelist)


def readLines(filename):
    f = open(filename,'r')
    T,P,N =0,0,0
    List = []
    it = 0
    for line in f:    ####### can not transfer value???!?!?!?!?
        try:
#        if(it==0):
#            it = 1
#            continue
            lis = []
            TOTAL, pos, neg = line.split()
            lis.append(int(TOTAL))
            lis.append(int(pos))
            lis.append(int(neg))
            List.append(lis)
        except:
            ValueError
            pass
#            print("a time value error")
#            print(filename)
    for ii in range(len(List)):
        T = T + List[ii][0]
        P = P + List[ii][1]
        N = N + List[ii][2]
    LL = list()
    LL = [T,P,N,len(List)]
    f.close()
    return LL

  
#print(T,P,N)











def main():
    list_Filename =list()
#    list_Filename = ["LA/beer_LA/beer_0319Mon_LA.txt","LA/beer_LA/beer_0320Tue_LA.txt","LA/beer_LA/beer_0321Wed_LA.txt","LA/beer_LA/beer_0322Thu_LA.txt","LA/beer_LA/beer_0323Fri_LA.txt","LA/beer_LA/beer_0324Sat_LA.txt","LA/beer_LA/beer_0325Sun_LA.txt","LA/beer_LA/beer_0326Mon_LA.txt","LA/beer_LA/beer_0327Tue_LA.txt",  
#"LA/coffee_LA/coffee_0319Mon_LA.txt" ,"LA/coffee_LA/coffee_0320Tue_LA.txt" ,"LA/coffee_LA/coffee_0321Wed_LA.txt" ,"LA/coffee_LA/coffee_0322Thu_LA.txt" ,"LA/coffee_LA/coffee_0323Fri_LA.txt" ,"LA/coffee_LA/coffee_0324Sat_LA.txt" ,"LA/coffee_LA/coffee_0325Sun_LA.txt" ,"LA/coffee_LA/coffee_0326Mon_LA.txt" ,"LA/coffee_LA/coffee_0327Tue_LA.txt" ,
#"LA/coke_n_cola_LA/COLA_COKE_0319Mon_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0320Tue_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0321Wed_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0322Thu_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0323Fri_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0324Sat_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0325Sun_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0326Mon_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0327Tue_LA.txt" , 
#"LA/juice_LA/juice_0319Mon_LA.txt", "LA/juice_LA/juice_0320Tue_LA.txt" ,"LA/juice_LA/juice_0321Wed_LA.txt" ,"LA/juice_LA/juice_0322Thu_LA.txt" ,"LA/juice_LA/juice_0323Fri_LA.txt" ,"LA/juice_LA/juice_0324Sat_LA.txt" ,"LA/juice_LA/juice_0325Sun_LA.txt" ,"LA/juice_LA/juice_0326Mon_LA.txt" ,"LA/juice_LA/juice_0327Tue_LA.txt", 
#"LA/tea_LA/tea_0319Mon_LA.txt", "LA/tea_LA/tea_0320Tue_LA.txt", "LA/tea_LA/tea_0321Wed_LA.txt", "LA/tea_LA/tea_0322Thu_LA.txt", "LA/tea_LA/tea_0323Fri_LA.txt", "LA/tea_LA/tea_0324Sat_LA.txt", "LA/tea_LA/tea_0325Sun_LA.txt", "LA/tea_LA/tea_0326Mon_LA.txt", "LA/tea_LA/tea_0327Tue_LA.txt", 
#"LA/water_LA/water_0319Mon_LA.txt", "LA/water_LA/water_0320Tue_LA.txt", "LA/water_LA/water_0321Wed_LA.txt", "LA/water_LA/water_0322Thu_LA.txt", "LA/water_LA/water_0323Fri_LA.txt", "LA/water_LA/water_0324Sat_LA.txt", "LA/water_LA/water_0325Sun_LA.txt", "LA/water_LA/water_0326Mon_LA.txt", "LA/water_LA/water_0327Tue_LA.txt", 
#"LA/wine_LA/wine_0319Mon_LA.txt", "LA/wine_LA/wine_0320Tue_LA.txt", "LA/wine_LA/wine_0321Wed_LA.txt","LA/wine_LA/wine_0322Thu_LA.txt","LA/wine_LA/wine_0323Fri_LA.txt","LA/wine_LA/wine_0324Sat_LA.txt","LA/wine_LA/wine_0325Sun_LA.txt","LA/wine_LA/wine_0326Mon_LA.txt","LA/wine_LA/wine_0327Tue_LA.txt"]



    list_Filename = ["newyork/beer_newyork/beer_0319Mon_newyork.txt", "newyork/beer_newyork/beer_0320Tue_newyork.txt", "newyork/beer_newyork/beer_0321Wed_newyork.txt", "newyork/beer_newyork/beer_0322Thu_newyork.txt", "newyork/beer_newyork/beer_0323Fri_newyork.txt", "newyork/beer_newyork/beer_0324Sat_newyork.txt", "newyork/beer_newyork/beer_0325Sun_newyork.txt", "newyork/beer_newyork/beer_0326Mon_newyork.txt", "newyork/beer_newyork/beer_0327Tue_newyork.txt",
"newyork/coffee_newyork/coffee_0319Mon_newyork.txt", "newyork/coffee_newyork/coffee_0320Thu_newyork.txt", "newyork/coffee_newyork/coffee_0321Wed_newyork.txt", "newyork/coffee_newyork/coffee_0322Thu_newyork.txt", "newyork/coffee_newyork/coffee_0323Fri_newyork.txt", "newyork/coffee_newyork/coffee_0324Sat_newyork.txt", "newyork/coffee_newyork/coffee_0325Sun_newyork.txt", "newyork/coffee_newyork/coffee_0326Mon_newyork.txt", "newyork/coffee_newyork/coffee_0327Tue_newyork.txt",
 "newyork/coke_n_cola_newyork/COLA_COKE_0319Mon_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0320Tue_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0321Wed_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0322Thu_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0323Fri_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0324Sat_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0325Sun_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0326Mon_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0327Tue_newyork.txt",
 "newyork/juice_newyork/juice_0319Mon_newyork.txt", "newyork/juice_newyork/juice_0320Tue_newyork.txt", "newyork/juice_newyork/juice_0321Wed_newyork.txt", "newyork/juice_newyork/juice_0322Thu_newyork.txt", "newyork/juice_newyork/juice_0323Fri_newyork.txt", "newyork/juice_newyork/juice_0324Sat_newyork.txt", "newyork/juice_newyork/juice_0325Sun_newyork.txt", "newyork/juice_newyork/juice_0326Mon_newyork.txt", "newyork/juice_newyork/juice_0327Tue_newyork.txt",
 "newyork/tea_newyork/tea_0319Mon_newyork.txt", "newyork/tea_newyork/tea_0320Tue_newyork.txt", "newyork/tea_newyork/tea_0321Wed_newyork.txt", "newyork/tea_newyork/tea_0322Thu_newyork.txt", "newyork/tea_newyork/tea_0323Fri_newyork.txt", "newyork/tea_newyork/tea_0324Sat_newyork.txt", "newyork/tea_newyork/tea_0325Sun_newyork.txt", "newyork/tea_newyork/tea_0326Mon_newyork.txt", "newyork/tea_newyork/tea_0327Thu_newyork.txt",
 "newyork/water_newyork/water_0319TMon_newyork.txt", "newyork/water_newyork/water_0320Tue_newyork.txt", "newyork/water_newyork/water_0321Wed_newyork.txt", "newyork/water_newyork/water_0322Thu_newyork.txt", "newyork/water_newyork/water_0323Fri_newyork.txt", "newyork/water_newyork/water_0324Sat_newyork.txt", "newyork/water_newyork/water_0325Sun_newyork.txt", "newyork/water_newyork/water_0326Mon_newyork.txt", "newyork/water_newyork/water_0327Tue_newyork.txt",
"newyork/wine_newyork/wine_0319Mon_newyork.txt", "newyork/wine_newyork/wine_0320Tue_newyork.txt","newyork/wine_newyork/wine_0321Wed_newyork.txt","newyork/wine_newyork/wine_0322Thu_newyork.txt","newyork/wine_newyork/wine_0323Fri_newyork.txt","newyork/wine_newyork/wine_0324Sat_newyork.txt","newyork/wine_newyork/wine_0325Sun_newyork.txt","newyork/wine_newyork/wine_0326Mon_newyork.txt","newyork/wine_newyork/wine_0327Tue_newyork.txt"]

    wf = open("NY_OUTPUT.txt","w+")
    SName = []
    indicator = 0
    for fina in range(len(list_Filename)):
        indicator = indicator + 1
        fff = read_file_name(list_Filename[fina])
        TPN = readLines(fff[2])
        if indicator == 1:
            wf.write("Title total_words total_positive_words total_negative_words Tweets_num\n")
        wf.write("%s %i %i %i %i\n"  %(fff[0], TPN[0], TPN[1], TPN[2], TPN[3]))
                
#        print(fff[2])
        SName.append(fff[0])
#    print(SName)
    wf.close()


if __name__ == "__main__":
    main()











