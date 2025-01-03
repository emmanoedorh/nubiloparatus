import boto3

from lib import KeyValueDict

DEFAULT_REGION_NAME = "us-east-2"

def get_client(client, region_name="us-east-2"):
    """
    Given a client, locate and return an instance of the client
    :param client: The wanted client
    :param region_name: service region
    :return: An instance of the client
    """
    return boto3.client(client, region_name=region_name)

def add_name_tag(client, resource_id, tag_names: list[KeyValueDict]):
    """
    Given a resource_id and a tag_name, add a tag to the resource
    :param client: The AWS client
    :param resource_id: The AWS resource ID
    :param tag_names: The tag name
    """
    return client.create_tags(
        Resources=[resource_id],
        Tags=tag_names,
    )