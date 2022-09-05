import boto3

my_session = boto3.session.Session()
client = boto3.client('ec2')
response = client.describe_instances()
my_region = my_session.region_name
print("{0:20} {1:30} {2:10} {3:30} {4:30} {5:10}".format("InstanceId", "InstanceName", "Region", "ImageId", "PrivateIp", "PublicIP"))
for instance in response["Reservations"]:
    instances = instance['Instances'][0]
    instanceId = instances['InstanceId']
    imageId = instances['ImageId']
    privateIp = instances['PrivateIpAddress']
    publicIp = "NA"
    if "PublicIpAddress" in instances.keys():
        publicIp = instance['Instances'][0]['PublicIpAddress']

    for tags in instances['Tags']:
        if tags['Key'] == 'Name':
            name = tags['Value']
            print("{0:20} {1:30} {2:10} {3:30} {4:30} {5:10}".format(instanceId, name, my_region, imageId, privateIp, publicIp))
