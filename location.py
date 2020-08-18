import os
import modules.config as con

outpath = os.path.join(os.getcwd(), 'output')
outpath_file = os.path.join(outpath, 'out.xlsx')
con.pathd = str(outpath_file).replace('\output\out.xlsx', '')
# bcd = ('cd',con.pathd)
# cd = ' '.join(bcd)
# f = open('working-directory.bat','w')
# f.write('@echo off' + '\n')
# f.write(str(cd) + '\n')
# f.write('python main.py')
# f.close()

os.system('working-directory.bat')