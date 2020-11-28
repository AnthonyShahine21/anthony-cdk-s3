#!/usr/bin/env python3

from aws_cdk import core

from anthony_cdk_s3.anthony_cdk_s3_stack import AnthonyCdkS3Stack


app = core.App()
AnthonyCdkS3Stack(app, "anthony-cdk-s3")

app.synth()
