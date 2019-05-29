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

open a browser of use postman to visit the url `http://localhost:8000/api/interview/slot`

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

## Check the documentation for more details

