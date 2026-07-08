class TestData:

    USERS = {
        'standard' : {
            'username': 'standard_user',
            'expected': 'success'
        },
        'locked' : {
            'username': 'locked_out_user',
            'expected': 'error',
            'error_message': 'Epic sadface: Sorry, this user has been locked out.'
        },
        'problem' : {
            'username': 'problem_user',
            'expected': 'success'
        },
        'glitch' : {
            'username': 'performance_glitch_user',
            'expected': 'success'
        },
        'error' : {
            'username': 'error_user',
            'expected': 'success'
        },
        'visual' : {
            'username': 'visual_user',
            'expected': 'success'
        }
    }

    PASSWORDS = 'secret_sauce'

    ITEMS = {
        'backpack': {
            'id': 'sauce-labs-backpack',
            'name': 'Sauce Labs Backpack',
            'price': '$29.99'
        },
        'bike_light': {
            'id': 'sauce-labs-bike-light',
            'name': 'Sauce Labs Bike Light',
            'price': '$9.99'
        },
        't_shirt': {
            'id': 'sauce-labs-bolt-t-shirt',
            'name': 'Sauce Labs Bolt T-Shirt',
            'price': '$15.99'
        },
        'fleece': {
            'id': 'sauce-labs-fleece-jacket',
            'name': 'Sauce Labs Fleece Jacket',
            'price': '$49.99'
        },
        'onesie': {
            'id': 'sauce-labs-onesie',
            'name': 'Sauce Labs Onesie',
            'price': '$7.99'
        },
        'red_t_shirt': {
            'id': 'test.allthethings()-t-shirt-(red)',
            'name': 'Test.allTheThings() T-Shirt (Red)',
            'price': '$15.99'
        }
    }
