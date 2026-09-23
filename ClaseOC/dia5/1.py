import RPi.GPIO as GPIO
import time

# Configuración
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # Configuramos el pin como SALIDA

try:
    print("Parpadeando LED... (Presiona Ctrl+C para salir)")
    while True:
        GPIO.output(LED_PIN, True)  # Prender (3.3V)
        time.sleep(1)               # Esperar 1 segundo
        GPIO.output(LED_PIN, False) # Apagar (0V)
        time.sleep(1)
except KeyboardInterrupt:
    print("Saliendo...")
finally:
    GPIO.cleanup() # Limpia los pines al terminar
