# Author - Brett Kim

mavs = [[33, 42], [5, 1], [42, 4]]

for lst in mavs:
    for score in lst:
        print(score)

rockets = {'players':
            {'name': 'James Harden',
            'points': 40,
            'assists': 8,
            'rebounds': 6,
            'physical_features': {'beard': True,
                                    'bald': False}
            }
        }

print(rockets['players']['points'])

malta = {'events':
            {
            2019: {'name': 'ESL Cologne',
            'winner': 'Astralis'
            },
            2020: {'name': 'ELEAGUE Boston',
            'winner': 'Cloud9',
            'runnerup': 'FaZe'}
            }
        }

print(malta['events'][2019]['winner'])
print(malta['events'][2020]['winner'])