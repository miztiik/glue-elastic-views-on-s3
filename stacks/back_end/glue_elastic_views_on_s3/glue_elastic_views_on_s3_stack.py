from aws_cdk import core as cdk

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

class GlueElasticViewsOnS3Stack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
