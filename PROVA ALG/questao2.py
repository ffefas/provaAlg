
salario_fixo = float(input("Digite o salário fixo: R$ "))
valor_vendas = float(input("Digite o valor das vendas: R$ "))

if valor_vendas <= 1500:
    comissao = valor_vendas * 0.05
    salario_total = salario_fixo + comissao
    print("O salário total é: R$ ", + float(salario_total))

else:
    comissao2 = valor_vendas - 1500
    salario_total = salario_fixo + (valor_vendas*0.05) + (comissao2*0.07)
    print("O salário total é: R$ ", + float(salario_total))
