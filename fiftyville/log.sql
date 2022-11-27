--SELECT id, description FROM crime_scene_reports WHERE day = 28 AND month = 7 AND street LIKE '%Humphrey%';
-- Get more information about the crimes that happend that day on that street

--Shorten my code AND get exact report
--SELECT description FROM crime_scene_reports WHERE id = 295;

--Linsten witnesses
--SELECT name, transcript FROM interviews WHERE day = 28 AND month = 7 AND (id BETWEEN 161 AND 163);
--Witness - Ruth, Eugene, Raymond

--ATM on Leggett Street before 10:15
--SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND atm_location LIKE 'Legget%' AND transaction_type = 'withdraw';

--FIND names from bank accounts
--SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7 AND atm_location LIKE 'Legget%' AND transaction_type = 'withdraw'));
--Suspects: Kenny, Iman, Benista, Taylor, Brooke, Luca, Diana, Bruce

--Security footage from bakery parking lot around 10:15
--SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND hour = 10 AND activity = 'exit' AND minute BETWEEN 15 AND 20;

--FIND names from license_plate
--SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 7 AND hour = 10 AND activity = 'exit' AND minute BETWEEN 15 AND 20);
--Suspects: Luca and Bruce

--Called someone for less than 1 minute - Planning to take the earliest flight tomorrow (July 29)
--SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60;

--FIND names from phone_numbers
--SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60);

--Suspects: Bruce
--FIND Bruce information
--SELECT * FROM people WHERE name = 'Bruce';

--Accomplice bought the flight tickets
--Find Bruce's accomplice
--SELECT name FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = 'Bruce') AND day = 28 AND duration < 60);

--FIND city they escaped
--FIND FiftyVille id
--SELECT * FROM airports WHERE city = 'Fiftyville';
--FIND earliest flight tomorrow
--SELECT city FROM airports WHERE id IN
SELECT city FROM airports WHERE id = (
SELECT destination_airport_id FROM flights WHERE day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
AND hour = (SELECT MIN(hour) FROM flights WHERE day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')));

--They escaped to New York City