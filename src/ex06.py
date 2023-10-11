# coding: utf-8

class Animal:
    origin_list: list = ['Europe', 'Africa', 'Asia']

    def __init__(self, p_name, p_b_year):
        self.name: str = p_name
        self.birth_year: int = p_b_year
        self.donors = {}
        self.origin = ''

    def __str__(self):
        return (f'name: {self.name}; birth: {self.birth_year}; origin: {self.origin}; '
                f'donors: {self.format_donors(self.donors)}')

    def gift(self, donor_id: str, amount: int):
        key = self.strip_donor_id(donor_id)
        self.donors[key] = self.donors.get(key, 0) + amount

    def set_origin(self, origin: str):
        self.origin = self.check_origin(origin)

    @classmethod
    def check_origin(cls, origin: str):
        return origin.capitalize() \
            if origin.upper() in list(map(lambda i: str(i).upper(), cls.origin_list)) \
            else '???'

    @staticmethod
    def strip_donor_id(donor_id: str) -> str:
        mapping: dict = str.maketrans({'/': '', ' ': ''})
        return donor_id.translate(mapping)

    @staticmethod
    def format_donors(donors: dict):
        return ','.join([f'{key} ({val})' for key, val in donors.items()])


class Fish(Animal):
    origin_list = ['Pacific', 'Atlantic', 'Rivers']

    def __init__(self, p_name, p_b_year, p_water):
        super().__init__(p_name, p_b_year)
        self.water = p_water

    def __str__(self):
        return (f'name: {self.name}; birth: {self.birth_year}; origin: {self.origin}; '
                f'water: {self.water}; donors: {self.format_donors(self.donors)}')


a1 = Animal('Lion Simba', 1994)
a1.set_origin('africa')
a1.gift( '700938/3869', 5000)
a1.gift( '700938 3869', 3000)
a1.gift( ' 9503833333 ', 4000)
print( a1 )
assert(str(a1)) == 'name: Lion Simba; birth: 1994; origin: Africa; donors: 7009383869 (8000),9503833333 (4000)'

f1 = Fish('Clownfish Nemo', 2003, 'saltwater')
f1.set_origin('pacific')
f1.gift( '700938/3869', 50)
f1.gift( '700938 3869', 30)
f1.gift( ' 9503833333 ', 40)
print( f1 )
assert(str(f1))== 'name: Clownfish Nemo; birth: 2003; origin: Pacific; water: saltwater; donors: 7009383869 (80),9503833333 (40)'
