import re
import sys
import math

def identify(ingredient_needed, quantity_needed, rules):
    total = 0
    supplies = {ingredient_needed: quantity_needed}
    instructions = [(ingredient_needed, quantity_needed, 0)]

    while len(instructions) > 0:
        (ingredient_needed, quantity_needed, left_over) = instructions.pop(0)

        if ingredient_needed in rules:
            (quantity, parts) = rules[ingredient_needed]

            factor = math.ceil(quantity_needed / quantity)

            for part in parts:
                supplies[part] = supplies.get(part, 0) + parts[part] * factor
                instructions.append( (part, parts[part]) )

                if part == "ORE":
                    final_checks[ingredient_needed] = 1

    return total

if __name__ == '__main__':
    rules = {}
    regex = ""
    with open(sys.argv[1]) as file:
        for line in file:
            regex = "(.*) => (.*)"
            matches = re.match(regex, line.strip())
            ingredients = matches.group(1).split(", ")
            (quantity, ingredient) = matches.group(2).split(" ")
            rules[ingredient] = (int(quantity), {ingredient.split(" ")[1]: int(ingredient.split(" ")[0]) for ingredient in ingredients})

    start_quantity = int(sys.argv[2])
    start_reactant = sys.argv[3]
    print(rules)
    print(identify(start_reactant, start_quantity, rules))
