SELECT p.firstname, p.lastname, a.city, a.state FROM person as p LEFT JOIN address as a ON p.personID = a.personId;
