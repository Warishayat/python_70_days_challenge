weekday=input("""Enter the weekday today:
        1:monday
        2:tuesday
        3:wednesday
        4:thursday
        5:friday
        6:saturday
        7:sunday
""")
case=weekday.lower()
match case:
    case 'monday':
        print("This is working day")
    case 'tuesday':
        print("The day is working day")
    case 'wednesday':
        print("The day is working day")
    case "thurusday":
        print("The day is working day")
    case 'friday':
        print("The day is working day")
    case "saturday":
        print("This is weekend")
    case 'sunday':
        print("This is weekend")
    case _:
        print("You enter wrong values")
