#!/usr/bin/env python3

import re
def fix_grammar_file():
    with open('grammar/DeepLearningDSL.g4', 'r') as f:
        content = f.read()
    print("🔍 Gramática original encontrada")
 io_match = re.search(r'io_function.*?;', content, re.DOTALL)
  if io_match:
        print("📋 Definición actual de io_function:")
        print(io_match.group(0))
     
    if plot_match:
        print("\n📋 Definición actual de plot_function:")
        print(plot_match.group(0))
    
    return content

if _name_ == "_main_":
    fix_grammar_file()
