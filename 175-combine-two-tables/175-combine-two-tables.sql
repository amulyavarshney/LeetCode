SELECT firstname, lastname, city, state FROM person LEFT JOIN address ON person.personID = address.personId;
