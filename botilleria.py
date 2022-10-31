##Clase
class product
{
##Atributos
  name = "" ##Nombre del producto
  stock = "" ##Cantidad del producto
  category = "" ##Categoría
  brand = "" ##Marca del producto
  description = "" ##Descripción breve
  barcode = "" ##Código de barras
  prov_price = "" ##Precio de compra al proveedor
  price = "" ##Precio de venta al consumidor
  alcohol_percentage = "" ##Porcentaje de Alcohol
  volume = "" ##Volumen en litros
  weight = "" ##En caso de vender otro tipo de producto, en gramos
  expiration_date = "" ##Fecha de caducidad
  critical_stock = "" ##Stock crítico para volver a adquirir el producto
  drinkable = "" ##Booleano para clasificar productos bebestibles de los demás
}
##Métodos
{
  critical_warning() ##Avisa cuando un producto se encuentra en stock crítico
  expiration_warning() ##Avisa cuando un producto se acerca a su fecha de caducidad
  show_data() ##Mostrar los datos en pantalla
  update_stock() ##Actualizar el stock al adquirir productos al proveedor
  update_prov_price() ##Actualizar precio de compra
  update_price() ##Actualizar precio de venta
  apply_discount() ##Aplicar descuento a los productos que lo requieran
}



