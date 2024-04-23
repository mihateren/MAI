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


def discount(cheque):
    disc_cheque = cheque.copy()
    disc_cheque['cost'] = cheque.apply(
        lambda row: row['cost'] * 0.5 if row['number'] > 2 else row['cost'], axis=1)
    return disc_cheque
