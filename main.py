def citire():

    result_list = []

    str_list = input("Introduceti elementele liste separate prin cate un spatiu: ")
    str_elemente = str_list.split(" ")

    for element in str_elemente:
        result_list.append(int(element))

    return result_list


def get_oglindit(n):
    """
    Determina oglinditul unui numar
    :param n: numarul
    :return: oglinditul lui n
    """

    oglindit = 0
    while n:
        oglindit = oglindit * 10 + (n % 10)
        n //= 10

    return oglindit


def is_dividing(n, lista):
    """
    Verifica daca n se divide cu toate elementele din lista
    :param n:
    :param lista:
    :return: True daca sse divide, False altfel
    """

    for divizor in lista:
        if n % divizor != 0:
            return False
    return True


def get_oglindite_daca_div(lista_1, lista_2, lista_3):

    """
    Determina toate elementele oglindite din primele 2 liste daca se divid cu toate elementele din a 3 a lista
    :param lista_1:
    :param lista_2:
    :param lista_3:
    :return: lista cu elemenetele oglindite
    """

    oglindit_list_1 = []
    oglindit_list_2 = []

    for element in range (0,len(lista_1)):
        if is_dividing(element, lista_3):
            oglindit = get_oglindit(element)
            lista_1[element] = oglindit

    for element in range(0, len(lista_2)):
        if is_dividing(element, lista_3):
            oglindit = get_oglindit(element)
            lista_2[element] = oglindit

    return lista_1, lista_2



def get_nr_evens(list):
    """
    Determina numarul de elemente pare dintr-o lista
    :param list:lista de elemente
    :return:numarul de elemente pare din lista
    """

    nr = 0

    for element in list:
        if element % 2 == 0:
            nr += 1

    return nr


def test_get_nr_evens():
    assert get_nr_evens([1, 2, 3, 4, 5]) == 2
    assert get_nr_evens([10, 1, 10, 1, 10]) == 3
    assert get_nr_evens([12, 14, 16, 18, 22]) == 5


def is_even_equal(lista_1, lista_2):
    """
    Verifica daca 2 liste au acelasi numar de elemente pare
    :param lista_1:prima lista de elemente
    :param lista_2:a doua lista de elemente
    :return:True daca au acelasi numar de elemente pare
            False in caz contrar
    """

    if get_nr_evens(lista_1) == get_nr_evens(lista_2):
        return True
    else:
        return False


def test_is_even_equal():
    assert is_even_equal([2, 3, 4], [2, 8]) is True
    assert is_even_equal([1, 3, 4, 5], [1, 3]) is False
    assert is_even_equal([2, 2, 2],[4, 4, 4]) is True


def get_intersection(lista_1, lista_2):
    """
    Determina intersectia a doua liste
    :param lista_1:prima lista
    :param lista_2:a doua lista
    :return:o noua lista care contine intersectia primelor doua
    """

    intersection_list = []

    for element in lista_1:
        if element in lista_2:
            intersection_list.append(element)

    return intersection_list


def test_get_intersection():
    assert get_intersection([1, 2, 3], [2,3]) == [2,3]
    assert get_intersection([1, 2, 3], [4, 5, 6]) == []
    assert get_intersection([12, 3, 7, 9], [12, 7, 22, 10, 5]) == [12, 7]


def is_palindrom(n):
    """
        Verifica daca un numar este palindrok
    :param n: numarul
    :return: True daca este palindrom, False in caz contrar
    """

    inv_n = 0
    k = n

    while k:
        inv_n = inv_n * 10 + (k % 10)
        k //= 10

    if inv_n == n:
        return True
    else:
        return False


def test_is_palindrom():
    assert is_palindrom(1221) is True
    assert is_palindrom(1332) is False
    assert is_palindrom(9999) is True


def merge_elements(el_1, el_2):
    """
    Concateneaza 2 numere
    :param el_1:primul numar
    :param el_2:al doilea numar
    :return:numarul rezultat din concatenare
    """

    power = 1
    k = el_2
    while k:
        power *= 10
        k //= 10

    el_1 = el_1 * power + el_2
    return el_1


def test_merge_elements():
    assert merge_elements(12, 13) == 1213
    assert merge_elements(12, 9) == 129
    assert merge_elements(199,991) == 199991


def get_all_palindroms_from_kat(lista_1, lista_2):
    """
    Afișeaza toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în
cele două liste.
    :param lista_1:prima lista de elemente
    :param lista_2:a doua lista de elemente
    :return:o lista care contine palindroamele create
    """

    palindroms_list = []

    if len(lista_1) > len(lista_2):
        minn_elem = len(lista_2)
    else:
        minn_elem = len(lista_1)


    for i in range(0, minn_elem):

        palindrom = merge_elements(lista_1[i], lista_2[i])

        if is_palindrom(palindrom):
            palindroms_list.append(palindrom)

    return palindroms_list


def test_get_all_palindroms_from_kat():
    assert get_all_palindroms_from_kat([12, 13, 2],[21, 31, 1]) == [1221, 1331]
    assert get_all_palindroms_from_kat([15, 0, 41],[51, 31, 14]) == [1551, 4114]



def main():

    lista_1 = []
    lista_2 = []

    while True:

        print("""
            1.Citire liste
            2.Verifica daca listele au acelasi numar de elemente pare
            3.Determina intersectia a doua liste
            4.Afiseaz toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste.
            5.Citiți o a treia listă și afișați listele obținute prin înlocuirea în cele două liste citite la punctul 1 a
tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele sunt divizibile
cu toate elementele din a treia lista. Dacă nu îndeplinesc regula, păstrați elementul așa cum e.
            x.Iesire din program
        """)

        optiune = input("Selectati optiunea: ")

        if optiune == '1':

            lista_1 = citire()
            lista_2 = citire()

            print(lista_1, lista_2)

        elif optiune == '2':

            if is_even_equal(lista_1, lista_2):
                print("DA")
            else:
                print("NU")

        elif optiune == '3':

            print(get_intersection(lista_1, lista_2))

        elif optiune == '4':

            print(get_all_palindroms_from_kat(lista_1, lista_2))

        elif optiune == '5':
            lista_3 = citire()
            print(get_oglindite_daca_div(lista_1, lista_2, lista_3))

        elif optiune == 'x':
            break

        else:
            print("Optiune invalida!")


test_get_intersection()
test_is_palindrom()
test_merge_elements()
test_get_all_palindroms_from_kat()
test_get_nr_evens()
test_is_even_equal()
main()
