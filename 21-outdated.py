
MonthsList = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("DATE: ").replace(",","")
        date = date.replace(" ", "/")
        date = date.split("/")
        if date[0] in MonthsList:
            date[0] = str(int(MonthsList.index(date[0])) + 1)
        elif int(date[0]) > 12:
            continue
        if int(date[1]) <= 31:
            print(date[2] + "-" + date[0].zfill(2) + "-" + date[1].zfill(2))
            break
        else:
            continue
    except ValueError:
        pass
