def bitwise_converter(line):
    word_list=line.split()
   
    index=0
    new_list=[]
    while(index <(len(word_list))):
        word=word_list[index]
            
        if(index<len(word_list)-1 and word=='bitwise'):
            index+=1
            word=word_list[index]
            if(word=='and'):
                new_list.append("&")
                index+=1
                continue
            elif(word=="or"):
                new_list.append("|")
                index+=1
                continue
            elif(word=='xor'):
                new_list.append('^')
                index+=1
                continue
            elif(word=='not'):
                new_list.append("~")
                index+=1
                continue
            elif(word=="right"):
                new_list.append(">>")
                index+=1
                continue
            elif(word=="left"):
                new_list.append("<<")
                index+=1
                continue

            
        else:
                new_list.append(word)
        index+=1
    new_line=" ".join(new_list)
    return(new_line)   
            
    
#print(bitwise_converter("a bitwise and b bitwise or c bitwise right d"))    


