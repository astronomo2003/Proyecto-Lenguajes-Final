#!/usr/bin/env python3

def analyze_interpreter():
    """Analizar intérprete actual"""
    
    try:
        with open('interpreter/dsl_interpreter.py', 'r') as f:
            content = f.read()
        
        print("🔍 Analizando intérprete...")
        
        # Buscar definición de clase
        if 'class DSLInterpreter' in content:
            print("✅ Clase DSLInterpreter encontrada")
        else:
            print("❌ Clase DSLInterpreter NO encontrada")
        
        # Buscar métodos visit
        visit_methods = []
        for line in content.split('\n'):
            if 'def visit' in line:
                visit_methods.append(line.strip())
        
        print(f"\n📋 Métodos visit encontrados ({len(visit_methods)}):")
        for method in visit_methods[:10]:  # Mostrar primeros 10
            print(f"  {method}")
        
        # Buscar visitIo_function específicamente
        if 'visitIo_function' in content:
            print("\n✅ visitIo_function encontrado")
        else:
            print("\n❌ visitIo_function NO encontrado")
        
        # Buscar visitPlot_function específicamente  
        if 'visitPlot_function' in content:
            print("✅ visitPlot_function encontrado")
        else:
            print("❌ visitPlot_function NO encontrado")
            
        return content
        
    except Exception as e:
        print(f"❌ Error analizando intérprete: {e}")
        return None

if _name_ == "_main_":
    analyze_interpreter()
