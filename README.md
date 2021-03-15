# Flask-Graphene-Demo

## setup

``` zsh
pipenv install
pipenv run python setup.py
```

## run

``` zsh
pipenv run python app.py
```

http://localhost:5000/graphql

## query

``` json
{
  employeeList{
    edges{
      node{
        name
        role {
          name
        }
        department{
          name
        }
      }
    }
  }
}
```

## references

- https://github.com/alexisrolland/flask-graphene-sqlalchemy/wiki/Flask-Graphene-SQLAlchemy-Tutorial