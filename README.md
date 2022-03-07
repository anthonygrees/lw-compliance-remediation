<a href="https://lacework.com"><img src="https://techally-content.s3-us-west-1.amazonaws.com/public-content/lacework_logo_full.png" width="600"></a>

# Lacework Compliance Remediation

Terraform module for remediating common non-compliant resources in AWS as detected by Lacework.

## Requirements

| Name      | Version    |
| --------- | ---------- |
| terraform | >= 0.12.31 |
| aws       | ~> 3.0     |
| lacework  | ~> 0.2     |

## Providers

| Name     | Version |
| -------- | ------- |
| archive  | 2.2.0   |
| aws      | 3.74.3  |
| lacework | 0.16.0  |
| local    | 2.1.0   |
| random   | 3.1.0   |
| template | 2.2.0   |

## Resources

| Name                                                                                                                                                                      | Type        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [aws_cloudwatch_event_bus.lacework_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_bus)                              | resource    |
| [aws_cloudwatch_event_permission.lacework_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_permission)                | resource    |
| [aws_cloudwatch_event_rule.lacework_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_rule)                            | resource    |
| [aws_cloudwatch_event_target.lacework_events](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_target)                        | resource    |
| [aws_cloudwatch_log_group.event_router](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group)                                 | resource    |
| [aws_iam_role.lambda_execution](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role)                                                     | resource    |
| [aws_iam_role_policy.lambda_ec2_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy)                                      | resource    |
| [aws_iam_role_policy.lambda_iam_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy)                                      | resource    |
| [aws_iam_role_policy.lambda_log_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy)                                      | resource    |
| [aws_iam_role_policy.lambda_s3_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy)                                       | resource    |
| [aws_lambda_function.event_router](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function)                                           | resource    |
| [aws_lambda_permission.allow_cloudwatch_invocation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission)                        | resource    |
| [lacework_alert_channel_aws_cloudwatch.remediation_channel](https://registry.terraform.io/providers/lacework/lacework/latest/docs/resources/alert_channel_aws_cloudwatch) | resource    |
| [lacework_alert_rule.remediation_rule](https://registry.terraform.io/providers/lacework/lacework/latest/docs/resources/alert_rule)                                        | resource    |
| [local_file.remediation_map](https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file)                                                          | resource    |
| [random_id.uniq](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/id)                                                                       | resource    |
| [archive_file.lambda_app](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file)                                                        | data source |
| [template_file.remediation_map](https://registry.terraform.io/providers/hashicorp/template/latest/docs/data-sources/file)                                                 | data source |

## Inputs

| Name                           | Description                                                                | Type           | Default                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required |
| ------------------------------ | -------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: |
| event_bridge_bus_name          | The desired name of the EventBridge event bus.                             | `string`       | `""`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    no    |
| event_bridge_rule_name         | The desired name of the EventBridge event rule.                            | `string`       | `""`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    no    |
| lacework_alert_rule_categories | The categories of Lacework alerts that should be sent to the alert channel | `list(string)` | <pre>[<br> "Compliance"<br>]</pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |    no    |
| lacework_alert_rule_severities | The severities of Lacework alerts that should be sent to the alert channel | `list(string)` | <pre>[<br> "Critical",<br> "High"<br>]</pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |    no    |
| lacework_aws_account           | The AWS account used by Lacework.                                          | `string`       | `"434813966438"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |    no    |
| lacework_integration_name      | The name to use for the Alert Channel integration in Lacework.             | `string`       | `"Compliance Events to CloudWatch"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |    no    |
| lacework_resource_prefix       | The name prefix to use for resources provisioned by the module.            | `string`       | `"lacework-remediation"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |    no    |
| lambda_function_name           | The desired name of the Lacework event router lambda function.             | `string`       | `""`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    no    |
| lambda_log_retention           | The number of days in which to retain logs for the remediation lambda      | `number`       | `30`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    no    |
| lambda_role_name               | The desired IAM role name for the Lacework remediation lambda function.    | `string`       | `""`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    no    |
| remediation_map                | A map of Lacework violation reasons to remediation functions.              | `map(string)`  | <pre>{<br> "AWS_CIS_1_3_AccessKey1NotUsed": "iam_disable_unused_access_key",<br> "AWS_CIS_1_3_PasswordNotUsed": "iam_disable_login_profile",<br> "AWS_CIS_1_4_AccessKey1NotRotated": "iam_disable_unused_access_key",<br> "LW_AWS_GENERAL_SECURITY_1_Ec2InstanceWithoutTags": "ec2_stop_instance",<br> "LW_S3_13_LoggingNotEnabled": "s3_enable_access_logs",<br> "LW_S3_16_VersioningNotEnabled": "s3_enable_versioning",<br> "LW_S3_1_ReadAccessGranted": "s3_delete_acls",<br> "LW_S3_2_WriteAccessGranted": "s3_delete_acls"<br>}</pre> |    no    |
| sqs_queue_name                 | The desired name of the SQS event queue.                                   | `string`       | `""`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    no    |

## Outputs

| Name                   | Description                 |
| ---------------------- | --------------------------- |
| event_bridge_bus_arn   | EventBridge Event Bus ARN   |
| event_bridge_bus_name  | EventBridge Event Bus Name  |
| event_bridge_rule_arn  | EventBridge Event Rule ARN  |
| event_bridge_rule_name | EventBridge Event Rule Name |
| lambda_function_arn    | Lambda Function ARN         |
| lambda_function_name   | Lambda Function Name        |
| lambda_role_arn        | Lambda IAM Role ARN         |
| lambda_role_name       | Lambda IAM Role Name        |
