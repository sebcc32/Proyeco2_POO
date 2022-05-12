from model.Acta import Acta

def agregar_acta(st, controller):
    # Objecto que modelará el formulario
    acta_obj = Acta()
    acta_obj.numero = st.number_input("Id acta")
    acta_obj.nombre_del_trabajo = st.text_input("Titulo del trabajo")
    acta_obj.fecha = st.date_input("Fecha de creacion del trabajo")
    acta_obj.autor = st.text_input("Nombre estudiante")
    acta_obj.tipo_de_trabajo = st.selectbox('¿Tipo de trabajo?', ["Aplicado", "investigacion"])
    acta_obj.directora = st.text_input("Nombre Directora")
    acta_obj.codirector = st.text_input("Nombre Co-director")
    st.write("Si no hay codirector poner: N/A")
    acta_obj.jurado1 = st.text_input("Nombre Primer Jurado")
    acta_obj.jurado2 = st.text_input("Nombre Segundo Jurado")
    enviado_btn = st.button("Enviar")
    if enviado_btn:
        controller.agregar_acta(acta_obj)
        st.write("El archivo se ha creado exitosamente")
    return controller