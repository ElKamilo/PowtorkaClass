import sys
from PIL import Image

user_choice = -1
garage = []



def salon_audi():
    car_index = 1
    first_car = 'Audi A3'
    second_car = 'Audi A8'
    third_car = 'Audi R8'
    exit = 'Wyjście'
    car_list = [first_car, second_car, third_car, exit]
    print('Witamy w salonie Audi. Jaki samochód Panu odpowiada najbardziej?')
    print('Mamy do wyboru 3 samochody.')
    print()
    print('Aby kupić samochód wybierz 1.')
    print('Aby zobaczyć auto przed kupnem wybierz 2.')
    print()
    try:
        choice1 = int(input())
    except ValueError:
        print('Wybierz cyfrę nie literę.')
        print()
        return

    while choice1 == 1:
        car_index = 1
        first_car = 'Audi A3'
        second_car = 'Audi A8'
        third_car = 'Audi R8'
        exit = 'Wyjście'
        car_list = [first_car, second_car, third_car, exit]

        for car in car_list:
            print(car + " " + '[' + str(car_index) + ']')
            car_index += 1
        print('Które auto wybierasz?')
        try:
            car_choice = int(input())
        except ValueError:
            print('Auto kupisz wybierając liczbę nie literę.')
            print()
            return
        if car_choice == 1:
            your_car = first_car
            print(f'Właśnie stałeś sie posiadaczem samochodu {your_car}')
            garage.append(your_car)
        elif car_choice == 2:
            your_car = second_car
            print(f'Właśnie stałeś sie posiadaczem samochodu {your_car}')
            garage.append(your_car)
        elif car_choice == 3:
            your_car = third_car
            print(f'Właśnie stałeś sie posiadaczem samochodu {your_car}')
            garage.append(your_car)
        elif car_choice == 4:
            return
        if car_choice not in [1, 2, 3]:
            print('Brak auta pod tym miejscem.')
        print()

    while choice1 == 2:
        print('Który samochód chcesz obejrzeć ?')
        for car in car_list:
            print(car + " " + '[' + str(car_index) + ']')
            car_index += 1
        # print('Audi A3 [1]')
        # print('Audi A8 [2]')
        # print('Audi R8 [3]')
        # print('Wyjście [4]')
        try:
            car_check = int(input())
        except ValueError:
            print('Wybierz cyfrę nie literę.')
            print()
            salon_audi()

        if car_check == 1:
            audi_A3 = Image.open('P:\Zadania i funkcje\Obrazki\A3.jpg')
            audi_A3.show()
        if car_check == 2:
            audi_A8 = Image.open('P:\Zadania i funkcje\Obrazki\A8.jpg')
            audi_A8.show()
        if car_check == 3:
            audi_R8 = Image.open('P:\Zadania i funkcje\Obrazki\R8.jpg')
            audi_R8.show()
        if car_check == 4:
            return


def salon_bmw():
    print('Salon BMW wita klienta. Zapraszamy do obejrzenia naszych samochodów.')
    print('Proszę wybrać jedno z trzech aut.')
    print()
    print('Samochody do kupna są pod numerem 1.')
    print('Podgląd aut przed kupnem znajdziemy pod numerem 2.')
    try:
        choice = int(input())
    except ValueError:
        print('Wybierz cyfrę nie literę.')
        print()
        return

    while choice == 1:
        car_index = 1
        first_car = 'BMW M3'
        second_car = 'BMW 840'
        third_car = 'BMW X5'
        exit = "Wyjście"
        car_list = [first_car, second_car, third_car, exit]

        for car in car_list:
            print(car + " " + '[' + str(car_index) + ']')
            car_index += 1
        print('Na które padł wybór?')
        try:
            car_choice = int(input())
        except ValueError:
            print('Auto nie kupisz wybierając literę.')
            print()
            return
        if car_choice == 1:
            your_car = first_car
            print(f'Od teraz twoje auto to {your_car}')
            garage.append(your_car)
        elif car_choice == 2:
            your_car = second_car
            print(f'Od teraz twoje auto to {your_car}')
            garage.append(your_car)
        elif car_choice == 3:
            your_car = third_car
            print(f'Od teraz twoje auto to {your_car}')
            garage.append(your_car)
        elif car_choice == 4:
            return
        if car_choice not in [1, 2, 3]:
            print('Auto w tym miejscu nie istnieje.')
        print()

    while choice == 2:
        print('Który samochód chcesz obejrzeć ?')
        # for car in car_list1:
        #     print(car + " " + '[' + str(car_index) + ']')
        #     car_index += 1
        print('BMW M3 [1]')
        print('BMW 840 [2]')
        print('BMW X5 [3]')
        print('Wyjście [4]')
        try:
            car_check = int(input())
        except ValueError:
            print('Wybierz cyfrę nie literę.')
            print()
            return
        if car_check == 1:
            bmw_m3 = Image.open('P:\Zadania i funkcje\Obrazki\\bmw-m3.jpg')
            bmw_m3.show()
        if car_check == 2:
            bmw840 = Image.open('P:\Zadania i funkcje\Obrazki\\bmw 840.jpg')
            bmw840.show()
        if car_check == 3:
            bmw_x5 = Image.open('P:\Zadania i funkcje\Obrazki\\bmw-x5.jpg')
            bmw_x5.show()
        if car_check == 4:
            return


