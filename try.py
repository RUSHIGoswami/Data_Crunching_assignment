# Importing the library
import pandas as pd
import time
import psutil
'''Here I will iteratively chunk the file in small amounts and concat them in iterations, but due to less time I am having i am uploading this much only but will complete this for sure.'''

'''Here I am using '''
start = time.time()
tsv1 = pd.read_csv("user_email_hash.1m.tsv", sep='\t', chunksize=100000)
tsv2 = pd.read_csv("ip_1m.tsv", sep='\t', chunksize=100000)

columns = ['email', 'plain_pass']
tsv3 = pd.read_csv("plain_32m.tsv", header=None, names=columns, sep='\t', chunksize=100000)
end = time.time()

user = pd.concat(tsv1)
ip = pd.concat(tsv2)
plain = pd.concat(tsv3)

startMerge = time.time()
'''Here I am using left outer join in order to write only those plain password and IPs which are available on user_email_hash.1m.tsv file as we would always have user_id and related user_name with email  '''
opnew = pd.merge(user, plain, how='left', on='email')
optsv = pd.merge(opnew, ip, how='left', on='id')
endMerge = time.time()
optsv.to_csv('output.tsv', sep='\t')
print('The CPU usage is: ', psutil.cpu_percent(4), '%')
used_memory = psutil.virtual_memory().used
print('RAM usage in GB:- ', (used_memory/1000000000))
print(endMerge - start,'sec.')