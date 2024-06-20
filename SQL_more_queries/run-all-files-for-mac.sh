#!/bin/bash

mysql -uroot -pYourRootPassword < 0-privileges.sql
mysql -uroot -pYourRootPassword < 1-create_user.sql
mysql -uroot -pYourRootPassword < 2-create_read_user.sql
mysql -uroot -pYourRootPassword < 3-force_name.sql
mysql -uroot -pYourRootPassword < 4-never_empty.sql
mysql -uroot -pYourRootPassword < 5-unique_id.sql
mysql -uroot -pYourRootPassword < 6-states.sql
mysql -uroot -pYourRootPassword < 7-cities.sql
mysql -uroot -pYourRootPassword < 8-cities_of_california_subquery.sql
mysql -uroot -pYourRootPassword < 9-cities_by_state_join.sql
mysql -uroot -pYourRootPassword < 10-genre_id_by_show.sql
mysql -uroot -pYourRootPassword < 11-genre_id_all_shows.sql
mysql -uroot -pYourRootPassword < 12-no_genre.sql
mysql -uroot -pYourRootPassword < 13-count_shows_by_genre.sql
mysql -uroot -pYourRootPassword < 14-my_genres.sql
mysql -uroot -pYourRootPassword < 15-comedy_only.sql
mysql -uroot -pYourRootPassword < 16-shows_by_genre.sql