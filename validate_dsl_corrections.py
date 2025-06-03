#!/usr/bin/env python3

"""
Validación DSL - Tests Corregidos con Sintaxis Correcta
======================================================

Tests corregidos usando la sintaxis correcta del DSL (matrices con dobles corchetes)
"""

import sys
import os

# Configurar rutas
sys.path.append('./interpreter')
sys.path.append('./generated')

def test_plot_fixed():
    """Test de plot() con sintaxis DSL correcta"""
    print("📊 Probando función plot() [SINTAXIS CORREGIDA]...")
    
    try:
        from dsl_interpreter import interpret_code
        
        # ✅ SINTAXIS CORRECTA: Usar dobles corchetes [[]]
        code = """
        datos = [[1, 4, 2, 8, 5, 3, 7]];
        print("Datos para graficar:");
        print(datos);
        plot(datos);
        """
        
        result, errors = interpret_code(code)
        
        if errors:
            print(f"❌ Errores en plot(): {errors}")
            return False
        else:
            print("✅ Función plot() funciona correctamente")
            return True
            
    except Exception as e:
        print(f"❌ Excepción en plot(): {e}")
        return False

def test_scatter_fixed():
    """Test de scatter() con sintaxis DSL correcta"""
    print("\n📈 Probando función scatter() [SINTAXIS CORREGIDA]...")
    
    try:
        from dsl_interpreter import interpret_code
        
        # ✅ SINTAXIS CORRECTA: Usar dobles corchetes [[]]
        code = """
        x_vals = [[1, 2, 3, 4, 5]];
        y_vals = [[2, 4, 1, 8, 6]];
        print("Datos X:");
        print(x_vals);
        print("Datos Y:");
        print(y_vals);
        scatter(x_vals, y_vals);
        """
        
        result, errors = interpret_code(code)
        
        if errors:
            print(f"❌ Errores en scatter(): {errors}")
            return False
        else:
            print("✅ Función scatter() funciona correctamente")
            return True
            
    except Exception as e:
        print(f"❌ Excepción en scatter(): {e}")
        return False

def test_histogram_fixed():
    """Test de histogram() con sintaxis DSL correcta"""
    print("\n📊 Probando función histogram() [SINTAXIS CORREGIDA]...")
    
    try:
        from dsl_interpreter import interpret_code
        
        # ✅ SINTAXIS CORRECTA: Usar dobles corchetes [[]]
        code = """
        hist_data = [[1, 2, 2, 3, 3, 3, 4, 4, 5]];
        print("Datos para histograma:");
        print(hist_data);
        histogram(hist_data);
        """
        
        result, errors = interpret_code(code)
        
        if errors:
            print(f"❌ Errores en histogram(): {errors}")
            return False
        else:
            print("✅ Función histogram() funciona correctamente")
            return True
            
    except Exception as e:
        print(f"❌ Excepción en histogram(): {e}")
        return False

def test_alternative_syntax():
    """Test de sintaxis alternativa usando variables individuales"""
    print("\n🔄 Probando sintaxis alternativa con variables...")
    
    try:
        from dsl_interpreter import interpret_code
        
        code = """
        // Crear datos usando variables individuales
        v1 = 1;
        v2 = 4;
        v3 = 2;
        v4 = 8;
        v5 = 5;
        
        // Crear matriz con variables
        datos = [[v1, v2, v3, v4, v5]];
        print("Datos calculados:");
        print(datos);
        plot(datos);
        """
        
        result, errors = interpret_code(code)
        
        if errors:
            print(f"❌ Errores en sintaxis alternativa: {errors}")
            return False
        else:
            print("✅ Sintaxis alternativa funciona correctamente")
            return True
            
    except Exception as e:
        print(f"❌ Excepción en sintaxis alternativa: {e}")
        return False

def test_matrix_extraction():
    """Test de cómo el plotter maneja matrices DSL"""
    print("\n🔢 Probando extracción de datos de matrices...")
    
    try:
        from dsl_interpreter import interpret_code
        
        code = """
        // Test con matriz de una sola fila (lista)
        lista_simple = [[10, 20, 15, 25, 18]];
        print("Lista como matriz:");
        print(lista_simple);
        plot(lista_simple);
        
        // Test con matriz real (múltiples filas)
        matriz_real = [[1, 2, 3], [4, 5, 6]];
        print("Matriz real:");
        print(matriz_real);
        // Nota: plot() debería manejar esto extrayendo la primera fila
        plot(matriz_real);
        """
        
        result, errors = interpret_code(code)
        
        if errors:
            print(f"❌ Errores en extracción de matrices: {errors}")
            return False
        else:
            print("✅ Extracción de matrices funciona correctamente")
            return True
            
    except Exception as e:
        print(f"❌ Excepción en extracción de matrices: {e}")
        return False

