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
    elif gender == "neuter":
        return {"prathama": [f"{s}am", f"{s}e", f"{s}Ani"], "dvitiya": [f"{s}am", f"{s}e", f"{s}Ani"], "tritiya": [f"{s}ena", f"{s}AByAm", f"{s}EH"], "caturthi": [f"{s}Aya", f"{s}AByAm", f"{s}eByaH"], "panchami": [f"{s}At", f"{s}AByAm", f"{s}eByaH"], "sasthi": [f"{s}asya", f"{s}ayoH", f"{s}AnAm"], "saptami": [f"{s}e", f"{s}ayoH", f"{s}ezu"], "sambodhana": [f"{s}a", f"{s}e", f"{s}Ani"]}
    return {}

def decline_A(base, gender):
    """For ā-kārānta feminine (e.g. kṛtā, ramā)"""
    s = base[:-1]
    if gender == "feminine":
        return {"prathama": [f"{s}A", f"{s}e", f"{s}AH"], "dvitiya": [f"{s}Am", f"{s}e", f"{s}AH"], "tritiya": [f"{s}ayA", f"{s}AByAm", f"{s}ABiH"], "caturthi": [f"{s}AyE", f"{s}AByAm", f"{s}AByaH"], "panchami": [f"{s}AyAH", f"{s}AByAm", f"{s}AByaH"], "sasthi": [f"{s}AyAH", f"{s}ayoH", f"{s}AnAm"], "saptami": [f"{s}AyAm", f"{s}ayoH", f"{s}Asu"], "sambodhana": [f"{s}e", f"{s}e", f"{s}AH"]}
    return {}

def decline_I(base, gender):
    """For ī-kārānta feminine (e.g. kurvatī, nadī)"""
    s = base[:-1]
    if gender == "feminine":
        return {"prathama": [f"{s}I", f"{s}yO", f"{s}yaH"], "dvitiya": [f"{s}Im", f"{s}yO", f"{s}IH"], "tritiya": [f"{s}yA", f"{s}IByAm", f"{s}IBiH"], "caturthi": [f"{s}yE", f"{s}IByAm", f"{s}IByaH"], "panchami": [f"{s}yAH", f"{s}IByAm", f"{s}IByaH"], "sasthi": [f"{s}yAH", f"{s}yoH", f"{s}InAm"], "saptami": [f"{s}yAm", f"{s}yoH", f"{s}Izu"], "sambodhana": [f"{s}i", f"{s}yO", f"{s}yaH"]}
    return {}

def decline_i(base, gender):
    s = base[:-1]
    if gender == "masculine":
        return {"prathama": [f"{s}iH", f"{s}I", f"{s}ayaH"], "dvitiya": [f"{s}im", f"{s}I", f"{s}In"], "tritiya": [f"{s}inA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}aye", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}eH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}eH", f"{s}yoH", f"{s}InAm"], "saptami": [f"{s}O", f"{s}yoH", f"{s}izu"], "sambodhana": [f"{s}e", f"{s}I", f"{s}ayaH"]}
    elif gender == "feminine":
        return {"prathama": [f"{s}iH", f"{s}I", f"{s}ayaH"], "dvitiya": [f"{s}im", f"{s}I", f"{s}IH"], "tritiya": [f"{s}yA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}yE", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}yAH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}yAH", f"{s}yoH", f"{s}InAm"], "saptami": [f"{s}yAm", f"{s}yoH", f"{s}izu"], "sambodhana": [f"{s}e", f"{s}I", f"{s}ayaH"]}
    elif gender == "neuter":
        return {"prathama": [f"{s}i", f"{s}inI", f"{s}Ini"], "dvitiya": [f"{s}i", f"{s}inI", f"{s}Ini"], "tritiya": [f"{s}iRA", f"{s}iByAm", f"{s}iBiH"], "caturthi": [f"{s}iRe", f"{s}iByAm", f"{s}iByaH"], "panchami": [f"{s}inaH", f"{s}iByAm", f"{s}iByaH"], "sasthi": [f"{s}inaH", f"{s}inoH", f"{s}InAm"], "saptami": [f"{s}ini", f"{s}inoH", f"{s}izu"], "sambodhana": [f"{s}i", f"{s}inI", f"{s}Ini"]}
    return {}

def decline_u(base, gender):
    s = base[:-1]
    if gender == "masculine":
        return {"prathama": [f"{s}uH", f"{s}U", f"{s}avaH"], "dvitiya": [f"{s}um", f"{s}U", f"{s}Un"], "tritiya": [f"{s}unA", f"{s}uByAm", f"{s}uBiH"], "caturthi": [f"{s}ave", f"{s}uByAm", f"{s}uByaH"], "panchami": [f"{s}oH", f"{s}uByAm", f"{s}uByaH"], "sasthi": [f"{s}oH", f"{s}voH", f"{s}UnAm"], "saptami": [f"{s}O", f"{s}voH", f"{s}uzu"], "sambodhana": [f"{s}o", f"{s}U", f"{s}avaH"]}
    elif gender == "feminine":
        return {"prathama": [f"{s}uH", f"{s}U", f"{s}avaH"], "dvitiya": [f"{s}um", f"{s}U", f"{s}UH"], "tritiya": [f"{s}vA", f"{s}uByAm", f"{s}uBiH"], "caturthi": [f"{s}vE", f"{s}uByAm", f"{s}uByaH"], "panchami": [f"{s}vAH", f"{s}uByAm", f"{s}uByaH"], "sasthi": [f"{s}vAH", f"{s}voH", f"{s}UnAm"], "saptami": [f"{s}vAm", f"{s}voH", f"{s}uzu"], "sambodhana": [f"{s}o", f"{s}U", f"{s}avaH"]}
    elif gender == "neuter":
        return {"prathama": [f"{s}u", f"{s}unI", f"{s}Uni"], "dvitiya": [f"{s}u", f"{s}unI", f"{s}Uni"], "tritiya": [f"{s}unA", f"{s}uByAm", f"{s}uBiH"], "caturthi": [f"{s}une", f"{s}uByAm", f"{s}uByaH"], "panchami": [f"{s}unaH", f"{s}uByAm", f"{s}uByaH"], "sasthi": [f"{s}unaH", f"{s}unoH", f"{s}UnAm"], "saptami": [f"{s}uni", f"{s}unoH", f"{s}uzu"], "sambodhana": [f"{s}u", f"{s}unI", f"{s}Uni"]}
    return {}

