import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argopy
import seaborn as sns
from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher()

ds2 = argo_loader.region([-50, 0, 45, 50,0,10,'2021-01-01', '2022-01-01']).to_dataframe()

ds2.to_csv('data2.csv')