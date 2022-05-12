import streamlit as st
from streamlit_option_menu import option_menu


class MainView:
    def __init__(self) -> None:
        super().__init__()

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
                                           "icon": {"color": "#c4c4c4", "font-size": "25px"},
                                           "nav-link": {"color": "#c4c4c4", "font-size": "25px", "text-align": "left",
                                                        "margin": "0px", "--hover-color": "#6689ff"},
                                           "nav-link-selected": {"background-color": "#0b4bff", "color": "white"}, })

    def controlar_menu(self):
        if self.menu_actual == "Asistente":
            with st.sidebar:
                self.menu_actual = option_menu("Menu", ["Asistente", 'Crear Acta', 'Ver Historicos'],
                                               icons=["person", 'mortarboard', 'stack-overflow'],
                                               menu_icon="display", default_index=0,
                                               styles={"nav-link-selected": {"background-color": "#0b4bff"}, })

        elif self.menu_actual == "Jurados":
            with st.sidebar:
                self.menu_actual = option_menu('Menu', ["Jurados", 'Exportar Acta', 'Evaluar Trabajo'],
                                               icons=["briefcase", 'file-pdf', 'pencil-square'],
                                               menu_icon="display", default_index=0,
                                               styles={"nav-link-selected": {"background-color": "#0b4bff"}, })

        elif self.menu_actual == "Directora":
            with st.sidebar:
                self.menu_actual = option_menu('Menu', ["Directora", 'Modificar Criterios', 'Ver Historicos',
                                                        'Editar Criterios'],
                                               icons=["cast", 'vector-pen', 'stack-overflow'],
                                               menu_icon="display", default_index=0,
                                               styles={"nav-link-selected": {"background-color": "#0b4bff"}, })



# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()
