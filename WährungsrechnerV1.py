def exchange (waehrung,betrag):
    if waehrung == "€":
        dollar = betrag * 1.15
        print(f"Umgerechnet sind das {dollar} $ ")
        pound = betrag * 0.88
        print(f"Umgerechnet sind das {pound} £")
    if waehrung == "$":
        euro = betrag * 0.86
        print(f"Umgerechnet sind das {euro} €")
        pound = betrag * 0,76
        print(f"Umgerechnet sind das {pound} £")
    if waehrung == "£":
        dollar = betrag * 1.32
        print(f"Umgerechnet sind das {dollar} $ ")
        euro = betrag * 1.13
        print(f"Umgerechnet sind das {euro} €")


while True:
    change = True

    waehrung = input("Wähle aus eine aus den drei währungen aus die umgerechnet werden soll in die anderen. $, €, £\n Gib mir deine Währung: ")
    betrag = int(input("Gib deinen Betrag: "))

    while change == True:
        exchange(waehrung,betrag)
        waehrung = ""
        betrag = 0
        change = False
