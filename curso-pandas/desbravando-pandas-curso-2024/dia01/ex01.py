# %%
import pandas as pd
# %%

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
# %%

series_dados = pd.Series(dados)

series_dados.describe()

# %%
# media
media = series_dados.mean()
media 

# %%
# desvio padrao
series_dados.std()

# %%
# maximo valor
series_dados.max()

# %%
