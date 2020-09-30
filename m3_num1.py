def plural_form(n, *args):
    if n == 0 or (11 <= n % 100 <= 14) or n >= 5 and (n % 10 == 0 or n % 10 >= 5 and n % 10 <= 9):
        return str(n)+' ' + args[2]
    elif n % 10 == 1:
        return str(n)+' ' + args[0]
    else:
        return str(n)+' ' + args[1]


# test
print(plural_form(1, 'яблоко', 'яблока', 'яблок'), plural_form(2, 'яблоко', 'яблока', 'яблок'), plural_form(11, 'студент',
                                                                                                            'студента', 'студентов'), plural_form(15, 'студент', 'студента', 'студентов'), plural_form(3, 'студент', 'студента', 'студентов'))
