#!/usr/bin/env python3

from stacks.back_end.dynamodb_stack.dynamodb_stack import DynamoDBStack

from aws_cdk import core as cdk


app = cdk.App()


# Source Dynamodb table for Glue Elastic Views
src_dynamodb_stack = DynamoDBStack(
    app,
    f"{app.node.try_get_context('project')}-srcDynamoDB-stack",
    stack_log_level="INFO",
    description="Miztiik Automation: Source Dynamodb table for Glue Elastic Views"
)


# Stack Level Tagging
_tags_lst = app.node.try_get_context("tags")

if _tags_lst:
    for _t in _tags_lst:
        for k, v in _t.items():
            cdk.Tags.of(app).add(k, v, apply_to_launched_instances=True)

app.synth()
