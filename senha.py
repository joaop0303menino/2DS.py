print('a senha deve conter no minimo 8 caracteres,letra maiuscula, letra minuscula, numero e caractere especial')

senha = input('digite a senha: ')

def valida_senha(senha):
  if len(senha) > 8:
    if not senha.isupper():
      if not senha.islower():
        if not senha.isascii():
          if not senha.isalnum():
            print('senha cadastrada com sucesso')
          else:
            print('senha invalida, a senha deve conter numeros')
            senha = input('digite a senha novamente: ')
        else:
          print('senha invalida, a senha deve conter caracteres especiais')
          senha = input('digite a senha novamente: ')
      else:
        print('senha invalida a senha deve conter letras minusculas')
        senha = input('digite a senha novamente: ')
    else:
      print('senha invalida, a senha deve conter letras maiusculas')
      senha = input('digite a senha novamente: ')
  else:
    print('senha invalida, a senha deve conter no minimo 8 caracteres')
    senha = input('digite a senha novamente: ')
  
print(valida_senha(senha))