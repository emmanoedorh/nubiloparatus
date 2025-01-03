from lib.client_locator import get_client


def create_vpc():
    """
    Create a VPC instance
    """
    vpc_client = get_client('ec2')
    return vpc_client, vpc_client.create_vpc(CidrBlock='10.0.0.0/16')
