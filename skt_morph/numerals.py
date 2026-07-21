NUMERAL_MAP = {
    "eka": {
        "masculine": {"prathama": ["ekaH","",""], "dvitiya": ["ekam","",""], "tritiya": ["ekena","",""], "caturthi": ["ekasmE","",""], "panchami": ["ekasmAt","",""], "sasthi": ["ekasya","",""], "saptami": ["ekasmin","",""]},
        "feminine": {"prathama": ["ekA","",""], "dvitiya": ["ekAm","",""], "tritiya": ["ekayA","",""], "caturthi": ["ekasyE","",""], "panchami": ["ekasyAH","",""], "sasthi": ["ekasyAH","",""], "saptami": ["ekasyAm","",""]},
        "neuter": {"prathama": ["ekam","",""], "dvitiya": ["ekam","",""], "tritiya": ["ekena","",""], "caturthi": ["ekasmE","",""], "panchami": ["ekasmAt","",""], "sasthi": ["ekasya","",""], "saptami": ["ekasmin","",""]}
    },
    "dvi": {
        "masculine": {"prathama": ["","dvO",""], "dvitiya": ["","dvO",""], "tritiya": ["","dvAByAm",""], "caturthi": ["","dvAByAm",""], "panchami": ["","dvAByAm",""], "sasthi": ["","dvayoH",""], "saptami": ["","dvayoH",""]},
        "feminine": {"prathama": ["","dve",""], "dvitiya": ["","dve",""], "tritiya": ["","dvAByAm",""], "caturthi": ["","dvAByAm",""], "panchami": ["","dvAByAm",""], "sasthi": ["","dvayoH",""], "saptami": ["","dvayoH",""]},
        "neuter": {"prathama": ["","dve",""], "dvitiya": ["","dve",""], "tritiya": ["","dvAByAm",""], "caturthi": ["","dvAByAm",""], "panchami": ["","dvAByAm",""], "sasthi": ["","dvayoH",""], "saptami": ["","dvayoH",""]}
    },
    "tri": {
        "masculine": {"prathama": ["","","trayaH"], "dvitiya": ["","","trIn"], "tritiya": ["","","triBiH"], "caturthi": ["","","triByaH"], "panchami": ["","","triByaH"], "sasthi": ["","","trayARAm"], "saptami": ["","","trizu"]},
        "feminine": {"prathama": ["","","tisraH"], "dvitiya": ["","","tisraH"], "tritiya": ["","","tifBiH"], "caturthi": ["","","tifByaH"], "panchami": ["","","tifByaH"], "sasthi": ["","","tifRAm"], "saptami": ["","","tifzu"]},
        "neuter": {"prathama": ["","","trIRi"], "dvitiya": ["","","trIRi"], "tritiya": ["","","triBiH"], "caturthi": ["","","triByaH"], "panchami": ["","","triByaH"], "sasthi": ["","","trayARAm"], "saptami": ["","","trizu"]}
    },
    "catur": {
        "masculine": {"prathama": ["","","catvAraH"], "dvitiya": ["","","caturaH"], "tritiya": ["","","caturBiH"], "caturthi": ["","","caturByaH"], "panchami": ["","","caturByaH"], "sasthi": ["","","caturRAm"], "saptami": ["","","caturzu"]},
        "feminine": {"prathama": ["","","catasraH"], "dvitiya": ["","","catasraH"], "tritiya": ["","","catasfBiH"], "caturthi": ["","","catasfByaH"], "panchami": ["","","catasfByaH"], "sasthi": ["","","catasfRAm"], "saptami": ["","","catasfzu"]},
        "neuter": {"prathama": ["","","catvAri"], "dvitiya": ["","","catvAri"], "tritiya": ["","","caturBiH"], "caturthi": ["","","caturByaH"], "panchami": ["","","caturByaH"], "sasthi": ["","","caturRAm"], "saptami": ["","","caturzu"]}
    },
    "paYcan": {
        "any": {"prathama": ["","","paYca"], "dvitiya": ["","","paYca"], "tritiya": ["","","paYcaBiH"], "caturthi": ["","","paYcaByaH"], "panchami": ["","","paYcaByaH"], "sasthi": ["","","paYcAnAm"], "saptami": ["","","paYcasu"]}
    },
    "zaz": {
        "any": {"prathama": ["","","zaw"], "dvitiya": ["","","zaw"], "tritiya": ["","","zaqBiH"], "caturthi": ["","","zaqByaH"], "panchami": ["","","zaqByaH"], "sasthi": ["","","zaRRAm"], "saptami": ["","","zawsu"]}
    },
    "saptan": {
        "any": {"prathama": ["","","sapta"], "dvitiya": ["","","sapta"], "tritiya": ["","","saptaBiH"], "caturthi": ["","","saptaByaH"], "panchami": ["","","saptaByaH"], "sasthi": ["","","saptAnAm"], "saptami": ["","","saptasu"]}
    },
    "azwan": {
        "any": {"prathama": ["","","azwO"], "dvitiya": ["","","azwO"], "tritiya": ["","","azwABiH"], "caturthi": ["","","azwAByaH"], "panchami": ["","","azwAByaH"], "sasthi": ["","","azwAnAm"], "saptami": ["","","azwAsu"]}
    },
    "navan": {
        "any": {"prathama": ["","","nava"], "dvitiya": ["","","nava"], "tritiya": ["","","navaBiH"], "caturthi": ["","","navaByaH"], "panchami": ["","","navaByaH"], "sasthi": ["","","navAnAm"], "saptami": ["","","navasu"]}
    },
    "daSan": {
        "any": {"prathama": ["","","daSa"], "dvitiya": ["","","daSa"], "tritiya": ["","","daSaBiH"], "caturthi": ["","","daSaByaH"], "panchami": ["","","daSaByaH"], "sasthi": ["","","daSAnAm"], "saptami": ["","","daSasu"]}
    }
}

def analyze_numeral(word_slp1):
    results = []
    for base, genders in NUMERAL_MAP.items():
        for gender, declensions in genders.items():
            for case, forms in declensions.items():
                for i, form in enumerate(forms):
                    if form == word_slp1:
                        vacana = ["eka", "dvi", "bahu"][i]
                        results.append({
                            "type": "numeral", "base_form": base,
                            "gender": gender, "case": case, "vacana": vacana
                        })
    return results

def decline_numeral(base, gender="any"):
    if base in NUMERAL_MAP:
        if gender in NUMERAL_MAP[base]: return NUMERAL_MAP[base][gender]
        elif "any" in NUMERAL_MAP[base]: return NUMERAL_MAP[base]["any"]
    raise ValueError(f"Numeral {base} in gender {gender} not supported.")
