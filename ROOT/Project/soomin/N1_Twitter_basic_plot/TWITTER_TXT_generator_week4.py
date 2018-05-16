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

#    list_Filename=["newyork/beer_newyork/beer_0409Mon_NY.txt","newyork/beer_newyork/beer_0410Tue_NY.txt","newyork/beer_newyork/beer_0411Wed_NY.txt","newyork/beer_newyork/beer_0412Thu_NY.txt","newyork/beer_newyork/beer_0413Fri_NY.txt","newyork/beer_newyork/beer_0414Sat_NY.txt","newyork/beer_newyork/beer_0415Sun_NY.txt",
#"newyork/coffee_newyork/coffee_0409Mon_NY.txt","newyork/coffee_newyork/coffee_0410Tue_NY.txt","newyork/coffee_newyork/coffee_0411Wed_NY.txt","newyork/coffee_newyork/coffee_0412Thu_NY.txt","newyork/coffee_newyork/coffee_0413Fri_NY.txt","newyork/coffee_newyork/coffee_0414Sat_NY.txt","newyork/coffee_newyork/coffee_0415Sun_NY.txt",
#"newyork/tea_newyork/tea_0409Mon_NY.txt","newyork/tea_newyork/tea_0410Tue_NY.txt","newyork/tea_newyork/tea_0411Wed_NY.txt","newyork/tea_newyork/tea_0412Thu_NY.txt","newyork/tea_newyork/tea_0413Fri_NY.txt","newyork/tea_newyork/tea_0414Sat_NY.txt","newyork/tea_newyork/tea_0415Sun_NY.txt",
#"newyork/juice_newyork/juice_0409Mon_NY.txt","newyork/juice_newyork/juice_0410Tue_NY.txt","newyork/juice_newyork/juice_0411Wed_NY.txt","newyork/juice_newyork/juice_0412Thu_NY.txt","newyork/juice_newyork/juice_0413Fri_NY.txt","newyork/juice_newyork/juice_0414Sat_NY.txt","newyork/juice_newyork/juice_0415Sun_NY.txt",
#"newyork/coke_n_cola_newyork/COLA_COKE_0409Mon_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0410Tue_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0411Wed_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0412Thu_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0413Fri_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0414Sat_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0415Sun_NY.txt",
#"newyork/water_newyork/water_0409Mon_NY.txt","newyork/water_newyork/water_0410Tue_NY.txt","newyork/water_newyork/water_0411Wed_NY.txt","newyork/water_newyork/water_0412Thu_NY.txt","newyork/water_newyork/water_0413Fri_NY.txt","newyork/water_newyork/water_0414Sat_NY.txt","newyork/water_newyork/water_0415Sun_NY.txt",
#"newyork/wine_newyork/wine_0409Mon_NY.txt","newyork/wine_newyork/wine_0410Tue_NY.txt","newyork/wine_newyork/wine_0411Wed_NY.txt","newyork/wine_newyork/wine_0412Thu_NY.txt","newyork/wine_newyork/wine_0413Fri_NY.txt","newyork/wine_newyork/wine_0414Sat_NY.txt","newyork/wine_newyork/wine_0415Sun_NY.txt"]

    list_Filename = ["LA/beer_LA/beer_0409Mon_LA.txt","LA/beer_LA/beer_0410Tue_LA.txt","LA/beer_LA/beer_0411Wed_LA.txt","LA/beer_LA/beer_0412Thu_LA.txt","LA/beer_LA/beer_0413Fri_LA.txt","LA/beer_LA/beer_0414Sat_LA.txt","LA/beer_LA/beer_0415Sun_LA.txt",
"LA/coffee_LA/coffee_0409Mon_LA.txt","LA/coffee_LA/coffee_0410Tue_LA.txt","LA/coffee_LA/coffee_0411Wed_LA.txt","LA/coffee_LA/coffee_0412Thu_LA.txt","LA/coffee_LA/coffee_0413Fri_LA.txt","LA/coffee_LA/coffee_0414Sat_LA.txt","LA/coffee_LA/coffee_0415Sun_LA.txt",
"LA/coke_n_cola_LA/COLA_COKE_0409Mon_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0410Tue_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0411Wed_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0412Thu_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0413Fri_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0414Sat_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0415Sun_LA.txt",
"LA/juice_LA/juice_0409Mon_LA.txt","LA/juice_LA/juice_0410Tue_LA.txt","LA/juice_LA/juice_0411Wed_LA.txt","LA/juice_LA/juice_0412Thu_LA.txt","LA/juice_LA/juice_0413Fri_LA.txt","LA/juice_LA/juice_0414Sat_LA.txt","LA/juice_LA/juice_0415Sun_LA.txt",
"LA/tea_LA/tea_0409Mon_LA.txt","LA/tea_LA/tea_0410Tue_LA.txt","LA/tea_LA/tea_0411Wed_LA.txt","LA/tea_LA/tea_0412Thu_LA.txt","LA/tea_LA/tea_0413Fri_LA.txt","LA/tea_LA/tea_0414Sat_LA.txt","LA/tea_LA/tea_0415Sun_LA.txt",
"LA/water_LA/water_0409Mon_LA.txt","LA/water_LA/water_0410Tue_LA.txt","LA/water_LA/water_0411Wed_LA.txt","LA/water_LA/water_0412Thu_LA.txt","LA/water_LA/water_0413Fri_LA.txt","LA/water_LA/water_0414Sat_LA.txt","LA/water_LA/water_0415Sun_LA.txt",
"LA/wine_LA/wine_0409Mon_LA.txt","LA/wine_LA/wine_0410Tue_LA.txt","LA/wine_LA/wine_0411Wed_LA.txt","LA/wine_LA/wine_0412Thu_LA.txt","LA/wine_LA/wine_0413Fri_LA.txt","LA/wine_LA/wine_0414Sat_LA.txt","LA/wine_LA/wine_0415Sun_LA.txt"]


