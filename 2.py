'''
Read the CSV file as an input argument (or take from user) to your program. Convert the csv and write in parquet (it is just another format). You can use any library. Test with https://support.staffbase.com/hc/en-us/article_attachments/360009197011/username-password-recovery-code.csv

IMPORTANT NOTEs: 
1. This works only with 64-bit python on Windows. Because pyarrow package works only on 64-bit version.
2. Tested with Python 3.9 64 bit on Windows, with pyarrow installed using "pip install pyarrow".

'''



import pyarrow.csv as pycsv
import pyarrow.parquet as pyparquet

# filename = input('Enter filename: ')
filename = 'username-password-recovery-code.csv'

table = pycsv.read_csv(filename)
pyparquet.write_table(table, filename.replace('csv', 'parquet'))

print('done.')