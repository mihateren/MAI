class Bug:
    def __repr__(self):
        raise Exception


try:
    a = Bug()
    func(a)
except Exception:
    print('Ура! Ошибка!')