def cars_in_garage():
    if len(garage) == 0:
        print('Zanim sprawdzisz co masz wypadałoby najpierw kupić.')
        return
    if len(garage) >= 1:
        # garage_car_list = []
        # for car in car_list:
        # print(car + " " + '[' + str(car_index) + ']')
        #     car_index += 1
        print(f'Twoje auta w garażu to {garage}')
        print('Masz jakieś plany co zrobić z tymi autami?')
        print('Wyświetl dane samochodu pod numerem 4.')
        print('Aby wyjść z garażu wciśnij 5.')
        print()
    try:
        garage_choice = input()
    except ValueError:
        print('Ten sam błąd co zwykle. Aby przetrwać używaj cyfr.')
        print()
        return
    if garage_choice == 5:
        return


def remove_car_from_garage():
    car_index_garage = 0
    while len(garage) == 0:
        print('Bieda piszczy drzwiami i oknami. Póki co garaż jest pusty.')
        return
    print('Skoro już musisz to, które auto chcesz sprzedać ?')

    for car in garage:
        print(car + " [" + str(car_index_garage) + "]")
        car_index_garage += 1
    try:
        sell_index = int(input('Wybierz indeks auta do sprzedania.\n'))
    except ValueError:
        print('Nie bądź baran wybierz liczbę.')
        print()
        return

    if sell_index < 0 or sell_index > len(garage) - 1:
        print('W tym miejscu jeszcze nie posiadasz auta.')
        return

    car_sell = garage.pop(sell_index)
    print(f'Właśnie pozbyłeś sie {car_sell}')


def save_cars_to_file():
    plik = open("Garage_lista.txt", "w")
    for car in garage:
        plik.write(car + "\n")
    plik.close()


def open_car_list():
    try:
        plik = open("Garage_lista.txt")
        for line in plik.readlines():
            garage.append(line.strip())
        plik.close()
    except FileNotFoundError:
        return


open_car_list()


def stop_working_app():
    sys.exit("Zakończyłeś działanie programu")


while user_choice != 10:
    if user_choice == 1:
        salon_audi()

    if user_choice == 2:
        salon_bmw()

    if user_choice == 3:
        cars_in_garage()

    if user_choice == 4:
        remove_car_from_garage()

    if user_choice == 5:
        save_cars_to_file()

    if user_choice == 6:
        stop_working_app()

    print()
    print('Stoisz przed salonami samochodów. Do którego chcesz wejść?')
    print()

    print("1. Salon Audi")
    print("2. Salon BMW")
    print("3. Sprawdź garaż.")
    print("4. Pozbycie się auta z garażu")
    print('5. Zapisz garaż do pliku.')
    print("6. Zakończ działanie programu")
    print()
    try:
        user_choice = int(input("Wybierz podpunkt z listy: \n"))
    except ValueError:
        print(ValueError)
        print('Wystąpił błąd oraz brak przekierowania. Musisz wybrać cyfrę nie literę.')
    print()