#   list_Filename=["newyork/beer_newyork/beer_0402Mon_NY.txt","newyork/beer_newyork/beer_0403Tue_NY.txt","newyork/beer_newyork/beer_0404Wed_NY.txt","newyork/beer_newyork/beer_0405Thu_NY.txt","newyork/beer_newyork/beer_0406Fri_NY.txt","newyork/beer_newyork/beer_0407Sat_NY.txt","newyork/beer_newyork/beer_0408Sun_NY.txt",
#"newyork/coffee_newyork/coffee_0402Mon_NY.txt","newyork/coffee_newyork/coffee_0403Tue_NY.txt","newyork/coffee_newyork/coffee_0404Wed_NY.txt","newyork/coffee_newyork/coffee_0405Thu_NY.txt","newyork/coffee_newyork/coffee_0406Fri_NY.txt","newyork/coffee_newyork/coffee_0407Sat_NY.txt","newyork/coffee_newyork/coffee_0408Sun_NY.txt",
#"newyork/tea_newyork/tea_0402Mon_NY.txt","newyork/tea_newyork/tea_0403Thu_NY.txt","newyork/tea_newyork/tea_0404Wed_NY.txt","newyork/tea_newyork/tea_0405Thu_NY.txt","newyork/tea_newyork/tea_0406Fri_NY.txt","newyork/tea_newyork/tea_0407Sat_NY.txt","newyork/tea_newyork/tea_0408Sun_NY.txt",
#"newyork/juice_newyork/juice_0402Mon_NY.txt","newyork/juice_newyork/juice_0403Tue_NY.txt","newyork/juice_newyork/juice_0404Wed_NY.txt","newyork/juice_newyork/juice_0405Thu_NY.txt","newyork/juice_newyork/juice_0406Fri_NY.txt","newyork/juice_newyork/juice_0407Sat_NY.txt","newyork/juice_newyork/juice_0408Sun_NY.txt",
#"newyork/coke_n_cola_newyork/ COLA_COKE_0402Mon_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0403Tue_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0404Wed_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0405Thu_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0406Fri_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0407Sat_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0408Sun_NY.txt",
#"newyork/water_newyork/water_0402Mon_NY.txt","newyork/water_newyork/water_0403Tue_NY.txt","newyork/water_newyork/water_0404Wed_NY.txt","newyork/water_newyork/water_0405Thu_NY.txt","newyork/water_newyork/water_0406Fri_NY.txt","newyork/water_newyork/water_0407Sat_NY.txt","newyork/water_newyork/water_0408Sun_NY.txt",
#"newyork/wine_newyork/wine_0402Mon_newyork.txt","newyork/wine_newyork/wine_0403Tue_newyork.txt","newyork/wine_newyork/wine_0404Wed_NY.txt","newyork/wine_newyork/wine_0405Thu_NY.txt","newyork/wine_newyork/wine_0406Fri_NY.txt","newyork/wine_newyork/wine_0407Sat_NY.txt","newyork/wine_newyork/wine_0408Sun_NY.txt"]


