PRONOUN_MAP = {
    "tad": {
        "masculine": {"prathama": ["saH", "tO", "te"], "dvitiya": ["tam", "tO", "tAn"], "tritiya": ["tena", "tAByAm", "tEH"], "caturthi": ["tasmE", "tAByAm", "teByaH"], "panchami": ["tasmAt", "tAByAm", "teByaH"], "sasthi": ["tasya", "tayoH", "tezAm"], "saptami": ["tasmin", "tayoH", "tezu"]},
        "feminine": {"prathama": ["sA", "te", "tAH"], "dvitiya": ["tAm", "te", "tAH"], "tritiya": ["tayA", "tAByAm", "tABiH"], "caturthi": ["tasyE", "tAByAm", "tAByaH"], "panchami": ["tasyAH", "tAByAm", "tAByaH"], "sasthi": ["tasyAH", "tayoH", "tAsAm"], "saptami": ["tasyAm", "tayoH", "tAsu"]},
        "neuter": {"prathama": ["tat", "te", "tAni"], "dvitiya": ["tat", "te", "tAni"], "tritiya": ["tena", "tAByAm", "tEH"], "caturthi": ["tasmE", "tAByAm", "teByaH"], "panchami": ["tasmAt", "tAByAm", "teByaH"], "sasthi": ["tasya", "tayoH", "tezAm"], "saptami": ["tasmin", "tayoH", "tezu"]}
    },
    "kim": {
        "masculine": {"prathama": ["kaH", "kO", "ke"], "dvitiya": ["kam", "kO", "kAn"], "tritiya": ["kena", "kAByAm", "kEH"], "caturthi": ["kasmE", "kAByAm", "keByaH"], "panchami": ["kasmAt", "kAByAm", "keByaH"], "sasthi": ["kasya", "kayoH", "kezAm"], "saptami": ["kasmin", "kayoH", "kezu"]},
        "feminine": {"prathama": ["kA", "ke", "kAH"], "dvitiya": ["kAm", "ke", "kAH"], "tritiya": ["kayA", "kAByAm", "kABiH"], "caturthi": ["kasyE", "kAByAm", "kAByaH"], "panchami": ["kasyAH", "kAByAm", "kAByaH"], "sasthi": ["kasyAH", "kayoH", "kAsAm"], "saptami": ["kasyAm", "kayoH", "kAsu"]},
        "neuter": {"prathama": ["kim", "ke", "kAni"], "dvitiya": ["kim", "ke", "kAni"], "tritiya": ["kena", "kAByAm", "kEH"], "caturthi": ["kasmE", "kAByAm", "keByaH"], "panchami": ["kasmAt", "kAByAm", "keByaH"], "sasthi": ["kasya", "kayoH", "kezAm"], "saptami": ["kasmin", "kayoH", "kezu"]}
    },
    "asmad": {
        "any": {"prathama": ["aham", "AvAm", "vayam"], "dvitiya": ["mAm", "AvAm", "asmAn"], "tritiya": ["mayA", "AvAByAm", "asmaBiH"], "caturthi": ["mahyam", "AvAByAm", "asmaByam"], "panchami": ["mat", "AvAByAm", "asmat"], "sasthi": ["mama", "AvayoH", "asmAkam"], "saptami": ["mayi", "AvayoH", "asmAsu"]}
    },
    "yuzmad": {
        "any": {"prathama": ["tvam", "yuvAm", "yUyam"], "dvitiya": ["tvAm", "yuvAm", "yuzmAn"], "tritiya": ["tvayA", "yuvAByAm", "yuzmaBiH"], "caturthi": ["tuByam", "yuvAByAm", "yuzmaByam"], "panchami": ["tvat", "yuvAByAm", "yuzmat"], "sasthi": ["tava", "yuvayoH", "yuzmAkam"], "saptami": ["tvayi", "yuvayoH", "yuzmAsu"]}
    }
}

def analyze_pronoun(word_slp1):
    results = []
    for base, genders in PRONOUN_MAP.items():
        for gender, declensions in genders.items():
            for case, forms in declensions.items():
                for i, form in enumerate(forms):
                    if form == word_slp1:
                        vacana = ["eka", "dvi", "bahu"][i]
                        results.append({
                            "type": "pronoun", "base_form": base,
                            "gender": gender, "case": case, "vacana": vacana
                        })
    return results

def decline_pronoun(base, gender="any"):
    if base in PRONOUN_MAP:
        if gender in PRONOUN_MAP[base]: return PRONOUN_MAP[base][gender]
        elif "any" in PRONOUN_MAP[base]: return PRONOUN_MAP[base]["any"]
    raise ValueError(f"Pronoun {base} in gender {gender} not supported.")
