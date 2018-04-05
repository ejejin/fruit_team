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
        pwf = open(("../output_files/"+FLIST[0]+"_Pos.txt"),"w+")
        nwf = open(("../output_files/"+FLIST[0]+"_Neg.txt"),"w+")
        pnwf = open(("../output_files/"+FLIST[0]+"_P_n_N.txt"),"w+")
        ijk = 0
        for line in rf:
            _,_,_,POSP,NEGP = line.split();
            try:
                if(ijk==0):
                    pwf.write("Postive_propotion\n")
                    nwf.write("Negative_propotion\n")
                    pnwf.write("Pos_Neg_propotion\n")
                    ijk = 1
                POSP = float(POSP); NEGP = float(NEGP)
                if(POSP>0.0):
                    pwf.write(str(POSP)+"\n")
                    pnwf.write(str(POSP)+"\n")
                if(NEGP>0.0):
                    NEGP = -NEGP
                    nwf.write(str(NEGP)+"\n")
                    pnwf.write(str(NEGP)+"\n")
            except:
                ValueError
                pass
    rf.close()
    pwf.close()
    nwf.close()
    print("file making is done")




def main():
    filelist = ["../../tea_0319Mon_LA_s.txt","../../beer_0319Mon_LA_s.txt"]
    POS_NEG_prop_MAKER(filelist)


if __name__=="__main__":
    main()

