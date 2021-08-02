users = {
    'afernando' : {
        'first' : 'aristoteles',
        'last' : 'oliveira',
        'email' : 'afernando@gmail.com'
        },
    'elainedba' : {
        'first' : 'elaine',
        'last' : 'silva',
        'email' : 'elainedba@gmail.com'
        },
    }

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = userinfo['first'] + " " + userinfo['last']
    email = userinfo['email']
    print(f'\tFull Name: {full_name.title()}')
    print(f'\tEmail: {email}')
