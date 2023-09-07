from Controller import Controller

print("Colorealo Guatematel")
print("###################")
print("\n")

while(True):
  print("Menú:")
  print("1) Crear tablero")
  print("2) Mostrar datos del estudiante")
  print("3) Salir")
  selected_option = input("Elija una opción: ")

  if selected_option == "1":
    print("Ha elejido '1) Crear tablero'")
    print("CREAR TABLA")
    width = int(input("Establezca el ancho del tablero: "))
    height = int(input("Establezca la altura del tablero: "))
    inst_controller = Controller(width, height)

    while inst_controller.add_cell():
      pass

    inst_controller.generate_graph()

  elif selected_option == "2":
    print("\n")
    print("+------------------------------+")
    print("| 202208521                    |")
    print("| Luis Rodrigo Morales Florián |")
    print("| IPC2                         |")
    print("| Sección C                    |")
    print("+------------------------------+")
    print("\n")
  elif selected_option == "3":
    print("\n")
    print("Ha salido de la aplicación")
    break