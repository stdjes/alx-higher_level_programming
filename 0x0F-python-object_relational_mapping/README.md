# 0x0F. Python - Object-relational mapping

## Description
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

<br />

## Install and activate venv
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
## Install MySQLdb module version 2.0.x
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
## Install SQLAlchemy module version 1.4.x
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
<br />

## Table of MySQLdb-Connect (without ORM)
Files | Description
----- | -----------
[0-select_states.py](./0-select_states.py) | lists all states from the database hbtn_0e_0_usa
[1-filter_states.py](./1-filter_states.py) | lists all states with a name starting with N from the database hbtn_0e_0_usa
[2-my_filter_states.py](./2-my_filter_states.py) | displays all values in the states table of hbtn_0e_0_usa where name matches the argument
[3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | same as file 2-my_filter_states.py but safe from SQL injection
[4-cities_by_state.py](./4-cities_by_state.py) | lists all cities from the database hbtn_0e_4_usa
[5-filter_cities.py](./5-filter_cities.py) | lists all cities of state giving as argument, using the database hbtn_0e_4_usa
<br />

## Table of SqlAlchemy (with ORM)
Files | Description
----- | -----------
[model_state.py](./model_state.py) | Define a Table states of the SQl by Class Inherted From Base = declarative_base()
[model_city.py](./model_city.py) | Define a Table cities of the SQl by Class Inherted From Base = declarative_base()
[6-model_state.py](./6-model_state.py) | Create the table states
[7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | lists all State objects from a database
[8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | prints the first State object from a database
[9-model_state_filter_a.py](./9-model_state_filter_a.py) | lists all State objects that contain the letter a from a database
[10-model_state_my_get.py](./10-model_state_my_get.py) | prints the State object with the name passed as argument
[11-model_state_insert.py](./11-model_state_insert.py) | adds the State object “Louisiana” to a database
[12-model_state_update_id_2.py](./12-model_state_update_id_2.py) | changes the name of a State object from the database
[13-model_state_delete_a.py](./13-model_state_delete_a.py) | deletes all State objects with a name containing the letter <a>
[14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) | prints all City objects from a database
<br />

## Table of Advanced (with ORM)
Files | Description
----- | -----------
[relationship_state.py](./relationship_state.py) | Define a Table states with relationship with cities table
[relationship_city.py](./relationship_city.py) | Define a Table cities with ForeignKey from states table
[100-relationship_states_cities.py](./100-relationship_states_cities.py) | create a State with a City and save to a database
[101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py) | lists all State objects, and corresponding City objects
[102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py) | lists all City objects by using relationship to access to the State linked to the City

## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
