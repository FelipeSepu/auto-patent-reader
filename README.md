Lector de Patentes de Auto 🚗🔍
Este es un script en Python que utiliza OpenCV y Tesseract OCR para detectar y leer patentes de autos a partir del flujo de video de una cámara IP (por ejemplo, usando la app IP Webcam en tu teléfono).

Características
Conexión a la cámara IP.
Procesamiento de imagen para encontrar posibles patentes.
OCR usando pytesseract para leer el texto.
Validación básica de patentes chilenas.
Requisitos
Python 3.7+
Tesseract OCR instalado.
Cámara IP configurada (puedes usar la app IP Webcam en Android).
Instalación
1. Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/tu-usuario/lector-patentes.git
cd lector-patentes
2. Crear un entorno virtual (opcional pero recomendado)
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instalar dependencias
bash
Copiar
Editar
pip install -r requirements.txt
Contenido del requirements.txt:

Copiar
Editar
opencv-python
pytesseract
numpy
4. Instalar Tesseract OCR
Windows:
Descarga el instalador desde: https://github.com/tesseract-ocr/tesseract/releases
Durante la instalación, recuerda la ruta (usualmente: C:\Program Files\Tesseract-OCR\tesseract.exe).
Añade esa ruta a tu PATH del sistema o modifica la línea en el script:
python
Copiar
Editar
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Linux (Ubuntu):
bash
Copiar
Editar
sudo apt update
sudo apt install tesseract-ocr
macOS:
bash
Copiar
Editar
brew install tesseract
Configuración
Asegúrate de que tu teléfono y tu PC estén en la misma red WiFi.

En tu teléfono, instala y abre IP Webcam.
Configura la aplicación y toma nota de la URL del flujo de video (por ejemplo: http://192.168.1.X:8080/video).
Modifica la variable IP_WEBCAM_URL en el script:
python
Copiar
Editar
IP_WEBCAM_URL = 'http://192.168.1.X:8080/video'
Uso
Ejecuta el script:

bash
Copiar
Editar
python nombre_del_script.py
Presiona q para salir.

Nota
Si el script no logra conectarse a la cámara, asegúrate de que:

La URL del flujo es correcta.
Estás en la misma red.
No hay un firewall bloqueando la conexión.
Mejoras futuras ✨
Soporte para más formatos de patentes.
Exportar resultados a un archivo.
Interfaz gráfica sencilla.
Licencia
MIT License

