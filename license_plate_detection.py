import cv2
import pytesseract
import numpy as np

# Configurar pytesseract (asegúrate de que Tesseract esté instalado y en el PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Cambia la ruta si es necesario

# URL del flujo de video de IP Webcam
IP_WEBCAM_URL = 'http://192.168.1.6:8080/video'

# Función para conectar al flujo de la cámara
def start_camera():
    try:
        # Abrir el stream de video
        cap = cv2.VideoCapture(IP_WEBCAM_URL)
        if not cap.isOpened():
            raise Exception("No se pudo conectar al flujo de la cámara del teléfono.")
        return cap
    except Exception as e:
        print(f"Error al iniciar la cámara: {e}")
        return None

def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  # Reducir ruido
    edges = cv2.Canny(gray, 50, 150)  # Ajustar umbrales para bordes

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            if 1.5 < w / h < 8 and w > 50 and h > 20:
                roi = gray[y:y+h, x:x+w]
                roi = cv2.resize(roi, (200, 50))  # Normalizar tamaño
                text = pytesseract.image_to_string(roi, config='--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                print(f"Texto detectado por OCR (sin validar): {text.strip()}")
                if validate_license_plate(text):
                    print("Patente detectada:", text.strip())
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, text.strip(), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame

# Función para validar una patente chilena
def validate_license_plate(text):
    text = text.strip().replace(" ", "")
    # Patrones básicos para patentes chilenas
    if len(text) == 6 and text[:4].isalnum() and text[4:].isdigit():
        return True
    return False

# Función principal
def main():
    cap = start_camera()
    if not cap:
        print("No se pudo iniciar la cámara. Verifica la conexión del teléfono y la URL del flujo.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error al leer el frame del video.")
                break

            # Procesar el frame para detectar patentes
            processed_frame = process_frame(frame)

            # Mostrar el frame procesado
            cv2.imshow("Detección de Patentes", processed_frame)

            # Salir con la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Detección detenida por el usuario.")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
