def enrolment_stats(lista_universidades):
    total_estudantes = []
    total_taxa = []

    for i in lista_universidades:
        total_estudantes.append(i[1])
        total_taxa.append(i[2])

    return total_estudantes, total_taxa

def mean(values):
    return sum(values)/len(values)

def median(values):
    values.sort()
    if len(values) % 2 == 1:
        center_index = int(len(values) / 2)
        return values[center_index]
    else:
        l_center_index (len(values) - 1) // 2
        r_center_index (len(values) + 1) // 2
        return mean([values[l_center_index], values[r_center_index]])
    


universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]

totals = enrolment_stats(universities)

print('*'*35)
print(f"Total Students: {sum(totals[0]):,}")
print(f"Total Tuiton: {sum(totals[1]):,}")
print(f"\nStudent mean: {mean(totals[0]):,.2f}")
print(f"Student median: {median(totals[0]):,}")
print(f"\nTuiton mean: {mean(totals[1]):,.2f}")
print(f"Tuiton median: {median(totals[1]):,}")
print('*'*35)
