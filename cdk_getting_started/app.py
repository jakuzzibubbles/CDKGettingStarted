#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_getting_started.cdk_getting_started_stack import CdkGettingStartedStack


app = cdk.App()
CdkGettingStartedStack(app, "CdkGettingStartedStack")

app.synth()
