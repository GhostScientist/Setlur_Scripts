# This script will analyze the generated data sets and output the following information
# Number of Overlaps per Chromosome
#   Total Per Chromosome for All Data Sets
#   Mean Overlaps per Chromomsome
#   Standard Deviation of Overlaps per Chromosome
#   Number of Overlaps Per Permutation Per Chromosome
#
#   Dakota Kim - July 11th, 2017
#   Setlur Lab

import xlrd

TAD_workbook = xlrd.open_workbook('/Users/dakotakim/Desktop/Setlur_Scripts/mmc4.xlsx')
TAD_worksheet = TAD_workbook.sheet_by_index(0)

# Constants for TAD_workbook
chromosome_column = 0
begin_column = 1
end_column = 2

# Constants for Permutation data
p_chromosome_column = 0
p_cnv_begin_column = 1
p_cnv_end_column = 2
p_cnv_size = 3

TAD_list = []

class p_cnv_data(object):
    def __init__(self, chr, cnv_begin, cnv_end, cnv_size):
        self.chromosome = chr
        self.cnv_beginning = cnv_begin
        self.cnv_ending = cnv_end
        self.cnv_size = cnv_size

class TAD_data(object):
    def __init__(self, chrom, tad_begin, tad_end):
        self.chromosome = chrom
        self.tad_begin = tad_begin
        self.tad_end = tad_end

def intersect(one_list, second_list): # One output per permutation file
    count_per_chromosome = []
    for z in range(1,23):
        val = 0
        count_per_chromosome.append(val)
    for x in range(0, len(one_list)):
        x_range = range(one_list[x].tad_begin, one_list[x].tad_end)
        x_set = set(x_range)
        for y in range(0, len(second_list)):
            if (second_list[y].chromosome == one_list[x].chromosome):
                y_range = range(second_list[y].cnv_beginning, second_list[y].cnv_ending)
                temp_var = x_set.intersection(y_range)
                if len(temp_var) >= 1:
                    index_to_increment = int(second_list[y].chromosome)
                    count_per_chromosome[index_to_increment-1] += 1
    return (count_per_chromosome)



def p_set_builder(excel_file):
    file_workbook = xlrd.open_workbook(excel_file)
    file_worksheet = file_workbook.sheet_by_index(0)
    p_data_list = []
    for x in range(0, 850):
        temp_chrom = int(file_worksheet.cell(x, p_chromosome_column).value)
        temp_cnv_begin = int(file_worksheet.cell(x, p_chromosome_column).value)
        temp_cnv_end = int(file_worksheet.cell(x, p_chromosome_column).value)
        temp_cnv_size = temp_cnv_end - temp_cnv_begin
        temp_p_object = p_cnv_data(temp_chrom, temp_cnv_begin, temp_cnv_end, temp_cnv_size)
        p_data_list.append(temp_p_object)
    return (p_data_list)

def mmc4_list_builder(): # Builds a list for TAD_data objects
    for x in range(0, 2187):
        chromosome = TAD_worksheet.cell(x, chromosome_column).value
        chromosome = int(chromosome[3:])
        tad_begin = int(TAD_worksheet.cell(x, begin_column).value)
        tad_end = int(TAD_worksheet.cell(x, end_column).value)
        temp_variable = TAD_data(chromosome, tad_begin, tad_end)
        TAD_list.append(temp_variable)
    return TAD_list

def output():
    print ("Is this reached?")
    mmc4_list_builder()
    overall_output = []
    for x in range(0, 1000):
        print("On interation %d" % x)
        file = '/Users/dakotakim/Desktop/Setlur_Scripts/permutation/permutation_dataset%d.xlsx' % x
        second_list = p_set_builder(file)
        overall_output.append(intersect(mmc4_list_builder(), second_list))
        print(overall_output[x])
    print (overall_output)

output()
