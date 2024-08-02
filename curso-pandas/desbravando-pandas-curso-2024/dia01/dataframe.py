# %%
import pandas as pd
# %%
data = {
    "nome": ["leandro", "bruna", "theo", "maria"],
    "sobrenome": ["facchini", "machado", "facchini", "maia"],
    "idade": [35, 36, 6, 58]
}

data

data["idade"][0]

# %%

df = pd.DataFrame(data)
df
# %%

df["idade"]
df["idade"].iloc[0]

type(df["idade"])
# %%

df["idade"].iloc[0]
df["sobrenome"]
df["sobrenome"].iloc[0]

# %%

linha = df.iloc[0]
type(linha)
# %%

df.index
# %%

df.columns
# %%

df.info()

# %%

df.info(memory_usage="deep")
# %%

df.dtypes
# %%

df['peso'] = [80, 53, 65, 14]

df.describe()

# %%

sumario = df.describe()

sumario['peso']['mean']
