import os
def text_convert_csv(filename, outputpath = ''):
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
    filelist = [FILE, FILENAME, filename, filename_NoRoot]   #[filename, filename.txt, absolute path filename, absolute path filename without txt file]

    if(outputpath == ''):
        Name_Output_File = filelist[3] + "/" + filelist[0] + "_t.csv"
        Name_Output_File = Name_Output_File.replace("//","/")
    elif(outputpath[0] == "/"):
        Name_Output_File = outputpath + "/"+ filelist[0] + "_t.csv"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    elif(outputpath[0] == "~"):
        Name_Output_File = outputpath.replace("~",os.environ['HOME']) +filelist[0]+ "_t.csv"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    else:
        Name_Output_File = os.getcwd() + "/" + outputpath + "/"+ filelist[0]+"_t.csv"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    f = open(filelist[2],'r')
    outfile = open(Name_Output_File,"w+")
    for line in f:
        Line = line.replace(" ",",")
        outfile.write(Line)
    f.close()
    outfile.close()
    return Name_Output_File


def csv_convert_txt(filename, outputpath = ''):
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
    FILE = FILENAME.replace(".csv","")
    filename_NoRoot = filename.replace(filename[len(filename)-loca:len(filename)],"")
    filelist = [FILE, FILENAME, filename, filename_NoRoot]   #[filename, filename.csv, absolute path filename.csv, absolute path filename without csv file]
    if(outputpath == ''):
        Name_Output_File = filelist[3] + "/" + filelist[0] + "_t.txt"
        Name_Output_File = Name_Output_File.replace("//","/")
    elif(outputpath[0] == "/"):
        Name_Output_File = outputpath + "/"+ filelist[0] + "_t.txt"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    elif(outputpath[0] == "~"):
        Name_Output_File = outputpath.replace("~",os.environ['HOME']) +filelist[0]+ "_t.txt"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    else:
        Name_Output_File = os.getcwd() + "/" + outputpath + "/"+ filelist[0]+"_t.txt"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    f = open(filelist[2],'r')
    outfile = open(Name_Output_File,"w+")
    for line in f:
        Line = line.replace(","," ")
        outfile.write(Line)
    f.close()
    outfile.close()
    return Name_Output_File





def main():
    Infile = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/newyork/beer_newyork/beer_0319Mon_newyork.txt"
    CSV_FILE = text_convert_csv(Infile,".")
    print(CSV_FILE)
    TXT_FILE = csv_convert_txt(CSV_FILE,".")
    print(TXT_FILE)


if __name__=="__main__":
    main()