#    list_Filename = ["LA/beer_LA/beer_0402Mon_LA.txt","LA/beer_LA/beer_0403Tue_LA.txt","LA/beer_LA/beer_0404Wed_LA.txt","LA/beer_LA/beer_0405Thu_LA.txt","LA/beer_LA/beer_0406Fri_LA.txt","LA/beer_LA/beer_0407Sat_LA.txt","LA/beer_LA/beer_0408Sun_LA.txt",
#"LA/coffee_LA/coffee_0402Mon_LA.txt","LA/coffee_LA/coffee_0403Tue_LA.txt","LA/coffee_LA/coffee_0404Wed_LA.txt","LA/coffee_LA/coffee_0405Thu_LA.txt","LA/coffee_LA/coffee_0406Fri_LA.txt","LA/coffee_LA/coffee_0407Sat_LA.txt","LA/coffee_LA/coffee_0408Sun_LA.txt",
#"LA/coke_n_cola_LA/COLA_COKE_0402Mon_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0403Tue_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0404Wed_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0405Thu_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0406Fri_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0407Sat_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0408Sun_LA.txt",
#"LA/juice_LA/juice_0402Mon_LA.txt","LA/juice_LA/juice_0403Tue_LA.txt","LA/juice_LA/juice_0404Wed_LA.txt","LA/juice_LA/juice_0405Thu_LA.txt","LA/juice_LA/juice_0406Fri_LA.txt","LA/juice_LA/juice_0407Sat_LA.txt","LA/juice_LA/juice_0408Sun_LA.txt",
#"LA/tea_LA/tea_0402Mon_LA.txt","LA/tea_LA/tea_0403Tue_LA.txt","LA/tea_LA/tea_0404Wed_LA.txt","LA/tea_LA/tea_0405Thu_LA.txt","LA/tea_LA/tea_0406Fri_LA.txt","LA/tea_LA/tea_0407Sat_LA.txt","LA/tea_LA/tea_0408Sun_LA.txt",
#"LA/water_LA/water_0402Mon_LA.txt","LA/water_LA/water_0403Tue_LA.txt","LA/water_LA/water_0404Wed_LA.txt","LA/water_LA/water_0405Thu_LA.txt","LA/water_LA/water_0406Fri_LA.txt","LA/water_LA/water_0407Sat_LA.txt","LA/water_LA/water_0408Sun_LA.txt",
#"LA/wine_LA/wine_0402Mon_LA.txt","LA/wine_LA/wine_0403Tue_LA.txt","LA/wine_LA/wine_0404Wed_LA.txt","LA/wine_LA/wine_0405Thu_LA.txt","LA/wine_LA/wine_0406Fri_LA.txt","LA/wine_LA/wine_0407Sat_LA.txt","LA/wine_LA/wine_0408Sun_LA.txt"]

