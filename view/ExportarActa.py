from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def crear_pdf():

    archivo = canvas.Canvas("form.pdf", pagesize=letter)
    archivo.setLineWidth(.3)
    archivo.setFont('Helvetica', 12)

    archivo.drawString(30,660,'Trabajo de grado denominado: ')
    archivo.drawString(30, 640, 'Autor: ')
    archivo.drawString(250, 640, 'ID: ')
    archivo.drawString(30, 620, 'Periodo: ')
    archivo.drawString(30, 600, 'Director: ')
    archivo.drawString(30, 580, 'Co-Director: ')
    archivo.drawString(30, 560, 'Enfasis en: ')
    archivo.drawString(30, 540, 'Modalidad: ')
    archivo.drawString(30, 520, 'Jurado 1: ')
    archivo.drawString(30, 500, 'Jurado 2: ')
    archivo.drawString(30, 460, 'En atencion al desarrollo de este Trabajo de Grado y al documento y sustentacion que presento el/la')
    archivo.drawString(30, 440, 'autor(a), los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios')
    archivo.drawString(30, 420, 'a evaluar y sus ponderaciones se estipulan en el articulo 7.1 de las Directrices para Trabajo de')
    archivo.drawString(30, 400, 'Grado de Maestria):')
    #archivo.drawString(500,750,"27/10/2016")
    #archivo.line(480,747,580,747)

    archivo.setFont('Helvetica-Bold', 13)
    archivo.drawString(222,745,'FACULTAD DE INGENIERIA')
    archivo.drawString(224, 725, 'MAESTRIA EN INGENIERIA')

    archivo.setFont('Helvetica-Bold', 12)
    archivo.drawString(170, 680, 'ACTA DE EVALUACION DE TRABAJO DE GRADO')
    archivo.drawString(30, 700, 'ACTA: ')
    archivo.drawString(450, 700, 'FECHA: ')

    archivo.setFont('Helvetica', 12)
    #archivo.drawString(500,725,"<NOMBRE>")
    #archivo.line(378,723,580,723)

    #archivo.drawString(30,703,'ETIQUETA:')
    #archivo.line(120,700,580,700)
    #archivo.drawString(120,500,"<ASUNTO DE LA CARTA GENERICO>")
    archivo.drawImage("https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png", 20, 720, 170, 60)

    archivo.save()