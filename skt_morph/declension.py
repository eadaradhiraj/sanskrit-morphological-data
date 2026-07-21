import re
from .irregulars import decline_irregular

def apply_natva(word):
    pattern = re.compile(r'([rfFz][aAiIuUfFxXeEoOkKgGNpPbBmyvhM]*)n(?=[aAiIuUfFxXeEoOmyv])')
    while pattern.search(word): word = pattern.sub(r'\g<1>R', word)
    return word

def decline_a(base, gender):
    s = base[:-1]
    if gender == "masculine": return {"prathama": [f"{s}aH", f"{s}O", f"{s}AH"], "dvitiya": [f"{s}am", f"{s}O", f"{s}An"], "tritiya": [f"{s}ena", f"{s}AByAm", f"{s}EH"], "caturthi": [f"{s}Aya", f"{s}AByAm", f"{s}eByaH"], "panchami": [f"{s}At", f"{s}AByAm", f"{s}eByaH"], "sasthi": [f"{s}asya", f"{s}ayoH", f"{s}AnAm"], "saptami": [f"{s}e", f"{s}ayoH", f"{s}ezu"], "sambodhana": [f"{s}a", f"{s}O", f"{s}AH"]}
    elif gender == "neuter": return {"prathama": [f"{s}am", f"{s}e", f"{s}Ani"], "dvitiya": [f"{s}am", f"{s}e", f"{s}Ani"], "tritiya": [f"{s}ena", f"{s}AByAm", f"{s}EH"], "caturthi": [f"{s}Aya", f"{s}AByAm", f"{s}eByaH"], "panchami": [f"{s}At", f"{s}AByAm", f"{s}eByaH"], "sasthi": [f"{s}asya", f"{s}ayoH", f"{s}AnAm"], "saptami": [f"{s}e", f"{s}ayoH", f"{s}ezu"], "sambodhana": [f"{s}a", f"{s}e", f"{s}Ani"]}
    return {}

def decline_A(base, gender):
    s = base[:-1]
    if gender == "feminine": return {"prathama": [f"{s}A", f"{s}e", f"{s}AH"], "dvitiya": [f"{s}Am", f"{s}e", f"{s}AH"], "tritiya": [f"{s}ayA", f"{s}AByAm", f"{s}ABiH"], "caturthi": [f"{s}AyE", f"{s}AByAm", f"{s}AByaH"], "panchami": [f"{s}AyAH", f"{s}AByAm", f"{s}AByaH"], "sasthi": [f"{s}AyAH", f"{s}ayoH", f"{s}AnAm"], "saptami": [f"{s}AyAm", f"{s}ayoH", f"{s}Asu"], "sambodhana": [f"{s}e", f"{s}e", f"{s}AH"]}
    return {}

def decline_I(base, gender):
    s = base[:-1]
    if gender == "feminine": return {"prathama": [f"{s}I", f"{s}yO", f"{s}yaH"], "dvitiya": [f"{s}Im", f"{s}yO", f"{s}IH"], "tritiya": [f"{s}yA", f"{s}IByAm", f"{s}IBiH"], "caturthi": [f"{s}yE", f"{s}IByAm", f"{s}IByaH"], "panchami": [f"{s}yAH", f"{s}IByAm", f"{s}IByaH"], "sasthi": [f"{s}yAH", f"{s}yoH", f"{s}InAm"], "saptami": [f"{s}yAm", f"{s}yoH", f"{s}Izu"], "sambodhana": [f"{s}i", f"{s}yO", f"{s}yaH"]}
    return {}

def decline_i(base, gender):
    s = base[:-1]
    if gender == "masculine": return {"prathama": [f"{s}iH", f"{s}I", f"{s}ayaH"], "dvitiya": [f"{s}im", f"{s}I", f"{s}In"], "tritiya": [f"{s}inA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}aye", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}eH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}eH", f"{s}yoH", f"{s}InAm"], "saptami": [f"{s}O", f"{s}yoH", f"{s}izu"], "sambodhana": [f"{s}e", f"{s}I", f"{s}ayaH"]}
    elif gender == "feminine": return {"prathama": [f"{s}iH", f"{s}I", f"{s}ayaH"], "dvitiya": [f"{s}im", f"{s}I", f"{s}IH"], "tritiya": [f"{s}yA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}yE", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}yAH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}yAH", f"{s}yoH", f"{s}InAm"], "saptami": [f"{s}yAm", f"{s}yoH", f"{s}izu"], "sambodhana": [f"{s}e", f"{s}I", f"{s}ayaH"]}
    elif gender == "neuter": return {"prathama": [f"{s}i", f"{s}inI", f"{s}Ini"], "dvitiya": [f"{s}i", f"{s}inI", f"{s}Ini"], "tritiya": [f"{s}iRA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}iRe", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}inaH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}inaH", f"{s}inoH", f"{s}InAm"], "saptami": [f"{s}ini", f"{s}inoH", f"{s}izu"], "sambodhana": [f"{s}i", f"{s}inI", f"{s}Ini"]}
    return {}

