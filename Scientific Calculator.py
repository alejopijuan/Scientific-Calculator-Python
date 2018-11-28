
#Alejo Pijuan
#Scientific Calculator


'''Requirements for inputs:
- All inputs need to have a space between each value, e.g. 'absol ( sqrt ( 10 + ( 5.5 * -2 ) / 9 ) ) '
- The program will break if invalid input is given. Simply restart it to keep going.
- User can quit the program by inputing 'q'
'''
'''The fundamental issue to solve while writing this program is solving for any kind of input,
typecasting the right elements of the input for the calculator to do its operations, deeply
understanding the inner workings of a stack
'''


def ChgOrderOfInput(rawInput):

    '''Initialize a stack'''
    theStack = Stack()
    '''List in which the new order of the input will be pushed'''
    fixedInput = []
    '''Split the input for smoother analysis'''
    inputToList = rawInput.split()

    for eachInput in inputToList:
        '''Had a lot of trouble making negative and float values work. Found the string method 'replace()'
and was able to then run the program smoothly with both types of values for any of the operations'''

        if eachInput.replace('-', '', 1).replace('.', '', 1).isdigit():
            fixedInput.append(eachInput)      

        elif eachInput == '(':
            theStack.push(eachInput)

        elif eachInput == ')':
            NotDigit = theStack.pop()

            while NotDigit != '(':
                fixedInput.append(NotDigit)
                NotDigit = theStack.pop()

        else:

            '''A dictionary with all the available symbols (not digits) as input'''
            dictOfSymbols = {}
            dictOfSymbols['('] = 50
            dictOfSymbols['+'] = 40
            dictOfSymbols['-'] = 40
            dictOfSymbols['*'] = 30
            dictOfSymbols['/'] = 30
            dictOfSymbols['sqrt'] = 20
            dictOfSymbols['^'] = 20
            dictOfSymbols['absol'] = 10

            '''The next while loop will check for comparison of the element at the top of the stack and the element
'forEach' which is taken from iterating through our inputs list. It will perform a pop if precedence of
the element in the stack is lower'''
            while (not theStack.isEmpty()) and (dictOfSymbols[theStack.peek()] <= dictOfSymbols[eachInput]):
                  fixedInput.append(theStack.pop())

            theStack.push(eachInput)

    while (not theStack.isEmpty()):
        fixedInput.append(theStack.pop())

    '''Return the new list in the order it will be analized'''
    return ' '.join(fixedInput)



class Stack:
    '''All operations of a stack needed for this program'''
    def __init__(self):
        self.digitOrSymbol = []


    def peek(self):
         return self.digitOrSymbol[len(self.digitOrSymbol)-1]

        
    def pop(self):
        return self.digitOrSymbol.pop()

    
    def push(self, value):
        self.digitOrSymbol.append(value)


    def isEmpty(self):
        return (self.digitOrSymbol == [])
    


        
            
if __name__ == '__main__':
    '''Create an infinite loop so after one calculation is done, the user can give another input'''

    while 1:
        '''Get the input from user, which will be modifiend with the ChgOrderOfInput equation'''
        UserInput= input('Insert Your Equation: ')

        myEquation = ChgOrderOfInput(UserInput)

        forCalculations = myEquation.split(' ')
        
        print(myEquation)

        usefulList = []

        if (forCalculations[0] != 'q'):
            '''q for quitting the program'''
            while len(forCalculations) != 0:
                '''there needs to be something in the list of strings'''
                popAndUse = forCalculations.pop(0)

                if popAndUse.replace('-', '', 1).replace('.', '', 1).isdigit():
                    usefulList.append(float(popAndUse))

                    '''Once we figured out how to grab each item fro the stack and position the to perform a sum operation,
we just copied the operation, created elif statements and just changed each operation in order of priority.
We always have to make sure that the stack has more than one element (except for absol and sqrt)
so that the operation can be processed. These types of operations are called binary operations.
Operations below are not sorted'''

                elif popAndUse == 'absol':

                    if len(usefulList) > 0:
                        usefulList.append(abs(usefulList.pop()))

                    else:                    
                        print ('NOT VALID INPUT')
                        break


                elif popAndUse == '%':
                    
                    if len(usefulList) > 1:                        
                        valueHolder = usefulList.pop()
                        usefulList.append(usefulList.pop() % valueHolder)

                    else:                        
                        print ('NOT VALID INPUT')
                        break


                    
                elif popAndUse == '-':
                    
                    if len(usefulList) > 1:
                        valueHolder = usefulList.pop()
                        usefulList.append(usefulList.pop() - valueHolder)

                    else:                        
                        print ('NOT VALID INPUT')
                        break


                    
                elif popAndUse == '+':
                    
                    if len(usefulList) > 1:
                        usefulList.append(usefulList.pop() + usefulList.pop())

                    else:                        
                        print ('NOT VALID INPUT')
                        break


                elif popAndUse == '/':
                    
                    if len(usefulList) > 1:
                        valueHolder = usefulList.pop()
                        usefulList.append(usefulList.pop() / valueHolder)
                        
                    else:                        
                        print ('NOT VALID INPUT')
                        break
                
                

                elif popAndUse == '*':
                    
                    if len(usefulList) > 1:
                        usefulList.append(usefulList.pop() * usefulList.pop())
                        
                    else:                        
                        print ('NOT VALID INPUT')
                        break

                
                

                elif popAndUse == '^':
                    
                    if len(usefulList) > 1:
                        valueHolder = usefulList.pop()
                        usefulList.append(pow(usefulList.pop(), valueHolder))

                    else:                        
                        print ('NOT VALID INPUT')
                        break
        
                        
                elif popAndUse == 'sqrt':
                    
                    if len(usefulList) > 0:
                        usefulList.append(pow(usefulList.pop(), 1/2))
                        
                    else:                        
                        print ('NOT VALID INPUT')
                        break

                

                else:                    
                    break
                
            print (usefulList.pop())

        else:
            print('Goodbye!')
            break
    
