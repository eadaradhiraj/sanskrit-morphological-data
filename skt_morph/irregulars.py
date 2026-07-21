IRREGULAR_NOUNS_MAP = {
    "go": {
        "masculine": {"prathama": ["gOH", "gAvO", "gAvaH"], "dvitiya": ["gAm", "gAvO", "gAH"], "tritiya": ["gavA", "goByAm", "goBiH"], "caturthi": ["gave", "goByAm", "goByaH"], "panchami": ["goH", "goByAm", "goByaH"], "sasthi": ["goH", "gavoH", "gavAm"], "saptami": ["gavi", "gavoH", "gozu"], "sambodhana": ["gOH", "gAvO", "gAvaH"]},
        "feminine": {"prathama": ["gOH", "gAvO", "gAvaH"], "dvitiya": ["gAm", "gAvO", "gAH"], "tritiya": ["gavA", "goByAm", "goBiH"], "caturthi": ["gave", "goByAm", "goByaH"], "panchami": ["goH", "goByAm", "goByaH"], "sasthi": ["goH", "gavoH", "gavAm"], "saptami": ["gavi", "gavoH", "gozu"], "sambodhana": ["gOH", "gAvO", "gAvaH"]}
    },
    "nau": {
        "feminine": {"prathama": ["nOH", "nAvO", "nAvaH"], "dvitiya": ["nAvam", "nAvO", "nAH"], "tritiya": ["nAvA", "nOByAm", "nOBiH"], "caturthi": ["nAve", "nOByAm", "nOByaH"], "panchami": ["nAvaH", "nOByAm", "nOByaH"], "sasthi": ["nAvaH", "nAvoH", "nAvAm"], "saptami": ["nAvi", "nAvoH", "nOzu"], "sambodhana": ["nOH", "nAvO", "nAvaH"]}
    },
    "sakhi": {
        "masculine": {"prathama": ["saKA", "saKAyO", "saKAyaH"], "dvitiya": ["saKAyam", "saKAyO", "saKIn"], "tritiya": ["saKyA", "saKiByAm", "saKiBiH"], "caturthi": ["saKye", "saKiByAm", "saKiByaH"], "panchami": ["saKyuH", "saKiByAm", "saKiByaH"], "sasthi": ["saKyuH", "saKyoH", "saKInAm"], "saptami": ["saKyO", "saKyoH", "saKizu"], "sambodhana": ["saKe", "saKAyO", "saKAyaH"]}
    },
    "pati": {
        "masculine": {"prathama": ["patiH", "patI", "patayaH"], "dvitiya": ["patim", "patI", "patIn"], "tritiya": ["patyA", "patiByAm", "patiBiH"], "caturthi": ["patye", "patiByAm", "patiByaH"], "panchami": ["patyuH", "patiByAm", "patiByaH"], "sasthi": ["patyuH", "patyoH", "patInAm"], "saptami": ["patyO", "patyoH", "patizu"], "sambodhana": ["pate", "patI", "patayaH"]}
    },
    "strI": {
        "feminine": {"prathama": ["strI", "striyO", "striyaH"], "dvitiya": ["striyam", "striyO", "striyaH"], "tritiya": ["striyA", "strIByAm", "strIBiH"], "caturthi": ["striyE", "strIByAm", "strIByaH"], "panchami": ["striyAH", "strIByAm", "strIByaH"], "sasthi": ["striyAH", "striyoH", "strIRAm"], "saptami": ["striyAm", "striyoH", "strIzu"], "sambodhana": ["stri", "striyO", "striyaH"]}
    },
    "prAYc": {
        "masculine": {"prathama": ["prAN", "prAYcO", "prAYcaH"], "dvitiya": ["prAYcam", "prAYcO", "prAcaH"], "tritiya": ["prAcA", "prAgByAm", "prAgBiH"], "caturthi": ["prAce", "prAgByAm", "prAgByaH"], "panchami": ["prAcaH", "prAgByAm", "prAgByaH"], "sasthi": ["prAcaH", "prAcoH", "prAcAm"], "saptami": ["prAci", "prAcoH", "prAkzu"], "sambodhana": ["prAN", "prAYcO", "prAYcaH"]}
    },
    "pratyaYc": {
        "masculine": {"prathama": ["pratyaN", "pratyaYcO", "pratyaYcaH"], "dvitiya": ["pratyaYcam", "pratyaYcO", "pratIcaH"], "tritiya": ["pratIcA", "pratyagByAm", "pratyagBiH"], "caturthi": ["pratIce", "pratyagByAm", "pratyagByaH"], "panchami": ["pratIcaH", "pratyagByAm", "pratyagByaH"], "sasthi": ["pratIcaH", "pratIcoH", "pratIcAm"], "saptami": ["pratIci", "pratIcoH", "pratyakzu"], "sambodhana": ["pratyaN", "pratyaYcO", "pratyaYcaH"]}
    }
}

def analyze_irregular(word_slp1):
    results = []
    for base, genders in IRREGULAR_NOUNS_MAP.items():
        for gender, declensions in genders.items():
            for case, forms in declensions.items():
                for i, form in enumerate(forms):
                    if form == word_slp1:
                        vacana = ["eka", "dvi", "bahu"][i]
                        results.append({
                            "type": "irregular_noun", "base_form": base,
                            "gender": gender, "case": case, "vacana": vacana
                        })
    return results

def decline_irregular(base, gender):
    if base in IRREGULAR_NOUNS_MAP and gender in IRREGULAR_NOUNS_MAP[base]:
        return IRREGULAR_NOUNS_MAP[base][gender]
    return None
