import xlrd
import pickle




mmc4_workbook = xlrd.open_workbook('/Users/dakotakim/Desktop/pySpear_Script/mmc4.xlsx')
supp_workbook = xlrd.open_workbook('/Users/dakotakim/Desktop/pySpear_Script/dakota_supp_table.xlsx')

class gene_data(object):
    def __init__(self, chr, begin, end, cell_row):
        self.chr = chr
        self.begin = begin
        self.end = end
        self.cell_row = cell_row

class supp_gene_data(object):
        def __init__(self, chr, begin, end, cell_row, gene):
            self.chr = chr
            self.begin = begin
            self.end = end
            self.cell_row = cell_row
            self.gene = gene

class intersected_data(object):
    def __init__(self, chromosome, x_begin, x_end, y_begin, y_end):
        self.chromosome = chromosome
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin
        self.y_end = y_end

# for mmc4
chromosome_col = 0
begin_col = 1
end_col = 2

# for supp_table
chrom_col = 1
beg_col = 2
ending_col = 3
gene_column = 5

mmc4_sheet = mmc4_workbook.sheet_by_index(0)
supp_sheet = supp_workbook.sheet_by_index(0)

mmc4_list = []
supp_list = []

overlap_list = []


def mmc4_listbuilder():
    for x in range(0, 2187): # Number of rows.
        chromosome = mmc4_sheet.cell(x, chromosome_col).value
        chromosome = int(chromosome[3:]) # isolates Chromosome number.
        begin = int(mmc4_sheet.cell(x, begin_col).value)
        end = int(mmc4_sheet.cell(x, end_col).value)
        temp_variable = gene_data(chromosome, begin, end, x);
        mmc4_list.append(temp_variable)


def supp_listbuilder():
    for x in range(0, 850):
        chromosome = supp_sheet.cell(x, chrom_col).value
        chromosome = int(chromosome)
        begin = int(supp_sheet.cell(x, beg_col).value)
        end = int(supp_sheet.cell(x, ending_col).value)
        gene = supp_sheet.cell(x, gene_column).value
        #print(begin)
        #print(end)
        temp_variable = supp_gene_data(chromosome, begin, end, x, gene)
        #print(temp_variable.begin)
        supp_list.append(temp_variable)


def overlap(one_list, second_list):
    count = 0
    for x in range(0, len(one_list)):
        x_range = range(one_list[x].begin, one_list[x].end)
        x_set = set(x_range)
        for y in range(0, len(second_list)):
            if (second_list[y].chr == one_list[x].chr):
                y_range = range(second_list[y].begin, second_list[y].end)
                temp_var = x_set.intersection(y_range)
                if len(temp_var) >= 10:
                    count+=1
                    print("""
                            Intersection Found:
                            Gene: %s
                            Chr: %d \t mmc4-Row: %d\t supp-Row: %d
                            mmc4-begin: %d\tmmc4-end: %d
                            supp-begin %d\tsupp-end: %d\t
                            """ % (second_list[y].gene, one_list[x].chr, one_list[x].cell_row, second_list[y].cell_row, one_list[x].begin, one_list[x].end, second_list[y].begin, second_list[y].end))
    print("Total count is %d" % count)

def chr_counter():
    chr_count_list = []
    for x in range(1, 23):
        chr_count_list.append(0) # Initializes list with 0 count for each chromosome.
    for x in range(0, 850): #This is the chrom-count from the SuppTble set.
        chr = int(supp_sheet.cell(x, chrom_col).value)
        chr_count_list[chr-1]+= 1
    print(chr_count_list)

def CNV_Size_tracker():


    if chr = 1:

    if chr = 2:

    if chr = 3:

    if chr = 4:

    if chr = 5:

    if chr = 6:

    if chr = 7:

    if chr = 8:

    if chr = 9:

    if chr = 10:

    if chr = 11:

    if chr = 12:

    if chr = 13:

    if chr = 14:

    if chr = 15:

    if chr = 16:

    if chr = 17:

    if chr = 18:

    if chr = 19:

    if chr = 20:

    if chr = 21:

    if chr = 22:




def main():
    chr_counter()

main()
