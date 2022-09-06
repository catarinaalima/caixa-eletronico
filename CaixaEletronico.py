import random
print('\nOlá, bem-vindo ao Caixa Eletrônico 24 horas.\n')

# Introdução ao MENU.
def menu():

# Variaveis.
 balance = 4000
 withdraw = 5
 account_data = 0
 opcao = 0
 while opcao != 5:

   print('Escolha a opção: ')
   print('1 - Extrato')
   print('2 - Saque')
   print('3 - Depósito')
   print('4 - Pagamento de conta')
   print('5 - Fechar/Sair')
   opcao = int(input('Opção: '))

   if (opcao == 1):
       account_number = random.randint(1000,9999) # Gerar números aleatórios entre 1000 e 9999
       print('Número da conta:', account_number)
       print('Saldo: R${:.2f}'.format(balance))
       print('Saques disponíveis:', withdraw)

   elif (opcao == 2):
       withdraw_ok = int(input('Digite o valor que você deseja sacar: '))
       if withdraw_ok <= balance:
           balance = balance - withdraw_ok # Calculo pra somar o valor da variavel depois de realizar o saque.
           print('Você sacou R${:.2f} da sua conta.'.format(withdraw_ok))
           print('Agora você tem R${:.2f} disponível em conta.'.format(balance))
           withdraw = withdraw -1 # Calculo pra saber quantos saques podem ser realizados.
           print('Você só pode realizar mais {} saques da sua conta.'.format(withdraw))

       else:
           print('Você não tem esse valor disponível na conta!')

   elif (opcao == 3):
       deposito = int(input('Digite o valor que você deseja depositar: '))
       balance = deposito + balance # Calculo para depositar dinheiro na sua conta bancária.
       print('Você depositou R${:.2f} na sua conta com sucesso e ficou com R${:.2f} disponível na conta!'.format(deposito, balance))

   elif (opcao == 4):
       pagar_conta = int(input('Digite o valor a pagar: '))
       if pagar_conta <= balance:
         balance = balance - pagar_conta # Calculo para cobrar de sua conta bancária.
         print('Conta paga com sucesso! Ficou R${:.2f} disponível na sua conta!'.format(balance))
       else:
         print('Valor indisponivel na conta.') # Aviso para caso não tenha dinheiro disponivel na sua conta.
   elif (opcao == 5):
       print('Volte sempre.')
   else:
       print('Opção inválida!')
menu()
