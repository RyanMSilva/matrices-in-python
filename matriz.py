def createI_matrix(lin, col):
    matrix = []
    for l in range(lin):
        line = []
        for c in range(col):
            if (l == c):
                val = 1
            else:
                val = 0
            line.append(val)
        matrix.append(line)
    return matrix

def create_matrix(lin, col):
    matrix = []
    for l in range(lin):
        line = []
        for c in range(col):
            val = int(input("What is the value to be written in the position [" + str(l+1) + "," + str(c+1) + "]?"))
            line.append(val)
        matrix.append(line)
    return matrix

def read_matrix():
    x = []
    y = []
    linha = int(input("Inform the number of lines in your matrix: "))
    coluna = int(input("Inform the number of columns in your matrix: "))
    your_matrix = create_matrix(linha, coluna)
    for l in range(linha):
        for c in range(coluna):
            x.append(your_matrix[l][c])
        y = x
        print(y)
        x = []

def even_matrix():
    even_num = []
    linha = int(input("Inform the number of lines in your matrix: "))
    coluna = int(input("Inform the number of columns in your matrix: "))
    your_matrix = create_matrix(linha, coluna)
    for l in range(linha):
        for c in range(coluna):
            if (your_matrix[l][c]%2 == 0):
                even_num.append(your_matrix[l][c])
    print("The even numbers are:", even_num)

def readI_matrix():
    x = []
    y = []
    var = 0
    linha = int(input("Inform the number of lines in your matrix: "))
    coluna = int(input("Inform the number of columns in your matrix: "))
    your_matrix = createI_matrix(linha, coluna)
    for l in range(linha):
        for c in range(coluna):
            x.append(your_matrix[l][c])
        y = x
        print(y)
        x = []

resp = input("Start program? [yes/no]")

while (resp == "yes"):
    print("|------------------------------------------------------------------|")
    print("[1] Create personalized matrix.")
    print("[2] Create personalized identity matrix.")
    print("[3] Create personalized matrix, with an even number's counter.")
    print("[4] Exit.")
    print("|------------------------------------------------------------------|")

    dec = int(input("What is the function you want to execute: "))

    m = 0

    if (dec == 1):
        m = read_matrix()
        print(m)
    elif (dec == 2):
        m = readI_matrix()
        print(m)
    elif (dec == 3):
        m = even_matrix()
        print(m)
    elif (dec == 4):
        exit()
    else:
        print("Please choose a valid option.")
        print()
        resp = input("Try again? [yes/no] ")
    resp = input("Try again? [yes/no] ")
