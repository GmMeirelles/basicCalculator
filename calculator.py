#Calculator with python

count = 1

while count == 1:
    #Functions

    #Sum
    def soma(num1, num2): print(f"Resultado: {num1+num2}")

    #Subtraction
    def sub(num1, num2): print(f"Resultado: {num1-num2}")

    #Division
    def div(num1, num2): 
        if num2>0:print(f"Resultado: {num1/num2}")
        else:print("Divisor não pode ser 0")

    #Multplication
    def mult(num1, num2): print(f"Resultado: {num1*num2}")

    #Presentation
    op = int(input("==========PYTHON CALCULATOR==========\n[1] Sum\n[2] Subtraction\n[3] Division\n[4] Multplication\nDigite a sua opção: "))

    #Verification
    if op > 4 or op<1:
        print("Digite uma opção válida.")
        break

    #Colect numbers
    num1 = int(input("Primeiro valor: "))
    num2 =  int(input("Segundo valor: "))

    #Make operations
    if op == 1:soma(num1, num2)
    elif op == 2:sub(num1, num2)
    elif op == 3:div(num1, num2)
    elif op == 4:mult(num1, num2)
    

    #Again?
    i = int(input("Deseja repetir?\n[1] Sim\n[2] Não\nDigite sua opção: "))
    if i == 1: count = i
    elif i == 2: count = 2
    else:
        print("Por não colocar um número válido irei encerrar o programa.")
        count = 2
