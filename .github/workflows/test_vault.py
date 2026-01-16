import unittest
from security_vault import check_password

class TestVault(unittest.TestCase):

    def test_01_password_length(self):
        """Validar: Mínimo 8 caracteres"""
        self.assertFalse(check_password("Ab1"))
        self.assertTrue(check_password("ValidPass123"))

    def test_02_has_numbers(self):
        """Validar: Debe contener números"""
        self.assertFalse(check_password("NoNumbersHere"))

    def test_03_has_uppercase(self):
        """Validar: Debe contener mayúsculas"""
        self.assertFalse(check_password("alllowercase123"))

    def test_04_no_admin_word(self):
        """Validar: No contiene la palabra 'admin'"""
        self.assertFalse(check_password("adminSecret123"))
        self.assertFalse(check_password("123ADMINpass"))

if __name__ == "__main__":
    # Ejecuta los tests con nivel de detalle 2 para ver el OK en cada uno
    unittest.main(verbosity=2)
