
aantal_studenten = int(input("hoeveel eerste jaars studenten zijn er? "))


lijstje_studenten_leefdtijd = []

for x in range(1,  aantal_studenten + 1):
    age = int(input(f"wat is de leefdtijd van student {x}? "))
    lijstje_studenten_leefdtijd.append(age)

teller = 0
opgetelde_leeftijd = 0

for leefdtijd in lijstje_studenten_leefdtijd:
    if leefdtijd < 18:
        teller = teller + 1

    opgetelde_leeftijd = opgetelde_leeftijd + leefdtijd

gemiddelde = opgetelde_leeftijd / aantal_studenten


print(f"het aantal studenten dat onder de 18 jaar is is: {teller}")
print(f"de gemiddelde leefdtijd is:  {gemiddelde}")


for passeer_nummer in range(len(lijstje_studenten_leefdtijd)-1, 0, -1):
    for i in range(passeer_nummer):
        if lijstje_studenten_leefdtijd[i]>lijstje_studenten_leefdtijd[i+1]:
            temp = lijstje_studenten_leefdtijd[i]
            lijstje_studenten_leefdtijd[i] = lijstje_studenten_leefdtijd[i+1]
            lijstje_studenten_leefdtijd[i+1] = temp


print("als alle leefdtijden gesorteerd zijn dan leverd dat deze volgorde op: ")
for item in lijstje_studenten_leefdtijd:
    print(item)
