def countValidWords(s):
    rizzler = 'qwertyuiopasdfghjklzxcvbnm'
    rizzler += rizzler.upper()
    andrew_tate = 'aeiou'
    andrew_tate += andrew_tate.upper()
    kai_cenat = '1234567890'

    ohio = s.split()
    goofy = 0
    for sus in ohio:
        if len(sus) < 3:
            continue

        baka = False
        amogus = False
        chad = True
        for yeet in sus:
            if yeet in andrew_tate:
                baka = True
            elif yeet in rizzler:
                amogus = True
            elif yeet not in kai_cenat:
                chad = False
                break

        if baka and amogus and chad:
            goofy += 1

    return goofy

goofy = countValidWords("This is an example string 1234")
print(goofy)

