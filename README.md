# PC parts - Rest API

### Instructions 

```bash
$ git clone https://github.com/datotoda/pc_rest.git
$ cd pc_rest
$ pip install -r requirements.txt
$ cd pc_rest
$ mv pc_rest/dotenv pc_rest/.env
$ nano pc_rest/.env  # fill data
$ python3 manage.py runserver
```

#### for demo data

```bash
$ python3 manage.py migrate
$ python3 manage.py fill_demo_data
```

## or you can use docker

```bash
$ git clone https://github.com/datotoda/pc_rest.git
$ cd pc_rest
$ mv pc_rest/dotenv pc_rest/.env
$ nano pc_rest/.env  # fill data
$ docker-compose up -d
```

#### default super user

username: admin

password: admin