def delete_lines(file_name,number_of_line):
    
    f=open(file_name,'r')
    lines=f.readlines()
    f.close()
    f=open(file_name,'w')
    content=""
    for i in range(len(lines)):
        if(i!=number_of_line and i!=0):
            content+="\n"+lines[i]
        if(i==0 and i!=number_of_line):
            content=lines[0]
    f.write(content)

