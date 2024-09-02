import re
from string import ascii_letters

def check_date_val(date: str):
    mat = re.fullmatch(r"\d{1,2}\.\d{1,2}", date)
    if not mat:
        return 
    
    d, m = map(int, mat.group().split("."))
    
    v = {
        1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
    }
    
    if m in v:
        if 1 <= d <= v[m]:
            return f"{d}.{m}"
    return


def check_per_val(uname: str):
    ALPHABET = ascii_letters+"_0123456789"
    
    if len(uname) < 6:
        return False
    
    if not (uname[0] == "@"):
        return False
    
    for let in set(uname[1:]):
        if let not in ALPHABET:
            return False
    
    return uname


if __name__ == "__main__":
    # print(check_date_val("001.01"))
    print(check_per_val("sdf@sdfsd"))
    
    