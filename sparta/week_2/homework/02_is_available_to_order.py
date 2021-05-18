shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()

    for order in orders:
        current_min = 0
        current_max = len(menus) - 1
        current_guess = (current_min + current_max) // 2

        while current_min <= current_max:
            if menus[current_guess] == order:
                break
            elif menus[current_guess] < order:
                current_min = current_guess + 1
            else:
                current_max = current_guess - 1

            current_guess = (current_min + current_max) // 2
        else:
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
