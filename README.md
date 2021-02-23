# heartarcade
A website developed with Django framework which offers the member to write quotes. They can tag their quotes to various categories. Anyone can sign in using their email address or facebook or twitter.Complete Rest Api is integrated


## Endpoints

1. User registration and login
    - https://heartarcade.herokuapp.com/api/account/signup/
    - http://heartarcade.herokuapp.com/api/account/login/
  
2.  Quotes
    - http://heartarcade.herokuapp.com/api/quote/
    - http://heartarcade.herokuapp.com/api/quote/category/
    - http://heartarcade.herokuapp.com/api/quote/category/inspirational/
    - http://heartarcade.herokuapp.com/api/quote/create/
    - http://heartarcade.herokuapp.com/api/quote/e8e39a82-b227-465b-90f1-c59a657a4c40/
    - http://heartarcade.herokuapp.com/api/quote/e8e39a82-b227-465b-90f1-c59a657a4c40/edit/
    - http://heartarcade.herokuapp.com/api/quote/e8e39a82-b227-465b-90f1-c59a657a4c40/delete/
	- http://heartarcade.herokuapp.com/api/profile/lutfor-rahman/
    
3. User Profile
    - http://heartarcade.herokuapp.com/api/profile/
	- http://heartarcade.herokuapp.com/api/profile/change-username/
    - http://heartarcade.herokuapp.com/api/profile/change-password/

    

