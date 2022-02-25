
--View users
SELECT * from users;

--Add user
INSERT INTO users (user_id, email, screen_name, country_code) VALUES (:user_idInput, :emailInput, :screen_nameInput, :countryInput);

--View user’s collections of game titles
SELECT user_id from collections;

--Add game to user collection
INSERT INTO collection (user_id, game_id) VALUES (:user_idInput, :game_idInput);

--View user wishlist
SELECT user_id from wishes;

--Add game to user wishlist
INSERT INTO wishes (user_id, game_id) VALUES (:user_idInput, :game_idInput);

--Delete game from user wishlist
DELETE FROM wishes WHERE user_id = :user_idInput AND game_id = :game_idInput;

--View user’s reviews of games.
SELECT user_id FROM ratings;

--Add review of game
INSERT INTO ratings (user_id, game_id, rating_value, rating_comment) VALUES (:user_idInput, :game_idInput, :rating_valueInput, :rating_commentInput);

--Delete review
DELETE FROM ratings WHERE user_id = :user_idInput AND game_id = :game_idInput;

--View games
SELECT * FROM games; 

--View users that have game in their collection <--- Jack, can you fix this one to display correctly? 
SELECT game_id FROM collection;

--View reviews of specific game 
SELECT game_id FROM ratings;
 