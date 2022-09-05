import time
from itertools import *


class KeyGen():

    def __init__(self, product_key, min_length, max_length):
        self.length_key = None
        self.specification_file = None
        self.product = product_key
        self.max_length = max_length
        self.min_length = min_length

    def get_specifications(self):
        try:
            list_specifications = []

            with open('specifications.txt', 'r', encoding='utf-8') as spec_file:
                lines = spec_file.readlines()
            for line in lines:
                line = line.strip('\n').lower()
                list_specifications.append(line)

            else:
                return list_specifications
        except Exception as e:
            print("Error get specification:", str(e))
            return "Error"

    def keys_combinations(self, length_key):
        self.length_key = length_key
        try:
            specifications = self.get_specifications()
            if specifications == "Error":
                return "Error"
            else:
                keys = combinations(specifications, self.length_key) #Уникальные без повторений
                # keys = permutations(specifications, self.length_key)  # С повторами
                return keys
        except Exception as e:
            print("Error keys generation:", str(e))
            return "Error"

    def finally_generation(self):
        # try:
        count = 0
        for length_key in range(self.min_length, self.max_length + 1):

            string_write_to_file = ''
            for key in self.keys_combinations(length_key):
                key = self.product + ' ' + ' '.join(key) + '\n'
                string_write_to_file += key
                count += 1
                if count >= 1000000:
                    with open('result.txt', 'a+', encoding='utf-8') as res_file:
                        res_file.write(string_write_to_file)
                    string_write_to_file = ''
                    count = 0
                    Flag = False
                else:
                    Flag = True
            if Flag:
                with open('result.txt', 'a+', encoding='utf-8') as res_file:
                    res_file.write(string_write_to_file)
                string_write_to_file = ''
        # except Exception as e:
        #     print("Error keys generation finally:", str(e))
        #     return "Error"


def main():
    min_length_key = int(input('Введите минимальную длину ключевого слова (целое число):'))
    max_length_key = int(input('Введите максимальную длину ключевого слова (целое число):'))

    main_keys = ['штора', 'портьера', 'комплект штор', 'занавеска']

    for main_key in main_keys:
        # print(f"Взяли в работу ключ: {main_key}")
        objKeyGen = KeyGen(main_key, min_length_key, max_length_key)
        objKeyGen.finally_generation()


if __name__ == '__main__':
    main()
