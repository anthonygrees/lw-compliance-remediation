# -*- coding: utf-8 -*-
"""
Lacework Remediation: iam_user_disable_unused_access_key.py

This function will disable any unused access keys for a user.
"""

import logging

import boto3

from botocore.exceptions import ClientError
from datetime import datetime, timezone

logger = logging.getLogger()

MAX_UNUSED_DAYS = 90


def get_days_from_last_use(access_key, iam_client):
    # Get current time
    curr_time = datetime.now(timezone.utc)

    access_key_id = access_key["AccessKeyId"]

    # Get the access key last used data
    access_key_last_use = iam_client.get_access_key_last_used(AccessKeyId=access_key_id)
    access_key_last_use = access_key_last_use["AccessKeyLastUsed"]

    # Check if the access key is ever been used, otherwise use create date
    if 'LastUsedDate' in access_key_last_use:
        # Return days since last use
        return (curr_time - access_key_last_use["LastUsedDate"]).days
    else:
        # Return days since create
        return (curr_time - access_key["CreateDate"]).days


def run_action(entity):
    logger.info("Initiating deactivation of unused access keys.")

    # Create an IAM client
    iam = boto3.client("iam")

    try:
        split_name = entity.split("user/")

        if len(split_name) == 2:
            username = split_name[1]

            # Get all access keys
            paginator = iam.get_paginator('list_access_keys')

            # Iterate through all access keys
            for access_keys in paginator.paginate(UserName=username):

                # Get a list of Access Key metadata
                access_keys = access_keys["AccessKeyMetadata"]

                # Loop through each access key
                for access_key in access_keys:

                    logger.info("### ACCESS KEY")
                    logger.info(access_key)

                    # Get access key id
                    access_key_id = access_key["AccessKeyId"]

                    # Calc the number of days since last use
                    days_from_last_use = get_days_from_last_use(access_key, iam)

                    # if the access key is not used for more than 90 days it will be turn inactive
                    if days_from_last_use > MAX_UNUSED_DAYS:

                        # Deactivate access key
                        iam.update_access_key(
                            UserName=username,
                            AccessKeyId=access_key_id,
                            Status="Inactive"
                        )
                        logger.info(f"IAM User '{username}' access key with id '{access_key_id}' "
                                    f"was deactivated due of being unused for {days_from_last_use} "
                                    "days.")
                    else:
                        logger.info(f"IAM User '{username}' access key with id '{access_key_id}' "
                                    f"was used {days_from_last_use} days ago.")
        else:
            logger.warning(f"Username {entity} was not properly parsed.")

    except ClientError as e:
        logger.error(f"Unexpected error: {e}.")
