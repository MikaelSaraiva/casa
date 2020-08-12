import json
import sys

def sumMonth(year, month) :
    market = {}
    with open("mercado.json", "r", encoding="utf-8") as marketFile:
        market = json.load(marketFile)
    purchases = market[year][month]
    purchasesResult = []

    for purchase in purchases:
        equallyAmount = 0
        users = purchase["users"]
        division = {}
        for user in users:
            division[user] = 0

        for item in purchase["items"]:
            if item["division"]:
                totalWeight = item["totalWeight"]
                for user, weight in item["division"].items():
                    division[user] += (item["valor"]/totalWeight)*weight

            else:
                equallyAmount += item["valor"]

        part = equallyAmount/len(users)
        for user in users:
            division[user] = "{:.2f}".format(division[user] + part)
            

        purchasesResult.append({
            "date": purchase["date"],
            "division": division
        })        
    print(purchasesResult)
    with open("mercadoDividido_"+month+"_"+year+".json", "w+", encoding="utf-8") as output_file:
        output_file.write(json.dumps(purchasesResult, indent=4, ensure_ascii=False))  

if __name__ == "__main__":
    year = sys.argv[1]
    month = sys.argv[2]
    print("Executando para o mês "+month+" de "+year)
    sumMonth(year, month)