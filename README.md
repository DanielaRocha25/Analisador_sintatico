# Analisador_sintatico

Sugesões de input para executar o programa:

Teste 1:

Informe uma expressão aritmética para verificar: 2+3*2

A expressão é válida. Resultado:  8

Teste 2:

Informe uma expressão aritmética para verificar: 6+4/2

A expressão é válida. Resultado:  8.0

Teste 3:

Informe uma expressão aritmética para verificar: 3+A

Expressão inválida. Começando no caracter: A

Conjunto First e Follow da gramática:
E → TE′
FIRST={num}
FOLLOW= {$, +, -}

E′ → E

E′ → ε
FIRST = {+, -, ε}
FOLLOW = {$, +, -}

T → FT′
FIRST = {num}
FOLLOW = {$, +, -}

T′ → +E

T′ → −E

T′ → ε
FIRST = {+, -, ε}
FOLLOW = {$, +, -}

F → VF′
FIRST = {num}
FOLLOW = {$, +, -}

F′→ ∗E 

F′ → /E 

F′ → ε 
FIRST = {*, /, ε}
FOLLOW = {$, +, -}

V → num
FIRST = {num}
FOLLOW = {*, /, ε}
