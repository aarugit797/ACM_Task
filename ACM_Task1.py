def date(p):
    l = p.split("-")
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    i = int(l[1]) - 1 
    lst_1=["1","21","31"]
    lst_2=["2","22"]
    lst_3=["3","23"] 
    if l[2] in lst_1:
        return f"{l[2]}st {months[i]} {l[0]}"
    elif l[2] in lst_2:
        return f"{l[2]}nd {months[i]} {l[0]}"
    elif l[2] in lst_3:
        return f"{l[2]}rd {months[i]} {l[0]}"
    else:
        return f"{l[2]}th {months[i]} {l[0]}"


def check(p):
    count = 0
    if p == 'Python':
        return "🐍"
    for i in p:
        if i == '-':
            break
        if i.isdigit():
            count += 1

    if count == 5:
        return "[REDACTED]"
    elif count == 4:
        return date(p)
    else:
        return p


para = input("Enter the para: ")
paras = para.split()

paras = [check(p) for p in paras]

result = " ".join(paras)
print(result)
