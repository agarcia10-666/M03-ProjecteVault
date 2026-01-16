import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def run_security_scan():
    # 1. Configuración de Chrome para modo Headless (Obligatorio para GitHub Actions)
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # 2. Inicializar el driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Simulación de la vulnerabilidad para el ejercicio
    # En un caso real, aquí iría la lógica de probar el diccionario contra el login.html
    password_de_la_app = "123456"  # Contraseña débil en tu login.html
    diccionario = ["admin", "password", "123456", "qwerty"]
    
    encontrada = False
    
    try:
        print("Iniciando escaneo de seguridad en modo Headless...")
        # Aquí el bot probaría las contraseñas...
        for p in diccionario:
            if p == password_de_la_app:
                encontrada = True
                break
        
        if encontrada:
            print(f"VULNERABILIDAD CRÍTICA: Contraseña '{password_de_la_app}' encontrada por el bot.")
            # ESTA LÍNEA HACE QUE LA PIPELINE SE PONGA ROJA
            sys.exit(1) 
        else:
            print("No se han encontrado vulnerabilidades críticas.")
            sys.exit(0)

    except Exception as e:
        print(f"Error durante el escaneo: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_security_scan()
