import sys
problems = ["32 + 3g8", "3801 - 2", "45 + 43", "123 + 49"]   
  
def arithmetic_arranger(problems, solved= False):
    Line1 = str()
    Line2 = str()
    Line3 = str()
    Line4 = str()
    paddinglist = list()

    #Error detection for being > 5
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        splitprob = problem.split(" ")
        # split problems apart into component operator and operands
        oper1 = splitprob[0]
        operator = splitprob[1]
        oper2 = splitprob[2]

        #if oper1 is not a digit or operator 2 is not a digit return error
        if not ( oper1.isdigit()  and oper2.isdigit()  ):
            return "Error: Numbers must only contain digits."
            
            
        #numbers can be max four digits
        if len(oper1) > 4 or len(oper2) > 4:
            return "Error: Numbers cannot be more than four digits."
            

        #operands must be + or -
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
            

        #find the longest operands and find the padding size by adding two to the length of it (one for a space and one for operator)
        #the first operand should be padded to the padding length
        #the second operand should padded to to the the maximum padding -2 to account for the operator and 1 extra space
        if len(oper1) > len(oper2):
            padding = len(oper1)+2
        elif len(oper1) < len(oper2):
            padding = len(oper2)+2
        else:   
            padding = len(oper1) +2 
        padding = int(padding)   




        #if you are on the last problem then don't add any padding at the end, otherwise add 4 white spaces of padding
        if problem == problems[-1]:
            Line1 = Line1 + oper1.rjust(padding)
            Line2 = Line2 + operator + " " + oper2.rjust(padding -2)
            Line3 = Line3 + "-" *padding
        else:
            Line1 = Line1 + oper1.rjust(padding) + "    "
            Line2 = Line2 + operator + " " + oper2.rjust(padding -2) + "    "
            Line3 = Line3 + "-" * padding + "    "
# if operator is + add them, if it is - then subtract

      #calculate the answer by converting to int and then back to string
        if operator == "+":
            answer = int(oper1) + int(oper2)
            answer = str(answer)
        else:  
            answer = int(oper1) - int(oper2)
            answer = str(answer)

      #put together the answer line and add padding unless on last problem
        if problem == problems[-1]:    
            Line4 = Line4 + answer.rjust(padding)
        else:
            Line4 = Line4 + answer.rjust(padding) + "    "

        
      #these last statements are outside of the 'for' loop and all the lines have been \
          # generated, now throw them together
    if solved == False:   
        Result = Line1 + "\n" + Line2 + "\n" + Line3
        return Result
    if solved == True:
        Result = Line1 + "\n" + Line2 + "\n" + Line3 + "\n" + Line4    
        return Result
