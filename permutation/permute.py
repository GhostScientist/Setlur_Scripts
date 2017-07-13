import xlrd
import xlsxwriter
from random import *

mmc4_workbook = xlrd.open_workbook('/Users/dakotakim/Desktop/pySpear_Script/mmc4.xlsx')
supp_workbook = xlrd.open_workbook('/Users/dakotakim/Desktop/pySpear_Script/dakota_supp_table.xlsx')

mmc4_sheet = mmc4_workbook.sheet_by_index(0)
supp_sheet = supp_workbook.sheet_by_index(0)

# for mmc4
chromosome_col = 0
begin_col = 1
end_col = 2

# for supp_table
chrom_col = 1
beg_col = 2
ending_col = 3
gene_column = 5

size_list = [] # Will keep track of chromosomes and CNV sizes

base_pair_info = []
for i in range(1, 23):
    base_pair_info.append(i)

base_pair_info = [
    [1, 247249719],
    [1, 242951149],
    [1, 199501827],
    [1, 191273063],
    [1, 180857866],
    [1, 170899992],
    [1, 158821424],
    [1, 146274826],
    [1, 140273252],
    [1, 135374737],
    [1, 134452384],
    [1, 132349534],
    [1, 114142980],
    [1, 106368585],
    [1, 100338915],
    [1, 88827254],
    [1, 78774742],
    [1, 76117153],
    [1, 63811651],
    [1, 62435964],
    [1, 46944323],
    [1, 49691432]
    ]


def CNV_Size_and_Frequency_tracker(): # This function will count the frequency of CNVs per Chromsome and their corresponding sizes.
    for x in range(0, 850):
        chromosome = int(supp_sheet.cell(x, chrom_col).value)
        cnv_start = int(supp_sheet.cell(x, beg_col).value)
        cnv_stop = int(supp_sheet.cell(x, ending_col).value)
        cnv_size = int(cnv_stop - cnv_start)
        size_list.append([chromosome, cnv_size])

def data_builder():
    #This method will need to output 1000 different xlsx files. Computing intensive work.
    for x in range(0,1000):
        print("Iteration %d has been reached" % x)
        row = 0
        col = 0
        list_of_values = [] # will take lists as entries of the formate [chr, cnv_begin, cnv_end, size]
        file_string = 'permutation_dataset'
        file_name = file_string + str(x) + '.xlsx'
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, "Chromosome")
        worksheet.write(row, col + 1,  "CNVBegin")
        worksheet.write(row, col + 2,  "CNVEnd")
        worksheet.write(row, col + 3,  "Distance")
        row += 1
        for each in size_list:
            temp_size = each[1]
            chrom_of_inter = each[0]
            random_spot = randint(1, base_pair_info[chrom_of_inter-1][1])
            if (random_spot + temp_size <= base_pair_info[chrom_of_inter-1][1]):
                start_spot = random_spot
                end_spot = random_spot + temp_size
            elif (random_spot + temp_size > base_pair_info[chrom_of_inter-1][1]):
                start_spot = random_spot - temp_size
                end_spot = random_spot
            list_of_values.append([chrom_of_inter, start_spot, end_spot, temp_size])
        for chrom, start, end, size in (list_of_values):
            worksheet.write(row, col, chrom)
            worksheet.write(row, col + 1,  start)
            worksheet.write(row, col + 2,  end)
            worksheet.write(row, col + 3,  size)
            row += 1
        workbook.close()

def main():
    CNV_Size_and_Frequency_tracker()
    data_builder()

main()
