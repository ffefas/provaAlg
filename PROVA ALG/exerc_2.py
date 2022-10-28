
salario_fixo = int(input("Digite o salário fixo: R$"))
valor_vendas = int(input("Digite o valor das vendas: R$"))
comissao1 = 0.05
comissao2 = 0.07

if valor_vendas <= 1500:
    comissao = valor_vendas * comissao1
    salario_total = salario_fixo + comissao
    print (f"O salário total é: R${salario_total}")

elif valor_vendas:
    comissao = valor_vendas * comissao2
    salario_total = salario_fixo + comissao
    print (f"O salário total é: R${salario_total}")
