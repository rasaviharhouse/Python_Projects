import json
from collections import defaultdict
import requests

url = 'https://api.taiga.io/api/v1'
username = ''
password = ''
auth_token = ''
project_slug = ''


def login():
    login_url = url + '/auth'
    print('Enter choice:')
    print('1. Login to Taiga')
    print('2. Exit')
    choice = input()

    if choice == '2':
        exit(0)

    if choice == '1':
        global username
        username = input('Enter username:')
        global password
        password = input('Enter password:')

        headers = {'Content-Type': 'application/json'}
        data = {'username': username,
                'password': password,
                'type': 'normal'}
        response = requests.request('POST', login_url, headers=headers, data=json.dumps(data))
        if response.ok:
            global auth_token
            auth_token = response.json()['auth_token']
            return True
        else:
            return False


if not login():
    print('Login attempt failed due to invalid credentials.')
    exit(0)

project_slug = input('\nEnter project slug:')


project_url = url + '/projects/by_slug'
params = {'slug': project_slug}

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + auth_token
}

response = requests.request('GET', project_url, headers=headers, params=params)
resp = response.json()

print('\nMembers:')

for m in resp['members']:
    print('\nMember Name:' + m['full_name'])
    print('Role name:' + m['role_name'])
    print('Role:' + str(m['role']))

sprints = []
milestones_url = url + '/milestones/'

print('\nSprints:\n')

for i, v in enumerate(resp['milestones'], 1):
    sprints.append(v['id'])
    response = requests.get(milestones_url + str(v['id']), headers=headers)
    resp = response.json()
    print(i, ':', resp['name'])
    print('Sprint start date:', resp['estimated_start'])
    print('Sprint end date:', resp['estimated_finish'])
    print('Total points in sprint:', resp['total_points'])
    print('Finished points in sprint:', resp['closed_points'])
    print()

sprint_num = int(input('Enter sprint number: '))

response = requests.get(milestones_url + str(sprints[sprint_num - 1]), headers=headers)
resp = response.json()

print('\nSprint:', sprint_num)
print('\nUser story count:', len(resp['user_stories']))
user_tasks = defaultdict(int)

for j, user_story in enumerate(resp['user_stories'], 1):
    print('\nUser story:', j)
    print('\nName:', user_story['subject'])
    print('Is_closed:', user_story['is_closed'])
    print('Created date:', user_story['created_date'])
    print('Modified date:', user_story['modified_date'])
    print('Finish date:', user_story['finish_date'])

    tasks_url = url + '/tasks'
    params = {
        'user_story': str(user_story['id'])
    }
    response = requests.get(tasks_url, headers=headers, params=params)
    res = response.json()

    print('\nTasks: ')

    for i, task in enumerate(res, 1):
        assignee = task['assigned_to_extra_info']['full_name_display']
        print('\nTask:', i)
        print('Assigned to:', assignee)
        print('Task name:', task['subject'])
        user_tasks[assignee] += 1

print('\nUser task count: ')
for k, v in user_tasks.items():
    print(k, ':', v)
