import numpy as np
from tabulate import tabulate

input_data = np.loadtxt("sol_lab2_input.txt", delimiter=',', dtype='f')

big_factory_income = input_data[1] * input_data[2] * 5 + input_data[3] * input_data[4] * 5 - input_data[0]
small_factory_income = input_data[6] * input_data[7] * 5 + input_data[8] * input_data[9] * 5 - input_data[5]

successive_info_incomes = (input_data[1] * input_data[12] * 4 + input_data[3] * input_data[13] * 4 - input_data[0] +
                        input_data[6] * input_data[12] * 4 + input_data[8] * input_data[13] * 4 - input_data[5]) * input_data[10]

nonsuccessive_info_incomes = 0 * input_data[11]

print(tabulate(headers=["Варіанти", "Результати (тис. $)"], tabular_data=[
    ["А) Великий завод", big_factory_income],
    ["Б) Малий завод", small_factory_income],
    ["В) Обидва заводи при зборі інформації", f"При позитивній інформації: {round(successive_info_incomes,3)} "
     f"\nПри негативній інформації: {nonsuccessive_info_incomes}"]
]))

variants = {big_factory_income: 'A', small_factory_income: 'Б', successive_info_incomes: 'В'}
print(f"Найвигідніший варіант: {variants.get(max(variants))}")
