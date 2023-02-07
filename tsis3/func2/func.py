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

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def single_above_5_5(i):
    if movies[i]["imdb"]>5.5:
        return True
    return False

print(single_above_5_5(int(input())))

#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def above_5_5(mov):
    for i in range(0,len(mov)):
        if mov[i]["imdb"]>5.5:
            x = mov[i]["name"]
            print(f"Name {x}")

print(above_5_5(movies))

#Write a function that takes a category name and returns just those movies under that category.
def category_mov(mov,cat):
    for i in range(0,len(mov)):
        if mov[i]["category"] == cat:
            x = mov[i]["name"]
            print(f"Name {x}")

print(category_mov(movies,input()))

#Write a function that takes a list of movies and computes the average IMDB score.
def avg_imdb(mov):
    cnt = 0
    for i in range(0,len(mov)):
        cnt += mov[i]["imdb"]
    return (cnt/len(mov))

print(avg_imdb(movies))

#Write a function that takes a category and computes the average IMDB score.
def avg_category_mov(mov,cat):
    cnt = 0
    y = 0
    for i in range(0,len(mov)):
        if mov[i]["category"] == cat:
            cnt+=mov[i]["imdb"]
            y+=1
    return (cnt/y)

print(avg_category_mov(movies,input()))
