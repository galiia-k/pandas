import pandas as pd
from matplotlib import pyplot as plt

table_1 = pd.read_html("results_ejudge.html")[0]
table_2 = pd.read_excel("students_info.xlsx")

table_1.fillna(0, inplace=True)
table_2.dropna(inplace=True)

table = table_1.merge(table_2, how='inner', left_on='User', right_on='login')

faculty_groups = table.groupby(['group_faculty']).Solved.mean().index
average_per_faculty_groups = table.groupby(['group_faculty']).Solved.mean().values

groups_out = table.groupby(['group_out']).Solved.mean().index
average_per_groups_out = table.groupby(['group_out']).Solved.mean().values

fig, ax = plt.subplots(1, 2)

ax[0].bar(list(map(str, faculty_groups)), average_per_faculty_groups)
ax[0].set_xlabel('faculty_group')
ax[0].set_ylabel('average mark')

ax[1].bar(list(map(str, groups_out)), average_per_groups_out)
ax[1].set_xlabel('group_out')

fig.suptitle('Average mark in a group')
plt.show()
plt.savefig('average_marks.png')

print("Номера факультетских групп: ", set(table.loc[(table_1.H >= 10) | (table_1.G >= 10)].group_faculty))
print("Номера групп по информатике: ", set(table.loc[(table_1.H >= 10) | (table_1.G >= 10)].group_out))