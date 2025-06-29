import pandas as pd
import streamlit as st
import joblib
from PIL import Image
import os
from src.utils.transformaciones import *
from src.utils.func_openai import generar_respuesta
from src.utils.mail_automatico import enviar_mail
from dotenv import load_dotenv
load_dotenv()

# Cargar pipeline y modelo
pipeline_transformacion_1 = joblib.load('./src/models/pipeline_transformacion_1_R_F.joblib')
pipeline_transformacion_2 = joblib.load('./src/models/pipeline_transformacion_2_XGB.joblib')
modelo_1 = joblib.load('./src/models/modelo_entrenado_1_R_F.joblib')
modelo_2 = joblib.load('./src/models/modelo_entrenado_2_XGB.joblib')

ruta_datos_clientes_1 = './src/data/datos_clientes_primera_deteccion.csv'
ruta_datos_clientes_2 = './src/data/datos_clientes_clasificacion.csv'
ruta_mail_nombre_cliente = './src/data/mail_nombre_clientes.csv'



st.set_page_config(page_title='Relación entre salud y sueño', page_icon= '😴')

def main():
    st.title('Relación entre la salud y el sueño')
    img = Image.open('./src/img/imagen_1.png')
    st.image(img, use_container_width=False)
    st.markdown('### 💤 Bienvenido a tu evaluación del sueño.')
    st.markdown('''
            
    Esta herramienta analiza tus hábitos de sueño, estrés y salud para ayudarte a identificar posibles problemas como insomnio o apnea del sueño.


    Este formulario no toma más de 1 minuto, con algunos datos personales y recibirás una evaluación instantánea y recomendaciones personalizadas.''')

    
    # recomendaciones para mejorar la experiencia del cliente
    st.markdown('\n')
    st.markdown('\n')
    st.markdown('\n')
    st.markdown('## **Recomendaciones**')
    st.markdown('''
                - Calcula su información de **Presión arterial, Presión sistólica y Presión diastólica** en un sitio cálido y relajado con su mejor Tensiómetro.
                - Puede rellenar cualquier pregunta de forma manual dentro de los límites y presione enter.
                ''')

    # creamos un formulario para poder predecir
    with st.form(key='formulario'):
        col1, col2 = st.columns(2)
        with col1:
            genero = st.selectbox('Género', ['Femenino', 'Masculino'])
            nurse = st.radio('¿Trabajador sanitario?', ['Sí', 'No'])
            calidad_sleep = st.slider('Calidad del sueño (0-10)', 0,10,5, help='0 indica muy mal, 10 indica excelente')
            deporte = st.number_input('Minutos de deporte diarios', 0,250,30)
            altura = st.number_input('Altura', 1.0,2.30,1.70,help="Introduce tu altura en metros")
            edad = st.number_input('Edad', 0,110, 28)

        with col2:
            estres = st.slider('Nivel de estrés (0-10)',0,10,5, help='0 indica muy mal, 10 indica excelente')
            sleep_duration = st.number_input("Horas de sueño", 0.0, 12.0, 7.0)
            pasos = st.number_input("Pasos diarios", 0, 30000, 6000)
            peso = st.number_input("Peso (en kg)", 30.0, 200.0, 60.0)
            systolic = st.number_input("Presión arterial sistólica", 90, 200, 120, help = 'Número más alto' )
            diastolic = st.number_input("Presión arterial diastólica", 50, 130, 80, help = 'Número más bajo')
            ritmo_cardiaco = st.number_input("Ritmo cardíaco (ppm)", 40, 200, 70)

        # generamos un botón que cuando le das se ejecuta el siguiente código y hace todo
        predecir = st.form_submit_button('Predecir mi calidad del sueño')
        # esto es para guardar los datos que salen por pantalla
        if 'predecir' not in st.session_state:
            st.session_state.predecir = False
        if predecir:
            st.session_state.predecir = True 
        # montamos una lista y le ponemos un diccionario para poder hacer un dataframe
        if st.session_state.predecir:
            respuesta_1 = [{
                'Nurse':nurse,
                'Age':edad,
                'Sleep Duration':sleep_duration,
                'Quality of Sleep':calidad_sleep,
                'Physical Activity Level': deporte,
                'Stress Level':estres,
                'Heart Rate':ritmo_cardiaco,
                'Daily Steps':pasos,
                'systolic':systolic,
                'diastolic':diastolic,
                'peso':peso,
                'altura':altura
            }]

            datos_1 = pd.DataFrame(respuesta_1)

            # le pasamos el pipeline para que haga sus tranformaciones
            transformado_1 = pipeline_transformacion_1.transform(datos_1)

            # saco el nombre de las columnas para hacer un dataset para guardar datos y usarlos para perfeccionar el model 				
            columnas_1 = [
            'BMI Category', 'systolic', 'diastolic', 'Pulse Pressure', 'Nurse', 'Age', 
            'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level',
            'Heart Rate', 'Daily Steps']

            # columnas con el orden que ha sido entrenado el modelo, porque no funcionaria bien sin ese order
            orden_dataframe_1 = [
                'Age', 'BMI Category', 'Daily Steps', 'Heart Rate', 'Nurse',
                'Physical Activity Level', 'Quality of Sleep', 'Sleep Duration',
                'Stress Level', 'diastolic', 'systolic', 'Pulse Pressure'
            ]
            # si no encuentra un archivo csv lo creamos
            if not os.path.exists(ruta_datos_clientes_1):
                df_1 = pd.DataFrame(transformado_1, columns=columnas_1, index= datos_1.index)
                df_1 = df_1[orden_dataframe_1] # le aplicamos el mismo order
                df_1.to_csv(ruta_datos_clientes_1, index=False)
            # si encuentra el archivo lo rellenamos con nueva información
            else:
                dataset_1 = pd.read_csv(ruta_datos_clientes_1)
                df_1 = pd.DataFrame(transformado_1, columns=columnas_1, index= datos_1.index)
                df_1 = df_1[orden_dataframe_1] # le aplicamos el mismo order
                unir_1 = pd.concat([dataset_1, df_1], axis=0)
                unir_1.to_csv(ruta_datos_clientes_1, index=False)

            # generamos un dataframe con los datos del pipeline para ponerlos en el mismo orden que el modelo ha sido entrenado
            transformado_1_1 = pd.DataFrame(transformado_1, columns=columnas_1)
            transformado_1_1 = transformado_1_1[orden_dataframe_1]


            # ahora le pasamos el model ya entrenado
            prediccion_1 = modelo_1.predict(transformado_1_1)

            # si la prediccion es 0 indica que no hay problema con el sueño, y si sale 1, indica que si tienes problema con el sueño
            if prediccion_1[0] == 0:
                st.success('### 😊 ¡Buenas noticias!')
                st.markdown('''
                    Según los datos proporcionados, no parece que tengas problemas de sueño.
                    🛌 **Consejos generales para mantener un buen descanso:**
                    - Mantén una rutina constante para acostarte y despertarte.
                    - Evita pantallas y luz azul al menos 1 hora antes de dormir.
                    - Haz ejercicio regularmente, pero no justo antes de dormir.
                    - Crea un ambiente cómodo, silencioso y oscuro en tu habitación.
                    - Evita cafeína, alcohol y cenas pesadas antes de dormir.
                    - Establece una rutina de sueño regular.''')
                st.info('🩺 **Importante:** Esta aplicación no sustituye una evaluación médica. Si notas cambios en tu calidad de sueño o te sientes cansado durante el día, consulta con un profesional.')
                            
                 
            # en caso que sea 1, se ejecuta otro proceso para correr otro modelo y clasificar que tipo de problema es
            elif prediccion_1[0] ==  1:
                respuesta_2 = [{
                    'Gender': genero,
                    'Nurse':nurse,
                    'Age':edad,
                    'Sleep Duration':sleep_duration,
                    'Quality of Sleep':calidad_sleep,
                    'Physical Activity Level': deporte,
                    'Stress Level':estres,
                    'Heart Rate':ritmo_cardiaco,
                    'Daily Steps':pasos,
                    'systolic':systolic,
                    'diastolic':diastolic
                }]
                datos_2 = pd.DataFrame(respuesta_2)

                # le pasamos el pipeline para que haga sus tranformaciones
                transformado_2 = pipeline_transformacion_2.transform(datos_2)

                # miramos que no esté ya creado y sino lo creamos
                # sacamos el nombre de las columnas del pipeline
                columnas_2 = [
                        'Gender_code','Nurse', 'Age', 'Sleep Duration','Quality of Sleep','Physical Activity Level',
                        'Stress Level','Heart Rate','Daily Steps','systolic','diastolic'
                        ]
                orden_dataframe_2 = [
                    'Gender_code','Nurse','Age','Sleep Duration','Quality of Sleep','Physical Activity Level',
                    'Stress Level','Heart Rate','Daily Steps','systolic','diastolic'
                ]
                # aquí se hace lo mismo que arriba, se pregunta si existe el dataset, si no está creado se crea y se rellena, 
                # se guarda con el mismo orden que el modelo ha sido entrenado
                if not os.path.exists(ruta_datos_clientes_2):
                    df_2 = pd.DataFrame(datos_2, columns=columnas_2, index= datos_2.index)
                    df_2 = df_2[orden_dataframe_2]
                    df_2.to_csv(ruta_datos_clientes_2, index=False)
                else:
                    dataset_2 = pd.read_csv(ruta_datos_clientes_2)
                    df_2 = pd.DataFrame(datos_2, columns=columnas_2, index= datos_2.index)
                    df_2 = df_2[orden_dataframe_2]
                    unir_2 = pd.concat([dataset_2, df_2], axis= 0)
                    unir_2.to_csv(ruta_datos_clientes_2, index=False)

                # para el modelo, creo un dataframe, y luego le cambio el order de las columnas para que funcione bien
                transformado_2_2 = pd.DataFrame(transformado_2, columns=columnas_2)
                transformado_2_2 = transformado_2_2[orden_dataframe_2]


                # ahora le pasamos el model ya entrenado
                prediccion_2 = modelo_2.predict(transformado_2_2)

                # si sale 0 indica que tienes insomnio y si sale 1 indica que tienes apena del sueño
                if prediccion_2[0] == 0:
                    st.error('### ⚠️ Posible Insomnio Detectado')
                    st.markdown('''
                    Los datos sugieren que podrías estar experimentando insomnio, un trastorno común que puede afectar tu salud y calidad de vida.

                    🔍 **Señales comunes:**
                    - Dificultad para conciliar o mantener el sueño.
                    - Despertarse muy temprano.
                    - Sensación de no haber descansado.

                    💡 **Sugerencias útiles:**
                    - Intenta mantener una rutina constante.
                    - Reduce el estrés con técnicas como meditación o respiración profunda.
                    - Limita el uso del móvil o la TV antes de dormir.
                    - Evita cafeína, alcohol y cenas pesadas antes de dormir.
                    - Establece una rutina de sueño regular.''')
                    st.info('🩺 **Importante:** Esta evaluación no reemplaza un diagnóstico médico. Si los síntomas son persistentes, consulta con un profesional de salud.')

                else:
                    st.error('### ⚠️ Posible Apnea del Sueño Detectada')
                    st.markdown('''
                    Los datos sugieren que podrías tener apnea del sueño, un trastorno donde la respiración se interrumpe repetidamente durante el sueño.

                    🔍 **Señales típicas:**
                    - Ronquidos fuertes.
                    - Pausas en la respiración al dormir.
                    - Somnolencia excesiva durante el día.

                    💡 **¿Qué puedes hacer?**
                    - Evita dormir boca arriba.
                    - Mantén un peso saludable.
                    - Consulta con un especialista del sueño para realizar un estudio clínico.
                    - Evita cafeína, alcohol y cenas pesadas antes de dormir.
                    - Establece una rutina de sueño regular.''')
                    st.info('🩺 **Advertencia:** La apnea puede tener consecuencias graves si no se trata. Esta app es una orientación inicial. Es clave hablar con un médico.')
                
    # tanto si sale que tiene problema o no del sueño, podrás preguntar dónde acudir o informacion para tratar el problema con chatgpt

    # Cuando le de a predecir, tanto si es bueno o malo el resultado saldrá este espacio donde podrá escribir su pregunta
    #tengo que guardar el 'predecir' porque da problemas para el segundo formulario
    if 'show_chat' not in st.session_state: # se usa así en streamlit
        st.session_state.show_chat = False # primero esta False
    if 'mostrar_formulario_mail' not in st.session_state:
        st.session_state.mostrar_formulario_mail = False
    if predecir: 
        st.session_state.show_chat = True # hasta que le damos a predecir y se pone en True
    
    if st.session_state.show_chat: # aquí si es True, ejecuta el codigo siguiente
        st.markdown('''
                ### ¿Tienes alguna duda dónde acudir en tu ciudad?

                    Puedes preguntarle a nuestro asistente virtual, por ejemplo:
                    - ¿Qué médico debo visitar si tengo insomnio en Madrid?
                    - ¿Dónde puedo hacer un estudio del sueño en Barcelona?
                    - ¿Qué tratamiento hay para la apnea del sueño en Granada?

                    Escribe tu pregunta a continuación y te responderemos al instante 👇''')
        with st.form(key='preg_cliente'):
            pregunta_cliente = st.text_input('Tu pregunta:', placeholder='Ej: ¿Qué especialista trata los problemas de sueño en Barcelona?')
            boton = st.form_submit_button('Enviar')
            if boton:
                if pregunta_cliente:
                    with st.spinner('Escribiendo...'):
                        respuesta = generar_respuesta(pregunta_cliente)
                        if respuesta:
                            st.markdown(respuesta)
                            st.session_state.respuesta = respuesta
                            st.session_state.mostrar_formulario_mail = True #para que se ejecute despues de este formulario el siguiente que es el del mail
                            
        if st.session_state.mostrar_formulario_mail: # aquí llamamos y comprobamos si está en True, para darle paso
            st.warning('# ¿Quieres tener esta información?')
            st.markdown('\n')
            st.markdown('# Dame tu mejor email y su nombre para enviarselo.')
            with st.form(key = 'mail'):
                info_nombre = st.text_input('Nombre y primer apellido')
                info_mail = st.text_input('Su mejor mail', placeholder= 'Ej: tu_sueño@gmail.com').strip()
                boton_mail = st.form_submit_button('Enviar mail')
                if boton_mail:
                    if '@' not in info_mail:
                        st.error('La dirección de correo no está bien escrita')
                    CORREO_REMITENTE = st.secrets['CORREO_REMITENTE']
                    CONTRASENA = st.secrets['CONTRASENA']
                    CORREO_DESTINATARIO = info_mail
                    CONTENIDO = f'''
                    Hola {info_nombre},
                    
                    {st.session_state.respuesta},

                    ¡Gracias por su confianza¡'''

                    enviar_mail(
                        CORREO_REMITENTE,
                        CONTRASENA,
                        CORREO_DESTINATARIO,
                        pregunta_cliente,
                        CONTENIDO)
                    
                    # vamos a guardar los datos de los clientes en un csv
                    # si no encuentra un archivo csv lo creamos
                    
                    # partimos el nombre
                    split_nombre = info_nombre.strip().split(' ',1)
                    #nos aseguramos por si alguien no quiere poner el apellido, 
                    # si en la lista que ha creado hay más de 1 objeto, indica que han puesto apellido, si no, se pone un string vacío
                    nom = split_nombre[0]
                    apell = split_nombre[1] if len(split_nombre) > 1 else ''
                    if not os.path.exists(ruta_mail_nombre_cliente):
                        d1 = pd.DataFrame([{
                                    'nombre':nom,
                                    'apellido':apell,
                                    'mail':info_mail}])
                        d1.to_csv(ruta_mail_nombre_cliente, index=False)
                    # si encuentra el archivo lo rellenamos con nueva información
                    else:
                        da_1 = pd.read_csv(ruta_mail_nombre_cliente)
                        d1 = pd.DataFrame([{
                                    'nombre':nom,
                                    'apellido':apell,
                                    'mail':info_mail}])
                        union = pd.concat([da_1, d1], axis=0)
                        union.to_csv(ruta_mail_nombre_cliente, index=False)
    contenedor = st.container()
    with contenedor:
        st.markdown('\n')
        st.markdown('\n')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/cristian-cabezas-delgado)")
        with col2:
            st.markdown("[💻 GitHub](https://github.com/cristiancabezas)")

if __name__ == '__main__':
    main()