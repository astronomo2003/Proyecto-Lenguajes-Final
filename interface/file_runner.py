#!/usr/bin/env python3

"""
File Runner para DSL Deep Learning
==================================

Módulo para ejecutar archivos DSL de forma no interactiva.
Permite procesar archivos .dsl individuales o múltiples archivos en lote.
"""

import sys
import os
import traceback

# Agregar rutas para importaciones
sys.path.append('./interpreter')
sys.path.append('./generated')

# Importar el intérprete DSL
try:
    from dsl_interpreter import interpret_code
except ImportError as e:
    print(f"Error: No se pudo importar el intérprete DSL: {e}")
    print("Asegúrate de que todos los archivos estén en su lugar.")
    sys.exit(1)


class FileRunner:
    """Ejecutor de archivos DSL no interactivo"""
    
    def __init__(self, verbose=False):
        """
        Inicializar el ejecutor de archivos
        
        Args:
            verbose (bool): Si True, muestra información detallada de ejecución
        """
        self.verbose = verbose
        self.execution_results = {}
    
    def run_file(self, filename):
        """
        Ejecutar un archivo DSL específico
        
        Args:
            filename (str): Ruta al archivo DSL
            
        Returns:
            bool: True si la ejecución fue exitosa, False si hubo errores
        """
        if not os.path.exists(filename):
            print(f"❌ Error: El archivo '{filename}' no existe.")
            return False
        
        if self.verbose:
            print(f"📄 Ejecutando archivo: {filename}")
            print("-" * 50)
        
        try:
            # Leer el contenido del archivo
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if self.verbose:
                print("📝 Contenido del archivo:")
                print(content)
                print("-" * 50)
            
            # Ejecutar el código DSL
            result, errors = interpret_code(content)
            
            # Procesar resultados
            if errors:
                print(f"❌ Errores encontrados en '{filename}':")
                for i, error in enumerate(errors, 1):
                    print(f"   {i}. {error}")
                self.execution_results[filename] = {
                    'status': 'ERROR',
                    'errors': errors,
                    'result': None
                }
                return False
            else:
                if self.verbose:
                    print(f"✅ Ejecución exitosa de '{filename}'")
                    if result is not None:
                        print(f"📊 Resultado final: {result}")
                else:
                    print(f"✅ {filename} ejecutado correctamente")
                
                self.execution_results[filename] = {
                    'status': 'SUCCESS',
                    'errors': [],
                    'result': result
                }
                return True
        
        except FileNotFoundError:
            print(f"❌ Error: No se pudo encontrar el archivo '{filename}'")
            return False
        except UnicodeDecodeError:
            print(f"❌ Error: No se pudo leer el archivo '{filename}' (problema de codificación)")
            return False
        except Exception as e:
            print(f"❌ Error inesperado al ejecutar '{filename}': {e}")
            if self.verbose:
                traceback.print_exc()
            return False
    
    def run_files(self, filenames):
        """
        Ejecutar múltiples archivos DSL
        
        Args:
            filenames (list): Lista de rutas a archivos DSL
            
        Returns:
            dict: Diccionario con resultados de cada archivo
        """
        if not filenames:
            print("❌ No se proporcionaron archivos para ejecutar")
            return {}
        
        results = {}
        total_files = len(filenames)
        
        print(f"🚀 Ejecutando {total_files} archivo(s) DSL...")
        print("=" * 60)
        
        for i, filename in enumerate(filenames, 1):
            print(f"\n📁 Archivo {i}/{total_files}: {filename}")
            
            success = self.run_file(filename)
            results[filename] = success
            
            if not success and not self.verbose:
                print("   💡 Usa --verbose para ver más detalles del error")
        
        # Mostrar resumen
        self._show_summary(results)
        return results
    
    def _show_summary(self, results):
        """Mostrar resumen de ejecución"""
        print("\n" + "=" * 60)
        print("📊 RESUMEN DE EJECUCIÓN")
        print("=" * 60)
        
        successful = sum(1 for success in results.values() if success)
        failed = len(results) - successful
        
        print(f"Total de archivos: {len(results)}")
        print(f"Exitosos: {successful}")
        print(f"Fallidos: {failed}")
        print(f"Tasa de éxito: {successful/len(results)*100:.1f}%")
        
        if failed > 0:
            print(f"\n❌ Archivos con errores:")
            for filename, success in results.items():
                if not success:
                    print(f"   • {filename}")
        
        if successful > 0:
            print(f"\n✅ Archivos ejecutados correctamente:")
            for filename, success in results.items():
                if success:
                    print(f"   • {filename}")
    
    def validate_file(self, filename):
        """
        Validar un archivo DSL sin ejecutarlo (solo verificar sintaxis)
        
        Args:
            filename (str): Ruta al archivo DSL
            
        Returns:
            bool: True si la sintaxis es válida, False si hay errores
        """
        if not os.path.exists(filename):
            print(f"❌ Error: El archivo '{filename}' no existe.")
            return False
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Solo verificar sintaxis, no ejecutar
            result, errors = interpret_code(content)
            
            if errors:
                print(f"❌ Errores de sintaxis en '{filename}':")
                for error in errors:
                    print(f"   • {error}")
                return False
            else:
                print(f"✅ Sintaxis válida en '{filename}'")
                return True
        
        except Exception as e:
            print(f"❌ Error al validar '{filename}': {e}")
            return False
    
    def get_execution_results(self):
        """
        Obtener resultados detallados de la última ejecución
        
        Returns:
            dict: Diccionario con resultados detallados
        """
        return self.execution_results.copy()
    
    def clear_results(self):
        """Limpiar historial de resultados"""
        self.execution_results.clear()


def main():
    """Función principal para uso desde línea de comandos"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Ejecutor de archivos DSL Deep Learning',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python file_runner.py ejemplo.dsl
  python file_runner.py archivo1.dsl archivo2.dsl --verbose
  python file_runner.py *.dsl
  python file_runner.py ejemplo.dsl --validate-only
        """
    )
    
    parser.add_argument(
        'files',
        nargs='+',
        help='Archivo(s) DSL para ejecutar'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Mostrar información detallada de ejecución'
    )
    
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Solo validar sintaxis, no ejecutar código'
    )
    
    parser.add_argument(
        '--summary-only',
        action='store_true',
        help='Solo mostrar resumen final, sin detalles'
    )
    
    args = parser.parse_args()
    
    # Crear runner
    runner = FileRunner(verbose=args.verbose and not args.summary_only)
    
    # Procesar archivos
    if args.validate_only:
        # Solo validar sintaxis
        print("🔍 Modo validación - Solo verificando sintaxis...")
        all_valid = True
        for filename in args.files:
            if not runner.validate_file(filename):
                all_valid = False
        
        if all_valid:
            print("\n✅ Todos los archivos tienen sintaxis válida")
            sys.exit(0)
        else:
            print("\n❌ Algunos archivos tienen errores de sintaxis")
            sys.exit(1)
    
    else:
        # Ejecutar archivos
        if len(args.files) == 1:
            # Un solo archivo
            success = runner.run_file(args.files[0])
            sys.exit(0 if success else 1)
        else:
            # Múltiples archivos
            results = runner.run_files(args.files)
            success_count = sum(1 for success in results.values() if success)
            sys.exit(0 if success_count == len(results) else 1)


if __name__ == "__main__":
    main()