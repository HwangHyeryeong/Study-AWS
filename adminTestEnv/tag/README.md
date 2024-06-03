## addNewTag
- 테스트 환경에 있는 리소스 중 'TestTag' 태그를 가진 리소스에 새로운 태그를 추가하는 함수

## 사용 API
- boto3(https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## 테스트 조건
- 대상 태그: 'TestTag'
- 추가 태그: 'NEWTAG'

## 테스트 실행 결과
**Status**: Succeeded 
**Max memory used**: 78 MB 
**Time**: 5795.93 ms

**Test Event Name**   
(unsaved) test event

**Response**   
{
  "statusCode": 200,
  "body": "Tags created successfully"
}
