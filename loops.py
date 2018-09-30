def special_detect(line):
    
    if(line[0:6]=='print '):
        count=line.count("var ")
        if("var " not in line):
            return("print(\""+line[6:len(line)]+"\")")
        else:
            return("print("+line[6:len(line)]+")")
        

            
            
            
    else:
        if(line[0:5]=="while"):
            line+=" :"
        elif(line[0:3]=='for'):
            line+=" :"
        elif(line=="else"):
            line+=" :"
        elif(line[0:6]=="define"):
          
            nline=""
            if(" of " in line):
                pos=line.index(" of ")
                nline=("def"+line[6:pos])
                
                params=line[pos+4:len(line)].split()
                nline+="("
                for i in range(len(params)-1):
                    nline+=(params[i]+",")
                nline+=(params[-1]+"):")
            return nline
        elif(line[0:5]=="class"):
            line+=" :"
        if ("square bracket open" in line):

            count=line.count("square bracket open")

            line=line.replace("square bracket open","[",count)
        if ("square bracket close" in line):

            count=line.count("square bracket close")

            line=line.replace("square bracket close","]",count)

        if ("bracket open " in line):

            count=line.count("bracket open")

            line=line.replace("bracket open","(",count)
        if("bracket close" in line):
            count=line.count("bracket close")
            line=line.replace("bracket close",")",count)
        dots=line.count(" dot ")
        commas=line.count("comma ")
        #print(commas)
        if(dots>0):
            line=line.replace("dot",".",dots)
        if(commas>0):
            line=line.replace("comma ",",",commas)

    return line
#print(special_detect("print var wejf   a  plus asjdjnd"))

    