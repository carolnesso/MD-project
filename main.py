"""
ARQUIVO PRINCIPAL (main.py)
"""

import prime
import keys
import mdc
import dictionaryies
import exp_modular
import savefile

def encrypt(code_msg, n, e):
    """
    Recebe uma sequencia numerica (onde cada numero representa um caractere
    digitado pelo usuario na messagem original), o valor 'n' e o expoente 'e'.
    
    Retorna a mensagem encriptada
    """
   
    mensagem = []
    for i in code_msg:
        mensagem.append(exp_modular.fast_mod_expn(i, e, n))
    print("This is your encrypted message:\n\n{}".format(mensagem))
    return mensagem

def generate_public_keys():
    """
    Pede ao usuário os valores 'p', 'q' e 'e'
    para gerar as chaves.

    Salva um arquivo com as chaves públicas 'n' e 'e'.
    """
    while True:
        p = 0
        q = 0
        e = 0
        while True:
            p = int(input("Enter a prime number: "))
            if prime.is_prime(p):
                break 
            print("Sorry, this number is not accepted.")
        
        while True:
            q = int(input("Enter another prime number: "))
            if prime.is_prime(q):
                break 
            print("Sorry, this number is not accepted.")
        if p*q >=27:
            break
        else:
            print("Sorry, P*Q is under to 27")
    
    phi = keys.calc_phi(p, q)

    while True:
        e = int(input("Enter a number between 1 and {} which is prime relation to {}: ".format(phi, phi)))
        if mdc.mdc_euclides(e, phi) == 1:
            break 
        print("Sorry, this number is not accepted.")

    n = keys.calc_n(p, q)
    
    savefile.save_file("n: {}\ne: {}".format(n, e), "public_keys.txt")


def decrypt(encrypted_msg):
    """
    Recebe como parametro uma sequencia numerica
    pede ao usuario os valores 'p', 'q' e 'e' e decripta a mensagem
    retornando uma mensagem ainda numerica mas que pode ser facilmente
    'devolvida' para a sua forma original (texto).
    """
    p = int(input("Enter your first key (p): "))
    q = int(input("Enter your second key (q): "))
    e = int(input("Enter your third key (e): "))
    n = keys.calc_n(p, q)
    phi = keys.calc_phi(p, q)
    d = keys.calc_d(e, phi)

    decriptado = []
    for i in encrypted_msg:
        decriptado.append(exp_modular.fast_mod_expn(int(i), d, n))
    return decriptado
    

def first_option(message, n, e):
    """
    chamada quando o usuário quer encriptar
    transforma o texto da mensagem numa sequencia
    numerica para ser posteriormente encriptada.
    
    retorna a mensagem já encriptada.
    """
    code_message = []
    letter_to_number = dictionaryies.code_letters()

    for i in message:
        code_message.append(letter_to_number[i])
    resultado = encrypt(code_message, n, e)
    return resultado

def second_option(message):
    """
    Chamada quando o usuário quer decriptar a mensagem
    separa a sequencia numerica por espaços.

    adiciona as letras à mensagem final decriptada
    e retorna a mensagem decriptada
    """
    n_message = message.split()
    numbers_to_letters = dictionaryies.letters_code()
    decrypted = decrypt(n_message)
    decodificated_message = ""
    for i in decrypted:
        decodificated_message += numbers_to_letters[i]
    print("\n\nYour original message:\n{}\n\n".format(decodificated_message))
    return decodificated_message


def control():
    """
    Controla o fluxo das ações do usuário no programa

    variavel option: guarda o número da intenção do usuário quanto a ação no programa
    variavel input_option: guarda o número com o tipo de entrada 'digitação' ou 'arquivo txt'
    """

    while True:
        option = int(input("What do you want to do?\n1. Generate public keys\n2. Encrypt\n3. Decrypt\n4. Kill this process\n::::  "))
        input_option = 0
        final_content = ""
        if option == 4:
            print("bye")
            break
        elif option != 1:
            input_option = int(input("Do you want 1. to type or 2. send a file?\n:::: "))
        else:
            generate_public_keys()
            break
        
        if input_option == 1:
            message = input("Enter your message here: ")
            message = message.upper() #Caso a mensagem nao esteja em caixa alta
            if option == 2:
                n = int(input("Enter your first key (n): "))
                e = int(input("Enter your second key (e): "))
                final_content = first_option(message, n, e) 
            elif option == 3:
                final_content = second_option(message) 

        elif input_option == 2:
            name_file = input("What is the file name?\n:::: ")
            message = ""
            with open(name_file) as file:
                for i in file:
                    for k in i:
                        if k != '\n':
                            message += k
            if option == 2:
                n = int(input("Enter your first key (n): "))
                e = int(input("Enter your second key (e): "))
                final_content = first_option(message, n, e) 
            elif option == 3:
                final_content = second_option(message)
        
        var = input("Do you want to save this message in a text file (y/n) ? ")
        if var == "y":
            savefile.save_file(final_content, "message.txt")
            
            print("\nDone!\n\n")
      
control()