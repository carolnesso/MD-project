"""
Recebe a mensagem 'input_text' e o nome do arquivo para salvar
caso a mensagem esteja no tipo list, transforma em string antes de salvar
"""
def save_file(input_text, name_file):
    f = open(name_file, "w")
    if(type(input_text) == list):
        a = ""
        for i in range(0, len(input_text)):
            a += str(input_text[i])
            if i < (len(input_text) - 1):
                a += " "
        f.write(a)
    else:
        f.write(input_text)
    f.close()