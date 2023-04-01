import pandas as pd
import numpy as np


chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    sqrt = 0
    sum = 0
    for i in np.nditer(x):
      sqrt += i**2
      sum += i
    return sqrt/len(x) - (sum/len(x))**2
