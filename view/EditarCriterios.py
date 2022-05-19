import json

"Se encarga de leer los datos dentro del Json que almacena cada uno de los criterios que hay hasta el momento"
file = open("model\ListaCriterios.json", "r")
js = file.read()
lista_criterios = json.loads(js)
file.close()

"Suma todos los ponderadoes de cada criterio y manda la suma de esto para ser revizado al agregar y editar criterios"
def revisar_criterios():
    suma = 0
    for llave in lista_criterios:
        suma+=lista_criterios[llave]
    return suma

"Funcion que se encarga de eliminar, crear y editar los criterios"
def editar_criterios(st):

    with st.expander("Editar criterio"):
        old_key = st.selectbox('Criterio a evaluar?', lista_criterios)
        st.write("")
        new_key = st.text_input("Editar criterio")
        ponderado = st.number_input("Nuevo ponderado")
        if st.button("Guardar"):
            lista_criterios[new_key] = lista_criterios[old_key]
            del lista_criterios[old_key]
            if revisar_criterios() + ponderado <= 1:
                lista_criterios[new_key] = ponderado
                st.success("El criterio se modifico correctamente")
            else:
                ponderado = 1 - revisar_criterios()
                lista_criterios[new_key] = ponderado
                st.info("El criterio se modifico correctamente, pero el poderado fue mas grande de lo esperado. Por lo cual se le agrego un ponderado que cumpliera con los requisitos del sistema")

    with st.expander("Eliminar criterio"):
        old_key = st.selectbox('Criterio a evaluar?', lista_criterios, key = 0)
        if st.button("Guardar", key = 0):
            del lista_criterios[old_key]
            st.success("El criterio se modifico correctamente")

    with st.expander("Añadir criterio"):
        criterio_nuevo = st.text_input("Nuevo criterio")
        ponderado_nuevo = st.number_input("Ponderado del criterio")
        if st.button("Guardar", key = 1):
            if revisar_criterios() + ponderado_nuevo <= 1:
                lista_criterios[criterio_nuevo] = ponderado_nuevo
                st.success("El criterio se creo correctamente")
            else:
                if revisar_criterios()<0.99:
                    ponderado_nuevo = 1 - revisar_criterios()
                    lista_criterios[criterio_nuevo] = ponderado_nuevo
                    st.info("El criterio se creo correctamente, pero el poderado fue mas grande de lo esperado. Por lo cual se le agrego un ponderado que cumpliera con los requisitos del sistema.")
                else:
                    st.error("Oh no! Tiene todos los criterios posible, la suma de los ponderados de cada criterio ya esta en un 100%. Si desea agregar uno nuevo, edite los ponderados para dejar un espacio a su nuevo criterio.")


    "Se encarga de escribir los nuevos datos dentro del Json en el cual se guardan los criterios"
    file = open("model\ListaCriterios.json", "w")
    criterios = json.dumps(lista_criterios, indent=4)
    file.write(criterios)
    file.close()
