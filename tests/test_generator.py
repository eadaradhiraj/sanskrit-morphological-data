import unittest
from skt_morph.sandhi import apply_upasarga_sandhi
from skt_morph.declension import decline_noun
from skt_morph.generator import conjugate, get_participle_declension
from skt_morph.pronouns import decline_pronoun
from skt_morph.numerals import decline_numeral

class TestSanskritGenerator(unittest.TestCase):
    def test_forward_sandhi(self):
        self.assertEqual(apply_upasarga_sandhi("vi + AN", "karoti"), "vyAkaroti")
        self.assertEqual(apply_upasarga_sandhi("pra + AN", "karoti"), "prAkaroti")
        self.assertEqual(apply_upasarga_sandhi("sam", "gacCati"), "saMgacCati")
        self.assertEqual(apply_upasarga_sandhi("ud", "karoti"), "utkaroti")
        self.assertEqual(apply_upasarga_sandhi("pra", "iti"), "preti")
        self.assertEqual(apply_upasarga_sandhi("pra", "ukta"), "prokta")
        self.assertEqual(apply_upasarga_sandhi("pra", "fca"), "prarca")
        self.assertEqual(apply_upasarga_sandhi("anu", "eti"), "anveti")
        self.assertEqual(apply_upasarga_sandhi("ni", "asya"), "nyasya")
        self.assertEqual(apply_upasarga_sandhi("sam", "Aneti"), "samAneti")
        self.assertEqual(apply_upasarga_sandhi("ud", "Cinatti"), "ucCinatti") 
        self.assertEqual(apply_upasarga_sandhi("ud", "jvalati"), "ujjvalati")
        self.assertEqual(apply_upasarga_sandhi("ud", "gacCati"), "udgacCati") 
        self.assertEqual(apply_upasarga_sandhi("nir", "gacCati"), "nirgacCati")
        self.assertEqual(apply_upasarga_sandhi("dus", "karoti"), "duskaroti")

    def test_declension_a_karanta(self):
        m_forms = decline_noun("wrampa", "masculine")
        self.assertEqual(m_forms["tritiya"][0], "wrampeRa")
        n_forms = decline_noun("wrampa", "neuter")
        self.assertEqual(n_forms["prathama"][0], "wrampam")
        with self.assertRaises(ValueError): decline_noun("wrampa", "feminine")

    def test_declension_A_I_karanta_feminine(self):
        f_A = decline_noun("kftA", "feminine")
        self.assertEqual(f_A["prathama"][2], "kftAH")
        f_I = decline_noun("kurvatI", "feminine")
        self.assertEqual(f_I["sasthi"][2], "kurvatInAm")
        with self.assertRaises(ValueError): decline_noun("kftA", "masculine")
        with self.assertRaises(ValueError): decline_noun("kurvatI", "neuter")

    def test_declension_i_karanta(self):
        m = decline_noun("hari", "masculine")
        self.assertEqual(m["prathama"][0], "hariH")
        f = decline_noun("mati", "feminine")
        self.assertEqual(f["caturthi"][0], "matyE")
        n = decline_noun("vAri", "neuter")
        self.assertEqual(n["sasthi"][1], "vAriRoH")

    def test_declension_u_karanta(self):
        m = decline_noun("guru", "masculine")
        self.assertEqual(m["sasthi"][2], "gurURAm")
        f = decline_noun("Denu", "feminine")
        self.assertEqual(f["dvitiya"][2], "DenUH")
        n = decline_noun("maDu", "neuter")
        self.assertEqual(n["tritiya"][0], "maDunA")

    def test_declension_f_karanta(self):
        m = decline_noun("kartf", "masculine")
        self.assertEqual(m["prathama"][0], "kartA")
        f = decline_noun("mAtf", "feminine")
        self.assertEqual(f["dvitiya"][2], "mAtFH")
        n = decline_noun("kartf", "neuter")
        self.assertEqual(n["prathama"][2], "kartFNi")

    def test_declension_at_karanta(self):
        m = decline_noun("gacCat", "masculine")
        self.assertEqual(m["prathama"][0], "gacCan")
        n = decline_noun("kurvat", "neuter")
        self.assertEqual(n["prathama"][2], "kurvanti")
        with self.assertRaises(ValueError): decline_noun("gacCat", "feminine")

    def test_declension_an_karanta(self):
        m = decline_noun("rAjan", "masculine")
        self.assertEqual(m["prathama"][0], "rAjA")

    def test_declension_in_karanta(self):
        m = decline_noun("balin", "masculine")
        self.assertEqual(m["prathama"][0], "balI")

    def test_declension_as_karanta(self):
        n = decline_noun("manas", "neuter")
        self.assertEqual(n["prathama"][2], "manAMsi")
        
    def test_declension_t_c_j_karanta(self):
        t = decline_noun("marut", "masculine")
        self.assertEqual(t["prathama"][0], "marut")
        c = decline_noun("vAc", "feminine")
        self.assertEqual(c["prathama"][0], "vAk")
        j = decline_noun("vaRij", "masculine")
        self.assertEqual(j["saptami"][2], "vaRikzu")

    def test_invalid_base(self):
        with self.assertRaises(ValueError): decline_noun("pazU", "masculine")
        with self.assertRaises(ValueError): decline_noun("hari", "unknown") 
        with self.assertRaises(ValueError): decline_noun("guru", "unknown") 
        with self.assertRaises(ValueError): decline_noun("kartf", "unknown") 
        with self.assertRaises(ValueError): decline_noun("rAjan", "feminine")
        with self.assertRaises(ValueError): decline_noun("balin", "neuter")
        with self.assertRaises(ValueError): decline_noun("manas", "masculine")
        with self.assertRaises(ValueError): decline_noun("marut", "feminine")
        with self.assertRaises(ValueError): decline_noun("vAc", "neuter")
        with self.assertRaises(ValueError): decline_noun("vaRij", "neuter")
        
    def test_pronouns(self):
        m = decline_pronoun("tad", "masculine")
        self.assertEqual(m["prathama"][0], "saH")
        
        any_default = decline_pronoun("asmad")
        self.assertEqual(any_default["prathama"][0], "aham")
        
        any_fallback = decline_pronoun("yuzmad", "feminine")
        self.assertEqual(any_fallback["prathama"][0], "tvam")
        
        with self.assertRaises(ValueError): decline_pronoun("unknown", "masculine")

    # --- NEW TESTS FOR NUMERALS ---
    def test_numerals_generation(self):
        m4 = decline_numeral("catur", "masculine")
        self.assertEqual(m4["prathama"][2], "catvAraH")
        
        any_default = decline_numeral("paYcan")
        self.assertEqual(any_default["prathama"][2], "paYca")
        
        any_fallback = decline_numeral("azwan", "feminine")
        self.assertEqual(any_fallback["prathama"][2], "azwO")
        
        with self.assertRaises(ValueError): decline_numeral("unknown_numeral")

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
