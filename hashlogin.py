import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if db.get(user)==None:
        print('Wrong username.')
    else:
        pwdhash = hashlib.md5()
        pwdhash.update(password.encode('utf-8'))
        if pwdhash.hexdigest() == db[user]:
            print('Login success!')
        else:
            print('Wrong password.')


login('bob','abc999')
