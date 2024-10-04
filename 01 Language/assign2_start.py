# The assignment expression operator := (or the "walrus" operator)

import pprint

#alt:
#values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
#val_data = {
#    "length": len(values),
#    "total": sum(values),
#    "average": sum(values) / len(values)
#}

# TODO: The walrus (or assignment) operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": (l := len(values)),
    "total": (t := sum(values)),
    "average": t / l
}
pprint.pp(val_data)