def test_real_world_example():
    """Test de ejemplo del mundo real con sintaxis correcta"""
    print("\n🌍 Probando ejemplo del mundo real...")
    
    try:
        from dsl_interpreter import interpret_code
        
        code = """
        print("=== ANÁLISIS DE TEMPERATURAS ===");
        
        // Datos de temperatura en una semana
        temperaturas = [[20, 22, 25, 28, 30, 27, 24]];
        dias = [[1, 2, 3, 4, 5, 6, 7]];
        
        print("Temperaturas de la semana:");
        print(temperaturas);
        
        print("Gráfica de temperaturas:");
        plot(temperaturas);
        
        print("Correlación días vs temperaturas:");
        scatter(dias, temperaturas);
        
        print("Distribución de temperaturas:");
        histogram(temperaturas);
        
        print("Análisis completado!");
        """
        
        result, errors = interpret_code(code)
        
        if errors:
            print(f"❌ Errores en ejemplo real: {errors}")
            return False
        else:
            print("✅ Ejemplo del mundo real funciona perfectamente")
            return True
            
    except Exception as e:
        print(f"❌ Excepción en ejemplo real: {e}")
        return False

def run_fixed_validation():
    """Ejecutar validación con sintaxis corregida"""
    print("🎯 DSL DEEP LEARNING - VALIDACIÓN CON SINTAXIS CORREGIDA")
    print("=" * 70)
    print("Probando funciones de gráficas con la sintaxis DSL correcta...")
    print()
    
    tests = [
        ("Plot (Sintaxis Corregida)", test_plot_fixed),
        ("Scatter (Sintaxis Corregida)", test_scatter_fixed),
        ("Histogram (Sintaxis Corregida)", test_histogram_fixed),
        ("Sintaxis Alternativa", test_alternative_syntax),
        ("Extracción de Matrices", test_matrix_extraction),
        ("Ejemplo del Mundo Real", test_real_world_example),
    ]
    
    passed = 0
    total = len(tests)
    
    for name, test_func in tests:
        print(f"📋 Test: {name}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {name} - PASÓ")
            else:
                print(f"❌ {name} - FALLÓ")
        except Exception as e:
            print(f"💥 {name} - EXCEPCIÓN: {e}")
        
        print("-" * 50)
    
    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN FINAL - VALIDACIÓN CORREGIDA")
    print("=" * 70)
    
    success_rate = (passed / total) * 100
    
    print(f"Tests ejecutados: {total}")
    print(f"Tests exitosos: {passed}")
    print(f"Tests fallidos: {total - passed}")
    print(f"Tasa de éxito: {success_rate:.1f}%")
    
    if passed == total:
        print("\n🎉 ¡PERFECTO! Todas las gráficas funcionan con sintaxis correcta")
        print("🚀 Tus correcciones del DSL son completamente exitosas")
        print("\n📋 Sintaxis DSL confirmada:")
        print("   ✅ Listas/Arrays: [[1, 2, 3, 4, 5]]")
        print("   ✅ Matrices: [[1, 2], [3, 4]]")
        print("   ✅ Gráficas: plot([[datos]])")
        print("   ✅ Scatter: scatter([[x]], [[y]])")
    elif passed >= total * 0.8:
        print("\n✅ ¡Excelente! La mayoría de tests pasaron")
        print("🔧 Solo ajustes menores necesarios")
    else:
        print("\n⚠️  Algunos tests aún fallan")
        print("🔍 Revisa los errores específicos arriba")
    
    print(f"\n💡 Comandos DSL correctos para usar:")
    print("   dsl> datos = [[1, 4, 2, 8, 5]];")
    print("   dsl> plot(datos);")
    print("   dsl> x = [[1, 2, 3]]; y = [[4, 5, 6]];")
    print("   dsl> scatter(x, y);")
    
    return passed == total

if __name__ == "__main__":
    print("🔧 Validación DSL con Sintaxis Corregida")
    print("Detectando la sintaxis correcta del lenguaje...")
    print()
    
    success = run_fixed_validation()
    
    if success:
        print("\n🏆 ¡VALIDACIÓN COMPLETAMENTE EXITOSA!")
        print("🎊 El DSL funciona perfectamente con la sintaxis correcta")
        print("\n🎯 Conclusión: Tus correcciones fueron 100% exitosas")
        print("    El problema era solo la sintaxis en los tests, no tu código")
    else:
        print("\n🔧 Revisar tests que aún fallan")
    
    sys.exit(0 if success else 1)
