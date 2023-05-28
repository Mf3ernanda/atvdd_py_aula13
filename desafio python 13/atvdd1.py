def conta_vogais(string):
  vogais = "aeiouAEIOU"
  contador = 0
  for v in string:
    if v in vogais:
      contador += 1
  return contador
print(conta_vogais(input('digite uma palavra:')))