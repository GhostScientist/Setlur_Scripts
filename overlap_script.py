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

base_pair_info = []
for i in range(1, 23):
    base_pair_info.append(i)

base_pair_info = [
    [1, 248956422],
    [1, 242193529],
    [1, 198295559],
    [1, 190214555],
    [1, 181538259],
    [1, 170805979],
    [1, 159345973],
    [1, 145138636],
    [1, 138394717],
    [1, 133797422],
    [1, 135086622],
    [1, 133275309],
    [1, 114364328],
    [1, 107043718],
    [1, 101991189],
    [1, 90338345],
    [1, 83257441],
    [1, 80373285],
    [1, 58617616],
    [1, 64444167],
    [1, 46709983],
    [1, 50818468]
    ]


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

chr1_sizelist = []
chr2_sizelist = []
chr3_sizelist = []
chr4_sizelist = []
chr5_sizelist = []
chr6_sizelist = []
chr7_sizelist = []
chr8_sizelist = []
chr9_sizelist = []
chr10_sizelist = []
chr11_sizelist = []
chr12_sizelist = []
chr13_sizelist = []
chr14_sizelist = []
chr15_sizelist = []
chr16_sizelist = []
chr17_sizelist = []
chr18sizelist = []
chr19sizelist = []
chr20_sizelist = []
chr21_sizelist = []
chr22_sizelist = []





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

#def chr_counter():
    #chr_count_list = []
    #for x in range(1, 23):
        #chr_count_list.append(0) # Initializes list with 0 count for each chromosome.
    #for x in range(0, 850): #This is the chrom-count from the SuppTble set.
        #chr = int(supp_sheet.cell(x, chrom_col).value)
        #chr_count_list[chr-1]+= 1
    #print(chr_count_list

def CNV_Size_and_Frequency_tracker(): # This function will count the frequency of CNVs per Chromsome and their corresponding sizes.
    chr_count_list = []
    for x in range(1, 23):
        chr_count_list.append(0) # Initializes list with 0 count for each chromosome.

    for x in range(0, 850):
        chr = int(supp_sheet.cell(x, chrom_col).value)
        chr_count_list[chr-1]+= 1
        cnv_start = int(supp_sheet.cell(x, beg_col).value)
        cnv_stop = int(supp_sheet.cell(x, ending_col).value)
        cnv_size = int(cnv_stop - cnv_start)
        if chr = 1:
            chr1_sizelist.append(cnv_size)
        elif chr = 2:
            chr2_sizelist.append(cnv_size)
        elif chr = 3:
            chr3_sizelist.append(cnv_size)
        elif chr = 4:
            chr4_sizelist.append(cnv_size)
        elif chr = 5:
            chr5_sizelist.append(cnv_size)
        elif chr = 6:
            chr6_sizelist.append(cnv_size)
        elif chr = 7:
            chr7_sizelist.append(cnv_size)
        elif chr = 8:
            chr8_sizelist.append(cnv_size)
        elif chr = 9:
            chr9_sizelist.append(cnv_size)
        elif chr = 10:
            chr10_sizelist.append(cnv_size)
        elif chr = 11:
            chr11_sizelist.append(cnv_size)
        elif chr = 12:
            chr12_sizelist.append(cnv_size)
        elif chr = 13:
            chr13_sizelist.append(cnv_size)
        elif chr = 14:
            chr14_sizelist.append(cnv_size)
        elif chr = 15:
            chr15_sizelist.append(cnv_size)
        elif chr = 16:
            chr16_sizelist.append(cnv_size)
        elif chr = 17:
            chr17_sizelist.append(cnv_size)
        elif chr = 18:
            chr18_sizelist.append(cnv_size)
        elif chr = 19:
            chr19_sizelist.append(cnv_size)
        elif chr = 20:
            chr20_sizelist.append(cnv_size)
        elif chr = 21:
            chr21_sizelist.append(cnv_size)
        elif chr = 22:
            chr22_sizelist.append(cnv_size)

def data_builder():

def main():
    chr_counter()

main()
