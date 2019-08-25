from budget import Budget
from edit import Edit_Ui
import time


project = Edit_Ui.load()

try:
    bud = Budget(project)
except Exception as e:
    print("Open project to edit it!")
    time.sleep(3)
    project = Edit_Ui.load()
    bud = Budget(project)

bud.plot_year_projection()
