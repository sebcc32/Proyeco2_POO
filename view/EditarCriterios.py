import json

file = open("model\ListaCriterios.json", "r")
js = file.read()
lista_criterios = json.loads(js)

def base(st):
    index = st.selectbox('Criterio a evaluar?', lista_criterios)
    col1, col2 = st.columns(1)
    with col1:
        edit = st.button("Editar")
    with col2:
        delete = st.button("Eliminar")
    if edit:
        pass #Tocara editar le Json, hay varias cosas que se requiere editar en esta opcion, pero como esta el Json no es posible

