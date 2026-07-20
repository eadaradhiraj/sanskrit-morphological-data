import re

NAMADHATU_RULES = [
    # kyac (wishing for oneself) -> a/A becomes I. e.g., putrIyati -> putra
    (r'Iya(ti|taH|nti|si|TaH|Ta|mi|vaH|maH|te|yate|yante)$', 'kyac', 'a'), 
    # kyaN (behaving like) -> a becomes A. e.g., SyenAyate -> Syena
    (r'Aya(te|yete|yante|se|yeTe|yaDve|ye|yAvahe|yAmahe)$', 'kyaN', 'a'),
    # kAmyac (wishing for oneself). e.g., putrakAmyati -> putra
    (r'kAmya(ti|taH|nti|si|TaH|Ta|mi|vaH|maH)$', 'kAmyac', ''),
]

def analyze_namadhatu(word_slp1):
    results = []
    for pattern, pratyaya, fallback_vowel in NAMADHATU_RULES:
        match = re.search(pattern, word_slp1)
        if match:
            stem = re.sub(pattern, '', word_slp1)
            base_noun = stem + fallback_vowel if pratyaya in ['kyac', 'kyaN'] and fallback_vowel else stem

            results.append({
                "type": "namadhatu",
                "base_noun": base_noun,
                "pratyaya": pratyaya,
                "meaning_hint": "Desires/behaves like " + base_noun,
                "note": f"Derived algorithmically using {pratyaya} suffix"
            })
    return results
