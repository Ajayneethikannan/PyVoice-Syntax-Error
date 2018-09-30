def arithmetic_convertor(line):
    word_list=line.split()
    
    index=0
    new_list=[]
    floor_flag=0
    for word in word_list:
        operations=0
        if(floor_flag==1):
            floor_flag=0
            index+=1
            continue
      
        if(word=="equals"):# for equal to statements
            new_list.append("=")
            operations+=1
        if(word=="plus"):# for plus to statements
            new_list.append("+")
            operations+=1
        if(word=="minus"):# for minus to statements
            new_list.append("-")
            operations+=1
        if(word=="multiply"):# for multiply to statements
            new_list.append("*")
            operations+=1
        if(word=="divide"):# for divide to statements
            new_list.append("/")
            operations+=1
        if(word=="floor" and index<len(word_list)-1):# for divide to statements
            if(word_list[index+1]=='divide'):
                operations+=1
                new_list.append("//")
                floor_flag=1
                index+=1
                continue
               
           
        if(word=="power"):# for power to statements
            new_list.append("**")
            operations+=1
        if(word=="modulo"):# for power to statements
            new_list.append("%")
            operations+=1
        if(word=="increment"):# for power to statements
            new_list.append("+=")
            operations+=1
        if(word=="decrement"):# for power to statements
            new_list.append("-=")
            operations+=1
        
        if(operations==0 and index<len(word_list)):new_list.append(word_list[index])
        
        index+=1
    new_line=" ".join(new_list)
    return(new_line)
#print(arithmetic_convertor("a plus b minus c power d modulo e floor divide g"))