""""
    Aqui se encuentran los menus de cada tipo de usuario
    y una descripcion de lo que pueden hacer en el sistema.
"""


def mesaje_inicio_asistente(st):
    st.title("Bienvenido Asistente")
    st.write("Usted sera el encargado de crear las nuevas actas de grado las")
    st.write("cuales van a ser calificadas una por una por los Jurados.")
    st.write("Usted tambien contara con acceso al historico en donde encontrara todas las")
    st.write("actas de grado que se han guardado en el sistema.")


def mesaje_inicio_jurados(st):
    st.title("Bienvenidos Jurados")
    st.write("Ustedes seran los encargados de calificar las actas de grado")
    st.write("en las cuales se le deberan colocar sus dos notas y tambien")
    st.write("un comentario a cada criterio.")
    st.write("Tambien tendran la posibilidad de exportar esta evaluacion")
    st.write("en formato PDF.")

def mesaje_inicio_directora(st):
    st.title("Bienvenido Director")
    st.write("Usted tendra acceso al historico de actas guardadas en el sistema y")
    st.write("tambien podra editar los criterios dentro del sistema, por ejemplo,")
    st.write("podra cambiar el ponderado de estos, editar el texto, eliminar criterios")
    st.write("y agregar nuevos.")

