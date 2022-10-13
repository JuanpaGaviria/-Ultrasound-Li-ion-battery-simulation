from time import sleep
import numpy as np
import time
import sys
class status_bar:
  def __init__(self, steps):
    self.steps = steps
    self.star_time = time.time()
    self.bar_graph = {
        "0": '[--------------------]',
        "5": '[■-------------------]',
        "10": '[■■------------------]',
        "15": '[■■■-----------------]',
        "20": '[■■■■----------------]',
        "25": '[■■■■■---------------]',
        "30": '[■■■■■■--------------]',
        "35": '[■■■■■■■-------------]',
        "40": '[■■■■■■■■------------]',
        "45": '[■■■■■■■■■-----------]',
        "50": '[■■■■■■■■■■----------]',
        "55": '[■■■■■■■■■■■---------]',
        "60": '[■■■■■■■■■■■■--------]',
        "65": '[■■■■■■■■■■■■■-------]',
        "70": '[■■■■■■■■■■■■■■------]',
        "75": '[■■■■■■■■■■■■■■■-----]',
        "80": '[■■■■■■■■■■■■■■■■----]',
        "85": '[■■■■■■■■■■■■■■■■■---]',
        "90": '[■■■■■■■■■■■■■■■■■■--]',
        "95":'[■■■■■■■■■■■■■■■■■■■-]',
        "100": '[■■■■■■■■■■■■■■■■■■■■]'
    }

    self.background = '\033[44m'
    self.green = '\033[92m'
    self.cyan = '\033[96m'
    self.bold = '\033[1m'
    self.endc ='\033[0m'

  def gx_return(self, perc):
    if perc < 5:
      return self.bar_graph["0"]
    elif perc < 10:
      return self.bar_graph["5"]
    elif perc < 15:
      return self.bar_graph["10"]
    elif perc < 20:
      return self.bar_graph["15"]
    elif perc < 25:
      return self.bar_graph["20"]
    elif perc < 30:
      return self.bar_graph["25"]
    elif perc < 35:
      return self.bar_graph["30"]
    elif perc < 40:
      return self.bar_graph["35"]
    elif perc < 45:
      return self.bar_graph["40"]
    elif perc < 50:
      return self.bar_graph["45"]
    elif perc < 55:
      return self.bar_graph["50"]
    elif perc < 60:
      return self.bar_graph["55"]
    elif perc < 65:
      return self.bar_graph["60"]
    elif perc < 70:
      return self.bar_graph["65"]
    elif perc < 75:
      return self.bar_graph["70"]
    elif perc < 80:
      return self.bar_graph["75"]
    elif perc < 85:
      return self.bar_graph["80"]
    elif perc < 90:
      return self.bar_graph["85"]
    elif perc < 95:
      return self.bar_graph["90"]
    elif perc > 95 and perc < 96:
      return self.bar_graph["95"]
    else:
      return self.bar_graph["100"]

  def update(self, c_step):
    perc = np.round(c_step/self.steps * 100, 2)
    sys.stdout.write("\r" + f'{self.bold}{self.gx_return(perc)} {perc}%{self.endc} | Step: {self.green}{c_step}/{self.steps}{self.endc} | CPU Time:{self.cyan} {np.round(time.time() - self.star_time, 4)}s{self.endc}')
    sys.stdout.flush()