#    list_Filename = ["LA/beer_LA/beer_0326Mon_LA.txt","LA/beer_LA/beer_0327Tue_LA.txt","LA/beer_LA/beer_0328Wed_LA.txt","LA/beer_LA/beer_0329Thu_LA.txt","LA/beer_LA/beer_0330Fri_LA.txt","LA/beer_LA/beer_0331Sat_LA.txt","LA/beer_LA/beer_0401Sun_LA.txt",
#"LA/coffee_LA/coffee_0326Mon_LA.txt","LA/coffee_LA/coffee_0327Tue_LA.txt","LA/coffee_LA/coffee_0328Wed_LA.txt","LA/coffee_LA/coffee_0329Thu_LA.txt","LA/coffee_LA/coffee_0330Fri_LA.txt","LA/coffee_LA/coffee_0331Sat_LA.txt","LA/coffee_LA/coffee_0401Sun_LA.txt",
#"LA/coke_n_cola_LA/COLA_COKE_0327Mon_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0328Tue_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0328Wed_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0329Thu_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0330Fri_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0331Sat_LA.txt","LA/coke_n_cola_LA/COLA_COKE_0401Sun_LA.txt",
#"LA/juice_LA/juice_0326Mon_LA.txt","LA/juice_LA/juice_0327Tue_LA.txt","LA/juice_LA/juice_0328Wed_LA.txt","LA/juice_LA/juice_0329Thu_LA.txt","LA/juice_LA/juice_0330Fri_LA.txt","LA/juice_LA/juice_0331Sat_LA.txt","LA/juice_LA/juice_0401Sun_LA.txt",
#"LA/tea_LA/tea_0326Mon_LA.txt","LA/tea_LA/tea_0327Tue_LA.txt","LA/tea_LA/tea_0328Wed_LA.txt","LA/tea_LA/tea_0329Thu_LA.txt","LA/tea_LA/tea_0330Fri_LA.txt","LA/tea_LA/tea_0331Sat_LA.txt","LA/tea_LA/tea_0401Sun_LA.txt",
#"LA/water_LA/water_0326Mon_LA.txt","LA/water_LA/water_0327Tue_LA.txt","LA/water_LA/water_0328Wed_LA.txt","LA/water_LA/water_0329Thu_LA.txt","LA/water_LA/water_0330Fri_LA.txt","LA/water_LA/water_0331Sat_LA.txt","LA/water_LA/water_0401Sun_LA.txt",
#"LA/wine_LA/wine_0326Mon_LA.txt","LA/wine_LA/wine_0327Tue_LA.txt","LA/wine_LA/wine_0328Wed_LA.txt","LA/wine_LA/wine_0329Thu_LA.txt","LA/wine_LA/wine_0330Fri_LA.txt","LA/wine_LA/wine_0331Sat_LA.txt","LA/wine_LA/wine_0401Sun_LA.txt"
#]



#   list_Filename=["newyork/beer_newyork/beer_0326Mon_newyork.txt","newyork/beer_newyork/beer_0327Tue_newyork.txt","newyork/beer_newyork/beer_0328Wed_NY.txt","newyork/beer_newyork/beer_0329Thu_NY.txt","newyork/beer_newyork/beer_0330Fri_NY.txt","newyork/beer_newyork/beer_0331Sat_NY.txt","newyork/beer_newyork/beer_0401Sun_NY.txt",
#"newyork/coffee_newyork/coffee_0326Mon_newyork.txt","newyork/coffee_newyork/coffee_0327Tue_newyork.txt","newyork/coffee_newyork/coffee_0328Wed_NY.txt","newyork/coffee_newyork/coffee_0329Thu_NY.txt","newyork/coffee_newyork/coffee_0330Fri_NY.txt","newyork/coffee_newyork/coffee_0331Sat_NY.txt","newyork/coffee_newyork/coffee_0401Sun_NY.txt",
#"newyork/tea_newyork/tea_0326Mon_newyork.txt","newyork/tea_newyork/tea_0327Thu_newyork.txt","newyork/tea_newyork/tea_0328Wed_NY.txt","newyork/tea_newyork/tea_0329Thu_NY.txt","newyork/tea_newyork/tea_0330Fri_NY.txt","newyork/tea_newyork/tea_0331Sat_NY.txt","newyork/tea_newyork/tea_0401Sun_NY.txt",
#"newyork/juice_newyork/juice_0326Mon_newyork.txt","newyork/juice_newyork/juice_0327Tue_newyork.txt","newyork/juice_newyork/juice_0328Wed_NY.txt","newyork/juice_newyork/juice_0329Thu_NY.txt","newyork/juice_newyork/juice_0330Fri_NY.txt","newyork/juice_newyork/juice_0331Sat_NY.txt","newyork/juice_newyork/juice_0401Sun_NY.txt",
#"newyork/coke_n_cola_newyork/ COLA_COKE_0326Mon_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0327Tue_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0328Wed_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0329Thu_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0330Fri_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0331Sat_NY.txt","newyork/coke_n_cola_newyork/COLA_COKE_0401Sun_NY.txt",
#"newyork/water_newyork/water_0326Mon_newyork.txt","newyork/water_newyork/water_0327Tue_newyork.txt","newyork/water_newyork/water_0328Wed_NY.txt","newyork/water_newyork/water_0329Thu_NY.txt","newyork/water_newyork/water_0330Fri_NY.txt","newyork/water_newyork/water_0331Sat_NY.txt","newyork/water_newyork/water_0401Sun_NY.txt",
#"newyork/wine_newyork/wine_0326Mon_newyork.txt","newyork/wine_newyork/wine_0327Tue_newyork.txt","newyork/wine_newyork/wine_0328Wed_NY.txt","newyork/wine_newyork/wine_0329Thu_NY.txt","newyork/wine_newyork/wine_0330Fri_NY.txt","newyork/wine_newyork/wine_0331Sat_NY.txt","newyork/wine_newyork/wine_0401Sun_NY.txt"
#]



