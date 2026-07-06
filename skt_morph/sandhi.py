import re

# Ordered from longest/most complex prefix to shortest to avoid partial matches
UPASARGA_PATTERNS = [
    (r'^samudA', 'sam + ud + AN', ''),
    (r'^sa[mMnYNR]u[dtcjNYRnl]A', 'sam + ud + AN', ''),
    (r'^sa[mMnYNR]u[dtcjNYRnl]', 'sam + ud', ''),  # <-- THE FIX IS HERE
    (r'^sa[mMnYNR]praty', 'sam + prati', ''),
    (r'^sa[mMnYNR]prati', 'sam + prati', ''),
    (r'^sa[mMnYNR]pra', 'sam + pra', ''),
    (r'^vyA', 'vi + AN', ''),
    (r'^pratyA', 'prati + AN', ''),
    (r'^paryA', 'pari + AN', ''),
    (r'^udA', 'ud + AN', ''),
    (r'^prA', 'pra + AN', ''),
    (r'^apA', 'apa + AN', ''),
    (r'^anvA', 'anu + AN', ''),
    (r'^avA', 'ava + AN', ''),
    (r'^nirA', 'nir + AN', ''),
    (r'^durA', 'dus + AN', ''),
    (r'^aDyA', 'aDi + AN', ''),
    (r'^apyA', 'api + AN', ''),
    (r'^atyA', 'ati + AN', ''),
    (r'^aByA', 'aBi + AN', ''),
    (r'^upA', 'upa + AN', ''),
    (r'^svA', 'su + AN', ''),
    (r'^vy', 'vi', ''),
    (r'^vi', 'vi', ''),
    (r'^praty', 'prati', ''),
    (r'^prati', 'prati', ''),
    (r'^pary', 'pari', ''),
    (r'^pari', 'pari', ''),
    (r'^sa[mMnYNR]', 'sam', ''),  
    (r'^sam', 'sam', ''),
    (r'^u[dt]y', 'ud', 'y'), 
    (r'^u[dtcjNYRnl]', 'ud', ''), 
    (r'^pra', 'pra', ''),
    (r'^parA', 'parA', ''),
    (r'^apa', 'apa', ''),
    (r'^anv', 'anu', ''),
    (r'^anu', 'anu', ''),
    (r'^ava', 'ava', ''),
    (r'^ni[rsSzR]', 'nir', ''),
    (r'^du[rsSzR]', 'dus', ''),
    (r'^ny', 'ni', ''),
    (r'^ni', 'ni', ''),
    (r'^aDy', 'aDi', ''),
    (r'^aDi', 'aDi', ''),
    (r'^apy', 'api', ''),
    (r'^api', 'api', ''),
    (r'^aty', 'ati', ''),
    (r'^ati', 'ati', ''),
    (r'^sv', 'su', ''),
    (r'^su', 'su', ''),
    (r'^aBy', 'aBi', ''),
    (r'^aBi', 'aBi', ''),
    (r'^upa', 'upa', ''),
    (r'^A', 'AN', ''),
]

def get_upasarga_splits(word):
    splits = []
    for pattern, canonical, prepend in UPASARGA_PATTERNS:
        match = re.match(pattern, word)
        if match:
            stripped = prepend + word[match.end():]
            if len(stripped) >= 2:  
                splits.append((canonical, stripped))
    return splits
