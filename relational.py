
def relational_convertor(line):
  
    
    less_equal=line.count("less than or equal to")
    great_equal=line.count("greater than or equal to")
    line=line.replace("less than or equal to","<=",less_equal)
    line=line.replace("greater than or equal to",">=",great_equal)
    less=line.count("less than")
    great=line.count("greater than")
    line=line.replace("less than","<",less)
    line=line.replace("greater than",">",great)
    equal=line.count("equal to")
    line=line.replace("equal to","==",equal)
    line = line.replace("integer", 'int',line.count("integer"))
    return line

