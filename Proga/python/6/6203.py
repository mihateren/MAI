import pandas as pd


def cheque(price_list, **kwargs):
    products = sorted(kwargs)
    cheque_dict = {
        'product': products,
        'price': [price_list[i] for i in products],
        'number': [kwargs[i] for i in products]
    }
    s = pd.DataFrame(cheque_dict)
    s['cost'] = s['price'] * s['number']
    return s