## Sample API Request & Response
**POST api/account/signup/**
- Details:This API end point is for creating a new user.

Request body:
```json
{
    "username": "NeilArmstrong",
    "email": "neil123@gmail.com",
    "password":"********",
    "password2":"********"
}
```

Response body:
```json
{
    "response": "succesfully registered a new user",
    "email": "neil123@gmail.com",
    "username": "NeilArmstrong",
    "token": "ea1aeef0258fe48921a522f08fefd6c12d99b7bc"
}
```

**POST api/account/login/**
- Details:This API end point is for signing in the new user.

Request body:
```json
{
    "username": "NeilArmstrong",
    "password":"********"
}
```

Response body:
```json
{
    "token": "ea1beef0258ye48921a622f08fefd7c18d99b7bc"
}
```

**GET /api/quote/**
- Details:This API end point is for Getting all the quotes.

Response body:
```json
{
    "count": 12,
    "next": "http://heartarcade.herokuapp.com/api/quote/?page=2",
    "previous": null,
    "results": [
        {
            "quote": "Callousness and insolence bring to bare unanimous social condemnation, while the simple efforts of politeness are admired; even in those who are otherwise despised.",
            "author": "shifat123",
            "categories": [
                "positive",
                "respect"
            ],
            "pub_date": "02/16/20",
            "slugged_username": "shifat123"
        },
        {
            "quote": "Work is love made visible. And if you cannot work with love but only with distaste, it is better that you should leave your work and sit at the gate of the temple and take alms of those who work with joy.",
            "author": "shifat123",
            "categories": [
                "love",
                "work"
            ],
            "pub_date": "02/16/20",
            "slugged_username": "shifat123"
        },
        {
            "quote": "Knowledge of the self is the mother of all knowledge. So it is incumbent on me to know my self, to know it completely, to know its minutiae, its characteristics, its subtleties, and its very atoms.",
            "author": "shifat123",
            "categories": [
                "courage",
                "dream",
                "education"
            ],
            "pub_date": "02/16/20",
            "slugged_username": "shifat123"
        },
    ]
}
```

**GET api/quote/category/**
- Details:This API end point is for getting all the quote categories. Token Authentication required.

Response body:
```json
{
    "count": 63,
    "next": "http://heartarcade.herokuapp.com/api/quote/category/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "alone"
        },
        {
            "id": 2,
            "title": "art"
        },
        {
            "id": 3,
            "title": "attitude"
        },
        {
            "id": 4,
            "title": "beauty"
        },
        {
            "id": 5,
            "title": "change"
        },
        {
            "id": 6,
            "title": "cool"
        },
        {
            "id": 7,
            "title": "courage"
        },
        {
            "id": 8,
            "title": "dream"
        },
        {
            "id": 9,
            "title": "education"
        },
        {
            "id": 10,
            "title": "environment"
        }
    ]
}
```

**GET api/quote/:quote_category/**
- Details:This API end point is for getting all the quote categories. Token Authentication required.

Response body:
```json
[
    {
        "quote": "Pain and foolishness lead to great bliss and complete knowledge, for Eternal Wisdom created nothing under the sun in vain.",
        "author": "shifat123",
        "categories": [
            "inspirational",
            "motivational"
        ],
        "pub_date": "02/16/20",
        "slugged_username": "shifat123"
    },
    {
        "quote": "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover.",
        "author": "MdLutforRahman",
        "categories": [
            "hope",
            "imagination",
            "inspirational"
        ],
        "pub_date": "02/17/20",
        "slugged_username": "mdlutforrahman"
    }
]
```

**POST api/quote/create/**
- Details:This API end point is for creating a new quote. Token Authentication required.

Request body:
```json
{
    "quote": "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
    "categories": [
        1,
        2
    ]
}
```

Response body:
```json
{
    "quote": "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
    "author": "2976383e-d781-4957-a5c1-bec1ec8067b2",
    "categories": [
        1,
        2
    ]
}
```

**GET api/quote/:quote_id/**
- Details:This API end point is for getting the details of a specific quote. Token Authentication required.

Response body:
```json
{
    "quote": "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
    "categories": [
        1,
        2
    ]
}
```

**POST api/quote/:id/edit/**
- Details:This API end point is for updating a sprcific quote. Token Authentication required.

Request body:
```json
{
    "quote": "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
    "categories": [
        1,
        2,
        4
    ]
}
```

Response body:
```json
{
    "success": "update successful"
}
```

**DELETE api/quote/:id/delete/**
- Details:This API end point is for deleting a specific quote. Token Authentication required.

Response body:
```json
{
    "success": "Delete successful"
}
```

**GET api/profile/:slug_username/**
- Details:This API end point is for getting all the quotes published by a specific user. Token Authentication required.

Response body:
```json
[
    {
        "quote": "Callousness and insolence bring to bare unanimous social condemnation, while the simple efforts of politeness are admired; even in those who are otherwise despised.",
        "author": "shifat123",
        "categories": [
            "positive",
            "respect"
        ],
        "pub_date": "02/16/20"
    },
    {
        "quote": "Work is love made visible. And if you cannot work with love but only with distaste, it is better that you should leave your work and sit at the gate of the temple and take alms of those who work with joy.",
        "author": "shifat123",
        "categories": [
            "love",
            "work"
        ],
        "pub_date": "02/16/20"
    },
    {
        "quote": "Knowledge of the self is the mother of all knowledge. So it is incumbent on me to know my self, to know it completely, to know its minutiae, its characteristics, its subtleties, and its very atoms.",
        "author": "shifat123",
        "categories": [
            "courage",
            "dream",
            "education"
        ],
        "pub_date": "02/16/20"
    },
    {
        "quote": "Nor shall derision prove powerful against those who listen to humanity or those who follow in the footsteps of divinity, for they shall live forever. Forever.",
        "author": "shifat123",
        "categories": [
            "humor",
            "intelligence"
        ],
        "pub_date": "02/16/20"
    },
    {
        "quote": "Pain and foolishness lead to great bliss and complete knowledge, for Eternal Wisdom created nothing under the sun in vain.",
        "author": "shifat123",
        "categories": [
            "inspirational",
            "motivational"
        ],
        "pub_date": "02/16/20"
    }
]
```

**GET api/profile/**
- Details:This API end point is for getting the details of the users. Token Authentication required.

Response body:
```json
{
    "username": "NeilArmstrong",
    "email": "neil123@gmail.com"
}
```

**GET api/profile/change-username**
- Details:This API end point is for getting the username of the users. Token Authentication required.

Response body:
```json
{
    "username": "NeilArmstrong"
}
```

**PUT api/profile/change-username**
- Details:This API end point is for updating the username of the users. Token Authentication required.

Request body:
```json
{
    "username": "Neil_Armstrong"
}
```

Response body:
```json
{
    "response": "Username update successful"
}
```

**PUT api/profile/change-password/**
- Details:This API end point is for updating the password of the users. Token Authentication required.

Request body:
```json
{
    "old_password":  "*********"
    ,
    "password":  "************"
    ,
    "confirm_password": "************"
}
```

Response body:
```json
{
    "Success": "Password has been updated successfully"
}
```
