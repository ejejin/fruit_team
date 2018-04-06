import os

def read_file_name(filename):             # returning [filename, filename.txt, absolute path filename, absolute path filename without txt file]
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
    return(filelist)



def POS_NEG_prop_MAKER(filelist):
    for FILE in filelist:
        FLIST = read_file_name(FILE)
#        print(FLIST)
        rf = open(FLIST[2],"r")
        pnwf = open(("../output_files/"+FLIST[0]+"_P_n_N.txt"),"w+")
        ijk = 0
        for line in rf:
            _,POS,NEG,_,_ = line.split();
            try:
                if(ijk==0):
                    pnwf.write("Pos_Neg_propotion\n")
                    ijk = 1
                POS = int(POS); NEG = int(NEG)
                EMO = POS - NEG
                if(EMO>0):
                    pnwf.write(str(EMO)+"\n")
                if(EMO<0):
                    pnwf.write(str(EMO)+"\n")
            except:
                ValueError
                pass
    rf.close()
    pnwf.close
    print("file making is done")




def main():
    filelist = ["/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0319Mon_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/beer_0319Mon_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/beer_0320Tue_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/beer_0321Wed_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/beer_0322Thu_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/beer_0323Fri_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/beer_0324Sat_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/beer_0325Sun_LA_s.txt"]
#    filelist = ["/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0319Mon_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0320Tue_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0321Wed_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0322Thu_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0323Fri_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0324Sat_LA_s.txt","/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/tea_0325Sun_LA_s.txt"]


    POS_NEG_prop_MAKER(filelist)


if __name__=="__main__":
    main()

