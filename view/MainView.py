import streamlit as st
from streamlit_option_menu import option_menu

from controller.Controlador import EvaluadorController
from view.Inicio import mesaje_inicio_asistente, mesaje_inicio_jurados, mesaje_inicio_directora
from view.EvalTrabajoGrado import agregar_acta, agregar_evaluacion
from view.ListaActa import listar_actas
from view.EditarCriterios import editar_criterios
from view.ExportarActa import elegir_acta_imprimir


# "Clase del main view"

class MainView:

    def __init__(self) -> None:
        super().__init__()

        if 'main_view' not in st.session_state:
            self.controller = EvaluadorController()
            st.session_state['main_view'] = self
        else:
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller

        self._dibujar_layout()

    def _dibujar_layout(self):

        """
        Se establece el menu principal para elegir a los usuarios
        """
        self.menu_actual = option_menu(None, ["Asistente", 'Jurados', 'Directora'],
                                       icons=['person', 'people', 'file-person'],
                                       menu_icon="cast", default_index=0, orientation="horizontal",
                                       styles={
                                           "container": {"padding": "0!important", "background-color": "#fafafa"},
                                           "icon": {"color": "#000000", "font-size": "25px"},
                                           "nav-link": {"color": "#000000", "font-size": "25px", "text-align": "left",
                                                        "margin": "0px", "--hover-color": "#FFFFFF"},
                                           "nav-link-selected": {"background-color": "#2C6394", "color": "white"}, })

    "Funcion encargada del menu, en la cual muestra cada menu de cada usuario y redirige al usuario a su menu designado "
    def controlar_menu(self):
        if self.menu_actual == "Asistente":
            with st.sidebar:
                self.menu_actual = option_menu("Menu", ["Asistente", 'Crear Acta', 'Ver Historicos'],
                                               icons=["person", 'mortarboard', 'stack-overflow'],
                                               menu_icon="display", default_index=0,
                                               styles={"nav-link-selected": {"background-color": "#2C6394"}, })

            if self.menu_actual == "Asistente":
                mesaje_inicio_asistente(st)
            elif self.menu_actual == "Crear Acta":
                agregar_acta(st, self.controller)
            elif self.menu_actual == "Ver Historicos":
                listar_actas(st, self.controller)

        elif self.menu_actual == "Jurados":
            with st.sidebar:
                self.menu_actual = option_menu('Menu', ["Jurados", 'Evaluar Trabajo', 'Exportar Acta'],
                                               icons=["briefcase", 'file-pdf', 'pencil-square'],
                                               menu_icon="display", default_index=0,
                                               styles={"nav-link-selected": {"background-color": "#2C6394"}, })

            if self.menu_actual == "Jurados":
                mesaje_inicio_jurados(st)
            elif self.menu_actual == "Evaluar Trabajo":
                agregar_evaluacion(st, self.controller)
            elif self.menu_actual == "Exportar Acta":
                elegir_acta_imprimir(st, self.controller)

        elif self.menu_actual == "Directora":
            with st.sidebar:
                self.menu_actual = option_menu('Menu', ["Directora", 'Modificar Criterios', 'Ver Historicos'],
                                               icons=["cast", 'vector-pen', 'stack-overflow'],
                                               menu_icon="display", default_index=0,
                                               styles={"nav-link-selected": {"background-color": "#2C6394"}, })

            if self.menu_actual == "Directora":
                mesaje_inicio_directora(st)
            elif self.menu_actual == "Ver Historicos":
                listar_actas(st, self.controller)
            elif self.menu_actual == "Modificar Criterios":
                editar_criterios(st)

# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
