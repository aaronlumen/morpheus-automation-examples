# A script that allows access to numerous rarely published api endpoints on the morpheusdata platform based on
# information found here: https://github.com/gomorpheus and here:  https://clidocs.morpheusdata.com/en/latest/
#
# The script should be called with the following syntax:
#
# python md_aaronlumen_script.py -u <MORPHEUS_DATA_USERNAME> -p <MORPHEUS_DATA_PASSWORD>
# github.com/aaronlumen@Lumen Technologies 
# kma
# August 2022:\A\a\r\o\n\ \S\u\r\i\n\a:aaron.\s\u\r\i\n\a@lumen.com:509-\3\1\9-99\9\8
#
#!/usr/bin/env python

import argparse
import requests

# Define arguments for the script
parser = argparse.ArgumentParser(description='Script for accessing rarely published API endpoints on the Lumen Edge Orchestrator \(Morpheus\) platform')
parser.add_argument('-u', '--username', help='Morpheus Username', required=True)
parser.add_argument('-p', '--password', help='Morpheus Password', required=True)
args = parser.parse_args()

# Set variables for username and password from arguments
username = args.username
password = args.password

# Define base URL for MorpheusData API calls [edgelab]
base_url = 'https://edgelab.lumen.com/'

# Define headers for MorpheusData API calls - must include content type and accept type as JSON
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Function for making GET API calls
def get_request(url, headers):
    response = requests.get(url, headers=headers)
    return response.json()

