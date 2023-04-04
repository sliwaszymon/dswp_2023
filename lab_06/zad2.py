def foo(nowy_plik, *pliki):
    with open(nowy_plik, 'w') as n:
        for plik in pliki:
            with open(plik, 'r') as s:
                for s_line in s:
                    if s_line.find('\n') >= 1:
                        n.write(s_line)
                    else:
                        n.write(s_line + '\n')


# foo('cc.txt', 'aaa.txt', 'bbb.txt')