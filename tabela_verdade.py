#ENTRADAS
N = int(input("").strip())
elementos1 = input("").strip()
elementos2 = input("").strip()
expressao = (input("").strip().upper()).split(" ")

#FUNÇÕES
def tabela_and(vetor1, vetor2, vetor3): #TABELA AND
    for i in range(len(vetor1)):
        if vetor1[i] and vetor2[i]:
            vetor3.append(True)
        else:
            vetor3.append(False)

def tabela_or(vetor1, vetor2,vetor3): #TABELA OR
    for i in range(N):
        if vetor1[i] or vetor2[i]:
            vetor3.append(True)
        else:
            vetor3.append(False)

def tabela_xor(vetor1, vetor2, vetor3): #TABELA XOR
    for i in range(N):
        if vetor1[i] == vetor2[i]:
            vetor3.append(False)
        else:
            vetor3.append(True)

def tabela_nand(vetor1, vetor2, vetor3): #TABELA NAND
    for i in range(N):
        if vetor1[i] == True and vetor2[i] == True:
            vetor3.append(False)
        else:
            vetor3.append(True)

def tabela_nor(vetor1, vetor2, vetor3): #TABELA NOR
    for i in range(N):
        if not vetor1[i] and not vetor2[i]:
            vetor3.append(True)
        else:
            vetor3.append(False)

def tabela_mor(vetor1, vetor2, vetor3): #TABELA MOR
    for i in range(N):
        if (not vetor1[i]) or vetor2[i]:
            vetor3.append(True)
        else:
            vetor3.append(False)

#VARIAVÉIS PRÉ DEFINIDAS
s1 = []
s2 = []
result1 = []
result2 = []

#CONT DE PALAVRAS
cont = len(expressao)

p = 0

#CONVERSOR DE TRUE E 1 / FALSE E 0
for i in range(len(elementos1)):
    if elementos1[i] == "1":
        s1.append(True)
    elif elementos1[i] == "0":
        s1.append(False)
    else:
        p += 1

for i in range(len(elementos2)):
    if elementos2[i] == "1":
        s2.append(True)
    elif elementos2[i] == "0":
        s2.append(False)
    else:
        p += 1


#RESTRIÇÕES
if p == 0:
    if len(elementos1) == len(elementos2):
        if cont == 3 or cont == 5:
            if N > 0 and N <= 1000:

                # PRIMEIRO OPERADOR LÓGICO
                if expressao[1] == "AND":
                    if expressao[0] == "S1" and expressao[2] == "S1":
                        result1.append(tabela_and(s1, s1, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S2":
                        result1.append(tabela_and(s2, s2, result1))
                    elif expressao[0] == "S1" and expressao[2] == "S2":
                        result1.append(tabela_and(s1, s2, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S1":
                        result1.append(tabela_and(s2, s1, result1))
                    else:
                        p += 1

                elif expressao[1] == "OR":
                    if expressao[0] == "S1" and expressao[2] == "S1":
                        result1.append(tabela_or(s1, s1, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S2":
                        result1.append(tabela_or(s2, s2, result1))
                    elif expressao[0] == "S1" and expressao[2] == "S2":
                        result1.append(tabela_or(s1, s2, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S1":
                        result1.append(tabela_or(s2, s1, result1))
                    else:
                        p += 1

                elif expressao[1] == "XOR":
                    if expressao[0] == "S1" and expressao[2] == "S1":
                        result1.append(tabela_xor(s1, s1, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S2":
                        result1.append(tabela_xor(s2, s2, result1))
                    elif expressao[0] == "S1" and expressao[2] == "S2":
                        result1.append(tabela_xor(s1, s2, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S1":
                        result1.append(tabela_xor(s2, s1, result1))
                    else:
                        p += 1

                elif expressao[1] == "MOR":
                    if expressao[0] == "S1" and expressao[2] == "S1":
                        result1.append(tabela_mor(s1, s1, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S2":
                        result1.append(tabela_mor(s2, s2, result1))
                    elif expressao[0] == "S1" and expressao[2] == "S2":
                        result1.append(tabela_mor(s1, s2, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S1":
                        result1.append(tabela_mor(s2, s1, result1))
                    else:
                        p += 1

                elif expressao[1] == "NAND":
                    if expressao[0] == "S1" and expressao[2] == "S1":
                        result1.append(tabela_nand(s1, s1, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S2":
                        result1.append(tabela_nand(s2, s2, result1))
                    elif expressao[0] == "S1" and expressao[2] == "S2":
                        result1.append(tabela_nand(s1, s2, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S1":
                        result1.append(tabela_nand(s2, s1, result1))
                    else:
                        p += 1

                elif expressao[1] == "NOR":
                    if expressao[0] == "S1" and expressao[2] == "S1":
                        result1.append(tabela_nor(s1, s1, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S2":
                        result1.append(tabela_nor(s2, s2, result1))
                    elif expressao[0] == "S1" and expressao[2] == "S2":
                        result1.append(tabela_nor(s1, s2, result1))
                    elif expressao[0] == "S2" and expressao[2] == "S1":
                        result1.append(tabela_nor(s2, s1, result1))
                    else:
                        p += 1

                else:
                    p += 1
                    
                                                
                if cont == 5: #EXPRESSÃO COM DOIS OPERADORES LÓGICOS

                    if expressao[3] == "AND":
                        if expressao[4] == "S1":
                            result2.append(tabela_and(result1, s1, result2))
                        elif expressao[4] == "S2":
                            result2.append(tabela_and(result1, s2, result2))
                        else:
                            p += 1

                    elif expressao[3] == "OR":
                        if expressao[4] == "S1":
                            result2.append(tabela_or(result1, s1, result2))
                        elif expressao[4] == "S2":
                            result2.append(tabela_or(result1, s2, result2))
                        else:
                            p += 1

                    elif expressao[3] == "XOR":
                        if expressao[4] == "S1":
                            result2.append(tabela_xor(result1, s1, result2))
                        elif expressao[4] == "S2":
                            result2.append(tabela_xor(result1, s2, result2))
                        else:
                            p += 1

                    elif expressao[3] == "MOR":
                        if expressao[4] == "S1":
                            result2.append(tabela_mor(result1, s1, result2))
                        elif expressao[4] == "S2":
                            result2.append(tabela_mor(result1, s2, result2))
                        else:
                            p += 1

                    elif expressao[3] == "NAND":
                        if expressao[4] == "S1":
                            result2.append(tabela_nand(result1, s1, result2))
                        elif expressao[4] == "S2":
                            result2.append(tabela_nand(result1, s2, result2))
                        else:
                            p += 1

                    elif expressao[3] == "NOR":
                        if expressao[4] == "S1":
                            result2.append(tabela_nor(result1, s1, result2))
                        elif expressao[4] == "S2":
                            result2.append(tabela_nor(result1, s2, result2))
                        else:
                            p += 1

                    else:
                        p += 1  

            else:
                p += 1            
        else:
            p += 1        
    else:
        p += 1
else:
    p += 1      
    
if p == 0:
    # PRINT DO RESULTADO
    if cont == 3:
        for i in range(N):
            if result1[i] == True:
                print(1, end="")
            else:
                print(0, end="")
        
    elif cont == 5:
        for i in range(N):
            if result2[i] == True:
                print(1, end="")
            else:
                print(0, end="")
                
else:
    print("ERRO")