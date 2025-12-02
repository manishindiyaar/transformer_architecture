# Find which movie in our database is the most similar to the user's query.

# find_scores_sequentially
scores = [];

for movie_vector in movie_db:
    current_score = 0.0

    for i in range(len(query)):
        current_score+= query[i]*movie_vector[i];

    scores.append(current_score);


# doing this same with matrix using parallel method.
# Convert to NumPy arrays
query_vector_np = np.array(query_list) 
movie_db_matrix_np = np.array(movie_db_list)

# The *entire* calculation
scores = movie_db_matrix_np @ query_vector_np
