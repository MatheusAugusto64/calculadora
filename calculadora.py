import time
import os


while True:
        time.sleep (1.0)
        print("...........................")
        print("----[CALCULADORA]----")
        time.sleep (1.0)
        print("...........................")
        print("[1]- SOMA! ")
        time.sleep (1.0)
        print("...........................")
        print('[2]- SUBTRAÇÃO! ')
        time.sleep (1.0)
        print("...........................")
        print("[3]- MULTIPLICAÇÃO! ")
        time.sleep (1.0)
        print("...........................")
        print("[4]- DIVISÃO! ")
        time.sleep (1.0)
        print("...........................")
        print("[5]- ENCERRAR CALCULADORA! ")
        time.sleep (1.0)
        print("...........................")
        try:
                operação= int(input("Digite o código da operação para o cálculo ser efetuado: "))
                os.system("cls")
        except:
                print("Opção inválida!!")
                time.sleep (1.0)
                print("...........................")
                continue
        
        if operação == 5:
                time.sleep (1.0)
                print(".")
                time.sleep (1.0)
                print(".")
                time.sleep (1.0)
                print(".")
                print("Fim do programa!!!")
                break
        
        while True:

                if operação == 1:
                        n1= float(input("Digite um número: "))
                        n2= float(input("Digite outro número: "))
                        os.system("cls")
                        print(f"A soma dos números é: {n1+n2}")
                        time.sleep(1)
                        os.system("pause")
                        os.system("cls")
                        print("[1]-Para efetuar outro cálculo")
                        print("[2]-Para voltar para o menu")
                        try:
                                o = int(input("Digite o código: "))
                                os.system("cls")
                        except:
                                print("Opção inválida!!")
                                time.sleep (1.0)
                                print("...........................")
                                continue
                        if o == 1:
                                continue
                        elif o == 2:
                                break
                        
                elif operação == 2:
                        n1= float(input("Digite um número: "))
                        n2= float(input("Digite outro número: "))
                        os.system("cls")
                        print(f"A subtração dos números é: {n1-n2}")
                        time.sleep(1)
                        os.system("pause")
                        os.system("cls")
                        print("[1]-Para efetuar outro cálculo:")
                        print("[2]-Para voltar para o menu:")
                        o = int(input("Digite o código: "))
                        os.system("cls")

                        if o == 1:
                                continue
                        elif o == 2:
                                break
                elif operação == 3:
                        n1= float(input("Digite um número: "))
                        n2= float(input("Digite outro número: "))
                        os.system("cls")
                        print(f'A multiplicação dos números é: {n1*n2}')
                        time.sleep(1)
                        os.system("pause")
                        os.system("cls")
                        print('[1]-Para efetuar outro cálculo:')
                        print('[2]-Para voltar para o menu:')
                        o = int(input("Digite o código: "))
                        os.system("cls")

                        if o == 1:
                                continue
                        elif o == 2:
                                break
                elif operação == 4:
                        n1= float(input('Digite um número: '))
                        n2= float(input('Digite outro número: '))
                        os.system("cls")
                        print(f'A divisão dos números é: {n1/n2}')
                        time.sleep(1)
                        os.system("pause")
                        os.system("cls")
                        print('[1]-Para efetuar outro cálculo:')
                        print('[2]-Para voltar para o menu:')
                        o = int(input("Digite o código: "))
                        os.system("cls")

                        if o == 1:
                                continue
                        elif o == 2:
                                break
       
                else:
                  print('Operação inválida!')
                  break
