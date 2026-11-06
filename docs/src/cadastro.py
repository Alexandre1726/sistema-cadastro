"""Sistema de Cadastro — RF01, RF02, RF03."""
import json
import os
from dataclasses import dataclass, asdict


@dataclass
class Usuario:
    nome: str
    email: str


class Cadastro:
    def __init__(self, arquivo="dados.json"):
        self.arquivo = arquivo

    def listar(self):
        if not os.path.exists(self.arquivo):
            return []
        with open(self.arquivo, encoding="utf-8") as f:
            return [Usuario(**u) for u in json.load(f)]

    def adicionar(self, usuario):
        if "@" not in usuario.email:
            raise ValueError("E-mail inválido")
        usuarios = self.listar() + [usuario]
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([asdict(u) for u in usuarios], f, ensure_ascii=False, indent=2)


def main():
    cadastro = Cadastro()
    while True:
        opcao = input("\n1-Cadastrar  2-Consultar  0-Sair: ").strip()
        if opcao == "1":
            try:
                cadastro.adicionar(Usuario(input("Nome: "), input("E-mail: ")))
                print("Usuário cadastrado.")
            except ValueError as e:
                print(e)
        elif opcao == "2":
            for u in cadastro.listar():
                print(f"- {u.nome} <{u.email}>")
        elif opcao == "0":
            break


if __name__ == "__main__":
    main()
