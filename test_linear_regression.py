import sys
sys.path.append('./interpreter')
sys.path.append('./generated')

def test_dsl_linear_regression_corrected():
    """Test de regresión lineal con sintaxis DSL correcta"""
    print("🧪 TESTING: Regresión Lineal DSL [SINTAXIS CORREGIDA]")
    print("=" * 55)
    
    try:
        from dsl_interpreter import interpret_code
        
        # ✅ Test 1: Sintaxis CORRECTA del DSL
        print("\n📊 Test 1: Regresión simple [SINTAXIS CORREGIDA]")
        code1 = """
        print("=== REGRESIÓN LINEAL BÁSICA ===");
        
        X = [[1], [2], [3], [4]];
        y = [[2, 4, 6, 8]];
        
        print("Datos X:"); print(X);
        print("Datos y:"); print(y);
        
        modelo = linear_regression(X, y);
        print("✅ Modelo ajustado");
        
        pred1 = predict(modelo, [[5]]);
        print("Predicción x=5:"); print(pred1);
        
        pred2 = predict(modelo, [[10]]);
        print("Predicción x=10:"); print(pred2);
        """
        
        result, errors = interpret_code(code1)
        if errors:
            print(f"❌ Test 1 falló: {errors}")
            return False
        print("✅ Test 1 exitoso")
        
        # ✅ Test 2: Formato matriz columna (alternativo)
        print("\n📊 Test 2: Formato matriz columna")
        code2 = """
        print("=== FORMATO MATRIZ COLUMNA ===");
        
        X_col = [[1], [2], [3], [4]];
        y_col = [[2], [4], [6], [8]];
        
        print("X como matriz columna:"); print(X_col);
        print("y como matriz columna:"); print(y_col);
        
        modelo2 = linear_regression(X_col, y_col);
        pred = predict(modelo2, [[6]]);
        print("Predicción x=6:"); print(pred);
        """
        
        result, errors = interpret_code(code2)
        if errors:
            print(f"❌ Test 2 falló: {errors}")
            return False
        print("✅ Test 2 exitoso")
        
        # ✅ Test 3: Ejemplo del mundo real
        print("\n📊 Test 3: Ejemplo del mundo real")
        code3 = """
        print("=== EJEMPLO: PRECIO vs ÁREA ===");
        
        // Área de casas en m²
        area = [[50], [75], [100], [125], [150]];
        
        // Precio en miles (relación lineal: precio = 2*área + 10)
        precio = [[110, 160, 210, 260, 310]];
        
        print("Área (m²):"); print(area);
        print("Precio (miles):"); print(precio);
        
        modelo_casa = linear_regression(area, precio);
        
        // Predecir precio para casa de 200m²
        pred_200m = predict(modelo_casa, [[200]]);
        print("Precio estimado para 200m²:"); print(pred_200m);
        
        // Predecir precio para casa de 80m²
        pred_80m = predict(modelo_casa, [[80]]);
        print("Precio estimado para 80m²:"); print(pred_80m);
        """
        
        result, errors = interpret_code(code3)
        if errors:
            print(f"❌ Test 3 falló: {errors}")
            return False
        print("✅ Test 3 exitoso")
        
        print("\n🎉 ¡TODOS LOS TESTS PASARON!")
        print("✅ Regresión lineal funcionando con sintaxis DSL correcta")
        return True
        
    except Exception as e:
        print(f"💥 Error en testing: {e}")
        import traceback
        traceback.print_exc()
        return False

def demonstrate_dsl_syntax():
    """Demostrar la sintaxis correcta del DSL"""
    print("\n📋 SINTAXIS DSL CORRECTA")
    print("=" * 30)
    
    syntax_examples = [
        ("❌ INCORRECTO", "y = [2, 4, 6, 8];"),
        ("✅ CORRECTO", "y = [[2, 4, 6, 8]];"),
        ("", ""),
        ("❌ INCORRECTO", "X = [1, 2, 3];"),
        ("✅ CORRECTO", "X = [[1], [2], [3]];"),
        ("✅ TAMBIÉN CORRECTO", "X = [[1, 2, 3]];"),
        ("", ""),
        ("🎯 REGRESIÓN LINEAL", ""),
        ("✅ Formato fila", "X = [[1], [2], [3]]; y = [[2, 4, 6]];"),
        ("✅ Formato columna", "X = [[1], [2], [3]]; y = [[2], [4], [6]];"),
    ]
    
    for label, syntax in syntax_examples:
        if syntax:
            print(f"{label:20} {syntax}")
        else:
            print()

