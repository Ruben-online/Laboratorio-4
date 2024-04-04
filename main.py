while True:
    print("Menu laboratorio 4\n")
    print("1. Torres de Hanoi")
    print("2. Laberinto")
    print("3. Salir")

    main_menu = input("Seleccione una opcion: ")


    if main_menu == "1":
        print("\nTorres de Hanoi")


        def hanoi(n, origen, destino, auxiliar):
            if n == 1:
                print(f"Mover disco 1 de {origen} a {destino}")
                return
            hanoi(n - 1, origen, auxiliar, destino)
            print(f"Mover disco {n} de {origen} a {destino}")
            hanoi(n - 1, auxiliar, destino, origen)


        def main():
            n = int(input("Ingrese el numero de discos: "))
            hanoi(n, "A", "C", "B")


        main()

    elif main_menu == "2":
        print("\nLaberinto")

    elif main_menu == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")