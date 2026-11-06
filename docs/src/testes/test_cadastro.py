import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from cadastro import Cadastro, Usuario


class TestCadastro(unittest.TestCase):
    def setUp(self):
        self.arq = os.path.join(tempfile.mkdtemp(), "dados.json")
        self.c = Cadastro(self.arq)

    def test_adicionar_e_listar(self):  # RF01, RF02
        self.c.adicionar(Usuario("Ana", "ana@ex.com"))
        self.assertEqual(self.c.listar()[0].nome, "Ana")

    def test_email_invalido(self):  # RF03
        with self.assertRaises(ValueError):
            self.c.adicionar(Usuario("Bob", "bob.com"))


if __name__ == "__main__":
    unittest.main()
