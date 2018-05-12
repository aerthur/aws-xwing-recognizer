import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('deeplens-xwing')
bucket_prefix="train"
objs = bucket.objects.filter(
    Prefix = bucket_prefix)

file = open('model.lst','w') 
i=0
idClass=0

for key in objs:
    if key.key[-1] == '/' or '.lst' in key.key:
        continue
    key = key.key.encode('utf-8').replace('train/', '')
    print(key)
    file.write(str(i)+'\t'+str(idClass)+'\t'+key+'\n')
    i+=1 

file.close()