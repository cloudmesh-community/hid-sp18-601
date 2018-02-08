MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'cities_db'
DOMAIN = {
    'city':{
        'schema':{
            'name':{
                'type':'string'
                },
            'population':{
                'type':'integer'
                },
            'area':{
                'type':'float'
                },
            'country':{
                'type':'string'
                },
            'state':{
                'type':'string'
                }
            }
        }
    }
RESOURSE_METHODS = ['GET','POST']
