# sandwich_main.py

from bread import cut_bread
from lettuce import prepare_lettuce


def make_sandwich():
    cut_bread()
    prepare_lettuce()
    print("三明治完成！")


if __name__ == "__main__":
    make_sandwich()
