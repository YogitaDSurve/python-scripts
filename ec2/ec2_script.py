import boto3

my_session = boto3.session.Session()
client = boto3.client('ec2')
response = client.describe_instances()
my_region = my_session.region_name
print("{0:20} {1:30} {2:20} {3:10}".format("InstanceId", "InstanceName", "Region", "ImageId"))
for instance in response["Reservations"]:
    instanceId = instance['Instances'][0]['InstanceId']
    imageId = instance['Instances'][0]['ImageId']
    for tags in instance['Instances'][0]['Tags']:
        if tags['Key'] == 'Name':
            name = tags['Value']
            print("{0:20} {1:30} {2:20} {3:10}".format(instanceId, name, my_region, imageId))
