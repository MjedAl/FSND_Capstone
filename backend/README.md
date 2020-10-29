# How to run the project:
Currently the API is live and deployed on heroku on the following link {
    https://udacity-casting-agency-api.herokuapp.com/
}

or you can try it locally after getting the required dependencies
```
    pip install -r requirements.txt
```
and setting up the required environment (they can be obtained from Auth0) {
    ALGORITHMS,API_AUDIENCE,AUTH0_DOMAIN
}

# Testing the endpoints:
you can try the API with the given [Postman collection](../testing_api_postman_collection.json), you just have to update the token if it's expired

# Endpoints:
Roles permissions:
```
Casting Assistant:
- GET movies and actors
Casting Director:
- GET movies and actors
- PATCH movies and actors
- DELETE actors
- POST actors
Casting Producer: 
- GET movies and actors
- PATCH movies and actors
- DELETE movies and actors
- POST movies and actors
```

#### All the endpoints will only work if you have permission. else it will return Unauthorized error 401.


## GET actors
### GET <host>/actors
```
- Request Arguments: None
- Response example:
{
    "actors": [
        {
            "age": "51",
            "gender": "male",
            "id": 1,
            "name": "Simon baker"
        },
        {
            "age": "49",
            "gender": "male",
            "id": 2,
            "name": "Michael C. Hall"
        }
    ],
    "success": true
}
```

## GET movies
### GET <host>/movies
```
- Request Arguments: None
- Response example:
{
    "movies": [
        {
            "id": 1,
            "release_date": "2008",
            "title": "Iron man 1"
        }
    ],
    "success": true
}
```

## DELETE actors
### DELETE <host>/actors/<actor_id>
```
- Request Arguments: the actor id
- request example:
Link:
<host>/actors/1

- Response example:
{
    "success": true
}
```

## DELETE movies/<id>
### DELETE <host>/movies/<movie_id>
```
- Request Arguments: the movie id
- request example:
Link:
<host>/movies/1

- Response example:
{
    "success": true
}
```

## POST actors
### POST <host>/actors
```
- Request Arguments: JSON with the name, age, gender, image_link
- request example:
{
    "name": "Michael C. Hall",
    "age": "49",
    "gender": "male",
    "image_link": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Michael_C._Hall_Comic-Con_2012.jpg"
}
- Response example:
{
    "actor_id": 2,
    "success": true
}
```

## POST movies
### POST <host>/movies
```
- Request Arguments: JSON with the title, release_date, poster_link
- request example:
{
    "title": "Iron man",
    "release_date": "2008",
    "poster_link": "https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg"
}
- Response example:
{
    "movie_id": 1,
    "success": true
}
```

## PATCH movies
### PATCH <host>/movies/<movie_id>
```
- Request Arguments: the movie id and JSON with the title, release_date, poster_link
- request example:
Link:
<host>/movies/1
Body:
{
    "title": "Iron man 1",
    "release_date": "2008",
    "poster_link": "https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg"
}
- Response example:
{
    "movie": {
        "id": 1,
        "release_date": "2008",
        "title": "Iron man 1"
    },
    "success": true
}
```

## PATCH actors
### PATCH <host>/actors/<actor_id>
```
- Request Arguments: the actor id and JSON with the name, age, gender, image_link
- request example:
Link:
<host>/actors/2
Body:
{
    "name": "Michael C. Hall",
    "age": "50",
    "gender": "male",
    "image_link": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Michael_C._Hall_Comic-Con_2012.jpg"
}
- Response example:
{
    "actor": {
        "age": "50",
        "gender": "male",
        "id": 2,
        "name": "Michael C. Hall"
    },
    "success": true
}
```