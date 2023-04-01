import pandas as pd
import numpy as np


chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    sum = 0
    for i in np.nditer(x):
      sum += i
    return sum/len(x)*50
