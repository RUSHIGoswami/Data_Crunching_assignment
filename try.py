import pandas as pd


'''Here I will iteratively chunk the file in small amounts and concat them in iterations, but due to less time I am having i am uploading this much only but will complete this for sure.'''

tsv1 = pd.read_csv("user_email_hash.1m.tsv", sep='\t')
tsv2 = pd.read_csv("ip_1m.tsv", sep='\t')

columns = ['email', 'plain_pass']
tsv3 = pd.read_csv("plain_32m.tsv", header=None, names=columns, sep='\t', )

opnew = pd.merge(tsv1, tsv3, how='left', on='email')
optsv = pd.merge(opnew, tsv2, how='left', on='id')

print(optsv)