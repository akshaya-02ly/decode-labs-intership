# ==============================================
# AI Recommendation System
# Project 3 - DecodeLabs
# ==============================================

# Dataset of movies with their genres

movies = [
    {"name": "Inception", "genres": ["Action", "Sci-Fi", "Thriller"]},
    {"name": "Interstellar", "genres": ["Sci-Fi", "Adventure", "Drama"]},
    {"name": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},
    {"name": "Titanic", "genres": ["Romance", "Drama"]},
    {"name": "Avengers: Endgame", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"name": "The Conjuring", "genres": ["Horror", "Thriller"]},
    {"name": "Frozen", "genres": ["Animation", "Family", "Adventure"]},
    {"name": "Toy Story", "genres": ["Animation", "Comedy", "Family"]},
    {"name": "3 Idiots", "genres": ["Comedy", "Drama"]},
    {"name": "Bahubali", "genres": ["Action", "Adventure", "Drama"]},
    {"name": "Doctor Strange", "genres": ["Action", "Fantasy", "Sci-Fi"]},
    {"name": "Spider-Man: No Way Home", "genres": ["Action", "Adventure", "Fantasy"]},
    {"name": "Joker", "genres": ["Crime", "Drama", "Thriller"]},
    {"name": "The Notebook", "genres": ["Romance", "Drama"]},
    {"name": "Finding Nemo", "genres": ["Animation", "Adventure", "Family"]}
]

# ==============================================
# Display Available Genres
# ==============================================

available_genres = sorted(set(
    genre for movie in movies for genre in movie["genres"]
))

print("=" * 50)
print("        AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Genres:")
for genre in available_genres:
    print("-", genre)

# ==============================================
# Take User Input
# ==============================================

user_input = input(
    "\nEnter your favorite genres (comma separated): "
)

user_preferences = [
    genre.strip().title()
    for genre in user_input.split(",")
]

# ==============================================
# Recommendation Logic
# ==============================================

recommendations = []

for movie in movies:

    score = len(
        set(user_preferences) &
        set(movie["genres"])
    )

    if score > 0:
        recommendations.append((movie["name"], score, movie["genres"]))

# ==============================================
# Sort Recommendations
# ==============================================

recommendations.sort(key=lambda x: x[1], reverse=True)

# ==============================================
# Display Results
# ==============================================

print("\n" + "=" * 50)

if recommendations:

    print("Recommended Movies\n")

    for movie, score, genres in recommendations:
        print(f"Movie : {movie}")
        print(f"Genres: {', '.join(genres)}")
        print(f"Similarity Score: {score}")
        print("-" * 50)

else:
    print("No matching recommendations found.")

print("\nThank you for using the AI Recommendation System!")