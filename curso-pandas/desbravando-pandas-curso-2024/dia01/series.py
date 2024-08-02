# %%
import pandas as pd

# %%
idades = [30, 42, 90, 34]
idades

sum(idades)

media = sum(idades)/len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades)-1)
variancia

# %%
# Transformacao para Series Pandas
series_idades = pd.Series(idades)
series_idades


# %%
# Metodos da series Pandas

# Media
series_idades.mean()
# %%
# Variaancia e desvio padrao
series_idades.var()
series_idades.std()

# %%
# Mediana
series_idades.median()
# %%
# Quartil
series_idades.quantile(0.75)

# %%
# Sumarizacao
series_idades.describe()

# %%
series_idades.shape
# %%

series_idades

series_idades[3]
# %%

series_idades.index

series_idades.index = [40, 10, 30, 20]
series_idades
# %%
series_idades.iloc[2:4]
# %%
series_idades.iloc[0:2]

# %%

series_idades.loc[40]
series_idades[40]
# %%

series_idades.name = 'idades'

# %%
series_idades
# %%

series_idades = pd.Series(idades, name='idades')

# %%

