import unittest
from skt_morph.analyzer import analyze

class TestSanskritAnalyzer(unittest.TestCase):
    def test_known_declension_stemming(self):
        result = analyze("kftena")
        self.assertIsNotNone(next((d for d in result.get("declensions", []) if d["base_form"] == "kfta" and d["dhatu_id"] == "8.0010" and d["case"] == "tritiya"), None))

    def test_declension_sasthi_bahu_natva(self):
        result = analyze("kftARAm")
        self.assertIsNotNone(next((d for d in result.get("declensions", []) if d["base_form"] == "kfta" and d["case"] == "sasthi" and d["vacana"] == "bahu"), None))

    def test_declension_caturthi_eka(self):
        result = analyze("kftAya")
        self.assertIsNotNone(next((d for d in result.get("declensions", []) if d["base_form"] == "kfta" and d["case"] == "caturthi" and d["vacana"] == "eka"), None))

    def test_foreign_word_fallback(self):
        result = analyze("wrampeRa")
        self.assertIsNotNone(next((d for d in result.get("declensions", []) if d["base_form"] == "wrampa" and d["dhatu_id"] is None), None))

    def test_avyaya_classification(self):
        result = analyze("kartum")
        self.assertTrue(len([p for p in result.get("participles", []) if p["type"] == "avyaya"]) > 0)

    def test_verb_with_upasarga(self):
        result = analyze("prakaroti")
        self.assertIsNotNone(next((v for v in result.get("verbs", []) if v["upasarga"] == "pra" and v["dhatu_id"] == "8.0010"), None))

    def test_participle_case_recognition(self):
        result = analyze("kartA")
        self.assertIsNotNone(next((p for p in result.get("participles", []) if p["base_form"] == "kartf" and p["gender"] == "masculine"), None))

    def test_general_search_atmanepada(self):
        result = analyze("kurute")
        self.assertIsNotNone(next((v for v in result.get("verbs", []) if v["dhatu_id"] == "8.0010" and v["voice"] == "Atmanepadam"), None))

    def test_invalid_lyap_hidden(self):
        result = analyze("prakftya")
        self.assertEqual(len([p for p in result.get("participles", []) if p["pratyaya"] == "lyap" and p["upasarga"] == ""]), 0)

    def test_dynamic_upasarga_stripping_verb_unseen(self):
        result = analyze("durAkaroti")
        verbs = result.get("verbs", [])
        self.assertIsNotNone(next((v for v in verbs if v["upasarga"] == "dus + AN" and v["note"] == "Dynamically matched via Sandhi split"), None))

    def test_dynamic_upasarga_stripping_participle_unseen(self):
        result = analyze("durAkartum")
        participles = result.get("participles", [])
        self.assertIsNotNone(next((p for p in participles if p["upasarga"] == "dus + AN" and p["note"] == "Dynamically matched via Sandhi split"), None))

    def test_dynamic_upasarga_stripping_declension_unseen(self):
        result = analyze("durAkftena")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["upasarga"] == "dus + AN" and d.get("note") == "Dynamic Upasarga Match"), None))

    def test_r_karanta_stemming(self):
        result = analyze("kartrA")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["base_form"] == "kartf" and d["dhatu_id"] == "8.0010" and d["case"] == "tritiya"), None))

    def test_u_karanta_stemming_fallback(self):
        result = analyze("neharURAm")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["base_form"] == "neharu" and d["dhatu_id"] is None and d["case"] == "sasthi"), None))

    def test_i_karanta_stemming_fallback(self):
        result = analyze("haraye")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["base_form"] == "hari" and d["dhatu_id"] is None and d["case"] == "caturthi"), None))

    def test_halanta_an_stemming(self):
        result = analyze("rAjAnam")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["base_form"] == "rAjan" and d["case"] == "dvitiya" and d["vacana"] == "eka"), None))

    def test_halanta_as_stemming(self):
        result = analyze("manasA")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["base_form"] == "manas" and d["case"] == "tritiya" and d["vacana"] == "eka"), None))
        
    def test_halanta_in_stemming(self):
        result = analyze("balinO")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["base_form"] == "balin" and d["vacana"] == "dvi"), None))

    def test_halanta_c_j_stemming(self):
        result = analyze("vAcaH")
        declensions = result.get("declensions", [])
        self.assertIsNotNone(next((d for d in declensions if d["base_form"] == "vAc" and d["case"] == "panchami/sasthi"), None))

    def test_namadhatu_kyac(self):
        result = analyze("putrIyati")
        namadhatus = result.get("namadhatus", [])
        self.assertIsNotNone(next((n for n in namadhatus if n["base_noun"] == "putra" and n["pratyaya"] == "kyac"), None))

    def test_namadhatu_kyan(self):
        result = analyze("SyenAyate")
        namadhatus = result.get("namadhatus", [])
        self.assertIsNotNone(next((n for n in namadhatus if n["base_noun"] == "Syena" and n["pratyaya"] == "kyaN"), None))

    def test_namadhatu_kamyac(self):
        result = analyze("putrakAmyati")
        namadhatus = result.get("namadhatus", [])
        self.assertIsNotNone(next((n for n in namadhatus if n["base_noun"] == "putra" and n["pratyaya"] == "kAmyac"), None))
        
    def test_pronouns(self):
        result = analyze("tasmE")
        pronouns = result.get("pronouns", [])
        self.assertIsNotNone(next((p for p in pronouns if p["base_form"] == "tad" and p["case"] == "caturthi"), None))

    # --- NEW TESTS FOR TADDHITA ---
    def test_taddhita_patronymic_a(self):
        result = analyze("vAsudevam") # Should stem to vAsudeva, then taddhita to vasudeva
        taddhitas = result.get("taddhitas", [])
        self.assertIsNotNone(next((t for t in taddhitas if t["base_noun"] == "vasudeva" and t["pratyaya"] == "aR"), None))

    def test_taddhita_patronymic_i(self):
        result = analyze("dASaraTiH")
        taddhitas = result.get("taddhitas", [])
        self.assertIsNotNone(next((t for t in taddhitas if t["base_noun"] == "daSaraTa" and t["pratyaya"] == "iY"), None))

    def test_taddhita_patronymic_eya(self):
        result = analyze("kOnteya")
        taddhitas = result.get("taddhitas", [])
        self.assertIsNotNone(next((t for t in taddhitas if t["base_noun"] == "kuntI" and t["pratyaya"] == "Qak"), None))

    def test_taddhita_abstract_tva(self):
        result = analyze("gurutvam")
        taddhitas = result.get("taddhitas", [])
        self.assertIsNotNone(next((t for t in taddhitas if t["base_noun"] == "guru" and t["pratyaya"] == "tva"), None))

    def test_taddhita_reverse_vriddhi_edge_cases(self):
        # Testing the reverse_vriddhi function directly via the analyzer
        from skt_morph.taddhita import reverse_vriddhi
        self.assertEqual(reverse_vriddhi("A"), "a")
        self.assertEqual(reverse_vriddhi("E"), "i")
        self.assertEqual(reverse_vriddhi("O"), "u")
        self.assertEqual(reverse_vriddhi("gArgyAyaRa"), "gargyAyaRa") # Note: Phonetic mapping for test purpose
        self.assertEqual(reverse_vriddhi(""), "")
        self.assertEqual(reverse_vriddhi("krm"), "krm") # No vowel match

if __name__ == "__main__": # pragma: no cover
    unittest.main(verbosity=2)
