# Zodiac Matcher Harvard CS50 Final Project
#### Video Demo:  <https://www.youtube.com/watch?v=t_GbW5LFSgk>
## Description
My final project for Harvard's C50 Introduction to Python Programming Course is a zodiac matcher. It is a CLI application that takes a user's birthday as input and finds their zodiac.
Then, the user gets a brief description of their zodiac by 		www.horoscope.com. Followed by a choice, whether to find a specific match with another person, or to find matches with all the zodiacs.

## Zodiacs

| Zodiac |Dates  |
|--|--|
| Aries | March 21 – April 19 |
| Taurus | April 20 – May 20 |
| Gemini | May 21 – June 20 |
| Cancer| June 22 – July 22|
| Leo | July 23 – August 22|
| Virgo | August 23 – September 22 |
| Libra | September 23 – October 23 |
| Scorpio | October 24 – November 21 |
| Sagittarius | November 22 - December 21 |
| Capricorn | December 22 – January 19 |
| Aquarius | January 20 – February 18 |
| Pisces | February 19 – March 20|

**Code Example** - How Zodiacs are stored in the program using Datetime library

    onst_year = 2024
    zodiacs_dates = [(date(const_year, 3, 21), date(const_year, 4, 19)), (date(const_year, 4, 21), date(const_year, 5, 20)),
                     (date(const_year, 5, 21), date(const_year, 6, 21)), (date(const_year, 6, 22), date(const_year, 7, 22)), (date(const_year, 7, 23), date(const_year, 8, 22)),
                     (date(const_year, 8, 23), date(const_year, 9, 22)), (date(const_year, 9, 23), date(const_year, 10, 23)), (date(const_year, 10, 24), date(const_year, 11, 21)), (date(const_year, 11, 22), date(const_year, 12, 21)), (date(const_year, 12, 22), date(const_year, 1, 19)), (date(const_year, 1, 20), date(const_year, 2, 18)), (date(const_year, 2, 19), date(const_year, 3, 20))]
    zodiacs_full = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpius', 'Sagittarius', 'Capricorn' , 'Aquarius' , 'Pisces']
    zodiacs = [emojize(f":{x.casefold()}:", language='alias') for x in zodiacs_full]
    three_type_data_zodiac = list(zip(zodiacs_dates, zodiacs_full, zodiacs))

## Algorithms and Methods
When prompted for another person's birthday, the user has a choice between three different methods and two algorithms (Shown below). These choices are used as parameters for the
`zodiac_compatibility_test` function (Arguments show below).

    zodiac_compatibility_test(set:zodiac1, set:zodiac1, str:method='traditional', str:algorithm=None) -> str

| Arguments | Description | Type|
|--|--|--|
| **zodiac1** | *(user_birthdate, user_zodiac_date_range, user_zodiac_full_name, user_zodiac_emoji)* | Set|
|**zodiac2**|*(other_person_birthdate, other_person_date_range, other_person_zodiac_full_name, other_person_zodiac_emoji*)|Set|
|**method**|*Three methods: traditional, traditional_percentage, and moonphase*|String|
|**algorithm**|*Two algorithms: score_high, and score_low*|String|

**Method Descriptions**

|Method| Description |
|--|--|
| traditional | *Uses traditional zodiac pairs to find compatibility. Returns a binary output > 'Match' or 'No Match'* |
| traditional_percentage | *Uses traditional zodiac pairs to find compatibility. Returns a rounded percantage to two decimal places > 'NN.NN%'* |
| moon_phase | *Uses the phase of the moon during birth to find compatibility. Returns '100%' if both have the same moon phase, or returns a rounded percentage to two decimal places> 'NN.NN%'* **(Does not need the algorithm parameter when used)** |

**Algorithm Descriptions**

|Algorithm | Description  |
|--|--|
| score_high | Finds the difference between the last date of `zodiac2` and the last date of `zodiac1`. Then divides it by the difference in the user and other person's birthdays.  |
| score_low | Finds the difference between the first date of `zodiac2` and the first date of `zodiac1`. Then divides it by the difference in the user and other person's birthdays  |

**Formula**

`differences_of_zodiacs.days/differences_of_users.days`

The only difference in the two algorithms is the method in which the differences_of_zodiacs is calculated.


|Algorithm |Example |
|--|--|
|**score_high** | `differences_of_zodiacs = abs(zodiac2[1][1] - zodiac1[1][1])` |
| **score_low** | `differences_of_zodiacs = abs(zodiac2[1][0] - zodiac1[1][0])` |

## Tests
Three test files for three functions: `get_zodiac_from_date`, `get_emoji_from_moon_phase`, and `is_date_valid`.

## Sources

| Library | Link |
|--|--|
| Regular Expressions | https://pypi.org/project/regex/ |
| System | https://docs.python.org/3/library/sys.html |
| Operating System | https://docs.python.org/3/library/os.html |
| Rich | https://pypi.org/project/rich/ |
| Astral | https://pypi.org/project/astral/ |
| Typer | https://pypi.org/project/typer-cli/ |
| Emoji | https://pypi.org/project/emoji/ |
| Beautiful Soup | https://pypi.org/project/bs4/ |
| Time | https://docs.python.org/3/library/time.html |
| Inquirer| https://pypi.org/project/inquirer/ |
| Requests | https://pypi.org/project/requests/ |

