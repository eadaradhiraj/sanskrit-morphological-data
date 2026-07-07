import unittest
from skt_morph.sandhi import apply_upasarga_sandhi
from skt_morph.declension import decline_noun
from skt_morph.generator import conjugate, get_participle_declension

class TestSanskritGenerator(unittest.TestCase):
    def test_forward_sandhi(self):
        self.assertEqual(apply_upasarga_sandhi("vi + AN", "karoti"), "vyAkaroti")
        self.assertEqual(apply_upasarga_sandhi("pra + AN", "karoti"), "prAkaroti")
        self.assertEqual(apply_upasarga_sandhi("sam", "gacCati"), "saMgacCati")
        self.assertEqual(apply_upasarga_sandhi("ud", "karoti"), "utkaroti")
        
        # Test Vowel Sandhi Branches
        self.assertEqual(apply_upasarga_sandhi("pra", "iti"), "preti")
        self.assertEqual(apply_upasarga_sandhi("pra", "ukta"), "prokta")
        self.assertEqual(apply_upasarga_sandhi("pra", "fca"), "prarca")
        self.assertEqual(apply_upasarga_sandhi("anu", "eti"), "anveti")
        self.assertEqual(apply_upasarga_sandhi("ni", "asya"), "nyasya")
        
        # Test Consonant Sandhi Branches
        self.assertEqual(apply_upasarga_sandhi("sam", "Aneti"), "samAneti")
        self.assertEqual(apply_upasarga_sandhi("ud", "Cinatti"), "ucCinatti") 
        self.assertEqual(apply_upasarga_sandhi("ud", "jvalati"), "ujjvalati")
        self.assertEqual(apply_upasarga_sandhi("ud", "gacCati"), "udgacCati") 
        
        # Test the 'else' branch (prefixes ending in r, s)
        self.assertEqual(apply_upasarga_sandhi("nir", "gacCati"), "nirgacCati")
        self.assertEqual(apply_upasarga_sandhi("dus", "karoti"), "duskaroti")

    def test_declension_generation(self):
        forms_a = decline_noun("wrampa", "masculine")
        self.assertEqual(forms_a["tritiya"][0], "wrampeRa") 
        
        forms_i = decline_noun("hari", "masculine")
        self.assertEqual(forms_i["prathama"][0], "hariH")
        
        forms_u = decline_noun("guru", "masculine")
        self.assertEqual(forms_u["prathama"][0], "guruH")
        
        forms_f = decline_noun("kartf", "masculine")
        self.assertEqual(forms_f["prathama"][0], "kartA")
        
        # Test missing branches (unsupported genders returning empty dicts)
        with self.assertRaises(ValueError): decline_noun("wrampa", "feminine")
        with self.assertRaises(ValueError): decline_noun("hari", "neuter")
        with self.assertRaises(ValueError): decline_noun("guru", "neuter")
        with self.assertRaises(ValueError): decline_noun("kartf", "neuter")

    def test_direct_conjugation_match(self):
        forms = conjugate("8.0010", upasarga="pra")
        self.assertIsNotNone(forms)
        self.assertEqual(forms["eka"], "prakaroti")

    def test_dynamic_conjugation(self):
        forms = conjugate("8.0010", upasarga="sam + ud + AN")
        self.assertIsNotNone(forms)
        self.assertEqual(forms["eka"], "samudAkaroti")  
        self.assertIsNone(conjugate("99.9999", upasarga="pra"))

    def test_direct_participle_match(self):
        forms = get_participle_declension("8.0010", pratyaya="tfc", gender="masculine", upasarga="")
        self.assertIsNotNone(forms)
        self.assertEqual(forms["prathama"][0], "kartA")

    def test_dynamic_participle_generation(self):
        forms = get_participle_declension("8.0010", pratyaya="tfc", gender="masculine", upasarga="sam + ud + AN")
        self.assertIsNotNone(forms)
        self.assertTrue(forms["prathama"][0] in ["samudAkarttA", "samudAkartA"]) 
        self.assertIsNone(get_participle_declension("99.9999", "tfc", "masculine"))

if __name__ == "__main__": # pragma: no cover
    unittest.main(verbosity=2)
