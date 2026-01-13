import pandas as pd
df=pd.read_csv('/Users/priyankap/Downloads/emp-data.csv')
df = df.dropna()
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df['Salary'] = df['Salary'].str.replace(r'[$,]', '', regex=True)
df['Salary']=pd.to_numeric(df['Salary'])

#1 gender counts
gc = df['Gender'].value_counts()
print(gc)

#2 gender counts in each dept/location
gcd=df.groupby(['Department','Gender']).size().unstack()
gcl=df[['Loc','Gender']].value_counts().unstack()
print('\nBased on department:\n',gcd)
print('\nBased on location:\n',gcl)

#3 highest avg pay department
avg_pay=df.groupby('Department')['Salary'].mean().idxmax()
print('\nDepartment with the highest average pay is',avg_pay)

#4 highest avg pay location
avg_pay_loc=df.groupby('Loc')['Salary'].mean().idxmax()
print('\nLocation with the highest average pay is',avg_pay_loc)

#5 percentage of each rating
rating_counts = df["Rating"].value_counts()
total_employees = len(df)
good_ratings = ["Good", "Very Good"]
poor_ratings = ["Poor", "Very Poor"]
average_ratings = ["Average"]
gp=rating_counts[good_ratings].sum() / total_employees * 100
bp=rating_counts[poor_ratings].sum() / total_employees * 100
ap=rating_counts[average_ratings].sum() / total_employees * 100
print(f"\nGood & Very Good Ratings: {gp:.2f}%")
print(f"Poor & Very Poor Ratings: {bp:.2f}%")
print(f"Average Rating: {ap:.2f}%\n")

#6 gender pay gap in each department
sal=df.groupby(['Department', 'Gender'])['Salary'].mean().unstack()
sal['Gap %']=((sal['Male']-sal['Female'])/sal['Male']) * 100
sal=sal.round(2)
sal['Gap interpretation']=sal['Gap %'].apply(lambda x: "Males earn more" if x > 0 else ("Females earn more" if x < 0 else "No difference"))
print("Gender pay gap for each department:\n",sal[['Gap %','Gap interpretation']])

#7 gender pay gap based on location
sal_loc=df.groupby(['Loc','Gender'])['Salary'].mean().unstack()
sal_loc['Gap %']=((sal_loc['Male']-sal_loc['Female'])/sal_loc['Male']) * 100
sal_loc=sal_loc.round(2)
sal_loc['Gap interpretation']=sal_loc['Gap %'].apply(lambda x: "Males earn more" if x > 0 else ("Females earn more" if x < 0 else "No difference"))
print("\nGender pay gap for each location:\n",sal_loc[['Gap %','Gap interpretation']])
