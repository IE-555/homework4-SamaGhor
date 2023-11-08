#!/usr/bin/env python
# coding: utf-8

# In[43]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('student_grades.csv')
studentID = df.iloc[:,0]
avgScore=df.iloc[:,1]
print (df)
#n,bins,patches=plt.hist(avgScore,bins=range(0,110,10),density=False,facecolor="g",alpha=0.75)
#print(n)
#print(bins)
f=n[0]+n[1]+n[2]+n[3]+n[4]+n[5]
d=n[6]
c=n[7]
b=n[8]
a=n[9]
print(a,b,c,d,f)
y=[f,d,c,b,a]
range=['F','D','C','B','A']
plt.bar(range,y,color='orange', edgecolor='black')
plt.ylim(0, 30)
plt.title("Students' Grade Distribution")
plt.ylabel("Count")
plt.xlabel("Grade Range")

for index, value in enumerate(y):
    plt.text(index, value + 1, str(value), ha='center')
 


# In[65]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('scatter_data.csv')
x= df.iloc[:,0]
y=df.iloc[:,1]
print(df)
plt.plot(x,y,'^',markersize=10, color="green", mfc="green", markeredgecolor="green",markeredgewidth=1,label="observations")
plt.title("Widget Measurements")
plt.ylabel("y [inches]")
plt.xlabel("x [inches]")
min_x=min(x)
max_x=max(x)
df_min=df[df['% x']==min_x]
min_y=df_min.iloc[:,1]
df_max=df[df['% x']==max_x]
max_y=df_max.iloc[:,1]
x_line=[min_x,max_x]
y_line=[min_y,max_y]
plt.plot(x_line,y_line,linestyle='dashed', color='red', markersize=10, markeredgewidth=1, label="extreme x points")
plt.legend()


# In[69]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('solution_data.csv')
result_df = pd.DataFrame()
problemID=df.iloc[:,0]
problemIDUni=problemID.unique()
solnMethod=df.iloc[:,1]
solnMethodUni=solnMethod.unique()
for i in problemIDUni:
# Create a new DataFrame where the '% Problem' column is 0
    df_new = df[df['% Problem'] == i]

# Filter the optimal values based on the 'SolnMethod' column
    optimal_value = df_new[df_new['SolnMethod'] == '|optimal|']['Value']

# Calculate the gap between the optimal values and the values in the DataFrame
    df_new['gap'] = ((optimal_value.values[0] - df_new['Value'])/optimal_value.values[0])*100
    result_df = pd.concat([df_new,result_df])
result_df
avg_gap_gen=result_df[result_df['SolnMethod']=='|genetic algorithm|']['gap'].mean()
avg_gap_sim=result_df[result_df['SolnMethod']=='|simulated annealing|']['gap'].mean()
avg_gap_tabu=result_df[result_df['SolnMethod']=='|tabu search|']['gap'].mean()
avg=[avg_gap_gen, avg_gap_sim, avg_gap_tabu]
data_1=result_df[result_df['SolnMethod']=='|genetic algorithm|']['gap']
data_2=result_df[result_df['SolnMethod']=='|simulated annealing|']['gap']
data_3=result_df[result_df['SolnMethod']=='|tabu search|']['gap']
# Labels for the months :
methods = ['genetic algorithm', 'simulated annealing', 'tabu search']
# Create two subplots sharing the x axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
# Add a title for the entire figure :
fig . suptitle ('Comparison of Optimality Gaps for Heuristics')
# Plot the Mean gaps in right subplot:
ax1 .bar (methods , avg , color='orange', edgecolor='black', linewidth=0.5)
# Add a title for the top subplot , and a label for its y- axis :
ax1 .set( title ='Mean Gaps', ylabel = 'Optimality Gap (%)')
ax1 . set_xticks (methods)

# Combine the data into a list
data = [data_1, data_2, data_3]

# Adding a title
plt.title('Distribution of Gap')
# Plot the boxplot in the left subplot :
ax2 . boxplot(data)
ax2.set_xticklabels(methods)
ax1.grid(False)
ax2.grid(False)





# In[54]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#read data:
df=pd.read_csv('violin_plot_example-query_1-03e231e21b3d-2023-05-01-16-02-33.csv')
#It sets the background to white with grid lines:
sns.set(style="whitegrid")
#We can add colors to each plot:
#colors_list = ['#78C850', '#F08030',  '#6890F0',  '#A8B820',  '#F8D030', '#E0C068', '#C03028', '#F85888', '#98D8D8']
#creating different violin plots in one figure:
f, ax = plt.subplots(figsize=(8, 8))
# Show each distribution with both violins (for male and female) and points
sns.violinplot(x="feed",y="weight",data=df, hue="sex", split=True, inner="box", palette=colors_list, cut=2, linewidth=3)
sns.stripplot(data=df, x="feed", y="weight", color='black', alpha=0.8)
sns.despine(left=True)
#add title
f.suptitle('Chick weights by feed type', fontsize=16, fontweight='bold')
#add label to X axis:
ax.set_xlabel("Feed",size = 14,alpha=0.7)
#add label to y axis:
ax.set_ylabel("Weight (g)",size = 14,alpha=0.7)
plt.ylim(0, 500)