#    list_Filename = ["LA/beer_LA/beer_0319Mon_LA.txt","LA/beer_LA/beer_0320Tue_LA.txt","LA/beer_LA/beer_0321Wed_LA.txt","LA/beer_LA/beer_0322Thu_LA.txt","LA/beer_LA/beer_0323Fri_LA.txt","LA/beer_LA/beer_0324Sat_LA.txt","LA/beer_LA/beer_0325Sun_LA.txt","LA/beer_LA/beer_0326Mon_LA.txt","LA/beer_LA/beer_0327Tue_LA.txt",  
#"LA/coffee_LA/coffee_0319Mon_LA.txt" ,"LA/coffee_LA/coffee_0320Tue_LA.txt" ,"LA/coffee_LA/coffee_0321Wed_LA.txt" ,"LA/coffee_LA/coffee_0322Thu_LA.txt" ,"LA/coffee_LA/coffee_0323Fri_LA.txt" ,"LA/coffee_LA/coffee_0324Sat_LA.txt" ,"LA/coffee_LA/coffee_0325Sun_LA.txt" ,"LA/coffee_LA/coffee_0326Mon_LA.txt" ,"LA/coffee_LA/coffee_0327Tue_LA.txt" ,
#"LA/coke_n_cola_LA/COLA_COKE_0319Mon_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0320Tue_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0321Wed_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0322Thu_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0323Fri_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0324Sat_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0325Sun_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0326Mon_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0327Tue_LA.txt" , 
#"LA/juice_LA/juice_0319Mon_LA.txt", "LA/juice_LA/juice_0320Tue_LA.txt" ,"LA/juice_LA/juice_0321Wed_LA.txt" ,"LA/juice_LA/juice_0322Thu_LA.txt" ,"LA/juice_LA/juice_0323Fri_LA.txt" ,"LA/juice_LA/juice_0324Sat_LA.txt" ,"LA/juice_LA/juice_0325Sun_LA.txt" ,"LA/juice_LA/juice_0326Mon_LA.txt" ,"LA/juice_LA/juice_0327Tue_LA.txt", 
#"LA/tea_LA/tea_0319Mon_LA.txt", "LA/tea_LA/tea_0320Tue_LA.txt", "LA/tea_LA/tea_0321Wed_LA.txt", "LA/tea_LA/tea_0322Thu_LA.txt", "LA/tea_LA/tea_0323Fri_LA.txt", "LA/tea_LA/tea_0324Sat_LA.txt", "LA/tea_LA/tea_0325Sun_LA.txt", "LA/tea_LA/tea_0326Mon_LA.txt", "LA/tea_LA/tea_0327Tue_LA.txt", 
#"LA/water_LA/water_0319Mon_LA.txt", "LA/water_LA/water_0320Tue_LA.txt", "LA/water_LA/water_0321Wed_LA.txt", "LA/water_LA/water_0322Thu_LA.txt", "LA/water_LA/water_0323Fri_LA.txt", "LA/water_LA/water_0324Sat_LA.txt", "LA/water_LA/water_0325Sun_LA.txt", "LA/water_LA/water_0326Mon_LA.txt", "LA/water_LA/water_0327Tue_LA.txt", 
#"LA/wine_LA/wine_0319Mon_LA.txt", "LA/wine_LA/wine_0320Tue_LA.txt", "LA/wine_LA/wine_0321Wed_LA.txt","LA/wine_LA/wine_0322Thu_LA.txt","LA/wine_LA/wine_0323Fri_LA.txt","LA/wine_LA/wine_0324Sat_LA.txt","LA/wine_LA/wine_0325Sun_LA.txt","LA/wine_LA/wine_0326Mon_LA.txt","LA/wine_LA/wine_0327Tue_LA.txt"]



