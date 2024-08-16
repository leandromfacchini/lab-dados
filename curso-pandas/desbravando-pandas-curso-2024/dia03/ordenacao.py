# %%
import pandas as pd
# %%

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df.sort_values(by='Points')
# %%

df = df.sort_values(by='Points', ascending=False)

# %%

df.sort_values(by="Points", ascending=True, inplace=True)
df

# %%

# Poder ser assim
df.sort_values(by="Points", ascending=False, inplace=True)
df.rename(columns={"Name": "Nome", "Points": "Pontos"}, inplace=True)
df

# %%

# Ou pode ser assim, encadeando comandos

df = (df.sort_values(by="Points", ascending=False)
        .rename(columns={"Name": "Nome", "Points": "Pontos"}))
df

# %%

df.sort_values(by=["Points", "Name"], ascending=[False, True]).tail(10)

# %%

df = (df.sort_values(by=["Points", "Name"], ascending=[False, True])
      .rename(columns={"Name": "Nome", "Points": "Pontos"}))
df

# %%
