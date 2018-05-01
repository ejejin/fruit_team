
def read_file_name(filename):             # returning [filename, filename.root, absolute path filename]
    from ROOT import TFile
    import os
    f = TFile(filename,"READ")

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
    FILE = FILENAME.replace(".root","")

    filelist = [FILE, FILENAME, filename]
    f.Close()
    return(filelist)



  
