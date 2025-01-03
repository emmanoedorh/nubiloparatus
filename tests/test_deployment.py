from lib.aws_services.vpc_service import create_vpc
from lib.client_locator import add_name_tag


def test_create_vpc_instance():
    """
    Test VPC instance creation
    """
    vpc_client, vpc_instance = create_vpc()
    vpc_instance_id = vpc_instance.get('Vpc', {}).get('VpcId')
    if vpc_instance_id:
        add_name_tag(vpc_client, vpc_instance_id, [{'key': "Name", 'value': ""}])


if __name__ == '__main__':
    test_create_vpc_instance()
