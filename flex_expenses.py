import json
import sys

def sum_month_flex_expenses(year, month):
    flex = {}
    with open("flex_expenses.json", "r", encoding="utf-8") as flex_file:
        flex = json.load(flex_file)
    purchases = flex[year][month]
    division = {
        "inã": {
            "paola": 0,
            "mikael": 0
        },
        "paola": {
            "inã": 0,
            "mikael": 0
        },
        "mikael": {
            "paola": 0,
            "inã": 0
        }
    }

    for item in purchases:
        for transfer in item["division"]:
            division[transfer["from"]][transfer["to"]] += transfer["valor"]

    for user_a in division:
        for user_b in division:
            if user_a == user_b:
                continue
            if division[user_a][user_b] >= division[user_b][user_a]:
                division[user_a][user_b] -= division[user_b][user_a]
                division[user_b][user_a] = 0
            else:
                division[user_b][user_a] -= division[user_a][user_b]
                division[user_a][user_b] = 0

    for user_a in division:
        for user_b in division[user_a]:
            division[user_a][user_b] = "R$ {:.2f}".format(division[user_a][user_b])

    print(division)
    with open("gastosFlexiveis_"+month+"_"+year+".json", "w+", encoding="utf-8") as output_file:
        output_file.write(json.dumps(division, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    YEAR = sys.argv[1]
    MONTH = sys.argv[2]
    print("Executando para o mês "+MONTH+" de "+YEAR)
    sum_month_flex_expenses(YEAR, MONTH)
