def leiaInt(a):
    while True:
        try:
            s = int(input(a))
        except:
            print('Digite um valor numérico!',end=' ')
        else:
            return s