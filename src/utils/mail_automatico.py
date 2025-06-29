import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_mail(remitente, password, destinatario, asunto, contenido):
    # necesario para el mail
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # añadimos el contendio al mensaje
    mensaje.attach(MIMEText(contenido, 'plain'))

    try:
        # el 587 sirve para conectar al servidor de gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.sendmail(remitente, destinatario, mensaje.as_string())
        server.quit()
        st.success('Correo enviado exitosamente.')
    except Exception as e:
        st.error(f'Error al enviar el correo: {str(e)}')
