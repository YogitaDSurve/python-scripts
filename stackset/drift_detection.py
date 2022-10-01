import boto3
import botocore

client = boto3.client('cloudformation')

response = client.list_stack_sets()

print("{0:90} {1:40}".format("Stack Name", "Stack Drift Status"))
for stack in response['Summaries']:
    stack_name = stack['StackSetName']
    stack_drift_status = stack['DriftStatus']
    print("{0:90} {1:40}".format(stack_name, stack_drift_status))

    if stack_drift_status == "NOT_CHECKED" or stack_drift_status == "DELETED" or stack_drift_status == "DRIFTED":
        stack_drift_status = "NOT_IN_SYNC"
        try:
            detect_drift = client.detect_stack_set_drift(
                StackSetName=f"{stack_name}",
                OperationPreferences={
                    'RegionConcurrencyType': 'PARALLEL',
                    'FailureToleranceCount': 30,
                    'MaxConcurrentCount': 30
                })
            OperationId = detect_drift['OperationId']
            stackSetOperations = client.describe_stack_set_operation(
                StackSetName=f"{stack_name}",
                OperationId=f"{OperationId}"
            )
            print("\n StackSet Operation Details: \n", stackSetOperations)
        except Exception:
            print("StackSet Operation in progress")
            print(Exception)
