print("Analisador sintatico recursivo descendente:")
print("E → TE′\nE′ → E\nE′ → ε\nT → FT′\nT′ → +E\nT′ → −E\nT′ → ε\nF → VF′\nF′→ ∗E\nF′ → /E\nF′ → ε \nV → num\nnum → [0 − 9][0 − 9]∗")
# Criação dos tokens
NUMERO = 1
SOMA = 2
SUBTRACAO = 3
MULTIPLICACAO = 4
DIVISAO = 5
FINAL = 6
ERRO = 7
# Criação da classe token para guardar seu valor e tipo
class Token:
    def __init__(self, tipo, valor):
        self.type = tipo
        self.value = valor

# A classe Analise_lexica é inicialiazada com o método construtor que define o texto, a posição e o caracter_atual
class Analise_lexica:
    def __init__(self, texto):
        self.text = texto
        self.pos = 0
        self.caracter_atual = self.text[self.pos]
# A função avancar() vai avançando na posição do caracter
    def avancar(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.caracter_atual = None
        else:
            self.caracter_atual = self.text[self.pos]
# A função verifica_numero verifica se o input digitado é um número com o isdigit(). Se sim chama o método
# avançar e retorna o número como um inteiro usando int().
    def verifica_numero(self):
        resultado = ''
        while self.caracter_atual is not None and self.caracter_atual.isdigit():
            resultado += self.caracter_atual
            self.avancar()
        return int(resultado)
# A função proximo_token faz um laço de repetição para verificar se os caracteres informados correspondem aos
# tokens registrados. Se o input não corresponder a nenhum dos tokens retorna que a expressao é inválida
    def proximo_token(self):
        expressaoValida = True
        while self.caracter_atual is not None and expressaoValida:
            if self.caracter_atual.isspace():
                self.avancar()
                continue
            elif self.caracter_atual.isdigit():
                return Token(NUMERO, self.verifica_numero())
            elif self.caracter_atual == '+':
                self.avancar()
                return Token(SOMA, '+')
            elif self.caracter_atual == '-':
                self.avancar()
                return Token(SUBTRACAO, '-')
            elif self.caracter_atual == '*':
                self.avancar()
                return Token(MULTIPLICACAO, '*')
            elif self.caracter_atual == '/':
                self.avancar()
                return Token(DIVISAO, '/')
            else:
                print(f'Expressão inválida. Começando no caracter: {self.caracter_atual}')
                expressaoValida = False
        if expressaoValida:
            return Token(FINAL, None)
        else:
            return Token(ERRO, None)

# A classe Analise_sintatica inicializa definindo o lexer e o token atual.
class Analise_sintatica:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token_atual = self.lexer.proximo_token()
# A função det_token() checa se o tipo do token é válido então determina o token_atual.
    def det_token(self, token_type):
        if self.token_atual.type == token_type and self.token_atual.type != ERRO:
            self.token_atual = self.lexer.proximo_token()
# A função fator() checa se o token é um número, se sim retorna o valor.
    def fator(self):
        token = self.token_atual
        if token.type == NUMERO:
            self.det_token(NUMERO)
            return token.value
# A função termo() checa se há token de mult. e divisão. Se sim chama a função det_token() e ao resultado será aplicado o operador
    def termo(self):
        resultado = self.fator()
        while self.token_atual.type in (MULTIPLICACAO, DIVISAO):
            token = self.token_atual
            if token.type == MULTIPLICACAO:
                self.det_token(MULTIPLICACAO)
                if self.token_atual.type != ERRO:
                    resultado *= self.fator()
            elif token.type == DIVISAO:
                self.det_token(DIVISAO)
                if self.token_atual.type != ERRO:
                    resultado /= self.fator()
        return resultado
# A função expr() checa se há token de soma e subt. Se sim chama a função det_token() e ao resultado será aplicado o operador.
# é chamada depois por causa da ordem de precedência.
    def expr(self):
        resultado = self.termo()
        while self.token_atual.type in (SOMA, SUBTRACAO):
            token = self.token_atual
            if token.type == SOMA:
                self.det_token(SOMA)
                if self.token_atual.type != ERRO:
                    resultado += self.termo()
            elif token.type == SUBTRACAO:
                self.det_token(SUBTRACAO)
                if self.token_atual.type != ERRO:
                    resultado -= self.termo()
        return resultado

# A função main cria a variavel expressao que vai receber a expressao do usuário e chama as funções de Analise_lexia e Analise_sintatica
def main():
    expressao = input('Informe uma expressão aritmética para verificar: ')
    lexer = Analise_lexica(expressao)
    parser = Analise_sintatica(lexer)
    resultado = parser.expr()
    if parser.token_atual.type != ERRO:
        print("A expressão é válida. Resultado: ", resultado)


main()
