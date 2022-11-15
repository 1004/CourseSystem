# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import sys
import os
from core.core_main_view import MainView

sys.path.append(
    os.path.dirname(__file__)
)

if __name__ == '__main__':
    mainView = MainView()
    mainView.run()
