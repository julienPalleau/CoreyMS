

# from ecommerce.customer import contact # absolute import which should be prefered as best practicce
# from ..customer import contact # relative import

from ecommerce.customer import contact  # absolute import
# from ..customer import contact # relative import
# prefere absolute import to relative one


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("Sales started")  # this is to show that a module is called only once
    calc_tax()
