import xlrd
import matplotlib.pyplot as plt
import numpy as np

print("Now opening the workbook")
supp_table = xlrd.open_workbook('/Users/dakotakim/Desktop/Setlur_Datasets/supplemental_table10.xlsx')
print("Now opening the superseries")
beta_values = xlrd.open_workbook('/Users/dakotakim/Desktop/Setlur_Datasets/GSE65820_series_matrix.xlsx')
print("DONE!")

workspace_supp = supp_table.sheet_by_index(0)
workspace_beta = beta_values.sheet_by_index(0)

# Making 4 lists, one for each category.
category_1 = []
category_2 = []
category_3 = []

category_col = 35
sample_id_col = 2
sample_title_row = 111
begin_mine = 148
end_mine = 100 # Only taking 10000 values for each subject.
beta_val_col = 2

used_subject_ids = []

# This will build expression data.

for x in range(3, 50): # Will go through table 10.1's category list.
    print("You've finally begun a loop!")
    if (workspace_supp.cell(x, category_col).value) == '1':
        sample_id_name = workspace_supp.cell(x, sample_id_col).value
        if sample_id_name not in used_subject_ids:
            used_subject_ids.append(sample_id_name)
            for y in range(2, 115):
                temp_name = workspace_beta.cell(sample_title_row,y).value
                sliced_name = temp_name[9:]
                if sample_id_name == sliced_name:
                    for x in range(begin_mine, end_mine):
                        print(float(workspace_beta.cell(beta_val_col, x).value))
                        category_1.append(float(workspace_beta.cell(beta_val_col, x).value))
        else:
            print("this is breaking")
            break
    elif (workspace_supp.cell(x, category_col).value) == '2':
        sample_id_name = workspace_supp.cell(x, sample_id_col).value
        if sample_id_name not in used_subject_ids:
            used_subject_ids.append(sample_id_name)
            for y in range(2, 115):
                temp_name = workspace_beta.cell(sample_title_row,y).value
                sliced_name = temp_name[9:]
                if sample_id_name == sliced_name:
                    for x in range(begin_mine, end_mine):
                        float(workspace_beta.cell(beta_val_col, x).value)
                        category_2.append(float(workspace_beta.cell(beta_val_col, x).value))
        else:
            print("this is breaking")
            break
    elif (workspace_supp.cell(x, category_col).value) == '3':
        sample_id_name = workspace_supp.cell(x, sample_id_col).value
        if sample_id_name not in used_subject_ids:
            used_subject_ids.append(sample_id_name)
            for y in range(2, 115):
                temp_name = workspace_beta.cell(sample_title_row,y).value
                sliced_name = temp_name[9:]
                if sample_id_name == sliced_name:
                    for x in range(begin_mine, end_mine):
                        float(workspace_beta.cell(beta_val_col, x).value)
                        category_3.append(float(workspace_beta.cell(beta_val_col, x).value))
        else:
            print("this is breaking")
            break

# Data has been acquired. Time to analyze

plt.boxplot(category_1)
plt.show()
