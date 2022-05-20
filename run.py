from streamlit import bootstrap
from streamlit import set_page_config

real_script = 'view/MainView.py'

"Se establece el nombre e icono de la pestaña de la pagina"
set_page_config(page_title="Actas de Grado", page_icon='🎓', layout="wide",
                           initial_sidebar_state="expanded")

bootstrap.run(real_script, f'run.py {real_script}', [], {})
