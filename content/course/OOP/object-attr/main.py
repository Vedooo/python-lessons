from prettytable import PrettyTable


x = PrettyTable()

x.field_names = ["Pokemon name", "Type"]
x.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Charmender", "Fire"],
        ["Pichu", "Electric"],
    ]
)

x.align["Pokemon name"] = "l"
x.align["Type"] = "l"

print(x)