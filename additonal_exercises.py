import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/priyankap/Downloads/emp-data.csv')
df = df.dropna()
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df['Salary'] = df['Salary'].str.replace(r'[$,]', '', regex=True)
df['Salary']=pd.to_numeric(df['Salary'])

sns.set(style="whitegrid")
plt.figure(figsize=(20, 8))

# 1. Gender & Location
plt.subplot(2, 3, 1)
sns.countplot(x='Loc', hue='Gender', data=df)
plt.title('Gender & Location')

# 2. Gender & Department
plt.subplot(2, 3, 2)
sns.countplot(x='Department', hue='Gender', data=df)
plt.title('Gender & Department')
plt.xticks(rotation=90)

# 3. Gender & Rating
plt.subplot(2, 3, 3)
sns.boxplot(x='Gender', y='Rating', data=df)
plt.title('Gender & Rating')

# 4. Gender & Salary
plt.subplot(2, 3, 4)
sns.boxplot(x='Gender', y='Salary', data=df)
plt.title('Gender & Salary')

# 5. Location & Salary
plt.subplot(2, 3, 5)
sns.boxplot(x='Loc', y='Salary', data=df)
plt.title('Location & Salary')
plt.xticks(rotation=25)

# 6. Department & Salary
plt.subplot(2, 3, 6)
sns.boxplot(x='Department', y='Salary', data=df)
plt.title('Department & Salary')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

