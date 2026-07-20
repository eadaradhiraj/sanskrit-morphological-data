import re

STEMMING_RULES = [
    (r'aH$', 'a', 'masc', 'prathama', 'eka'), (r'O$', 'a', 'masc', 'prathama/dvitiya', 'dvi'), (r'AH$', 'a', 'masc', 'prathama', 'bahu'),
    (r'am$', 'a', 'masc/neut', 'dvitiya/prathama', 'eka'), (r'An$', 'a', 'masc', 'dvitiya', 'bahu'), (r'e[nR]a$', 'a', 'masc/neut', 'tritiya', 'eka'),
    (r'AByAm$', 'a', 'masc/neut', 'tritiya/caturthi/panchami', 'dvi'), (r'EH$', 'a', 'masc/neut', 'tritiya', 'bahu'),
    (r'Aya$', 'a', 'masc/neut', 'caturthi', 'eka'), (r'eByaH$', 'a', 'masc/neut', 'caturthi/panchami', 'bahu'),
    (r'At$', 'a', 'masc/neut', 'panchami', 'eka'), (r'asya$', 'a', 'masc/neut', 'sasthi', 'eka'),
    (r'ayoH$', 'a', 'masc/neut', 'sasthi/saptami', 'dvi'), (r'A[nR]Am$', 'a', 'masc/neut', 'sasthi', 'bahu'),
    (r'e$', 'a', 'masc/neut', 'saptami', 'eka'), (r'ezu$', 'a', 'masc/neut', 'saptami', 'bahu'), (r'Ani$', 'a', 'neut', 'prathama/dvitiya', 'bahu'),
    (r'iH$', 'i', 'masc/fem', 'prathama', 'eka'), (r'im$', 'i', 'masc/fem/neut', 'dvitiya/prathama', 'eka'), (r'In$', 'i', 'masc', 'dvitiya', 'bahu'),
    (r'IH$', 'i', 'fem', 'prathama/dvitiya', 'bahu'), (r'i[nR]A$', 'i', 'masc/neut', 'tritiya', 'eka'), (r'yA$', 'i', 'fem', 'tritiya', 'eka'),
    (r'aye$', 'i', 'masc/fem', 'caturthi', 'eka'), (r'yE$', 'i', 'fem', 'caturthi', 'eka'), (r'eH$', 'i', 'masc/fem', 'panchami/sasthi', 'eka'),
    (r'yAH$', 'i', 'fem', 'panchami/sasthi', 'eka'), (r'yAm$', 'i', 'fem', 'saptami', 'eka'), (r'I[nR]Am$', 'i', 'masc/fem/neut', 'sasthi', 'bahu'),
    (r'izu$', 'i', 'masc/fem/neut', 'saptami', 'bahu'), (r'iByAm$', 'i', 'masc/fem/neut', 'tritiya/caturthi/panchami', 'dvi'),
    (r'iByaH$', 'i', 'masc/fem/neut', 'caturthi/panchami', 'bahu'), (r'iBiH$', 'i', 'masc/fem/neut', 'tritiya', 'bahu'),
    (r'I$', 'i', 'masc/fem/neut', 'prathama/dvitiya', 'dvi'), (r'ayaH$', 'i', 'masc/fem', 'prathama', 'bahu'), (r'Ini$', 'i', 'neut', 'prathama/dvitiya', 'bahu'),
    (r'uH$', 'u', 'masc/fem', 'prathama', 'eka'), (r'um$', 'u', 'masc/fem/neut', 'dvitiya/prathama', 'eka'), (r'Un$', 'u', 'masc', 'dvitiya', 'bahu'),
    (r'UH$', 'u', 'fem', 'prathama/dvitiya', 'bahu'), (r'u[nR]A$', 'u', 'masc/neut', 'tritiya', 'eka'), (r'vA$', 'u', 'fem', 'tritiya', 'eka'),
    (r'ave$', 'u', 'masc/fem', 'caturthi', 'eka'), (r'vE$', 'u', 'fem', 'caturthi', 'eka'), (r'oH$', 'u', 'masc/fem', 'panchami/sasthi', 'eka'),
    (r'vAH$', 'u', 'fem', 'panchami/sasthi', 'eka'), (r'vAm$', 'u', 'fem', 'saptami', 'eka'), (r'U[nR]Am$', 'u', 'masc/fem/neut', 'sasthi', 'bahu'),
    (r'uzu$', 'u', 'masc/fem/neut', 'saptami', 'bahu'), (r'uByAm$', 'u', 'masc/fem/neut', 'tritiya/caturthi/panchami', 'dvi'),
    (r'uByaH$', 'u', 'masc/fem/neut', 'caturthi/panchami', 'bahu'), (r'uBiH$', 'u', 'masc/fem/neut', 'tritiya', 'bahu'),
    (r'U$', 'u', 'masc/fem/neut', 'prathama/dvitiya', 'dvi'), (r'avaH$', 'u', 'masc/fem', 'prathama', 'bahu'), (r'Uni$', 'u', 'neut', 'prathama/dvitiya', 'bahu'),
    (r'tA$', 'tf', 'masc/fem', 'prathama', 'eka'), (r'tArO$', 'tf', 'masc/fem', 'prathama/dvitiya', 'dvi'), (r'tAraH$', 'tf', 'masc/fem', 'prathama', 'bahu'),
    (r'tAram$', 'tf', 'masc/fem', 'dvitiya', 'eka'), (r'tFn$', 'tf', 'masc', 'dvitiya', 'bahu'), (r'tFH$', 'tf', 'fem', 'dvitiya', 'bahu'),
    (r'trA$', 'tf', 'masc/fem', 'tritiya', 'eka'), (r'tre$', 'tf', 'masc/fem', 'caturthi', 'eka'), (r'tuH$', 'tf', 'masc/fem', 'panchami/sasthi', 'eka'),
    (r'tari$', 'tf', 'masc/fem', 'saptami', 'eka'), (r'tF[nR]Am$', 'tf', 'masc/fem', 'sasthi', 'bahu'), (r'tfzu$', 'tf', 'masc/fem', 'saptami', 'bahu'),
    (r'tfByAm$', 'tf', 'masc/fem', 'tritiya/caturthi/panchami', 'dvi'), (r'tfByaH$', 'tf', 'masc/fem', 'caturthi/panchami', 'bahu'), (r'tfBiH$', 'tf', 'masc/fem', 'tritiya', 'bahu'),
    (r'A$', 'an', 'masc', 'prathama', 'eka'), (r'AnO$', 'an', 'masc', 'prathama/dvitiya', 'dvi'), (r'AnaH$', 'an', 'masc', 'prathama', 'bahu'),
    (r'Anam$', 'an', 'masc', 'dvitiya', 'eka'), (r'nA$', 'an', 'masc/neut', 'tritiya', 'eka'),
    (r'I$', 'in', 'masc', 'prathama', 'eka'), (r'inO$', 'in', 'masc', 'prathama/dvitiya', 'dvi'), (r'inaH$', 'in', 'masc', 'prathama/dvitiya/panchami/sasthi', 'bahu'),
    (r'aH$', 'as', 'neut', 'prathama/dvitiya', 'eka'), (r'asI$', 'as', 'neut', 'prathama/dvitiya', 'dvi'), (r'AMsi$', 'as', 'neut', 'prathama/dvitiya', 'bahu'), (r'asA$', 'as', 'masc/neut', 'tritiya', 'eka'),
    # --- HALANTA T/D ---
    (r't$', 't', 'masc/neut', 'prathama', 'eka'), (r'tO$', 't', 'masc', 'prathama/dvitiya', 'dvi'), (r'taH$', 't', 'masc/fem', 'prathama/dvitiya/panchami/sasthi', 'bahu'), (r'dByAm$', 't', 'masc/neut', 'tritiya/caturthi/panchami', 'dvi'), (r'dBiH$', 't', 'masc/neut', 'tritiya', 'bahu'),
    # --- HALANTA C & J ---
    (r'k$', 'c', 'masc/fem', 'prathama', 'eka'), (r'k$', 'j', 'masc/fem', 'prathama', 'eka'), (r'cA$', 'c', 'masc/fem', 'tritiya', 'eka'), (r'jA$', 'j', 'masc/fem', 'tritiya', 'eka'),
    (r'gByAm$', 'c', 'masc/fem', 'tritiya/caturthi/panchami', 'dvi'), (r'gByAm$', 'j', 'masc/fem', 'tritiya/caturthi/panchami', 'dvi'), (r'kzu$', 'c', 'masc/fem', 'saptami', 'bahu'), (r'kzu$', 'j', 'masc/fem', 'saptami', 'bahu'),
    (r'cO$', 'c', 'masc/fem', 'prathama/dvitiya', 'dvi'), (r'caH$', 'c', 'masc/fem', 'panchami/sasthi', 'eka'), (r'jO$', 'j', 'masc/fem', 'prathama/dvitiya', 'dvi'), (r'jaH$', 'j', 'masc/fem', 'panchami/sasthi', 'eka')
]

def get_stems(word_slp1):
    guessed_stems = []
    for pattern, replacement, gender, vibhakti, vacana in STEMMING_RULES:
        if re.search(pattern, word_slp1):
            guessed_stems.append({"stem": re.sub(pattern, replacement, word_slp1), "gender": gender, "case": vibhakti, "vacana": vacana})
    return guessed_stems
