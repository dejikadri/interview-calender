# interview-calender
Interview booking api
#
This Api allows the booking of Interview slots by both candidates and interviewers.

##Cloning the repo

Turn the app, point to the repo `https://github.com/dejikadri/interview-calender.git` and issue the command below
`git clone https://github.com/dejikadri/interview-calender.git`. Make sure you are in the folder where you want to keep the code.

##Setup
Make sure you have `docker` and `docker compose`  installed.


Navigate to the repo directory and issue the command `docker-compose build`
A series of messages will scroll up on the screen and after thst issue the command `docker-compose up` 
you should see the following output on your screen
``` 
System check identified no issues (0 silenced).
May 28, 2019 - 16:32:10
Django version 2.2.1, using settings 'app.settings'
Starting development server at http://0.0.0.0:8001/
Quit the server with CONTROL-C.
```

open a browser or use postman to visit the url `http://localhost:8000/api/interview/slot`

this will display a json list of interview slots.
``` 
[
    {
        "candidate": Gunther,
        "interviewer": Adolfus,
        "instruction_notes": "make it there please",
        "interview_date": "2019-05-20",
        "interview_start_time": "14:29:54.385075",
        "interview_end_time": "02:00:00"
    },
    {
        "candidate": Mike,
        "interviewer": Junita,
        "instruction_notes": "make it there please",
        "interview_date": "2019-05-28",
        "interview_start_time": "14:29:54.385075",
        "interview_end_time": "12:00:00"
    },
    {
        "candidate": Deji,
        "interviewer": Biodun,
        "instruction_notes": "make it there please",
        "interview_date": "2019-05-28",
        "interview_start_time": "14:29:54.385075",
        "interview_end_time": "12:00:00"
    }
]
```


#### Sample Json to create a new  Candidate (POST)
```
{
    "full_name": "deji",
    "email": "dj@deji.com",
    "phone_number": "000-222-444",
    "skype_id": "ad.dk"
}
```

#### Sample PATCH request to update an interview slot to add either a candidate of an interviewer
 ```
    {
        "candidate": 1,
        "interviewer": null,
        "instruction_notes": "make it there please",
        "interview_date": "2019-07-28",
        "interview_start_time": "17:00",
        "interview_end_time": "02:00:00"
    }

```

#### To simulate a Clashing Interview slot
```
    {
        "candidate": 1,
        "interviewer": null,
        "instruction_notes": "make it there please",
        "interview_date": "2019-07-28",
        "interview_start_time": "17:00",
        "interview_end_time": "02:00:00"
    }
```
#### Get the token
`curl -X POST 127.0.0.1:8000/api/user/login/ --data 'email=x@x.com&password=katana123'`

#### Use the Token Like below. 
```curl -X GET 127.0.0.1:8000/api/interview/slot/ -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InhAeC5jb20iLCJleHAiOjE1NTkxNjU1MTUsImVtYWlsIjoieEB4LmNvbSJ9.yCiaJy2UM0-I75xaWgAJWz2hOPmy_HTsfTziqdrusPg'```