def decline_u(base, gender):
    s = base[:-1]
    if gender == "masculine": return {"prathama": [f"{s}uH", f"{s}U", f"{s}avaH"], "dvitiya": [f"{s}um", f"{s}U", f"{s}Un"], "tritiya": [f"{s}unA", f"{s}uByAm", f"{s}uBiH"], "caturthi": [f"{s}ave", f"{s}uByAm", f"{s}uByaH"], "panchami": [f"{s}oH", f"{s}uByAm", f"{s}uByaH"], "sasthi": [f"{s}oH", f"{s}voH", f"{s}UnAm"], "saptami": [f"{s}O", f"{s}voH", f"{s}uzu"], "sambodhana": [f"{s}o", f"{s}U", f"{s}avaH"]}
    elif gender == "feminine": return {"prathama": [f"{s}uH", f"{s}U", f"{s}avaH"], "dvitiya": [f"{s}um", f"{s}U", f"{s}UH"], "tritiya": [f"{s}vA", f"{s}uByAm", f"{s}uBiH"], "caturthi": [f"{s}vE", f"{s}uByAm", f"{s}uByaH"], "panchami": [f"{s}vAH", f"{s}uByAm", f"{s}uByaH"], "sasthi": [f"{s}vAH", f"{s}voH", f"{s}UnAm"], "saptami": [f"{s}vAm", f"{s}voH", f"{s}uzu"], "sambodhana": [f"{s}o", f"{s}U", f"{s}avaH"]}
    elif gender == "neuter": return {"prathama": [f"{s}u", f"{s}unI", f"{s}Uni"], "dvitiya": [f"{s}u", f"{s}unI", f"{s}Uni"], "tritiya": [f"{s}unA", f"{s}uByAm", f"{s}uBiH"], "caturthi": [f"{s}une", f"{s}uByAm", f"{s}uByaH"], "panchami": [f"{s}unaH", f"{s}uByAm", f"{s}uByaH"], "sasthi": [f"{s}unaH", f"{s}unoH", f"{s}UnAm"], "saptami": [f"{s}uni", f"{s}unoH", f"{s}uzu"], "sambodhana": [f"{s}u", f"{s}unI", f"{s}Uni"]}
    return {}

def decline_f(base, gender):
    s = base[:-1]
    if gender == "masculine": return {"prathama": [f"{s}A", f"{s}ArO", f"{s}AraH"], "dvitiya": [f"{s}Aram", f"{s}ArO", f"{s}Fn"], "tritiya": [f"{s}rA", f"{s}fByAm", f"{s}fBiH"], "caturthi": [f"{s}re", f"{s}fByAm", f"{s}fByaH"], "panchami": [f"{s}uH", f"{s}fByAm", f"{s}fByaH"], "sasthi": [f"{s}uH", f"{s}roH", f"{s}FRAm"], "saptami": [f"{s}ari", f"{s}roH", f"{s}fzu"], "sambodhana": [f"{s}ar", f"{s}ArO", f"{s}AraH"]}
    elif gender == "feminine": return {"prathama": [f"{s}A", f"{s}ArO", f"{s}AraH"], "dvitiya": [f"{s}Aram", f"{s}ArO", f"{s}FH"], "tritiya": [f"{s}rA", f"{s}fByAm", f"{s}fBiH"], "caturthi": [f"{s}re", f"{s}fByAm", f"{s}fByaH"], "panchami": [f"{s}uH", f"{s}fByAm", f"{s}fByaH"], "sasthi": [f"{s}uH", f"{s}roH", f"{s}FRAm"], "saptami": [f"{s}ari", f"{s}roH", f"{s}fzu"], "sambodhana": [f"{s}ar", f"{s}ArO", f"{s}AraH"]}
    elif gender == "neuter": return {"prathama": [f"{s}f", f"{s}fRI", f"{s}FNi"], "dvitiya": [f"{s}f", f"{s}fRI", f"{s}FNi"], "tritiya": [f"{s}fRA", f"{s}fByAm", f"{s}fBiH"], "caturthi": [f"{s}fRe", f"{s}fByAm", f"{s}fByaH"], "panchami": [f"{s}fRaH", f"{s}fByAm", f"{s}fByaH"], "sasthi": [f"{s}fRaH", f"{s}fRoH", f"{s}FRAm"], "saptami": [f"{s}fRi", f"{s}fRoH", f"{s}fzu"], "sambodhana": [f"{s}f", f"{s}fRI", f"{s}FNi"]}
    return {}

