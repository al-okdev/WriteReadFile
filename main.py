from pprint import pprint

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file:
    while True:
        name_recipe = file.readline().rstrip()

        if not name_recipe:
            break

        count_ingredient = int(file.readline().rstrip())

        # print(name_recipe)
        # print(count_ingredient)


        ingredient_list = []

        for item in range(count_ingredient):
            ingredient_dict = {}
            item_line_ingredient = file.readline().rstrip().split(' | ')
            ingredient_dict['ingredient_name'] = item_line_ingredient[0]
            ingredient_dict['quantity'] = item_line_ingredient[1]
            ingredient_dict['measure'] = item_line_ingredient[2]

            ingredient_list.append(ingredient_dict)

        # print(ingredient_list)

        cook_book[name_recipe] = ingredient_list

        file.readline()



# pprint(cook_book)
print()


def get_shop_list_by_dishes(dishes, person_count):

    result_dict = {}

    for item_dishes in dishes:
        if cook_book[item_dishes]:
            count_dishe = dishes.count(item_dishes)
            for item in cook_book[item_dishes]:
                temp_dict = {}
                temp_dict['measure'] = item['measure']
                temp_dict['quantity'] = int(item['quantity']) * person_count * count_dishe
                result_dict[item['ingredient_name']] = temp_dict

    return result_dict



pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 1))
