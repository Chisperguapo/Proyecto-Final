class Carro: # Inicialización de la clase carro.
    def __init__(self, request): # Metodo constructor que inicializa la clase.
        self.request=request # Creamos un atributo y le asignamos como contenido el objeto request
        self.session=request.session # Se accede al atributo session del objeto request para mantener el contenido así se cierre sesion.
        carro=self.session.get("carro") # Se intenta obtener el valor asociado con la clave carro del objecto session, si no hay valor asociado se le asignara none a la variable 'carro'

        if not carro: # Se verifica si el carro tiene un valor falso(None)
            carro=self.session["carro"]={} # Si es falso, se le agrega un diccionario vacío a 'carro' en el objeto session. 
        self.carro=carro # Se asigna el contenido de 'carro' al atributo 'carro' de la instancia Carro.

    def guardar_carro(self): # Definimos una función para guardar los cambios del carro.
        self.session["carro"]=self.carro # Se asigna el contenido del atributo 'carro' de la instancia al valor asociado con la clave 'carro' en el objeto session, es decir, que se traera la información que este almacenada en la clave 'carro' en la session activa.
        self.session.modified=True # Indicamos 'True' para indicar que el objeto 'session' ha sido modificado.

    def agregar(self, producto, precio):
        producto_id = str(producto.id)
        if producto_id not in self.carro.keys():
            self.carro[producto.id] = {
                'producto_id': producto.id,
                'producto': producto.nombre,
                'precio_unitario': precio, 
                'cantidad': 1,
                'precio_total': precio,
                'imagen': producto.imagen.url
            }
        else:
            self.carro[producto_id]["cantidad"] += 1
        self.guardar_carro()

    def sumar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            self.carro[producto_id]["cantidad"]+=1
        self.guardar_carro()

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro :
            self.carro[producto_id]["cantidad"] -= 1
            if self.carro[producto_id]["cantidad"] < 1:
                self.eliminar(producto)
        self.guardar_carro()

    def limpiar(self):
        self.session["carro"]={}
        self.session.modified=True