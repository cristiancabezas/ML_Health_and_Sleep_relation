# 💤 Prediction and Classification of Sleep Disorders
- Access the application and test the project:
[APP](https://health-and-sleep-relation.streamlit.app/)
- Access the presentation video:
[VIDEO](https://youtu.be/jOaEQNkqQfE)

This machine learning project aims to help detect and classify sleep disorders in people using personal health and lifestyle data. It also includes an interactive application in **Streamlit** that allows users to obtain an automatic diagnosis, receive useful recommendations, information from specialized centers, and receive this information via email.

## 🎯 Project Objectives

* Predict whether a person has healthy sleep or not.
* Classify the type of sleep disorder detected:

  * **Insomnia**
  * **Sleep apnea**
* Suggests nearby medical centers or personalized advice.
* Facilitates emailing of results and recommendations.


## 📊 Dataset

The model was trained with a dataset that included variables such as:

* Age, gender, physical activity level, heart rate, blood pressure, sleep quality, etc.



## 🧐 About the models

During the project, various tests were performed:

* Variable selection using techniques such as:

  * Feature importance
  * Hypothesis testing
  * Automated methods such as RFE, SFS, SelectFromModel, and Lasso
* Multiple model comparison:

  * XGBoost, Random Forest, CatBoost, Gradient Boosting, LightGBM, among others.
* Cross-validation with key metrics: **recall, f1-score, ROC-AUC, precision**.



## 🔍 Machine Learning Models

* **Random Forest Classifier**
  Detects if the person has problems with sleep quality.

* **XGBoost Classifier**
  Classifies the type of disorder when a problem is detected.


## 📊 Results against the Models' tests

| Model  | Task  | Precision | Recall | f1-score |
| ----- | ---- | ----- | --- | ---| 
| Random Forest  | Unhealthy Sleep Detection | 96%  | 96%  | 96% | 
| XGBoost Classifier |  Classification of the type of disorder | 87%     | 87%  | 87%|



## 🧠 Technologies and Tools Used

* **Python**
* **Jupyter Notebook**, **Visual Studio Code**
* **Scikit-learn** – Modeling and evaluation
* **XGBoost** – Classification of disorders
* **Streamlit** – Interactive web interface
* **Pandas / Seaborn / NumPy / Matplotlib** – Data analysis and visualization
* **Joblib** - Saving Models and Pipelines
* **Streamlit** - Web application
* **Smtplib** – Sending emails


## 📂 Project structure
```
💤 ML_Health_and_Sleep_Relation/
|
├── 🐍 app.py                        # Streamlit App
├── 📄 README.md                     # Brief description of the project
├── 📄 main.ipynb                    # Main project notebook
├── 📄 presentacion_ML.pdf           # Final presentation
|
└── 📂 src/
    ├── 📂 data/                     # Datasets
    ├── 📂 img/                      # Images and graphics used
    ├── 📂 models/                   # Trained Models and Pipelines
    ├── 📂 notebooks/                # Jupyter notebooks (EDA, modeling, tuning)
    └── 📂 utils/                    # Functions
```


## 👤 Target Audience

* People interested in their sleep quality.
* Healthcare professionals seeking an exploratory tool.
* Researchers in sleep disorders and personal well-being.


## 📌 Final advice

This project does not replace a medical diagnosis, but can serve as a preventive or guidance tool.


## ✅ Result

- Access the application and test the project:
[APP](https://health-and-sleep-relation.streamlit.app/)
- Access the presentation video:
[VIDEO](https://youtu.be/jOaEQNkqQfE)


## 📬 Contact

Do you have questions, suggestions, or want to collaborate on the project?

- **Email**: cabezasdelgadocristian@gmail.com  
- **LinkedIn**: [Cristia Cabezas](https://linkedin.com/in/cristian-cabezas-delgado)


        



---------

# 💤 Predicción y Clasificación de Trastornos del Sueño

- Accede a la aplicación y prueba el proyecto:
[APP](https://health-and-sleep-relation.streamlit.app/)
- Accede al vídeo de la presentación:
[VIDEO](https://youtu.be/jOaEQNkqQfE)

Este proyecto de Machine Learning tiene como objetivo ayudar a detectar y clasificar trastornos del sueño en personas, a partir de datos personales sobre salud y estilo de vida. Además, incluye una aplicación interactiva en **Streamlit** que permite al usuario obtener un diagnóstico automático, recibir recomendaciones útiles, información de centros especializados y envío por correo electrónico de esa información.


## 🎯 Objetivos del Proyecto

* Predecir si una persona tiene un sueño saludable o no.
* Clasificar el tipo de trastorno del sueño detectado:

  * **Insomnio**
  * **Apnea del sueño**
* Te sugiere centros médicos cercanos o consejos personalizados.
* Facilita el envío de los resultados y recomendaciones por correo electrónico.


## 📊 Dataset

El modelo fue entrenado con un conjunto de datos que incluye variables como:

* Edad, género, nivel de actividad física, frecuencia cardíaca, presión arterial, calidad del sueño, etc.



## 🧐 Sobre los modelos

Durante el proyecto, se hicieron diferentes pruebas:

* Selección de variables mediante técnicas como:

  * Importancia de características (feature importance)
  * Tests de hipótesis
  * Métodos automáticos como RFE, SFS, SelectFromModel y Lasso
* Comparación de múltiples modelos:

  * XGBoost, Random Forest, CatBoost, Gradient Boosting, LightGBM, entre otros.
* Validación cruzada con métricas clave: **recall, f1-score, ROC-AUC, precision**.


## 🔍 Modelos de Machine Learning

* **Random Forest Classifier**
  Detecta si la persona tiene problemas en la calidad del sueño.

* **XGBoost Classifier**
  Clasifica el tipo de trastorno cuando se detecta un problema.


## 📊 Resultados contra test de los Modelos

| Modelo  | Tarea  | Precisión | Recall | f1-score |
| ----- | ---- | ----- | --- | ---| 
| Random Forest  | Detección de sueño no saludable | 96%  | 96%  | 96% | 
| XGBoost Classifier | Clasificación del tipo de trastorno | 87%     | 87%  | 87%|



## 🧠 Tecnologías y Herramientas Utilizadas

* **Python**
* **Jupyter Notebook**, **Visual Studio Code**
* **Scikit-learn** – Modelado y evaluación
* **XGBoost** – Clasificación de trastornos
* **Streamlit** – Interfaz web interactiva
* **Pandas / Seaborn / NumPy / Matplotlib** – Análisis y visualización de datos
* **Joblib** - Guardado de Modelos y Pipelines
* **Streamlit** - Aplicación web
* **Smtplib** – Envío de correos electrónicos


## 📂 Estructura del proyecto
```
💤 ML_Health_and_Sleep_Relation/
|
├── 🐍 app.py                        # Aplicación Streamlit
├── 📄 README.md                     # Descripción breve del proyecto
├── 📄 main.ipynb                    # Notebook principal del proyecto
├── 📄 presentacion_ML.pdf           # Presentación final
|
└── 📂 src/
    ├── 📂 data/                     # Conjuntos de dato
    ├── 📂 img/                      # Imágenes y gráficos utilizados
    ├── 📂 models/                   # Modelos y Pipelines entrenados
    ├── 📂 notebooks/                # Jupyter notebooks (EDA, modelado, ajuste)
    └── 📂 utils/                    # Funciones
```


## 👤 Público Objetivo

* Personas interesadas en su calidad de sueño.
* Profesionales de la salud que deseen una herramienta exploratoria.
* Investigadores en trastornos del sueño y bienestar personal.


## 📌 Notas Finales

Este proyecto no sustituye un diagnóstico médico, pero puede servir como herramienta preventiva o de orientación.


## ✅ Resultado

Este análisis sirve como punto de partida para tomar una decisión informada sobre si abrir un negocio de açaí en Badalona puede ser viable. Las conclusiones y recomendaciones se basan en datos reales y públicos.

- Accede a la aplicación y prueba el proyecto:
[APP](https://health-and-sleep-relation.streamlit.app/)
- Accede al vídeo de la presentación:
[VIDEO](https://youtu.be/jOaEQNkqQfE)


## 📬 Contacto

¿Tienes preguntas, sugerencias o quieres colaborar en el proyecto?

- **Email**: cabezasdelgadocristian@gmail.com
- **LinkedIn**: [Cristia Cabezas](https://linkedin.com/in/cristian-cabezas-delgado)