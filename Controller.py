from LinkedList import LinkedList
import graphviz
import datetime

class _Cell:
    def __init__(self, row: int, column: int, info: str) -> None:
        self.row = row
        self.column = column
        self.info = info


class Controller:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.cells = LinkedList()

    def add_cell(self):
        print("\n")
        if self.cells.get_length() == (self.width * self.height):
            print("El tablero ya está lleno")
            return None
        
        color_letters = ("A","R","V","P","N")

        print("% NUEVO NODO:")
        print("Escriba la letra que quiere almacenar en la celda: ")
        for col in color_letters:
            print(f"- {col}")

        info = input()
        if not info in color_letters:
            print("ERROR: El valor ingresado no está entre las opciones proporcionadas")
            return True

        print("Ingresa la fila: ")
        print(f"Rango: 1-{self.height}")
        row = int(input())

        if row < 1 or row > self.height:
            print("ERROR: La fila establecida está fuera del rango")
            return True
        
        print("Ingresa la columna: ")
        print(f"Rango: 1-{self.width}")
        column = int(input())

        if column < 1 or column > self.width:
            print("ERROR: La columna establecida está fuera del rango")
            return True
        
        if self.get_cell_by_row_and_col(row, column):
            print("ERROR: Esa celda ya ha sido tomada")
            return True
        else:
            self.cells.append(_Cell(row, column, info))
            print("Pieza guardada con éxito")
            print("\n")

            # Método: imprimir tabla
            for h in range(self.height):
                new_row = ""
                for w in range(self.width):
                    new_row += f"| {self.get_cell_by_row_and_col(h+1,w+1).data.info if self.get_cell_by_row_and_col(h+1,w+1) else ' '} {'|' if w == (self.width-1) else ''}"

                print(new_row)
            return True
        

    def get_cell_by_row_and_col(self, row: int, column: int):
        counter = 1
        while self.cells.get_elem_by_position(counter):
            if self.cells.get_elem_by_position(counter).data.row == row and self.cells.get_elem_by_position(counter).data.column == column:
                return self.cells.get_elem_by_position(counter)
            
            counter += 1
        
        return None
    
    def generate_graph(self):
        dot = graphviz.Digraph()
        alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        
        dot.node("A1", "Coloréalo Guatematel")
        for h in range(self.height + 1):
            for w in range(self.width + 1):
                new_node_name = alphabet[h+1] + str(w+1)
                prev_node_name = alphabet[h] + str(w+1)
                if h == 0:
                    dot.node(new_node_name, str(w))
                    dot.edge("A1", new_node_name)
                elif w == 0:
                    dot.node(new_node_name, str(h))
                    dot.edge(prev_node_name, new_node_name)
                else:
                    dot.node(new_node_name, label=" ", style="filled" ,fillcolor=self.get_color_by_letter(self.get_cell_by_row_and_col(h,w).data.info))
                    dot.edge(prev_node_name, new_node_name)

        new_name = "grafica_"+ datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        dot.render(new_name, view=True)
                    
    def get_color_by_letter(self, letter: str):
        if letter == "A":
            return "#0abde3"
        elif letter == "R":
            return "#ff6b6b"
        elif letter == "V":
            return "#1dd1a1"
        elif letter == "P":
            return "#5f27cd"
        elif letter == "N":
            return "#ff9f43"
        