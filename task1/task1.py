import sys

def itoBase(nb, baseDst, baseSrc=10):

    try:

        base=int(baseDst)
        from_base=int(baseSrc)
        if isinstance(nb, str):
            nb = int(nb, from_base)
        else:
            nb = int(nb)

        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if nb < base:
            return alphabet[nb]
        else:
            return itoBase(nb // base, base) + alphabet[nb % base]
    except ValueError:
        return ("Форматы ввода: Число(обязательно могут использоваться символы 0-Z) ВКакуюСистемуПереводим(обязательно) ИзКакойСистемы(не обязательно по умолчанию 10) Системы счисления 2,3...36 Пример 20 2 Пример A 3 16")

#print(itoBase(20, 2))

if __name__ == "__main__":

    try:
        print(itoBase(*sys.argv[1:]))
    except TypeError:
        print("Форматы ввода: Число(обязательно могут использоваться символы 0-Z) ВКакуюСистемуПереводим(обязательно) ИзКакойСистемы(не обязательно по умолчанию 10) Системы счисления 2,3...36 Пример 20 2 Пример A 3 16"  )


