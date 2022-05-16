import streamlit as st
from streamlit_option_menu import option_menu

from controller.Controlador import EvaluadorController
from view.Inicio import mesaje_inicio_asistente, mesaje_inicio_jurados, mesaje_inicio_directora
from view.EvalTrabajoGrado import agregar_acta, agregar_evaluacion
from view.ListaActa import listar_actas
from view.EditarCriterios import base
from view.ExportarActa import elegir_acta_imprimir

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
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Actas de Grado", page_icon='', layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        # self.col1, self.col2, self.col3 = st.columns([1, 6, 1])

        # Define lo que abrá en la barra de menu
        self.menu_actual = option_menu(None, ["Asistente", 'Jurados', 'Directora'],
                                       icons=['person', 'people', 'file-person'],
                                       menu_icon="cast", default_index=0, orientation="horizontal",
                                       styles={
                                           "container": {"padding": "0!important", "background-color": "#fafafa"},
                                           "icon": {"color": "#000000", "font-size": "25px"},
                                           "nav-link": {"color": "#000000", "font-size": "25px", "text-align": "left",
                                                        "margin": "0px", "--hover-color": "#FFFFFF"},
                                           "nav-link-selected": {"background-color": "#2C6394", "color": "white"}, })

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
                self.menu_actual = option_menu('Menu', ["Directora", 'Modificar Criterios', 'Ver Historicos',
                                                        'Editar Criterios'],
                                               icons=["cast", 'vector-pen', 'stack-overflow'],
                                               menu_icon="display", default_index=0,
                                               styles={"nav-link-selected": {"background-color": "#2C6394"}, })

            if self.menu_actual == "Directora":
                mesaje_inicio_directora(st)
            elif self.menu_actual == "Ver Historicos":
                listar_actas(st, self.controller)
            elif self.menu_actual == "Editar Criterios":
                base(st)

# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
