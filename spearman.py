import xlrd, sys, scipy
import matplotlib.pyplot as plt
import numpy as np

excel_file = sys.argv[0] # Takes in path to excel file as argument.

"""Let me see if its simpler to create an external text_file with all
 of the relevant datasets and their respective paths. If I do that,
it should make it much simpler to run the new scripts a single time.
I will experiment with a respective file for output, perhaps as an image?
This will require a method to create and associate Subject ID with their
analysis/output. Also, multi-line comments are easier this way."""

data = xlrd.open_workbook('/Users/dakotakim/Desktop/test_file.xlsx')

# Create a list for both the chromosomes and the beta values
# I'll start with 100 different ID's. I can see what kind of stuff
# we'll be getting from this approach.
# 119 beta values per sample

workspace = data.sheet_by_index(0)

dict = {}
beta_values = []

for x in range(148, 248):
    for i in range(2, 119):

        #print(str(workspace.cell(x,0).value) + ":" + str(workspace.cell(x,i).value))
        if workspace.cell(x,i).value != '' :
            beta_values.append(float(workspace.cell(x,i).value))
    dict[workspace.cell(x,0).value] = (beta_values) # Maps each list to a CpG site.
    beta_values = [] # Resets the list of beta values.

box_list=[]
my_chroms = []

for entry in dict.keys(): # For loop to plot Box plots for each CpG site.
    my_chroms.append(str(entry))
    box_list.append(dict[entry])



temp = []
for i in range(0, len(my_chroms)):
    temp.append(i)

x = np.array(temp)

plt.boxplot(box_list,vert=1)
plt.xticks(x, my_chroms, rotation=90, fontsize=10)
plt.show()
