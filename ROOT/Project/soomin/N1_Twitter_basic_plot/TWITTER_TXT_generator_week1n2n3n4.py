###This code is for calulating total words, total positive words, total negative words, tweet number :: txt file
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

#    list_Filename = ["LA/beer_LA/beer_w1w2w3w4_1Mon_LA.txt","LA/beer_LA/beer_w1w2w3w4_2Tue_LA.txt","LA/beer_LA/beer_w1w2w3w4_3Wed_LA.txt","LA/beer_LA/beer_w1w2w3w4_4Thu_LA.txt","LA/beer_LA/beer_w1w2w3w4_5Fri_LA.txt","LA/beer_LA/beer_w1w2w3w4_6Sat_LA.txt","LA/beer_LA/beer_w1w2w3w4_7Sun_LA.txt",#"LA/beer_LA/beer_0326Mon_LA.txt","LA/beer_LA/beer_0327Tue_LA.txt",  
#"LA/coffee_LA/coffee_w1w2w3w4_1Mon_LA.txt" ,"LA/coffee_LA/coffee_w1w2w3w4_2Tue_LA.txt" ,"LA/coffee_LA/coffee_w1w2w3w4_3Wed_LA.txt" ,"LA/coffee_LA/coffee_w1w2w3w4_4Thu_LA.txt" ,"LA/coffee_LA/coffee_w1w2w3w4_5Fri_LA.txt" ,"LA/coffee_LA/coffee_w1w2w3w4_6Sat_LA.txt" ,"LA/coffee_LA/coffee_w1w2w3w4_7Sun_LA.txt" ,#"LA/coffee_LA/coffee_0326Mon_LA.txt" ,"LA/coffee_LA/coffee_0327Tue_LA.txt" ,
#"LA/coke_n_cola_LA/COLA_COKE_w1w2w3w4_1Mon_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_w1w2w3w4_2Tue_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_w1w2w3w4_3Wed_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_w1w2w3w4_4Thu_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_w1w2w3w4_5Fri_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_w1w2w3w4_6Sat_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_w1w2w3w4_7Sun_LA.txt" ,#"LA/coke_n_cola_LA/COLA_COKE_0326Mon_LA.txt" ,"LA/coke_n_cola_LA/COLA_COKE_0327Tue_LA.txt" , 
#"LA/juice_LA/juice_w1w2w3w4_1Mon_LA.txt", "LA/juice_LA/juice_w1w2w3w4_2Tue_LA.txt" ,"LA/juice_LA/juice_w1w2w3w4_3Wed_LA.txt" ,"LA/juice_LA/juice_w1w2w3w4_4Thu_LA.txt" ,"LA/juice_LA/juice_w1w2w3w4_5Fri_LA.txt" ,"LA/juice_LA/juice_w1w2w3w4_6Sat_LA.txt" ,"LA/juice_LA/juice_w1w2w3w4_7Sun_LA.txt" ,#"LA/juice_LA/juice_0326Mon_LA.txt" ,"LA/juice_LA/juice_0327Tue_LA.txt", 
#"LA/tea_LA/tea_w1w2w3w4_1Mon_LA.txt", "LA/tea_LA/tea_w1w2w3w4_2Tue_LA.txt", "LA/tea_LA/tea_w1w2w3w4_3Wed_LA.txt", "LA/tea_LA/tea_w1w2w3w4_4Thu_LA.txt", "LA/tea_LA/tea_w1w2w3w4_5Fri_LA.txt", "LA/tea_LA/tea_w1w2w3w4_6Sat_LA.txt", "LA/tea_LA/tea_w1w2w3w4_7Sun_LA.txt", #"LA/tea_LA/tea_0326Mon_LA.txt", "LA/tea_LA/tea_0327Tue_LA.txt", 
#"LA/water_LA/water_w1w2w3w4_1Mon_LA.txt", "LA/water_LA/water_w1w2w3w4_2Tue_LA.txt", "LA/water_LA/water_w1w2w3w4_3Wed_LA.txt", "LA/water_LA/water_w1w2w3w4_4Thu_LA.txt", "LA/water_LA/water_w1w2w3w4_5Fri_LA.txt", "LA/water_LA/water_w1w2w3w4_6Sat_LA.txt", "LA/water_LA/water_w1w2w3w4_7Sun_LA.txt", #"LA/water_LA/water_0326Mon_LA.txt", "LA/water_LA/water_0327Tue_LA.txt", 
#"LA/wine_LA/wine_w1w2w3w4_1Mon_LA.txt", "LA/wine_LA/wine_w1w2w3w4_2Tue_LA.txt", "LA/wine_LA/wine_w1w2w3w4_3Wed_LA.txt","LA/wine_LA/wine_w1w2w3w4_4Thu_LA.txt","LA/wine_LA/wine_w1w2w3w4_5Fri_LA.txt","LA/wine_LA/wine_w1w2w3w4_6Sat_LA.txt","LA/wine_LA/wine_w1w2w3w4_7Sun_LA.txt"]#,"LA/wine_LA/wine_0326Mon_LA.txt","LA/wine_LA/wine_0327Tue_LA.txt"]



    list_Filename = ["newyork/beer_newyork/beer_w1w2w3w4_1Mon_NY.txt", "newyork/beer_newyork/beer_w1w2w3w4_2Tue_NY.txt", "newyork/beer_newyork/beer_w1w2w3w4_3Wed_NY.txt", "newyork/beer_newyork/beer_w1w2w3w4_4Thu_NY.txt", "newyork/beer_newyork/beer_w1w2w3w4_5Fri_NY.txt", "newyork/beer_newyork/beer_w1w2w3w4_6Sat_NY.txt", "newyork/beer_newyork/beer_w1w2w3w4_7Sun_NY.txt", #"newyork/beer_newyork/beer_0326Mon_NY.txt", "newyork/beer_newyork/beer_0327Tue_NY.txt",
"newyork/coffee_newyork/coffee_w1w2w3w4_1Mon_NY.txt", "newyork/coffee_newyork/coffee_w1w2w3w4_2Tue_NY.txt", "newyork/coffee_newyork/coffee_w1w2w3w4_3Wed_NY.txt", "newyork/coffee_newyork/coffee_w1w2w3w4_4Thu_NY.txt", "newyork/coffee_newyork/coffee_w1w2w3w4_5Fri_NY.txt", "newyork/coffee_newyork/coffee_w1w2w3w4_6Sat_NY.txt", "newyork/coffee_newyork/coffee_w1w2w3w4_7Sun_NY.txt", #"newyork/coffee_newyork/coffee_0326Mon_NY.txt", "newyork/coffee_newyork/coffee_0327Tue_NY.txt",
"newyork/coke_n_cola_newyork/COLA_COKE_w1w2w3w4_1Mon_NY.txt", "newyork/coke_n_cola_newyork/COLA_COKE_w1w2w3w4_2Tue_NY.txt", "newyork/coke_n_cola_newyork/COLA_COKE_w1w2w3w4_3Wed_NY.txt", "newyork/coke_n_cola_newyork/COLA_COKE_w1w2w3w4_4Thu_NY.txt", "newyork/coke_n_cola_newyork/COLA_COKE_w1w2w3w4_5Fri_NY.txt", "newyork/coke_n_cola_newyork/COLA_COKE_w1w2w3w4_6Sat_NY.txt", "newyork/coke_n_cola_newyork/COLA_COKE_w1w2w3w4_7Sun_NY.txt", #"newyork/coke_n_cola_newyork/COLA_COKE_0326Mon_NY.txt", "newyork/coke_n_cola_newyork/COLA_COKE_0327Tue_NY.txt",
"newyork/juice_newyork/juice_w1w2w3w4_1Mon_NY.txt", "newyork/juice_newyork/juice_w1w2w3w4_2Tue_NY.txt", "newyork/juice_newyork/juice_w1w2w3w4_3Wed_NY.txt", "newyork/juice_newyork/juice_w1w2w3w4_4Thu_NY.txt", "newyork/juice_newyork/juice_w1w2w3w4_5Fri_NY.txt", "newyork/juice_newyork/juice_w1w2w3w4_6Sat_NY.txt", "newyork/juice_newyork/juice_w1w2w3w4_7Sun_NY.txt", #"newyork/juice_newyork/juice_0326Mon_NY.txt", "newyork/juice_newyork/juice_0327Tue_NY.txt",
"newyork/tea_newyork/tea_w1w2w3w4_1Mon_NY.txt", "newyork/tea_newyork/tea_w1w2w3w4_2Tue_NY.txt", "newyork/tea_newyork/tea_w1w2w3w4_3Wed_NY.txt", "newyork/tea_newyork/tea_w1w2w3w4_4Thu_NY.txt", "newyork/tea_newyork/tea_w1w2w3w4_5Fri_NY.txt", "newyork/tea_newyork/tea_w1w2w3w4_6Sat_NY.txt", "newyork/tea_newyork/tea_w1w2w3w4_7Sun_NY.txt", #"newyork/tea_newyork/tea_0326Mon_NY.txt", "newyork/tea_newyork/tea_0327Thu_NY.txt",
"newyork/water_newyork/water_w1w2w3w4_1Mon_NY.txt", "newyork/water_newyork/water_w1w2w3w4_2Tue_NY.txt", "newyork/water_newyork/water_w1w2w3w4_3Wed_NY.txt", "newyork/water_newyork/water_w1w2w3w4_4Thu_NY.txt", "newyork/water_newyork/water_w1w2w3w4_5Fri_NY.txt", "newyork/water_newyork/water_w1w2w3w4_6Sat_NY.txt", "newyork/water_newyork/water_w1w2w3w4_7Sun_NY.txt",# "newyork/water_newyork/water_0326Mon_NY.txt", "newyork/water_newyork/water_0327Tue_NY.txt",
"newyork/wine_newyork/wine_w1w2w3w4_1Mon_NY.txt", "newyork/wine_newyork/wine_w1w2w3w4_2Tue_NY.txt","newyork/wine_newyork/wine_w1w2w3w4_3Wed_NY.txt","newyork/wine_newyork/wine_w1w2w3w4_4Thu_NY.txt","newyork/wine_newyork/wine_w1w2w3w4_5Fri_NY.txt","newyork/wine_newyork/wine_w1w2w3w4_6Sat_NY.txt","newyork/wine_newyork/wine_w1w2w3w4_7Sun_NY.txt"]#,"newyork/wine_newyork/wine_0326Mon_NY.txt","newyork/wine_newyork/wine_0327Tue_NY.txt"]


    wf = open("NY_OUTPUT_week1n2n3n4.txt","w+")
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