#    list_Filename = ["newyork/beer_newyork/beer_0319Mon_newyork.txt", "newyork/beer_newyork/beer_0320Tue_newyork.txt", "newyork/beer_newyork/beer_0321Wed_newyork.txt", "newyork/beer_newyork/beer_0322Thu_newyork.txt", "newyork/beer_newyork/beer_0323Fri_newyork.txt", "newyork/beer_newyork/beer_0324Sat_newyork.txt", "newyork/beer_newyork/beer_0325Sun_newyork.txt", "newyork/beer_newyork/beer_0326Mon_newyork.txt", "newyork/beer_newyork/beer_0327Tue_newyork.txt",
#"newyork/coffee_newyork/coffee_0319Mon_newyork.txt", "newyork/coffee_newyork/coffee_0320Thu_newyork.txt", "newyork/coffee_newyork/coffee_0321Wed_newyork.txt", "newyork/coffee_newyork/coffee_0322Thu_newyork.txt", "newyork/coffee_newyork/coffee_0323Fri_newyork.txt", "newyork/coffee_newyork/coffee_0324Sat_newyork.txt", "newyork/coffee_newyork/coffee_0325Sun_newyork.txt", "newyork/coffee_newyork/coffee_0326Mon_newyork.txt", "newyork/coffee_newyork/coffee_0327Tue_newyork.txt",
# "newyork/coke_n_cola_newyork/COLA_COKE_0319Mon_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0320Tue_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0321Wed_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0322Thu_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0323Fri_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0324Sat_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0325Sun_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0326Mon_newyork.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0327Tue_newyork.txt",
# "newyork/juice_newyork/juice_0319Mon_newyork.txt", "newyork/juice_newyork/juice_0320Tue_newyork.txt", "newyork/juice_newyork/juice_0321Wed_newyork.txt", "newyork/juice_newyork/juice_0322Thu_newyork.txt", "newyork/juice_newyork/juice_0323Fri_newyork.txt", "newyork/juice_newyork/juice_0324Sat_newyork.txt", "newyork/juice_newyork/juice_0325Sun_newyork.txt", "newyork/juice_newyork/juice_0326Mon_newyork.txt", "newyork/juice_newyork/juice_0327Tue_newyork.txt",
# "newyork/tea_newyork/tea_0319Mon_newyork.txt", "newyork/tea_newyork/tea_0320Tue_newyork.txt", "newyork/tea_newyork/tea_0321Wed_newyork.txt", "newyork/tea_newyork/tea_0322Thu_newyork.txt", "newyork/tea_newyork/tea_0323Fri_newyork.txt", "newyork/tea_newyork/tea_0324Sat_newyork.txt", "newyork/tea_newyork/tea_0325Sun_newyork.txt", "newyork/tea_newyork/tea_0326Mon_newyork.txt", "newyork/tea_newyork/tea_0327Thu_newyork.txt",
# "newyork/water_newyork/water_0319TMon_newyork.txt", "newyork/water_newyork/water_0320Tue_newyork.txt", "newyork/water_newyork/water_0321Wed_newyork.txt", "newyork/water_newyork/water_0322Thu_newyork.txt", "newyork/water_newyork/water_0323Fri_newyork.txt", "newyork/water_newyork/water_0324Sat_newyork.txt", "newyork/water_newyork/water_0325Sun_newyork.txt", "newyork/water_newyork/water_0326Mon_newyork.txt", "newyork/water_newyork/water_0327Tue_newyork.txt",
#"newyork/wine_newyork/wine_0319Mon_newyork.txt", "newyork/wine_newyork/wine_0320Tue_newyork.txt","newyork/wine_newyork/wine_0321Wed_newyork.txt","newyork/wine_newyork/wine_0322Thu_newyork.txt","newyork/wine_newyork/wine_0323Fri_newyork.txt","newyork/wine_newyork/wine_0324Sat_newyork.txt","newyork/wine_newyork/wine_0325Sun_newyork.txt","newyork/wine_newyork/wine_0326Mon_newyork.txt","newyork/wine_newyork/wine_0327Tue_newyork.txt"]


    wf = open("LA_OUTPUT.txt","w+")
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











