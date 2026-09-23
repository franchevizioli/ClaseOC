import RPi.GPIO as GPIO
import time

# Configuración
LED_PIN1 = 17
LED_PIN2 = 22
LED_PIN3 = 5
LED_PIN4= 18
LED_PIN5 = 24
LED_PIN6 = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT) # Configuramos el pin como SALIDA
GPIO.setup(LED_PIN2, GPIO.OUT) 
GPIO.setup(LED_PIN3, GPIO.OUT) 
GPIO.setup(LED_PIN4, GPIO.OUT) 
GPIO.setup(LED_PIN5, GPIO.OUT) 
GPIO.setup(LED_PIN6, GPIO.OUT) 
try:
    print("esepere su semaforo.. (Presiona Ctrl+C para salir)")
    while True:
        print(f"primer semaforo")
        GPIO.output(LED_PIN1, True)  # Prender (3.3V)
        GPIO.output(LED_PIN4, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN1, False)  # Prender (3.3V)
        GPIO.output(LED_PIN2, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN2, False)  # Prender (3.3V)
        GPIO.output(LED_PIN3, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN3, False)  # Prender (3.3V)
        GPIO.output(LED_PIN2, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN2, False)  # Prender (3.3V)
        GPIO.output(LED_PIN1, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN4, False)  # Prender (3.3V)
        GPIO.output(LED_PIN5, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN5, False)  # Prender (3.3V)
        GPIO.output(LED_PIN6, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN6, False)  # Prender (3.3V)
        GPIO.output(LED_PIN5, True)  # Prender (3.3V)
        time.sleep(1)
        GPIO.output(LED_PIN5, False)  # Prender (3.3V)
        GPIO.output(LED_PIN4, True)  # Prender (3.3V)
        time.sleep(0.5)
        
        
except KeyboardInterrupt:
    print("Saliendo...")
finally:
    GPIO.cleanup() # Limpia los pines al terminar
