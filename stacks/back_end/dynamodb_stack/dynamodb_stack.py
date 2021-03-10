from aws_cdk import core as cdk
from aws_cdk import aws_dynamodb as _ddb

import os


class GlobalArgs:
    """
    Helper to define global statics
    """

    OWNER = "MystiqueAutomation"
    ENVIRONMENT = "production"
    REPO_NAME = "glue-elastic-views-on-s3"
    SOURCE_INFO = f"https://github.com/miztiik/{REPO_NAME}"
    VERSION = "2021_03_07"
    MIZTIIK_SUPPORT_EMAIL = ["mystique@example.com", ]


class DynamoDBStack(cdk.Stack):

    def __init__(
        self,
        scope: cdk.Construct,
        construct_id: str,
        stack_log_level: str,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        id_prefix_str = f"elasticViews"
        ddb_table_name = "elasticViewsMoviesTable_2021"

        # create dynamo table
        movies_table = _ddb.Table(
            self,
            f"{id_prefix_str}SrcDdb",
            partition_key=_ddb.Attribute(
                name="year",
                type=_ddb.AttributeType.NUMBER
            ),
            sort_key=_ddb.Attribute(
                name="title",
                type=_ddb.AttributeType.STRING
            ),
            read_capacity=50,
            write_capacity=50,
            table_name=f"{ddb_table_name}",


            removal_policy=cdk.RemovalPolicy.DESTROY
        )


        ###########################################
        ################# OUTPUTS #################
        ###########################################
        output_0 = cdk.CfnOutput(
            self,
            "AutomationFrom",
            value=f"{GlobalArgs.SOURCE_INFO}",
            description="To know more about this automation stack, check out our github page."
        )

        output_1 = cdk.CfnOutput(
            self,
            "srcMoviesDdbTable",
            value=f"https://console.aws.amazon.com/events/home?region={cdk.Aws.REGION}#/eventbus/{movies_table.table_name}",
            description="Source Dynamodb table for Glue Elastic Views"
        )
