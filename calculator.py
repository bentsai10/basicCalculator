from tkinter import *

root = Tk()
root.title("Calculator")

#number and operation arrays to keep track of user input
numbers = []
operations = []

#function called when a number button is pressed
#Clears default 0 displayed to display number pressed
#If previous number in equation being displayed, clear way for new number
def numberPressed(number):
    if text.get() == "0":
        text.set("")
    if len(numbers) > 0:
        if numbers[0]%1 ==0:
            prevNum = int(numbers[0])
        else:
            prevNum = float(numbers[0])
        if len(operations) > 0 and text.get() == str(prevNum):
            text.set("")
            #numberEntry.delete(0, END)
    text.set(text.get() + str(number))
    #numberEntry.insert(END, number)
#function called when clear button is pressed
#clears the display and numbers/operations arrays, then displays default 0
def clearPressed():
    text.set("0")
    numbers.clear()
    operations.clear()
#function called when any operation button is pressed
#Address cases of negation and % so that no new number added to numbers array
#Based on the given operation, perform the given operation
#If the operation is =, calculate the final result
def operationPressed(operation):
    if operation == "=":
        print(text.get())
        if float(text.get()) != 0:
            numbers.append(float(text.get()))
        print(numbers)
        calculate()
    elif operation == "%":
        newNum = float(text.get())/100
        numbers.clear()
        operations.clear()
        text.set(str(newNum))
    elif operation == "negate":
        newNum = float(text.get())*(-1)
        if newNum%1 ==0:
            newNum = int(newNum)
        text.set(str(newNum))
    else:
        numbers.append(float(text.get()))
        operations.append(operation)
        print(numbers)
        print(operations)
#function to calculate final value
#Loops until there is only 1 or less elements in numbers array
#pops elements from numbers and operations to calculate final value
def calculate():
    if float(text.get())%1 ==0:
        newNum = int(text.get())
    else:
        newNum = float(text.get())
    while len(numbers) > 1:
        num1 = numbers.pop(0)
        num2 = numbers.pop(0)
        op = operations.pop(0)
        if op == "+":
            newNum = num1 + num2
        elif op == "-":
            newNum = num1 - num2
        elif op =="*":
            newNum = num1 * num2
        else:
            newNum = float(num1)/num2
            print(newNum)
    if len(operations) == 1 :
        num1 = numbers.pop(0)
        op = operations.pop(0)
        if op == "+":
            newNum = num1 + num1
        elif op == "-":
            newNum = num1 - num1
        elif op == "*":
            newNum = num1 * num1
        else:
            newNum = num1 / num1
    if newNum%1 ==0:
        newNum = int(newNum)
    else:
        newNum = float(newNum)
    text.set(str(newNum))
    numbers.clear()
    operations.clear()
text = StringVar()
#Create entry window to display numbers clicked on by user
numberEntry = Entry(root, width = 30, borderwidth = 10, bg = "#000000", fg = "#ffffff", textvariable = text, state = DISABLED)
#Create buttons for the 10 essential digits
button1 = Button(root, text = "1", padx = 20, pady = 10, bg = '#000000', fg = 'white', width = 2, command=lambda:numberPressed(1))
button2 = Button(root, text = "2", padx = 20, pady = 10, bg = "#000000", fg = "white", width = 2, command=lambda:numberPressed(2))
button3 = Button(root, text = "3", padx = 20, pady = 10, bg = '#000000', fg = 'white', width = 2, command=lambda:numberPressed(3))
button4 = Button(root, text = "4", padx = 20, pady = 10, bg = "#000000", fg = "white", width = 2, command=lambda:numberPressed(4))
button5 = Button(root, text = "5", padx = 20, pady = 10, bg = "#000000", fg = "white", width = 2, command=lambda:numberPressed(5))
button6 = Button(root, text = "6", padx = 20, pady = 10, bg = "#000000", fg = "white", width = 2, command=lambda:numberPressed(6))
button7 = Button(root, text = "7", padx = 20, pady = 10, bg = "#000000", fg = "white", width = 2, command=lambda:numberPressed(7))
button8 = Button(root, text = "8", padx = 20, pady = 10, bg = "#000000", fg = "white", width = 2, command=lambda:numberPressed(8))
button9 = Button(root, text = "9", padx = 20, pady = 10, bg = "#000000", fg = "white", width = 2, command=lambda:numberPressed(9))
button0 = Button(root, text = "0", padx = 40, pady = 10, bg = "#000000", fg = "white", width = 5, command=lambda:numberPressed(0))

#Create buttons for basic math operations
plusButton = Button(root, text = "+", padx = 20, pady = 5, bg = 'orange', fg = "white", width = 2, command=lambda:operationPressed("+"))
minusButton = Button(root, text = "-", padx = 20, pady = 5, bg = "orange", fg = "white", width = 2, command=lambda:operationPressed("-"))
timesButton = Button(root, text = "x", padx = 20, pady = 5, bg = "orange", fg = "white", width = 2, command=lambda:operationPressed("*"))
divideButton = Button(root, text = "÷", padx = 20, pady = 5, bg = "orange", fg = "white", width = 2, command=lambda:operationPressed("/"))
equalButton = Button(root, text = "=", padx = 20, pady = 5, bg = "orange", fg = "white", width = 2, command=lambda:operationPressed("="))
decimalButton = Button(root, text = ".", padx = 20, pady = 5, bg = "gray", fg = "black", width = 2)
negateButton = Button(root, text = "+/-", padx = 20, pady = 5, bg = "gray", fg = "black", width = 2, command=lambda:operationPressed("negate"))
percentButton = Button(root, text = "%", padx = 20, pady = 5, bg = "gray", fg = "black", width = 2, command=lambda:operationPressed("%"))
clearButton = Button(root, text = "C", padx = 20, pady = 5, bg = "gray", fg = "black", width = 2, command = clearPressed)

root.bind('1', lambda event: numberPressed(1))
root.bind('2', lambda event: numberPressed(2))
root.bind('3', lambda event: numberPressed(3))
root.bind('4', lambda event: numberPressed(4))
root.bind('5', lambda event: numberPressed(5))
root.bind('6', lambda event: numberPressed(6))
root.bind('7', lambda event: numberPressed(7))
root.bind('8', lambda event: numberPressed(8))
root.bind('9', lambda event: numberPressed(9))
root.bind('0', lambda event: numberPressed(0))
root.bind('<Return>', lambda event: operationPressed("="))
root.bind('+', lambda event: operationPressed("+"))
root.bind('-', lambda event: operationPressed("-"))
root.bind('*', lambda event: operationPressed("*"))
root.bind('/', lambda event: operationPressed("/"))
root.bind('%', lambda event: operationPressed("%"))
root.bind('n', lambda event: operationPressed("negate"))

#Position the Entry object at the top of the window spanning 3 columns
numberEntry.grid(row = 0, column = 0, columnspan = 4)

#Position each digit button according to traditional calculator layout
button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)
button0.grid(row = 5, column = 0, columnspan = 2)

#Position each operation button according to traditional calculator layout
plusButton.grid(row = 4, column = 3)
minusButton.grid(row = 3, column = 3)
timesButton.grid(row = 2, column = 3)
divideButton.grid(row = 1, column = 3)
equalButton.grid(row = 5, column = 3)
decimalButton.grid(row = 5, column = 2)
clearButton.grid(row = 1, column = 0)
negateButton.grid(row = 1, column = 1)
percentButton.grid(row = 1, column= 2)

text.set("0")
print(text.get())
root.mainloop()
