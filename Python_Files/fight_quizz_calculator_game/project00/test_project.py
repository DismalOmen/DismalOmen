from project import dice_roll
from project import easy_calculator, easy_calculator0 ,easy_calculator1

def main():
    test_dice_roll()
    test_easy_calculator()
    test_easy_calculator0()
    test_easy_calculator1()




def test_easy_calculator1():
    assert easy_calculator1(2 , 3) == 6
    assert easy_calculator1(150, 250) == 37500

def test_easy_calculator0():
    assert easy_calculator0(3 , 3) == 0
    assert easy_calculator0(250, 250) == 0

def test_easy_calculator():
    assert easy_calculator(2 , 3) == 5
    assert easy_calculator(150, 250) == 400

def test_dice_roll():
    assert dice_roll() == print(f"""


     _______     /\O    O.
    /O     /\   /  \      .
   /   O  /O \ / O  \O____O\ ))
((/_____O/    ..    /O     /
  \O    O\    / \  /   O  /
   \O    O\ O/   \/_____O/
    \O____O\/ ))         ))
  ((

         """)


if __name__ == "__main__":
    main()