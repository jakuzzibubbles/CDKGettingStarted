from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
)
from constructs import Construct

class ZweitesCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queue = sqs.Queue(
             self, "ZweitesCdkQueue",
            visibility_timeout=Duration.seconds(300),
        )
        
        bucket = s3.Bucket(self, "ZweitesBucket-2024-LN")
