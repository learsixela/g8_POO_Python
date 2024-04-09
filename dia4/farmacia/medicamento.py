class Medicamento():
    IVA = 0.18

    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_final = 0.0
        self.descuento = 0.0

    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    #metodo get
    @property
    def precio(self):
        return self.precio_final
    
    @precio.setter
    def precio(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            self.precio_final = precio_bruto + precio_bruto * self.IVA
        
            if self.precio_final >= 10000 and self.precio_final < 20000:
                self.descuento = 0.1
            elif self.precio_final >= 20000:
                self.descuento = 0.2

            #ojo revisar
            if self.descuento:
                self.precio_final *= 1 - self.descuento

        else:
            print("El valor debe ser mayor cero")

    # Este es el método que se debe agregar
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()
    
    def __iadd__(self, other):
        if self == other:#se dirige al metodo __eq__
            self.stock += other.stock
        return self
    
    def __str__(self):
        print("METODO __str___")
        return f"NOMBRE:{self.nombre}\nSTOCK: {self.stock}\nPRECIO:{self.precio_final} "