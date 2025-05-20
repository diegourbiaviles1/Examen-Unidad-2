class Cancion:
    """
    Clase que representa una cancion en la lista de reproduccion.
    Tiene nombre y enlaces al siguiente y anterior nodo (lista doblemente enlazada).
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return self.nombre


class ListaReproduccion:
    """
    Clase que simula una lista de reproduccion de musica.
    Permite recorrer hacia adelante o atras, agregar y eliminar canciones.
    """
    def __init__(self):
        self.primera = None
        self.actual = None

    def agregar_cancion(self, nombre):
        """
        Agrega una cancion al final de la lista.
        """
        nueva = Cancion(nombre)
        if self.primera is None:
            self.primera = nueva
            self.actual = nueva
        else:
            temp = self.primera
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp
        print(f"-> Cancion '{nombre}' agregada a la lista.")

    def eliminar_cancion_actual(self):
        """
        Elimina la cancion que esta siendo reproducida.
        """
        if self.actual is None:
            print("-> No hay cancion para eliminar.")
            return

        nombre = self.actual.nombre
        anterior = self.actual.anterior
        siguiente = self.actual.siguiente

        # Reconectar nodos
        if anterior:
            anterior.siguiente = siguiente
        else:
            self.primera = siguiente

        if siguiente:
            siguiente.anterior = anterior

        # Mover el puntero actual
        self.actual = siguiente if siguiente else anterior
        print(f"-> Cancion '{nombre}' eliminada.")

    def siguiente_cancion(self):
        """
        Mueve el puntero a la siguiente cancion si existe.
        """
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"-> Reproduciendo: {self.actual.nombre}")
        else:
            print("-> No hay siguiente cancion.")

    def anterior_cancion(self):
        """
        Mueve el puntero a la cancion anterior si existe.
        """
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"-> Reproduciendo: {self.actual.nombre}")
        else:
            print("-> No hay cancion anterior.")

    def mostrar_lista(self):
        """
        Muestra toda la lista de canciones, marcando la que esta en reproduccion.
        """
        if self.primera is None:
            print("-> Lista de reproduccion vacia.")
            return

        print("Lista de reproduccion:")
        temp = self.primera
        while temp:
            if temp == self.actual:
                print(f"-> {temp.nombre} [REPRODUCIENDO]")
            else:
                print(f"   {temp.nombre}")
            temp = temp.siguiente