def quick_dsl_test():
    """Test ultra-rápido para verificar sintaxis"""
    print("\n🚀 TEST RÁPIDO: Verificación de Sintaxis")
    print("=" * 45)
    
    try:
        from dsl_interpreter import interpret_code
        
        # Test sintaxis básica
        print("🔍 Probando sintaxis básica...")
        
        basic_tests = [
            ("Variable simple", "x = 5;"),
            ("Lista DSL", "lista = [[1, 2, 3]];"),
            ("Matriz DSL", "matriz = [[1], [2], [3]];"),
            ("Print", "print([[\"Hola DSL\"]]);"),
        ]
        
        all_passed = True
        for name, code in basic_tests:
            result, errors = interpret_code(code)
            if errors:
                print(f"❌ {name}: {errors}")
                all_passed = False
            else:
                print(f"✅ {name}")
        
        if all_passed:
            print("\n✅ Sintaxis DSL básica funcionando")
            
            # Test regresión lineal simple
            print("\n🔍 Probando regresión lineal...")
            regression_code = """
            X = [[1], [2]];
            y = [[2, 4]];
            modelo = linear_regression(X, y);
            pred = predict(modelo, [[3]]);
            print("Predicción:"); print(pred);
            """
            
            result, errors = interpret_code(regression_code)
            if errors:
                print(f"❌ Regresión lineal: {errors}")
                return False
            else:
                print("✅ Regresión lineal básica funcionando")
                return True
        else:
            print("\n❌ Problemas con sintaxis básica")
            return False
            
    except Exception as e:
        print(f"💥 Error: {e}")
        return False

def main():
    """Función principal"""
    print("🔧 CORRECCIÓN: Sintaxis DSL para Regresión Lineal")
    print("=" * 60)
    
    # 1. Mostrar sintaxis correcta
    demonstrate_dsl_syntax()
    
    # 2. Test rápido de sintaxis
    if not quick_dsl_test():
        print("\n❌ PROBLEMA: Sintaxis básica no funciona")
        print("🔧 Verificar archivos del intérprete DSL")
        return False
    
    # 3. Test completo de regresión lineal
    print("\n" + "="*60)
    success = test_dsl_linear_regression_corrected()
    
    print("\n" + "="*60)
    if success:
        print("🏆 ÉXITO TOTAL: Regresión Lineal DSL Funcionando")
        print()
        print("🎯 SINTAXIS CONFIRMADA:")
        print("   ✅ Listas: [[1, 2, 3, 4]]")
        print("   ✅ Matrices: [[1], [2], [3], [4]]")
        print("   ✅ Regresión: linear_regression(X, y)")
        print("   ✅ Predicción: predict(modelo, X_new)")
        print()
        print("💡 Usa en la consola:")
        print("   python interface/console.py")
        print("   dsl> X = [[1], [2], [3]];")
        print("   dsl> y = [[2, 4, 6]];")
        print("   dsl> modelo = linear_regression(X, y);")
        print("   dsl> predict(modelo, [[5]]);")
        
    else:
        print("🔧 RESULTADO: Aún necesita corrección")
        print()
        print("📝 PRÓXIMOS PASOS:")
        print("   1. Verificar que ml_engine.py tiene las correcciones")
        print("   2. Comprobar sintaxis DSL: usar dobles corchetes [[]]")
        print("   3. Revisar archivos ANTLR generados")
    
    return success

if __name__ == "__main__":
    success = main()
    
    if success:
        print(f"\n🎉 ¡Regresión lineal lista para usar!")
        input("Presiona Enter para continuar...")
    else:
        print(f"\n🔧 Revisar problemas y aplicar correcciones")
        input("Presiona Enter para continuar...")
    
    sys.exit(0 if success else 1)
