"Funcion que se encarga de itera los elementos de evaluacion agregados para mostrarlos"
def listar_actas(st, controller):
    st.title("Datos guardados:")
    for id in controller.actas:
        with st.container():
            acta = controller.actas[id]
            "Crea un expander para cada una de las actas basandose en el ID del acta"
            with st.expander(f"Acta # {acta.numero}"):
                st.write("Fecha: ", str(acta.fecha))
                st.write("Autor: ", acta.autor)
                st.write("Tipo de trabajo: ", acta.tipo_de_trabajo)
                st.write("Directora: ", acta.directora)
                st.write("Co-director: ", acta.codirector)
                st.write("Jurado 1: ", acta.jurado1)
                st.write("Jurado 2: ", acta.jurado2)
                "Recorre los criterios evaluados en el acta para mostrarlos con su information adicional"
                for clave in acta.criterio:
                    with st.container():
                        crit = acta.criterio[clave]
                        st.write("Descripcion: ", crit.descripcion)
                        st.write("Observaciones: ", crit.observacion)
                        st.write("Nota 1: ", str(crit.nota1))
                        st.write("Nota 2: ", str(crit.nota2))
                        st.write("Ponderado: ", str(crit.ponderado))
                st.write("Nota Final: ", acta.nota)
