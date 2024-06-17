# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:01:51 2024

@author: Helio
"""

class ContaBancaria:
    def __init__(self, titular, numero, saldo_inicial=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "Erro: Valor de depósito inválido."

    def sacar(self, valor):
        if valor > self.saldo:
            return "Erro: Saldo insuficiente."
        elif valor <= 0:
            return "Erro: Valor de saque inválido."
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            return f"Saque de R${valor:.2f} realizado com sucesso."

    def mostrar_extrato(self):
        if not self.extrato:
            return "Não houve movimentações."
        else:
            extrato_str = "\n".join(self.extrato)
            return f"Extrato:\n{extrato_str}\nSaldo atual: R${self.saldo:.2f}"

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def mostrar_contas(self):
        contas_str = "\n".join([f"Conta {conta.numero} - Saldo: R${conta.saldo:.2f}" for conta in self.contas])
        return f"Contas de {self.nome}:\n{contas_str}"

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        clientes_str = "\n".join([f"Cliente: {cliente.nome} - CPF: {cliente.cpf}" for cliente in self.clientes])
        return f"Clientes do banco {self.nome}:\n{clientes_str}"

def main():
    banco = Banco("Banco Exemplo")

    while True:
        print("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[c] Criar Conta\n[a] Adicionar Cliente\n[q] Sair")
        opcao = input("=> ")

        if opcao == "d":
            numero_conta = input("Número da conta: ")
            valor = float(input("Valor a depositar: "))
            conta = next((c for c in banco.clientes[0].contas if c.numero == numero_conta), None)
            if conta:
                print(conta.depositar(valor))
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            numero_conta = input("Número da conta: ")
            valor = float(input("Valor a sacar: "))
            conta = next((c for c in banco.clientes[0].contas if c.numero == numero_conta), None)
            if conta:
                print(conta.sacar(valor))
            else:
                print("Conta não encontrada.")

        elif opcao == "e":
            numero_conta = input("Número da conta: ")
            conta = next((c for c in banco.clientes[0].contas if c.numero == numero_conta), None)
            if conta:
                print(conta.mostrar_extrato())
            else:
                print("Conta não encontrada.")

        elif opcao == "c":
            nome_cliente = input("Nome do cliente: ")
            cpf_cliente = input("CPF do cliente: ")
            numero_conta = input("Número da conta: ")
            saldo_inicial = float(input("Saldo inicial: "))
            cliente = next((cl for cl in banco.clientes if cl.cpf == cpf_cliente), None)
            if cliente:
                conta = ContaBancaria(nome_cliente, numero_conta, saldo_inicial)
                cliente.adicionar_conta(conta)
                print(f"Conta {numero_conta} criada com sucesso para {nome_cliente}.")
            else:
                print("Cliente não encontrado. Adicione o cliente primeiro.")

        elif opcao == "a":
            nome_cliente = input("Nome do cliente: ")
            cpf_cliente = input("CPF do cliente: ")
            cliente = Cliente(nome_cliente, cpf_cliente)
            banco.adicionar_cliente(cliente)
            print(f"Cliente {nome_cliente} adicionado com sucesso.")

        elif opcao == "q":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
