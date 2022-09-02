import boto3

client = boto3.client('ec2')
response = client.describe_instances()
tab = "\t"
print("InstanceId"+tab+tab+"InstanceName")
for instance in response["Reservations"]:
    instanceId = instance['Instances'][0]['InstanceId']
    for tags in instance['Instances'][0]['Tags']:
        if tags['Key'] == 'Name':
            name = tags['Value']
            print(instanceId+tab+name)
