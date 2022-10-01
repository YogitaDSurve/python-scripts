import boto3

my_session = boto3.session.Session()
s3 = boto3.client('s3')
response = s3.list_buckets()
my_region = my_session.region_name
account_id = boto3.client("sts").get_caller_identity()["Account"]
print(account_id)
print("{0:60} {1:30} {2:20} {3:20} {4:20} {5:10}".format("BucketName", "Public Access Block", "Region", "Size", "CreationDate", "ModificationDate"))
for bucket in response['Buckets']:
    name = bucket["Name"]
    print("{0:60}".format(name))
    try:
        public_access_block = s3.get_public_access_block(Bucket=f"{name}", ExpectedBucketOwner=f"{account_id}")
        print(public_access_block)
    except Exception:
        print("Permission insufficient for accessing the bucket")
        print(Exception)
