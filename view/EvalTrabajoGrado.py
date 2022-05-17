from model.Acta import Acta
from model.Criterio import Criterio
import json

"Se encarga de leer los datos dentro del Json que almacena cada uno de los criterios que hay hasta el momento"
file = open("model\ListaCriterios.json", "r")
js = file.read()
lista_criterios = json.loads(js)

"Funcion encargada de crear a"
def agregar_acta(st, controller):
    col1, col2, col3 = st.columns(3)

    acta_obj = Acta()

    with col1:
        acta_obj.numero = st.number_input("Id acta")
        acta_obj.nombre_del_trabajo = st.text_input("Titulo del trabajo")
        acta_obj.fecha = st.date_input("Fecha de creacion del trabajo")
    with col2:
        acta_obj.autor = st.text_input("Nombre estudiante")
        acta_obj.tipo_de_trabajo = st.selectbox('¿Tipo de trabajo?', ["Aplicado", "investigacion"])
        acta_obj.directora = st.text_input("Nombre Directora")
    with col3:
        acta_obj.codirector = st.text_input("Nombre Co-director", "N/A")
        acta_obj.jurado1 = st.text_input("Nombre Primer Jurado")
        acta_obj.jurado2 = st.text_input("Nombre Segundo Jurado")
    try:
        for llave in controller.actas:
            if (controller.actas[llave].numero == acta_obj.numero):
                raise ValueError("ID del acta repetido")
        enviado_btn = st.button("Enviar")
        if enviado_btn:
            controller.agregar_acta(acta_obj)
            st.write("El archivo se ha creado exitosamente")
        return controller
    except Exception as error:
        st.error(error)


def agregar_evaluacion(st, controller):
    contador = 0
    actas_llaves = controller.actas.keys()
    acta_evaluar = st.selectbox("¿Que acta vas a calificar?", actas_llaves)  # Asi encuentro todas las llaves del directorio acta
    nota = 0
    criterios_temp = {}
    #llave = st.selectbox('Criterio a evaluar?', lista_criterios)
    for clave in lista_criterios:
        criterio_obj = Criterio()
        st.title(clave)
        criterio_obj.descripcion = str(clave)
        criterio_obj.observacion = st.text_input("Observaciones adicionales", key = contador )
        contador += 1
        criterio_obj.nota1 = st.number_input("Nota primer jurado", key = contador)
        contador += 1                            #aqui lleno los objetos de la clase criterio
        criterio_obj.nota2 = st.number_input("Nota segundo jurado", key = contador)
        contador += 1
        criterio_obj.ponderado = lista_criterios[clave]
        st.write("El ponderado es de: ", criterio_obj.ponderado) #pon el ponderado automaticamente de lista_criterios si puedes y vuelve a poner los ponderados en el jsonxD
        criterios_temp[criterio_obj.descripcion] = criterio_obj
        nota += ( ( (criterio_obj.nota1 + criterio_obj.nota2) / 2 ) * criterio_obj.ponderado )

    enviado_btn = st.button("Enviar")
    if enviado_btn:
        controller.actas[acta_evaluar].agregar_criterio(criterios_temp)     #aqui estoy metiendo los objetos de criterio
        controller.actas[acta_evaluar].agregar_nota_definitiva(nota)
        st.write("El archivo se ha creado exitosamente")                                                           #al diccionario criterio que tengo en acta que elegi

    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal