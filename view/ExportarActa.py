from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

"Funcion encargada de crear el PDF del acta requerida"
def crear_pdf(acta):
    archivo = canvas.Canvas("form.pdf", pagesize=letter)
    archivo.setLineWidth(.3)

    archivo.setFont('Helvetica-Bold', 13)
    archivo.drawString(222,745,'FACULTAD DE INGENIERIA')
    archivo.drawString(224, 725, 'MAESTRIA EN INGENIERIA')

    archivo.setFont('Helvetica', 12)
    archivo.drawString(30, 660, f'Nombre del trabajo: {acta.nombre_del_trabajo}')
    archivo.drawString(30, 640, f'Autor: {acta.autor}')
    archivo.drawString(30, 620, f'Tipo de trabajo: {acta.tipo_de_trabajo}')
    archivo.drawString(30, 600, f'Director: {acta.directora}')
    archivo.drawString(30, 580, f'Co-Director: {acta.codirector}')
    archivo.drawString(30, 560, f'Jurado 1: {acta.jurado1}')
    archivo.drawString(30, 540, f'Jurado 2: {acta.jurado2}')
    archivo.drawString(30, 500, 'En atencion al desarrollo de este Trabajo de Grado y al documento y sustentacion que presento el/la')
    archivo.drawString(30, 480, 'autor(a), los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios')
    archivo.drawString(30, 460, 'a evaluar y sus ponderaciones se estipulan en el articulo 7.1 de las Directrices para Trabajo de')
    archivo.drawString(30, 440, 'Grado de Maestria):')

    archivo.setFont('Helvetica-Bold', 12)
    archivo.drawString(170, 680, 'ACTA DE EVALUACION DE TRABAJO DE GRADO')
    archivo.drawString(30, 700, f'ACTA: {acta.numero}')
    archivo.drawString(450, 700, f'FECHA: {acta.fecha}')
    archivo.drawImage("https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png", 20, 720, 170, 60)

    "Proceso encargado de agregar cada criterio con su informacion agregada por los jueces"
    identificador = 1
    y = 400
    for clave in acta.criterio:
        crit = acta.criterio[clave]

        archivo.setFont('Helvetica-Bold', 12)
        archivo.drawString(30, y, f'{identificador}. {crit.descripcion}')
        identificador += 1
        archivo.setFont('Helvetica', 12)
        nota_parcial = ( (crit.nota1 + crit.nota2) / 2 )
        y-=20
        archivo.drawString(30, y, f'Nota parcial: {nota_parcial}')
        archivo.drawString(450, y, f'Ponderado: {crit.ponderado * 100}%')
        y-=20
        archivo.drawString(30, y, f'Observaciones: {crit.observacion}')
        y -= 20
        archivo.line(30, y, 580, y)
        y -= 20
        archivo.line(30, y, 580, y)
        y -= 20
        if( y <= 0 ):
            y = 660
            archivo.showPage()
            archivo.setFont('Helvetica-Bold', 12)
            archivo.drawString(170, 680, 'ACTA DE EVALUACION DE TRABAJO DE GRADO')
            archivo.drawString(30, 700, f'ACTA: {acta.numero}')
            archivo.drawString(450, 700, f'FECHA: {acta.fecha}')
            archivo.drawImage("https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png", 20, 720, 170, 60)

    "Verifica que el Y en el PDF al terminar la anterior secuencia no este fuera de la distacia requerida para asi crear o no una nueva pagina"
    if (y <= 0):
        y = 660
        archivo.showPage()
        archivo.setFont('Helvetica-Bold', 12)
        archivo.drawString(170, 680, 'ACTA DE EVALUACION DE TRABAJO DE GRADO')
        archivo.drawString(30, 700, f'ACTA: {acta.numero}')
        archivo.drawString(450, 700, f'FECHA: {acta.fecha}')
        archivo.drawImage("https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png", 20, 720, 170, 60)
        archivo.drawString(30, y, f'Como resultado de estas calificaciones parciales y sus ponderciones, la calificacion del trabajo')
        archivo.drawString(30, y-20, f'de grado es: {acta.nota}')
        archivo.drawString(30, y-40, 'Observaciones adicionales: ')
        archivo.line(30, y-60, 580, y-60)
        archivo.line(30, y-80, 580, y-80)
        archivo.line(100, y - 140, 200, y - 140)
        archivo.drawString(120, y-160, "Jurado 1")

        archivo.line(400, y - 140, 500, y - 140)
        archivo.drawString(420, y-160, "Jurado 2")

    else:
        archivo.setFont('Helvetica-Bold', 12)
        archivo.drawString(30, y, f'Como resultado de estas calificaciones parciales y sus ponderciones, la calificacion del trabajo')
        archivo.drawString(30, y-20, f'de grado es: {acta.nota}')
        archivo.drawString(30, y-40, 'Observaciones adicionales: ')
        archivo.line(30, y-60, 580, y-60)
        archivo.line(30, y-80, 580, y-80)
        archivo.line(100, y - 140, 200, y - 140)
        archivo.drawString(120, y-160, "Jurado 1")

        archivo.line(400, y - 140, 500, y - 140)
        archivo.drawString(420, y-160, "Jurado 2")


    archivo.save()
    os.startfile("Acta.pdf")

"Funcion en la cual se escoge el acta que se desea guardar en formato PDF"
def elegir_acta_imprimir(st, controller):
    st.title("Actas almacenadas:")

    actas_llaves = controller.actas.keys()
    acta_evaluar = st.selectbox("¿Que acta quieres imprimir?", actas_llaves)

    enviado_btn = st.button("Descargar")
    if enviado_btn:
        crear_pdf(controller.actas[acta_evaluar])