def decline_at(base, gender):
    s = base[:-2]
    if gender == "masculine": return {"prathama": [f"{s}an", f"{s}antO", f"{s}antaH"], "dvitiya": [f"{s}antam", f"{s}antO", f"{s}ataH"], "tritiya": [f"{s}atA", f"{s}adByAm", f"{s}adBiH"], "caturthi": [f"{s}ate", f"{s}adByAm", f"{s}adByaH"], "panchami": [f"{s}ataH", f"{s}adByAm", f"{s}adByaH"], "sasthi": [f"{s}ataH", f"{s}atoH", f"{s}atAm"], "saptami": [f"{s}ati", f"{s}atoH", f"{s}atsu"], "sambodhana": [f"{s}an", f"{s}antO", f"{s}antaH"]}
    elif gender == "neuter": return {"prathama": [f"{s}at", f"{s}atI", f"{s}anti"], "dvitiya": [f"{s}at", f"{s}atI", f"{s}anti"], "tritiya": [f"{s}atA", f"{s}adByAm", f"{s}adBiH"], "caturthi": [f"{s}ate", f"{s}adByAm", f"{s}adByaH"], "panchami": [f"{s}ataH", f"{s}adByAm", f"{s}adByaH"], "sasthi": [f"{s}ataH", f"{s}atoH", f"{s}atAm"], "saptami": [f"{s}ati", f"{s}atoH", f"{s}atsu"], "sambodhana": [f"{s}an", f"{s}atI", f"{s}anti"]}
    return {}

def decline_an(base, gender):
    s = base[:-2]
    if gender == "masculine": return {"prathama": [f"{s}A", f"{s}AnO", f"{s}AnaH"], "dvitiya": [f"{s}Anam", f"{s}AnO", f"{s}naH"], "tritiya": [f"{s}nA", f"{s}aByAm", f"{s}aBiH"], "caturthi": [f"{s}ne", f"{s}aByAm", f"{s}aByaH"], "panchami": [f"{s}naH", f"{s}aByAm", f"{s}aByaH"], "sasthi": [f"{s}naH", f"{s}noH", f"{s}nAm"], "saptami": [f"{s}ni", f"{s}noH", f"{s}asu"], "sambodhana": [f"{s}an", f"{s}AnO", f"{s}AnaH"]}
    return {}

def decline_in(base, gender):
    s = base[:-2]
    if gender == "masculine": return {"prathama": [f"{s}I", f"{s}inO", f"{s}inaH"], "dvitiya": [f"{s}inam", f"{s}inO", f"{s}inaH"], "tritiya": [f"{s}inA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}ine", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}inaH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}inaH", f"{s}inoH", f"{s}inAm"], "saptami": [f"{s}ini", f"{s}inoH", f"{s}izu"], "sambodhana": [f"{s}in", f"{s}inO", f"{s}inaH"]}
    return {}

def decline_as(base, gender):
    s = base[:-2]
    if gender == "neuter": return {"prathama": [f"{s}aH", f"{s}asI", f"{s}AMsi"], "dvitiya": [f"{s}aH", f"{s}asI", f"{s}AMsi"], "tritiya": [f"{s}asA", f"{s}oByAm", f"{s}oBiH"], "caturthi": [f"{s}ase", f"{s}oByAm", f"{s}oByaH"], "panchami": [f"{s}asaH", f"{s}oByAm", f"{s}oByaH"], "sasthi": [f"{s}asaH", f"{s}asoH", f"{s}asAm"], "saptami": [f"{s}asi", f"{s}asoH", f"{s}aHsu"], "sambodhana": [f"{s}aH", f"{s}asI", f"{s}AMsi"]}
    return {}

def decline_t(base, gender):
    s = base[:-1]
    if gender in ["masculine", "neuter"]: return {"prathama": [f"{s}t", f"{s}tO", f"{s}taH"], "dvitiya": [f"{s}tam", f"{s}tO", f"{s}taH"], "tritiya": [f"{s}tA", f"{s}dByAm", f"{s}dBiH"], "caturthi": [f"{s}te", f"{s}dByAm", f"{s}dByaH"], "panchami": [f"{s}taH", f"{s}dByAm", f"{s}dByaH"], "sasthi": [f"{s}taH", f"{s}toH", f"{s}tAm"], "saptami": [f"{s}ti", f"{s}toH", f"{s}tsu"], "sambodhana": [f"{s}t", f"{s}tO", f"{s}taH"]}
    return {}

def decline_c(base, gender):
    s = base[:-1]
    if gender in ["masculine", "feminine"]: return {"prathama": [f"{s}k", f"{base}O", f"{base}aH"], "dvitiya": [f"{base}am", f"{base}O", f"{base}aH"], "tritiya": [f"{base}A", f"{s}gByAm", f"{s}gBiH"], "caturthi": [f"{base}e", f"{s}gByAm", f"{s}gByaH"], "panchami": [f"{base}aH", f"{s}gByAm", f"{s}gByaH"], "sasthi": [f"{base}aH", f"{base}oH", f"{base}Am"], "saptami": [f"{base}i", f"{base}oH", f"{s}kzu"], "sambodhana": [f"{s}k", f"{base}O", f"{base}aH"]}
    return {}

