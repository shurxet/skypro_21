from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items, company):
        self._items = items
        self._company = company

    @abstractmethod
    def add(self, title, count):
        pass

    @abstractmethod
    def remove(self, title, count):
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._capacity += count
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._capacity += count
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Request:
    def __init__(self, info):
        self.info = self._split_info(info)
        self.from_ = self.info[4]
        self.to = self.info[6]
        self.amount = int(self.info[1])
        self.product = self.info[2]

    @staticmethod
    def _split_info(info):
        return info.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"


def main():
    while(True):
        #user_input = "Доставить 3 печеньки из склад в магазин"
        user_input = input("Введите запрос: ")

        if user_input == "stop":
            break

        request = Request(user_input)
        print(request)



        # from_ = store if request.from_ == "склад" else shop
        # to = store if request.to == "склад" else shop

        if request.from_ == request.to:
            print("Пункт назначения == Пункт отправки")
            continue

        if request.from_ == "склад":

            if request.product in store.items:
                print(f"Нужный товар есть в пункте \"{request.from_}\"")
            else:
                print(f"В пункте {request.from_} нет такого товара")
                continue

            if store.items[request.product] >= request.amount:
                print(f"Нужное количество есть в пункте \"{request.from_}\"")
            else:
                print(f"В пункте {request.from_} не хватает {request.amount - store.items[request.product]}")
                continue

            if shop.get_free_space >= request.amount:
                print(f"В пункте \"{request.to}\" достаточно место")
                #print(to.get_free_space)
            else:
                #print(to.get_free_space)
                print(f"В пункте {request.to} не хватает {request.amount - shop.get_free_space} ")
                continue

            if request.to == "магазин" and shop.get_unique_items_count == 5 and request.product not in shop.items:
                print("В магазине достаточно уникальных значений")
                continue

            store.remove(request.product, request.amount)
            print(f"Курьер забрал {request.amount} {request.product} из пункта {request.from_}")
            print(f"Курьер везёт {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}")
            shop.add(request.product, request.amount)
            print(f"Курьер доставил {request.amount} {request.product} в пункт {request.to}")

        else:
            if request.product in shop.items:
                print(f"Нужный товар есть в пункте \"{request.from_}\"")
            else:
                print(f"В пункте {request.from_} нет такого товара")
                continue

            if shop.items[request.product] >= request.amount:
                print(f"Нужное количество есть в пункте \"{request.from_}\"")
            else:
                print(f"В пункте {request.from_} не хватает {request.amount - shop.items[request.product]}")
                continue

            if store.get_free_space >= request.amount:
                print(f"В пункте \"{request.to}\" достаточно место")
                #print(to.get_free_space)
            else:
                #print(to.get_free_space)
                print(f"В пункте {request.to} не хватает {request.amount - store.get_free_space} ")
                continue

            store.remove(request.product, request.amount)
            print(f"Курьер забрал {request.amount} {request.product} из пункта {request.from_}")
            print(f"Курьер везёт {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}")
            store.add(request.product, request.amount)
            print(f"Курьер доставил {request.amount} {request.product} в пункт {request.to}")

        print("="*30)
        print("На складе:")
        for title, count in store.items.items():
            print(f"{title}: {count}")
        print(f"Свободного места {store.get_free_space}")
        print("="*30)
        print("В магазине:")
        for title, count in shop.items.items():
            print(f"{title}: {count}")
        print(f"Свободного места {shop.get_free_space}")
        print("=" * 30)





if __name__ == "__main__":
    store = Store()
    shop = Shop()

    store_items = {
        "вода": 5,
        "шоколад": 10,
        "печеньки": 38,
    }
    store.items = store_items

    # user_input = "Доставить 3 печеньки из склад в магазин"

    main()






