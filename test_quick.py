#!/usr/bin/env python3

import sys
import os

# Agregar rutas necesarias
sys.path.append('./interpreter')
sys.path.append('./generated')

# Importar el intérprete
try:
    from dsl_interpreter import interpret_code
except ImportError as e:
    print(f"❌ Error al importar: {e}")
    print("Asegúrate de que todos los archivos estén en su lugar")
    sys.exit(1)

def run_test():
    """Prueba básica del intérprete"""
    print("Ejecutando prueba rápida...")
    code = "x = 5; y = 3; z = x + y; z;"
    
    try:
        result, errors = interpret_code(code)
        
        if errors:
            print("❌ Error:", errors)
            return False
        
        if result == 8:
            print("✅ ¡Prueba exitosa! El DSL está funcionando correctamente.")
            return True
        else:
            print(f"❌ Prueba fallida: esperado 8, obtenido {result}")
            return False
    except Exception as e:
        print(f"❌ Excepción: {e}")
        return False

if __name__ == "__main__":
    success = run_test()
    if success:
        print("🎉 El DSL está listo para usar!")
    else:
        print("🔧 Revisa la instalación y configuración")
    
    input("Presiona Enter para continuar...")