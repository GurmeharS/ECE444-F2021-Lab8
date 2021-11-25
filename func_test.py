import requests
import time

url = "http://lab-8-env-1.eba-krjr2uaz.us-east-2.elasticbeanstalk.com/fakenews"


TESTS = [
    {
        "Expected": 0, 
        "text": "(CNN) After spending 43 years behind bars for a crime he said he didn't commit, a \
            Missouri man's conviction has been set aside, according to a news release from Jackson County Prosecutor Jean Peters \
            Baker. Senior Judge James Welsh filed his ruling Tuesday morning to set aside the conviction of 62-year-old Kevin \
            Strickland, who served 43 years at Western Missouri Correctional Center in Cameron, Missouri, after he was convicted of \
            one count of capital murder and two counts of second-degree murder in a triple homicide. He received a 50-year life sentence \
            without the possibility for parole for a crime he maintained he wasn't involved in."
    },
    {
        "Expected": 0, 
        "text": "After spending 43 years behind bars for a crime he said he didn't commit, a \
            Missouri man's conviction has been set aside, according to a news release from Jackson County Prosecutor Jean Peters \
            Baker. Senior Judge James Welsh filed his ruling Tuesday morning to set aside the conviction of 62-year-old Kevin \
            Strickland, who served 43 years at Western Missouri Correctional Center in Cameron, Missouri, after he was convicted of \
            one count of capital murder and two counts of second-degree murder in a triple homicide. He received a 50-year life sentence \
            without the possibility for parole for a crime he maintained he wasn't involved in."
    },
    {
        "Expected": 1, 
        "text": "It s official the inmates are running the asylum A police department in Northampton, Massachusetts is ending its High-Five \
            Friday program at local elementary schools due to concerns that undocumented children and others may feel uncomfortable seeing an \
            officer at school.The program, started by the Northampton Police Department in December, had officers stand outside of a school \
            each Friday morning to high-five students as they walked in to begin the day. WFBToday was High-5 Friday at Bridge St School! Thanks\
            to everyone who participated! The kids and officers all had fun! #highfiveHere are a few tweets that were sent out by the NPD highlighting\
            their high-five program with kids:Today was High-5 Friday at Bridge St School! Thanks to everyone who participated! The kids and officers \
            all had fun! #highfive pic.twitter.com/Trz0yoW3Qh Northampton Police (@NorthamptonPD) December 9, 2016Today was High-Five Friday! Thanks \
            to Jackson St School for hosting! We hope that everyone had a great time! Happy Friday!! #highfive pic.twitter.com/MWY6JBlHlK Northampton\
            Police (@NorthamptonPD) January 6, 2017Here is part of their Facebook explanation for doing away with the high-five program:This is the \
            same Northampton Police Department by the way, that celebrated the great turn-out for the nasty women march that was really about \
            protesting Trump and defending abortion. Does it make you feel any safer when you see a police department bragging about their \
            promotion of lawless liberal politics?"
    },   
    {
        "Expected": 1, 
        "text": "VATICAN CITY - News outlets around the world are reporting on the news that Pope Francis has made the unprecedented decision to endorse a US presidential candidate. His statement in support of Donald Trump was released from the Vatican this evening:"
    }
]


def get_probability(text):
    payload = "{\n\t\"text\": \"" + text + "\"\n}"
        
    headers = {
        'Content-Type': "application/json"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    return response.json()

def run_test(text):
    start = time.time()
    resp = None
    for i in range(50):
        if not i%10:
            print(f"Call #{i}")
        resp = get_probability(text)
    time_elapsed = time.time() - start
    return resp, time_elapsed / 50

def main():
    results = []
    for i, test in enumerate(TESTS):
        print(f"Running test {i+1}, expecting {test['Expected']}")
        resp, avg_time = run_test(test['text'])
        results.append(f"Test {i+1}. Expected: {test['Expected']}, Actual: {resp['result']}, Avg time: {avg_time} seconds")
    for result in results:
        print(result)
    
if __name__ == "__main__":
    main()