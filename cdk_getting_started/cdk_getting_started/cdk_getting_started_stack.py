from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
)
from constructs import Construct

class CdkGettingStartedStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "linhSpecialBucket-2024")
        
