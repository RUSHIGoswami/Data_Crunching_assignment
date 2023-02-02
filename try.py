# Importing the library
import warnings
import pandas as pd
import time
import psutil


#checking memory usage before executing code
used_memory_at_starting = psutil.virtual_memory().used/1000000000 


'''Here I will iteratively chunk the file in small amounts and concat them in iterations, but due to less time I am having i am uploading this much only but will complete this for sure.'''
start = time.time()
tsv1 = pd.read_csv("user_email_hash.1m.tsv", sep='\t', dtype={'id': object})
tsv2 = pd.read_csv("ip_1m.tsv", sep='\t', dtype={'id': object, 'ip_address': object})

columns = ['email', 'plain_pass']
tsv3 = pd.read_csv("plain_32m.tsv", header=None, names=columns, sep='\t', nrows=2900000)
end = time.time()
warnings.simplefilter(action='ignore', category=FutureWarning) # With this unwanted warning won't be displayed due to very large inputs.

# # user = pd.concat(tsv1)
# # ip = pd.concat(tsv2)
# plain = pd.concat(tsv3)

'''Here I am using left outer join in order to write only those plain password and IPs which are available on user_email_hash.1m.tsv file as we would always have user_id and related user_name with email  '''
startMerge = time.time()
opnew = pd.merge(tsv1, tsv3, how='left', on='email')
optsv = pd.merge(opnew, tsv2, how='left', on='id')
endMerge = time.time()

 # Writing output tsv file
optsv.to_csv('output.tsv', sep='\t')

# # print('The CPU usage is: ', psutil.cpu_percent(4), '%')
# # print('RAM usage in GB:- ', total_used_memory)
total_used_memory = psutil.virtual_memory().used/1000000000
print("Total memory used in execution is ",(total_used_memory - used_memory_at_starting)*1000,"MB")
print("Total time taken in execution ",endMerge - start,'sec.')