# Function for making POST API calls
def post_request(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Function for making PUT API calls
def put_request(url, headers, payload):
    response = requests.put(url, headers=headers, json=payload)
    return response.json()

# Function for making DELETE API calls
def delete_request(url, headers):
    response = requests.delete(url, headers=headers)
    return response.json()


# Login to MorpheusData platform and get access token
login_url = base_url + 'oauth/token'
login_payload = {'grant_type': 'password', 'username': username, 'password': password}
login_response = post_request(login_url, headers, login_payload)
access_token = login_response['17fbd63f-11c3-not-today-folks-ae24bdc4']

# Set header to use access token for all subsequent API calls - loop results from [aaronlumen-morph-customer-apiToken script] to seed and feed for desired metrics from each ID
headers['Authorization'] = 'Bearer ' + access_token

# Get list of all accounts
accounts_url = base_url + 'api/accounts'
accounts_response = get_request(accounts_url, headers)
print(accounts_response)

# Get account by id - loop results from previous query to seed and feed for desired metrics from each ID
account_id = '<ACCOUNT_ID>' # Replace with actual account id
account_url = base_url + 'api/accounts/' + account_id
account_response = get_request(account_url, headers)
print(account_response)

# Get list of all clouds
clouds_url = base_url + 'api/clouds'
clouds_response = get_request(clouds_url, headers)
print(clouds_response)

# Get cloud by id - loop results from previous query to seed and feed for desired metrics from each ID
cloud_id = '<CLOUD_ID>' # Replace with actual cloud id
cloud_url = base_url + 'api/clouds/' + cloud_id
cloud_response = get_request(cloud_url, headers)
print(cloud_response)

# Get list of all instances
instances_url = base_url + 'api/instances'
instances_response = get_request(instances_url, headers)
print(instances_response)

# Get instance by id - loop results from previous query to seed and feed for desired metrics from each ID
instance_id = '<INSTANCE_ID>' # Replace with actual instance id
instance_url = base_url + 'api/instances/' + instance_id
instance_response = get_request(instance_url, headers)
print(instance_response)

# Get list of all jobs
jobs_url = base_url + 'api/jobs'
jobs_response = get_request(jobs_url, headers)
print(jobs_response)

# Get job by id - loop results from previous query to seed and feed for desired metrics from each ID
job_id = '<JOB_ID>' # Replace with actual job id
job_url = base_url + 'api/jobs/' + job_id
job_response = get_request(job_url, headers)
print(job_response)

# Get list of all layers
layers_url = base_url + 'api/layers'
layers_response = get_request(layers_url, headers)
print(layers_response)

# Get layer by id - loop results from previous query to seed and feed for desired metrics from each ID
layer_id = '<LAYER_ID>' # Replace with actual layer id
layer_url = base_url + 'api/layers/' + layer_id
layer_response = get_request(layer_url, headers)
print(layer_response)

# Get list of all load balancers
load_balancers_url = base_url + 'api/loadBalancers'
load_balancers_response = get_request(load_balancers_url, headers)
print(load_balancers_response)

# Get load balancer by id - loop results from previous query to seed and feed for desired metrics from each ID
load_balancer_id = '<LOAD_BALANCER_ID>' # Replace with actual load balancer id
load_balancer_url = base_url + 'api/loadBalancers/' + load_balancer_id
load_balancer_response = get_request(load_balancer_url, headers)
print(load_balancer_response)

# Get list of all networks
networks_url = base_url + 'api/networks'
networks_response = get_request(networks_url, headers)
print(networks_response)

# Get network by id - loop results from previous query to seed and feed for desired metrics from each ID
network_id = '<NETWORK_ID>' # Replace with actual network id
network_url = base_url + 'api/networks/' + network_id
network_response = get_request(network_url, headers)
print(network_response)

# Get list of all plans
plans_url = base_url + 'api/plans'
plans_response = get_request(plans_url, headers)
print(plans_response)

# Get plan by id - loop results from previous query to seed and feed for desired metrics from each ID
plan_id = '<PLAN_ID>' # Replace with actual plan id
plan_url = base_url + 'api/plans/' + plan_id
plan_response = get_request(plan_url, headers)
print(plan_response)

# Get list of all regions - - loop results from previous query to seed and feed for desired metrics from each ID
regions_url = base_url + 'api/regions'
regions_response = get_request(regions_url, headers)
print(regions_response)

# Get region by id - loop results from previous query to seed and feed for desired metrics from each ID
region_id = '<REGION_ID>' # Replace with actual region id
region_url = base_url + 'api/regions/' + region_id
region_response = get_request(region_url, headers)
print(region_response)

# Get list of all snapshots
snapshots_url = base_url + 'api/snapshots'
snapshots_response = get_request(snapshots_url, headers)
print(snapshots_response)

# Get snapshot by id - loop results from previous query to seed and feed for desired metrics from each ID
snapshot_id = '<SNAPSHOT_ID>' # Replace with actual snapshot id
snapshot_url = base_url + 'api/snapshots/' + snapshot_id
snapshot_response = get_request(snapshot_url, headers)
print(snapshot_response)

# Get list of all storage volumes
storage_volumes_url = base_url + 'api/storageVolumes'
storage_volumes_response = get_request(storage_volumes_url, headers)
print(storage_volumes_response)

# Get storage volume by id - loop results from previous query to seed and feed for desired metrics from each ID
storage_volume_id = '<STORAGE_VOLUME_ID>' # Replace with actual storage volume id
storage_volume_url = base_url + 'api/storageVolumes/' + storage_volume_id
storage_volume_response = get_request(storage_volume_url, headers)
print(storage_volume_response)

# Get list of all tags
tags_url = base_url + 'api/tags'
tags_response = get_request(tags_url, headers)
print(tags_response)

# Get tag by id - loop results from previous query to seed and feed for desired metrics from each ID
tag_id = '<TAG_ID>' # Replace with actual tag id
tag_url = base_url + 'api/tags/' + tag_id
tag_response = get_request(tag_url, headers)
print(tag_response)

# Get list of all users
users_url = base_url + 'api/users'
users_response = get_request(users_url, headers)
print(users_response)

# Get user by id - loop results from previous query to seed and feed for desired metrics from each ID 
user_id = '<USER_ID>' # Replace with actual user id
user_url = base_url + 'api/users/' + user_id
user_response = get_request(user_url, headers)
print(user_response)

# Get list of all zones 
zones_url = base_url + 'api/zones'
zones_response = get_request(zones_url, headers)
print(zones_response)

# Get zone by id - loop results from previous query to seed and feed for desired metrics from each ID
zone_id = '<ZONE_ID>' # Replace with actual zone id
zone_url = base_url + 'api/zones/' + zone_id
zone_response = get_request(zone_url, headers)
print(zone_response)

