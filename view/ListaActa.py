
def listar_actas(st, controller):
    #Itera los elementos de evaluacion agregados y los muestra

    st.title("Datos guardados:")
        #No sirve listar, intente recorrer el diccionario actas pero no quiere servir
    for id in controller.actas:                                #Ni con el metodo que mostro la profesora sirve, no se como cambiar eso
        with st.container():
            acta = controller.actas[id]
            with st.expander(f"Acta # {acta.numero}"):
                st.write("Fecha: ", str(acta.fecha))
                st.write("Autor: ", acta.autor)
                st.write("Tipo de trabajo: ", acta.tipo_de_trabajo)
                st.write("Directora: ", acta.directora)
                st.write("Co-director: ", acta.codirector)
                st.write("Jurado 1: ", acta.jurado1)
                st.write("Jurado 2: ", acta.jurado2)
                for clave in acta.criterio:
                    with st.container():
                        crit = acta.criterio[clave]
                        st.write("Descripcion: ", crit.descripcion)
                        st.write("Observaciones: ", crit.observacion)
                        st.write("Nota 1: ", str(crit.nota1))
                        st.write("Nota 2: ", str(crit.nota2))
                        st.write("Ponderado: ", str(crit.ponderado))
                st.write("Nota Final: ", acta.nota)
