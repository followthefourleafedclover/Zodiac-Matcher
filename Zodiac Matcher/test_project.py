from project import get_zodiac_from_date
from project import get_emoji_from_moon_phase
from project import is_date_valid
import datetime
import pytest

def test_is_date_valid():
    assert is_date_valid("2/19/2007") == True # test a regular american date
    assert is_date_valid("02/19/2007") == False # cannot use 0 for representing numbers less than 1 in month
    assert is_date_valid("02/09/2007") == False # cannot use 0 for representing numbers less than 1 in day
    assert is_date_valid("2/19/07") == True # can use 0 for representing numbers less than year
    assert is_date_valid("2/31/2007") == True # day must be 31 or less, month does matter since it is handled elsewhere in the program
    assert is_date_valid("2/45/2007") == False # day cannot be greater than 31 no matter the month
    assert is_date_valid("2/19/3000") == True # year can be in the future
    assert is_date_valid("13/19/2007") == False # month can't be more than 12
    assert is_date_valid("2.0/1.9/2.0.0.7") == False # no other characters in date
    assert is_date_valid("5/1/2") == True # year can be just one digit without 0's
    assert is_date_valid("2/19/-1") == False # year cannot be negative
    assert is_date_valid("2/19/12007") == False # cannot have a year more than 4 digits
    assert is_date_valid("cat") == False # cannot have a anything that is not a date

def test_get_emoji_from_moon_phase():
    with pytest.raises(ValueError):
        get_emoji_from_moon_phase(28) # Raises a ValueError if phase is greater than 28, because python library astral represents moon phases from numbers 0-27.99

    assert get_emoji_from_moon_phase(4.81) == "🌑" # function returns correct phase in emoji with float as input
    assert get_emoji_from_moon_phase(0) == "🌑" # correctly displays phase 1
    assert get_emoji_from_moon_phase(10) == "🌓" # correctly displays phase 2
    assert get_emoji_from_moon_phase(15) == "🌕" # correctly displays phase 3
    assert get_emoji_from_moon_phase(22) == "🌗" # correctly displays phase 4

def test_get_zodiac_from_date():
    with pytest.raises(ValueError):
        get_zodiac_from_date(datetime.date(1998, 4, 1)) # raises Value error if year is not 2024 which the program does elsewhere

    assert get_zodiac_from_date(datetime.date(2024, 4, 1)) == ((datetime.date(2024, 3, 21), datetime.date(2024, 4, 19)), 'Aries', '♈') # uses 2024 as a constant date to compare date ranges returns correct three type data for Aries
    assert get_zodiac_from_date(datetime.date(2024, 5, 1)) == ((datetime.date(2024, 4, 21), datetime.date(2024, 5, 20)), 'Taurus', '♉') # uses 2024 as a constant date to compare date ranges returns correct three type data for Taurus
    assert get_zodiac_from_date(datetime.date(2024, 6, 1)) == ((datetime.date(2024, 5, 21), datetime.date(2024, 6, 21)), 'Gemini', '♊') # uses 2024 as a constant date to compare date ranges returns correct three type data for Gemini
    assert get_zodiac_from_date(datetime.date(2024, 7, 1)) == ((datetime.date(2024, 6, 22), datetime.date(2024, 7, 22)), 'Cancer', '♋')# uses 2024 as a constant date to compare date ranges returns correct three type data for Cancer
    assert get_zodiac_from_date(datetime.date(2024, 8, 1)) == ((datetime.date(2024, 7, 23), datetime.date(2024, 8, 22)), 'Leo', '♌') # uses 2024 as a constant date to compare date ranges returns correct three type data for Leo
    assert get_zodiac_from_date(datetime.date(2024, 9, 1)) == ((datetime.date(2024, 8, 23), datetime.date(2024, 9, 22)), 'Virgo', '♍') # uses 2024 as a constant date to compare date ranges returns correct three type data for Virgo
    assert get_zodiac_from_date(datetime.date(2024, 10, 1)) == ((datetime.date(2024, 9, 23), datetime.date(2024, 10, 23)), 'Libra', '♎') # uses 2024 as a constant date to compare date ranges returns correct three type data for Libra
    assert get_zodiac_from_date(datetime.date(2024, 11, 1)) == ((datetime.date(2024, 10, 24), datetime.date(2024, 11, 21)), 'Scorpius', '♏') # uses 2024 as a constant date to compare date ranges returns correct three type data for Sccorpius
    assert get_zodiac_from_date(datetime.date(2024, 12, 1)) == ((datetime.date(2024, 11, 22), datetime.date(2024, 12, 21)), 'Sagittarius', '♐') # uses 2024 as a constant date to compare date ranges returns correct three type data for Sagittarius
    assert get_zodiac_from_date(datetime.date(2024, 1, 1)) == ((datetime.date(2024, 12, 22), datetime.date(2024, 1, 19)), 'Capricorn', '♑') # uses 2024 as a constant date to compare date ranges returns correct three type data for Capricorn
    assert get_zodiac_from_date(datetime.date(2024, 2, 1)) == ((datetime.date(2024, 1, 20), datetime.date(2024, 2, 18)), 'Aquarius', '♒') # uses 2024 as a constant date to compare date ranges returns correct three type data for Aquarius
    assert get_zodiac_from_date(datetime.date(2024, 3, 1)) == ((datetime.date(2024, 2, 19), datetime.date(2024, 3, 20)), 'Pisces', '♓') # uses 2024 as a constant date to compare date ranges returns correct three type data for Pisces