def decline_f(base, gender):
    s = base[:-1]
    if gender == "masculine":
        return {"prathama": [f"{s}A", f"{s}ArO", f"{s}AraH"], "dvitiya": [f"{s}Aram", f"{s}ArO", f"{s}Fn"], "tritiya": [f"{s}rA", f"{s}fByAm", f"{s}fBiH"], "caturthi": [f"{s}re", f"{s}fByAm", f"{s}fByaH"], "panchami": [f"{s}uH", f"{s}fByAm", f"{s}fByaH"], "sasthi": [f"{s}uH", f"{s}roH", f"{s}FRAm"], "saptami": [f"{s}ari", f"{s}roH", f"{s}fzu"], "sambodhana": [f"{s}ar", f"{s}ArO", f"{s}AraH"]}
    elif gender == "feminine":
        return {"prathama": [f"{s}A", f"{s}ArO", f"{s}AraH"], "dvitiya": [f"{s}Aram", f"{s}ArO", f"{s}FH"], "tritiya": [f"{s}rA", f"{s}fByAm", f"{s}fBiH"], "caturthi": [f"{s}re", f"{s}fByAm", f"{s}fByaH"], "panchami": [f"{s}uH", f"{s}fByAm", f"{s}fByaH"], "sasthi": [f"{s}uH", f"{s}roH", f"{s}FRAm"], "saptami": [f"{s}ari", f"{s}roH", f"{s}fzu"], "sambodhana": [f"{s}ar", f"{s}ArO", f"{s}AraH"]}
    elif gender == "neuter":
        return {"prathama": [f"{s}f", f"{s}fRI", f"{s}FNi"], "dvitiya": [f"{s}f", f"{s}fRI", f"{s}FNi"], "tritiya": [f"{s}fRA", f"{s}fByAm", f"{s}fBiH"], "caturthi": [f"{s}fRe", f"{s}fByAm", f"{s}fByaH"], "panchami": [f"{s}fRaH", f"{s}fByAm", f"{s}fByaH"], "sasthi": [f"{s}fRaH", f"{s}fRoH", f"{s}FRAm"], "saptami": [f"{s}fRi", f"{s}fRoH", f"{s}fzu"], "sambodhana": [f"{s}f", f"{s}fRI", f"{s}FNi"]}
    return {}

def decline_at(base, gender):
    """For Śatṛ participles (e.g. gacChat, kurvat)"""
    s = base[:-2]
    if gender == "masculine":
        return {"prathama": [f"{s}an", f"{s}antO", f"{s}antaH"], "dvitiya": [f"{s}antam", f"{s}antO", f"{s}ataH"], "tritiya": [f"{s}atA", f"{s}adByAm", f"{s}adBiH"], "caturthi": [f"{s}ate", f"{s}adByAm", f"{s}adByaH"], "panchami": [f"{s}ataH", f"{s}adByAm", f"{s}adByaH"], "sasthi": [f"{s}ataH", f"{s}atoH", f"{s}atAm"], "saptami": [f"{s}ati", f"{s}atoH", f"{s}atsu"], "sambodhana": [f"{s}an", f"{s}antO", f"{s}antaH"]}
    elif gender == "neuter":
        return {"prathama": [f"{s}at", f"{s}atI", f"{s}anti"], "dvitiya": [f"{s}at", f"{s}atI", f"{s}anti"], "tritiya": [f"{s}atA", f"{s}adByAm", f"{s}adBiH"], "caturthi": [f"{s}ate", f"{s}adByAm", f"{s}adByaH"], "panchami": [f"{s}ataH", f"{s}adByAm", f"{s}adByaH"], "sasthi": [f"{s}ataH", f"{s}atoH", f"{s}atAm"], "saptami": [f"{s}ati", f"{s}atoH", f"{s}atsu"], "sambodhana": [f"{s}an", f"{s}atI", f"{s}anti"]}
    return {}

def decline_noun(base, gender):
    res = {}
    if base.endswith('A'): res = decline_A(base, gender)
    elif base.endswith('I'): res = decline_I(base, gender)
    elif base.endswith('a'): res = decline_a(base, gender)
    elif base.endswith('i'): res = decline_i(base, gender)
    elif base.endswith('u'): res = decline_u(base, gender)
    elif base.endswith('f'): res = decline_f(base, gender)
    elif base.endswith('at'): res = decline_at(base, gender)
    
    if not res:
        raise ValueError(f"Generation for base '{base}' in gender '{gender}' not supported yet.")
        
    for case, forms in res.items():
        res[case] = [apply_natva(w) for w in forms]
    return res
