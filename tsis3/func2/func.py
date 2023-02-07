movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def check_score_greater(movies):
    for i in range(len(movies)):
        if(movies[i]['imdb']>5.5):
            return True
        else:
            return False

print(check_score_greater(movies))


def send_good_films(movies):
    for i in range(len(movies)):
        if(movies[i]['imdb']>5.5):
            print(movies[i]["name"])

print(send_good_films(movies))

def send_good_films(movies):
    for i in range(len(movies)):
        if(movies[i]['imdb'] < 5.5):
            print(movies[i]["name"])

print(send_good_films(movies))

def movie_b_cat(movies,cat):
    for i in range(len(movies)):
        if movies[i]["category"] == cat:
            print(movies[i]["name"])
        

print(movie_b_cat(movies,"Romance"))


def average(movies):
    sum = 0;
    cnt = 0;
    av = 0;
    for i in range(len(movies)):
        sum += movies[i]["imdb"]
        cnt += 1
        av = sum // cnt

print(average(movies))


def more_the_average(movies):
    aver = 7
    for i  in range(len(movies)):
        if movies[i]["imdb"] >= aver:
            print(movies[i]["category"])

print(more_the_average(movies))