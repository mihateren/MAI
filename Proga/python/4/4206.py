def order(*keys):
    names = {
        "Эспрессо": {
            "coffee": 1,
            "milk": 0,
            "cream": 0
        },
        "Капучино": {
            "coffee": 1,
            "milk": 3,
            "cream": 0
        },
        "Макиато": {
            "coffee": 2,
            "milk": 1,
            "cream": 0
        },
        "Кофе по-венски": {
            "coffee": 1,
            "milk": 0,
            "cream": 2
        },
        "Латте Макиато": {
            "coffee": 1,
            "milk": 2,
            "cream": 1
        },
        "Кон Панна": {
            "coffee": 1,
            "milk": 0,
            "cream": 1
        }
    } 
    coffee = in_stock["coffee"]
    milk = in_stock["milk"]
    cream = in_stock["cream"]
    for x in keys:
        if coffee >= names[x]["coffee"] and milk >= names[x]["milk"] and cream >= names[x]["cream"]:
            in_stock["coffee"] -= names[x]["coffee"]
            in_stock["milk"] -= names[x]["milk"]
            in_stock["cream"] -= names[x]["cream"]
            return x
    return "К сожалению, не можем предложить Вам напиток"