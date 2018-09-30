import arithmetic
import bitwise
import relational
import loops
def code_creator(line):
    line=arithmetic.arithmetic_convertor(line)
    line=bitwise.bitwise_converter(line)
    line=relational.relational_convertor(line)
    line=loops.special_detect(line)
    return line
#print(code_creator("a equals a plus b plus c divide e divide f power g minus xyz bitwise and r bitwise right q decrement 3"))

    