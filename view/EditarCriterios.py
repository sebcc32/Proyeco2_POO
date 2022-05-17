import json

file = open("model\ListaCriterios.json", "r")
js = file.read()
lista_criterios = json.loads(js)
file.close()

def editar_criterios(st):

    with st.expander("Editar criterio"):
        old_key = st.selectbox('Criterio a evaluar?', lista_criterios)
        st.write("")
        new_key = st.text_input("Editar criterio")
        ponderado = st.number_input("Nuevo ponderado")
        if st.button("Guardar"):
            lista_criterios[new_key] = lista_criterios[old_key]
            lista_criterios[new_key] = ponderado
            del lista_criterios[old_key]
            st.success("El criterio se modifico correctamente")

    with st.expander("Eliminar criterio"):
        old_key = st.selectbox('Criterio a evaluar?', lista_criterios, key = 0)
        if st.button("Guardar", key = 0):
            del lista_criterios[old_key]
            st.success("El criterio se modifico correctamente")

    with st.expander("Añadir criterio"):
        criterio_nuevo = st.text_input("Nuevo criterio")
        ponderado_nuevo = st.number_input("Ponderado del criterio")
        if st.button("Guardar", key = 1):
            lista_criterios[criterio_nuevo] = ponderado_nuevo
            st.success("El criterio se modifico correctamente")

    file = open("model\ListaCriterios.json", "w")
    criterios = json.dumps(lista_criterios, indent=4)
    file.write(criterios)
    file.close()
