from matplotlib import pyplot as plt
import matplotlib as mpl
import sys
prec = []
num_tran=[]
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
# prec_file = '/Users/alainashumate/remote_salz/final/human_new/prec'
# num_tran_file = '/Users/alainashumate/remote_salz/final/human_new/num.tran'

prec_file = sys.argv[1]
num_tran_file = sys.argv[2]
with open(prec_file) as pf:
    for line in pf:
        prec.append(float(line.strip().split(',')[1]))


with open(num_tran_file) as nf:
    for line in nf:
        num_tran.append(float(line.strip().split(',')[1]))

print(prec, num_tran)
plt.scatter(prec, num_tran, c=['blue', 'purple' ,'red'], s=100)
plt.xlabel('Precision (%)')
plt.ylabel('# Annotated Transcripts Assembled')

plt.savefig('/Users/alainashumate/Desktop/' + "new_human_data.svg",
            format='svg', dpi=1200,
            transparent=True)