def decline_j(base, gender):
    s = base[:-1]
    if gender in ["masculine", "feminine"]: return {"prathama": [f"{s}k", f"{base}O", f"{base}aH"], "dvitiya": [f"{base}am", f"{base}O", f"{base}aH"], "tritiya": [f"{base}A", f"{s}gByAm", f"{s}gBiH"], "caturthi": [f"{base}e", f"{s}gByAm", f"{s}gByaH"], "panchami": [f"{base}aH", f"{s}gByAm", f"{s}gByaH"], "sasthi": [f"{base}aH", f"{base}oH", f"{base}Am"], "saptami": [f"{base}i", f"{base}oH", f"{s}kzu"], "sambodhana": [f"{s}k", f"{base}O", f"{base}aH"]}
    return {}

def decline_S(base, gender):
    s = base[:-1]
    if gender in ["masculine", "feminine"]: return {"prathama": [f"{s}k", f"{base}O", f"{base}aH"], "dvitiya": [f"{base}am", f"{base}O", f"{base}aH"], "tritiya": [f"{base}A", f"{s}gByAm", f"{s}gBiH"], "caturthi": [f"{base}e", f"{s}gByAm", f"{s}gByaH"], "panchami": [f"{base}aH", f"{s}gByAm", f"{s}gByaH"], "sasthi": [f"{base}aH", f"{base}oH", f"{base}Am"], "saptami": [f"{base}i", f"{base}oH", f"{s}kzu"], "sambodhana": [f"{s}k", f"{base}O", f"{base}aH"]}
    return {}

def decline_z(base, gender):
    s = base[:-1]
    if gender in ["masculine", "feminine"]: return {"prathama": [f"{s}w", f"{base}O", f"{base}aH"], "dvitiya": [f"{base}am", f"{base}O", f"{base}aH"], "tritiya": [f"{base}A", f"{s}qByAm", f"{s}qBiH"], "caturthi": [f"{base}e", f"{s}qByAm", f"{s}qByaH"], "panchami": [f"{base}aH", f"{s}qByAm", f"{s}qByaH"], "sasthi": [f"{base}aH", f"{base}oH", f"{base}Am"], "saptami": [f"{base}i", f"{base}oH", f"{s}wsu"], "sambodhana": [f"{s}w", f"{base}O", f"{base}aH"]}
    return {}

def decline_h(base, gender):
    s = base[:-1]
    if gender in ["masculine", "feminine"]: return {"prathama": [f"{s}w", f"{base}O", f"{base}aH"], "dvitiya": [f"{base}am", f"{base}O", f"{base}aH"], "tritiya": [f"{base}A", f"{s}qByAm", f"{s}qBiH"], "caturthi": [f"{base}e", f"{s}qByAm", f"{s}qByaH"], "panchami": [f"{base}aH", f"{s}qByAm", f"{s}qByaH"], "sasthi": [f"{base}aH", f"{base}oH", f"{base}Am"], "saptami": [f"{base}i", f"{base}oH", f"{s}wsu"], "sambodhana": [f"{s}w", f"{base}O", f"{base}aH"]}
    return {}

def decline_noun(base, gender):
    # First, check if it's an irregular noun that bypasses math
    irreg = decline_irregular(base, gender)
    if irreg: return irreg
    
    res = {}
    if base.endswith('A'): res = decline_A(base, gender)
    elif base.endswith('I'): res = decline_I(base, gender)
    elif base.endswith('a'): res = decline_a(base, gender)
    elif base.endswith('i'): res = decline_i(base, gender)
    elif base.endswith('u'): res = decline_u(base, gender)
    elif base.endswith('f'): res = decline_f(base, gender)
    elif base.endswith('at'): res = decline_at(base, gender)
    elif base.endswith('an'): res = decline_an(base, gender)
    elif base.endswith('in'): res = decline_in(base, gender)
    elif base.endswith('as'): res = decline_as(base, gender)
    elif base.endswith('t'): res = decline_t(base, gender)
    elif base.endswith('c'): res = decline_c(base, gender)
    elif base.endswith('j'): res = decline_j(base, gender)
    elif base.endswith('S'): res = decline_S(base, gender)
    elif base.endswith('z'): res = decline_z(base, gender)
    elif base.endswith('h'): res = decline_h(base, gender)
    if not res: raise ValueError(f"Generation for base '{base}' in gender '{gender}' not supported yet.")
    for case, forms in res.items(): res[case] = [apply_natva(w) for w in forms]
    return res
