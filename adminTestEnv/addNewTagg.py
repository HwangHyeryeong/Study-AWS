import json
import boto3
        
TARGET_TAG = 'TestTag'
NEW_TAG = 'CHECKCHECK'        


def lambda_handler(event, context):
    try:
        resources = getResources()
        # print(resources)
        tagAwsResources(resources, NEW_TAG);
        
        return {
            'statusCode': 200,
            'body': 'Tags created successfully'
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }


# 모든 ARN 목록 읽어오기: {arn, 태그값} 쌍 저장
def getResources():
    try:
        client = boto3.client('resourcegroupstaggingapi')
        
        resources = []
        token = None
    
        while True:
            if paginationToken:
                response = client.get_resources(
                    TagFilters=[{'Key': TARGET_TAG}],
                    Pagination_token = token
                )
            else:
                response = client.get_resources(
                    TagFilters=[{'Key': TARGET_TAG}]
                )

            for resource in response['ResourceTagMappingList']:
                arn = resource['ResourceARN']
                tags = resource.get('Tags', [])
                for tag in tags:
                    if tag['Key'] == TARGET_TAG:
                        resources.append((arn, tag['Value']))
                        break
    
            # 더 넘어올 데이터 있는지 토근값 확인(null이면 마지막 페이지)
            token = response.get('Pagination_token')
            if not token:
                break
        
        print("Success@getResources()")        
        return resources
        
    except Exception as e:
        print(f"Error@getResources(): {str(e)}")
        
        
# ARN으로 태깅
def tagAwsResources(resources, tagKey):
    try:
        tag_client = boto3.client('resourcegroupstaggingapi')
        
        for resource in resources:
            arn = []
            arn.append(resource[0])
            response = tag_client.tag_resources(
                        ResourceARNList = arn,
                        Tags = {
                            tagKey: resource[1]
                        }
                    )
            print(f"[TAGGED RESOURCE]: {response[0]}, [OWNER]: {response[1]}")
            
        print("Success@tagAwsResources()")
        return
    
    except Exception as e:
        print(f"Error@tagAwsResources(): {str(d)}")
