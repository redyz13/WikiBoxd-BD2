# WikiBoxd MongoDB Schema

## Overview

WikiBoxd uses MongoDB as a document-oriented DBMS to model a movie-oriented platform inspired by Letterboxd.

The database is based on the MovieLens Latest Small dataset and is extended with synthetic application data such as textual reviews, watchlists and custom lists.

The main modeling pattern is **referencing**, using identifiers to connect documents across collections. This approach keeps the main entities independent while allowing the application to combine data through aggregation pipelines when needed.

---

## Collections

The database model includes the following collections:

- `users`
- `movies`
- `reviews`
- `watchlist`
- `lists`
- `list_movies`

---

## `users`

Stores application users derived from MovieLens `userId`.

### Fields

| Field | Type | Description |
|---|---|---|
| `_id` | integer | User identifier derived from MovieLens `userId` |
| `username` | string | Synthetic username generated for the application |

### Example

~~~json
{
  "_id": 1,
  "username": "user_1"
}
~~~

---

## `movies`

Stores movie catalog information derived from MovieLens `movies.csv`.

### Fields

| Field | Type | Description |
|---|---|---|
| `_id` | integer | Movie identifier derived from MovieLens `movieId` |
| `title` | string | Movie title |
| `genres` | array of strings | Movie genres |

### Example

~~~json
{
  "_id": 1,
  "title": "Toy Story (1995)",
  "genres": ["Adventure", "Animation", "Children", "Comedy", "Fantasy"]
}
~~~

---

## `reviews`

Stores ratings and textual reviews associated with users and movies.

MovieLens ratings are imported as initial rating documents. Textual review content is represented by `review_text` and can be populated with synthetic data.

### Fields

| Field | Type | Description |
|---|---|---|
| `_id` | string | Review identifier |
| `user_id` | integer | Reference to `users._id` |
| `movie_id` | integer | Reference to `movies._id` |
| `rating` | number | Rating value |
| `review_text` | string | Textual review content |
| `timestamp` | integer | Timestamp from MovieLens rating data, if available |

### Example

~~~json
{
  "_id": "1_1",
  "user_id": 1,
  "movie_id": 1,
  "rating": 4.0,
  "review_text": "",
  "timestamp": 964982703
}
~~~

---

## `watchlist`

Stores movies saved by users in their personal watchlist.

### Fields

| Field | Type | Description |
|---|---|---|
| `_id` | string | Watchlist entry identifier |
| `user_id` | integer | Reference to `users._id` |
| `movie_id` | integer | Reference to `movies._id` |

### Example

~~~json
{
  "_id": "1_50",
  "user_id": 1,
  "movie_id": 50
}
~~~

---

## `lists`

Stores custom movie lists created by users.

### Fields

| Field | Type | Description |
|---|---|---|
| `_id` | string | List identifier |
| `user_id` | integer | Reference to `users._id` |
| `name` | string | List name |
| `description` | string | List description |

### Example

~~~json
{
  "_id": "list_1",
  "user_id": 1,
  "name": "Favorite sci-fi movies",
  "description": "A personal selection of science fiction movies."
}
~~~

---

## `list_movies`

Stores the relationship between custom lists and movies.

This collection models a many-to-many relationship between `lists` and `movies`.

### Fields

| Field | Type | Description |
|---|---|---|
| `_id` | string | List-movie relation identifier |
| `list_id` | string | Reference to `lists._id` |
| `movie_id` | integer | Reference to `movies._id` |

### Example

~~~json
{
  "_id": "list_1_260",
  "list_id": "list_1",
  "movie_id": 260
}
~~~

---

## Relationships

| Source collection | Field | Target collection | Target field |
|---|---|---|---|
| `reviews` | `user_id` | `users` | `_id` |
| `reviews` | `movie_id` | `movies` | `_id` |
| `watchlist` | `user_id` | `users` | `_id` |
| `watchlist` | `movie_id` | `movies` | `_id` |
| `lists` | `user_id` | `users` | `_id` |
| `list_movies` | `list_id` | `lists` | `_id` |
| `list_movies` | `movie_id` | `movies` | `_id` |

---

## Modeling Choices

### Referencing

The main modeling pattern is referencing. This choice is appropriate because:

- users, movies, reviews and lists are independent entities;
- movies can be referenced by many reviews, watchlist entries and custom lists;
- user-generated content can grow independently from movie catalog data;
- the model remains flexible and easy to extend;
- aggregation pipelines can combine related documents when composite views are required.

### Selective Denormalization

The base schema is reference-oriented. Selective denormalization is considered only as a performance-oriented optimization and must remain limited to data that improves common read operations without making updates unnecessarily complex.

In this initial schema, references remain the primary way to represent relationships between collections.

---

## Notes on Identifiers

MovieLens identifiers are preserved where possible:

- `movieId` maps to `movies._id`
- `userId` maps to `users._id`
- review identifiers combine user and movie identifiers when derived from ratings

This makes the import process deterministic and keeps relationships stable across repeated imports.