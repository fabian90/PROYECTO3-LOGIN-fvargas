# from Implementation.ingredientesAnterior import Base, Complemento
# from Implementation.productosAnterior import Copa, Malteada
# from Implementation.heladeriaAnterior import Heladeria
# from funciones import es_sano, contar_calorias, calcular_costo, calcular_rentabilidad, producto_mas_rentable

# def prueba() -> None:
#     # Ingredientes
#     helado_fresa = Base("Helado de Fresa", 1200, 150, 10, False, "Fresa")
#     chispas_chocolate = Complemento("Chispas de chocolate", 500, 200, 5, False)
#     mani_japones = Complemento("Mani Japonés", 900, 300, 7, False)

#     # Productos
#     copa_fresa = Copa("Copa de Fresa", 7500, [helado_fresa, chispas_chocolate, mani_japones], "Grande")
#     malteada_choco = Malteada("Malteada Choco", 8500, [helado_fresa, chispas_chocolate, mani_japones], 16)

#     # Heladería
#     heladeria = Heladeria()
#     heladeria.agregar_producto(copa_fresa)
#     heladeria.agregar_producto(malteada_choco)

#     # Pruebas adicionales

#     # Prueba función es_sano
#     print("Es sano: "+ str(es_sano(90, False)))  # Output: True
#     print("Es sano: "+str(es_sano(150, True)))  # Output: True
#     print("Es sano: "+str(es_sano(150, False)))  # Output: False

#     # Prueba función contar_calorias
#     print("Calorias: "+ str( contar_calorias([150, 200, 300])))  # Output: 617.50

#     # Prueba función calcular_costo
#     ingrediente1 = {"nombre": "Helado de Fresa", "precio": 1200}
#     ingrediente2 = {"nombre": "Chispas de chocolate", "precio": 500}
#     ingrediente3 = {"nombre": "Mani Japonés", "precio": 900}
#     print("Calcular costo: "+ str(calcular_costo(ingrediente1, ingrediente2, ingrediente3)))  # Output: 2600

#     # Prueba función calcular_rentabilidad
#     precio_venta = 7500
#     print("Calcular rentabilidad: "+ str(calcular_rentabilidad(precio_venta, ingrediente1, ingrediente2, ingrediente3)))  # Output: 4900

#     # Prueba función producto_mas_rentable
#     producto1 = {"nombre": "Samurai de fresas", "rentabilidad": 4900}
#     producto2 = {"nombre": "Samurai de mandarinas", "rentabilidad": 2500}
#     producto3 = {"nombre": "Malteada chocoespacial", "rentabilidad": 11000}
#     producto4 = {"nombre": "Cupihelado", "rentabilidad": 3200}
#     print("productos mas rentable: "+ str(producto_mas_rentable(producto1, producto2, producto3, producto4)))  # Output: "Malteada chocoespacial"

#     # Prueba método producto_mas_rentable de Heladeria
#     producto_rentable = heladeria.producto_mas_rentable()
#     if producto_rentable:
#         print(producto_rentable.nombre)  # Output: "Malteada Choco"

#     # Prueba método vender_producto
#     heladeria.vender_producto("Copa de Fresa1")
#     heladeria.vender_producto("Copa de Fresa")
#     heladeria.vender_producto("Copa de Fresa")
#     heladeria.vender_producto("Copa de Fresa")
#     print("Inventario Helado de Fresa: " + str(helado_fresa.inventario))  # Output: 9

# if __name__ == "__main__":
#     prueba()