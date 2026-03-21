#create a dictionary
genes = {'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
genes['MYC'] = 11.6 
import numpy as np
import matplotlib.pyplot as plt


#set and draw a bar plot
gene_expression =  (genes['TP53'],genes['EGFR'],genes['BRCA1'],genes['PTEN'],genes['ESR1'],genes['MYC'])
x_num = np.arange(6) 
width = 0.35
bar_plot = plt.bar(x_num, gene_expression, width)
plt.xlabel ('gene_types')
plt.ylabel ('gene_expression')
plt.title ('gene_expression_level')
plt.xticks(x_num, ('TP53','EGFR','BRCA1','PTEN','ESR1','MYC1'))
plt.yticks(np.arange(0, 16 ,1))
plt.show()

#print the expression level of a specific gene
specific_gene = 'MYC' # gene of interest
if specific_gene in genes:
    print('the expression level of', specific_gene, 'is', genes[specific_gene])
else:
    print('specific gene is out of the list, please check and corrct it')

#Calculate the average gene expression level across all genes
average_level = (gene_expression[0] + gene_expression[1] +gene_expression[2] + gene_expression[3] + gene_expression[ 4] + gene_expression[5])/6
print('the the average gene expression level across all genes is', average_level)
