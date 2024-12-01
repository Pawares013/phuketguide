from django.shortcuts import render

def movie_list(request):
    movies = [
        {'title': 'Attack on Titan', 'year': 2013},
        {'title': 'Your Name', 'year': 2016},
        {'title': 'Spirited Away', 'year': 2001},
        {'title': 'Naruto', 'year': 2002},
        {'title': 'Death Note', 'year': 2006},
        {'title': 'One Piece', 'year': 1999},
        {'title': 'Demon Slayer', 'year': 2019},
        {'title': 'My Hero Academia', 'year': 2016},
        {'title': 'Jujutsu Kaisen', 'year': 2020},
        {'title': 'Tokyo Ghoul', 'year': 2014},
    ]
    return render(request, 'movies/list.html', {'movies': movies})