import unittest

from compte.cb_d import CB_D


class TestCBDProxy(unittest.TestCase):

    def test_retirer_ok(self):
        compte = CB_D(titulaire=object(), solde=100.0)
        compte.retirer(30.0)
        self.assertEqual(compte.solde, 70.0)

    def test_retirer_refuse_si_pas_de_titulaire(self):
        compte = CB_D(titulaire=None, solde=100.0)
        with self.assertRaises(ValueError):
            compte.retirer(10.0)

    def test_retirer_refuse_si_solde_insuffisant(self):
        compte = CB_D(titulaire=object(), solde=10.0)
        with self.assertRaises(ValueError):
            compte.retirer(30.0)
        self.assertEqual(compte.solde, 10.0)


if __name__ == "__main__":
    unittest.main()
