'''
Created on 25-Oct-2017

@author: bigdata
'''
import os
import math
def test_File(filename):
    print os.path.basename(filename)
    source_size = os.stat(filename).st_size
    bytes_per_chunk = 5*1024*1024
    chunks_count = int(math.ceil(source_size / float(bytes_per_chunk)))
    print chunks_count
    for i in range(0,chunks_count):
        offset = i * bytes_per_chunk
        remaining_bytes = source_size - offset
        bytes = min([bytes_per_chunk, remaining_bytes])
        print bytes
        part_num = i+1
        print "uploading part " + str(part_num) + " of " + str(chunks_count)
        with open(filename, 'r') as fp:
            fp.seek(offset)
         
    
#test_File("/home/bigdata/bigdata_noahdata/Alex_Py/testpy.csv")    
