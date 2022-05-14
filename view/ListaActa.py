from view.EvalTrabajoGrado import agregar_acta

def listar_actas(st, controller):
    #Itera los elementos de evaluacion agregados y los muestra

    st.title("Datos guardados:")
        #No sirve listar, intente recorrer el diccionario actas pero no quiere servir
    for id in controller.actas:                                #Ni con el metodo que mostro la profesora sirve, no se como cambiar eso
        with st.container():
            acta = controller.actas[id]
            st.write("Acta #", acta.numero)
            st.write(acta.fecha)
            st.write(acta.autor)
            st.write(acta.tipo_de_trabajo)
            st.write(acta.directora)
            st.write(acta.codirector)
            st.write(acta.jurado1)
            st.write(acta.jurado2)
            for clave in acta.criterio:
                with st.container():
                    crit = acta.criterio[clave]
                    st.write(crit.descripcion)
                    st.write(crit.observacion)
                    st.write(crit.nota1)
                    st.write(crit.nota2)
                    st.write(crit.ponderado)


