import re

def apply_natva(word):
    pattern = re.compile(r'([rfFz][aAiIuUfFxXeEoOkKgGNpPbBmyvhM]*)n(?=[aAiIuUfFxXeEoOmyv])')
    while pattern.search(word):
        word = pattern.sub(r'\g<1>R', word)
    return word

def decline_a(base, gender):
    s = base[:-1]
    if gender == "masculine":
        return {"prathama": [f"{s}aH", f"{s}O", f"{s}AH"], "dvitiya": [f"{s}am", f"{s}O", f"{s}An"], "tritiya": [f"{s}ena", f"{s}AByAm", f"{s}EH"], "caturthi": [f"{s}Aya", f"{s}AByAm", f"{s}eByaH"], "panchami": [f"{s}At", f"{s}AByAm", f"{s}eByaH"], "sasthi": [f"{s}asya", f"{s}ayoH", f"{s}AnAm"], "saptami": [f"{s}e", f"{s}ayoH", f"{s}ezu"], "sambodhana": [f"{s}a", f"{s}O", f"{s}AH"]}
    return {}

def decline_i(base, gender):
    s = base[:-1]
    if gender == "masculine":
        return {"prathama": [f"{s}iH", f"{s}I", f"{s}ayaH"], "dvitiya": [f"{s}im", f"{s}I", f"{s}In"], "tritiya": [f"{s}inA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}aye", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}eH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}eH", f"{s}yoH", f"{s}InAm"], "saptami": [f"{s}O", f"{s}yoH", f"{s}izu"], "sambodhana": [f"{s}e", f"{s}I", f"{s}ayaH"]}
    return {}

def decline_u(base, gender):
    s = base[:-1]
    if gender == "masculine":
        return {"prathama": [f"{s}uH", f"{s}U", f"{s}avaH"], "dvitiya": [f"{s}um", f"{s}U", f"{s}Un"], "tritiya": [f"{s}unA", f"{s}uByAm", f"{s}uBiH"], "caturthi": [f"{s}ave", f"{s}uByAm", f"{s}uByaH"], "panchami": [f"{s}oH", f"{s}uByAm", f"{s}uByaH"], "sasthi": [f"{s}oH", f"{s}voH", f"{s}UnAm"], "saptami": [f"{s}O", f"{s}voH", f"{s}uzu"], "sambodhana": [f"{s}o", f"{s}U", f"{s}avaH"]}
    return {}

def decline_f(base, gender):
    s = base[:-1] # For kartf, s = kart
    if gender == "masculine":
        return {
            "prathama": [f"{s}A", f"{s}ArO", f"{s}AraH"],
            "dvitiya": [f"{s}Aram", f"{s}ArO", f"{s}Fn"],
            "tritiya": [f"{s}rA", f"{s}fByAm", f"{s}fBiH"],
            "caturthi": [f"{s}re", f"{s}fByAm", f"{s}fByaH"],
            "panchami": [f"{s}uH", f"{s}fByAm", f"{s}fByaH"],
            "sasthi": [f"{s}uH", f"{s}roH", f"{s}FRAm"],
            "saptami": [f"{s}ari", f"{s}roH", f"{s}fzu"],
            "sambodhana": [f"{s}ar", f"{s}ArO", f"{s}AraH"]
        }
    return {}

def decline_noun(base, gender):
    res = {}
    if base.endswith('a'): res = decline_a(base, gender)
    elif base.endswith('i'): res = decline_i(base, gender)
    elif base.endswith('u'): res = decline_u(base, gender)
    elif base.endswith('f'): res = decline_f(base, gender)
    
    if not res:
        raise ValueError(f"Generation for base '{base}' in gender '{gender}' not supported yet.")
        
    for case, forms in res.items():
        res[case] = [apply_natva(w) for w in forms]
    return res
