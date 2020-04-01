import SparkFiles
import os

###
path = os.path.join(tempdir, "test.txt")

#entrada para funcionalidades spark
sc = SparkContext()
batch = []
max = None
processed = 0

def writeBatchData(b):
    
    session = driver.session()
    session.run('UNWIND {batch} AS row CREATE (n:Node {v: row})', {'batch': b})
    session.close()

def write2neo(v):
    batch.append(v)
    global processed
    processed += 1
    if len(batch) >= 1000 or processed >= max:
        writeBatchData(batch)
        batch[:] = []

dt = sc.parallelize(range(1, 100000))
max = dt.count()
dt.foreach(write2neo)