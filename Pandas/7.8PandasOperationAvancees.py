#7.8Pandas: operations avancees
# https://www.youtube.com/watch?v=o4yZiZWP8Iw&list=PL2CXLryTKuwwy0jaLB10vXU6_Tkk4yPC4&index=8
"""
Une des grandes forces de pandas est le support d'operations avancees, comme la concatenation, le merge qu'on peut
egalement appeler jointure, le regroupement et le pivot. Ce sont des operations que l'on trouve habituellement dans
les bases de donnees et qui sont extremement puissantes.
"""
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                   columns=list('ab'),
                   index=list('xy'))

df2 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                   columns=list('ab'),
                   index=list('zt'))

print(df1)
print("\n")
print(df2)
print("\n")
# On va mettre les deux dataframe l'un au dessus de l'autre
print(pd.concat([df1, df2]))

# On va mettre les deux dataframe l'un a cote de l'autre
print("\n")
df1 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                   columns=list('ab'),
                   index=list('xy'))

df2 = pd.DataFrame(np.random.randint(1, 10, size=(2, 2)),
                   columns=list('cd'),
                   index=list('xy'))
print(pd.concat([df1, df2], axis=1))