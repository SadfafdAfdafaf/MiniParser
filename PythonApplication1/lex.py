import ply.lex as lex

keywords = (
  "BEGIN", "END", "ANUS", 'ID'
)

tokens = keywords + (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'FLOATLITERAL',
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_ignore  = ' \t\x0C'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOATLITERAL(t):
	r'[-+]\d+\.\d+'
	t.value = float(t.value)
	return t

def t_ID(t):
  r'[A-Za-z_][\w_]*'
  if t.value in keywords:
    t.type = t.value.upper()
    return t
  t.type = "ID"
  return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def buildlexer():
  return lex.lex()

data = '''
3 + 4 * -10.6
  + -20 *2
'''

lexer = buildlexer()
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)