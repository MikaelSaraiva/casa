import json
import sys

def sum_month_market_purchases(year, month):
    market = {}
    with open("market.json", "r", encoding="utf-8") as market_file:
        market = json.load(market_file)
    purchases = market[year][month]
    purchases_result = []
    total_division = {
        "inã": 0,
        "paola": 0,
        "mikael": 0
    }
    for purchase in purchases:
        equally_amount = 0
        total_users = 3
        division = {
            "inã": 0,
            "paola": 0,
            "mikael": 0
        }

        for item in purchase["items"]:
            if item["division"]:
                total_weight = 0
                for weight in item["division"].values():
                    total_weight += weight

                for user, weight in item["division"].items():
                    division[user] += (item["valor"]*weight)/total_weight
            else:
                equally_amount += item["valor"]

        part = equally_amount/total_users
        for user in division:
            total_division[user] += division[user] + part
            division[user] = "{:.2f}".format(division[user] + part)

        purchases_result.append({
            "date": purchase["date"],
            "description": purchase["description"],
            "division": division
        })
    for user in total_division:
        total_division[user] = "R$ {:.2f}".format(total_division[user])
    purchases_result.append({
        "date": "NO DATE",
        "description": "TOTAL",
        "division": total_division
    })
    print(json.dumps(purchases_result, indent=4, ensure_ascii=False))
    with open("mercadoDividido_"+month+"_"+year+".json", "w+", encoding="utf-8") as output_file:
        output_file.write(json.dumps(purchases_result, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    YEAR = sys.argv[1]
    MONTH = sys.argv[2]
    print("Executando para o mês "+MONTH+" de "+YEAR)
    sum_month_market_purchases(YEAR, MONTH)
