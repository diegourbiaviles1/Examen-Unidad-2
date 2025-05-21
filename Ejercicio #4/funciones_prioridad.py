class PriorityQueue:
    """Cola de prioridad con prioridades enteras (menor valor => mayor prioridad)."""
    def __init__(self):
        self._items = []

    def is_empty(self) -> bool:
        """Devuelve True si la cola está vacía."""
        return not self._items

    def enqueue(self, item: str, priority: int) -> None:
        """
        Agrega un elemento con su prioridad.
        priority: entero, menor = mayor prioridad.
        """
        # Insertar y mantener orden por prioridad ascendente
        self._items.append((priority, item))
        self._items.sort(key=lambda x: x[0])

    def dequeue(self) -> tuple:
        """
        Elimina y devuelve el elemento con mayor prioridad (menor valor numérico).
        Lanza IndexError si está vacía.
        Devuelve: (item, priority)
        """
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")
        pr, itm = self._items.pop(0)
        return itm, pr

    def peek(self) -> tuple:
        """
        Devuelve el próximo elemento sin extraerlo.
        Si está vacía, devuelve None.
        """
        if self.is_empty():
            return None
        pr, itm = self._items[0]
        return itm, pr

    def __len__(self) -> int:
        """Número de elementos en la cola."""
        return len(self._items)
