import zad4

miesiace_en = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

months = {
    "pl": zad4.miesiace_pl,
    "en": miesiace_en
}

print(months['pl'][4])
print(months['en'][4])