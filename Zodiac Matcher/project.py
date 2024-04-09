import re
import sys
import os
import typer
from datetime import date
from rich.console import Console, Group
from rich import print
from rich.prompt import Prompt
from rich.progress import Progress
from rich.progress import track
from rich.panel import Panel
from rich import box
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.layout import Layout
import time
from astral import moon
from rich.live import Live
from emoji import emojize
import inquirer
import requests
from bs4 import BeautifulSoup
# from https://www.oocities.org/spunk1111/celestal.htm
main_img = r'''
         _.-----._
       .'   .-'``|'.
      /    /    -*- \
     ;   <{      |   ;
     |    _\ |       |
     ;   _\ -*- |    ;
      \   \  | -*-  /
       '._ '.__ |_.'
          '-----'
'''
const_year = 2024
# Use 2024 as the constant date: Only uses Months and Days for calculations
zodiacs_dates = [(date(const_year, 3, 21), date(const_year, 4, 19)), (date(const_year, 4, 21), date(const_year, 5, 20)),
                 (date(const_year, 5, 21), date(const_year, 6, 21)), (date(const_year, 6, 22), date(const_year, 7, 22)), (date(const_year, 7, 23), date(const_year, 8, 22)),
                 (date(const_year, 8, 23), date(const_year, 9, 22)), (date(const_year, 9, 23), date(const_year, 10, 23)), (date(const_year, 10, 24), date(const_year, 11, 21)), (date(const_year, 11, 22), date(const_year, 12, 21)), (date(const_year, 12, 22), date(const_year, 1, 19)), (date(const_year, 1, 20), date(const_year, 2, 18)), (date(const_year, 2, 19), date(const_year, 3, 20))]
zodiacs_full = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpius', 'Sagittarius', 'Capricorn' , 'Aquarius' , 'Pisces']
zodiacs = [emojize(f":{x.casefold()}:", language='alias') for x in zodiacs_full]
three_type_data_zodiac = list(zip(zodiacs_dates, zodiacs_full, zodiacs))

def main():

     console = Console()


     layout = Layout(name='menu')

     layout['menu'].split(
          Layout(name='header', size=5),
          Layout(name='main', ratio=1),
          Layout(name='footer', size=5)
     )
     def make_footer():
          return Panel(Text(text="Github: https://github.com/followthefourleafedclover                                                                                                   Email: sreevarpatiyara@gmail.com", justify='left', style='bold'), title=Text(text="Github and Email", style="bold"), title_align='center', border_style="plum3",box=box.ROUNDED, expand=True)
     def make_main():
          return Panel(Text(text=f"\n> Zodiac Matcher is a Python CLI Application based on the modules and libaries used in the CS50 Course such as emojize, sys, datetime, regular expressions, etc to find your zodiac and potential matches.\n> Uses python's rich libaray to display information in the terminal with color and asthetics -> https://pypi.org/project/rich/\n> For more information please read the README.md file attached\n{main_img}", justify='left'), title=Text(text="Preface", style="bold"), border_style="plum3",box=box.ROUNDED)

     def make_header(t):
          return Panel(Text(text=f"{t} \n*                *\n══════════════════════════ ❀•°❀°•❀ ══════════════════════════", justify="center", style="bold"), title=Text(text="Zodiac Matcher", style="bold"), title_align='center', border_style="plum3",box=box.ROUNDED, expand=False)

     layout['main'].update(make_main())
     layout['header'].update(make_header("♈Zodiac Matcher ♈"))
     layout['footer'].update(make_footer())

     with Live(layout, refresh_per_second=4):
               t_ = time.time() + 10
               while time.time() < t_:
                    layout['header'].update(make_header("🖥️  Sreevar Patiyara 🖥️"))
                    time.sleep(2)
                    layout['header'].update(make_header("♈Zodiac Matcher ♈"))
                    time.sleep(2)
     def clear():
          os.system('cls' if os.name == 'nt' else 'clear') # taken from https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python

     clear()

     while True:
          not_valid_string = "Please enter a valid date in the format M/D/Y"
          try:
               date_ = Prompt.ask(prompt=Text(text="Please Enter your Birthday", style="bold plum3"))

          except EOFError:
                    sys.exit("Successfully Exitted the Program :) ")

          valid = False

          if is_date_valid(date_):
               valid = True
               date_list = date_.split('/')
               try:
                    user_date = date(const_year, int(date_list[0]), int(date_list[1]))
               except ValueError as e:
                    not_valid_string += f" -> {e}"
                    valid = False

               if valid:
                    console.print(f'[navajo_white1][bold]Month: [cornflower_blue]{date_list[0]}, [navajo_white1][bold]Day: [cornflower_blue]{date_list[1]}, [navajo_white1][bold]Year: [cornflower_blue]{date_list[2]}')
                    user_date_range, user_zodiac_full, user_zodiac = get_zodiac_from_date(user_date)
                    time.sleep(1)
                    clear()
                    with Progress() as progress:
                         task = progress.add_task("Calculating Zodiac...", total=1000)

                         while not progress.finished:
                              progress.update(task ,advance=0.01)

                    clear()
                    if user_zodiac_full == 'Scorpius':
                         raw_data = requests.get(f"https://www.horoscope.com/zodiac-signs/scorpio")
                    else:
                         raw_data = requests.get(f"https://www.horoscope.com/zodiac-signs/{user_zodiac_full.casefold()}")

                    parsed_data  = BeautifulSoup(raw_data.content, 'html5lib')

                    desc_list = []
                    paragraphs = parsed_data.find_all('p')
                    for item in paragraphs:
                         desc_list.append(item.text)

                    response = desc_list[1]

                    #print(desc_list)

                    my_zodiac_layout = Layout(name='Zodiac')

                    my_zodiac_layout.split(Layout(name='top', size = 10),
                                           Layout(name='bottom', size = 5))

                    def make_zodiac_header():
                         return Panel(Text(text=f"\n{user_zodiac} \n\n {response}", justify='center', style='bold'), title=Text(text=user_zodiac_full, style="bold"), title_align='center', border_style="plum3",box=box.ROUNDED, expand=True)
                    def make_zodiac_footer():
                         return Panel(Text(text=f'This description was scraped from {Text(text='https://www.horoscope.com', style='bold')}, please vist to learn more about zodiacs, astrology and more \n{desc_list[-1]}', justify='center', style='bold'), title=Text(text="Sources", style="bold"), title_align='center', border_style="plum3",box=box.ROUNDED, expand=True)
                    my_zodiac_layout['top'].update(make_zodiac_header())
                    my_zodiac_layout['bottom'].update(make_zodiac_footer())
                    with Live(my_zodiac_layout, refresh_per_second=4):
                         t_ = time.time() + 15
                         while time.time() < t_:
                              my_zodiac_layout['top'].update(make_zodiac_header())
                              my_zodiac_layout['bottom'].update(make_zodiac_footer())

                    #console.print(f"[bold][plum3]Your Zodiac: {user_zodiac_full} {user_zodiac}")

                    clear()

                    user_four_type_data = (user_date, user_date_range, user_zodiac_full, user_zodiac)


                    option = inquirer.list_input("Choice", choices=['See Every Match', 'Match With One Other Person'], carousel=True)


                    if option == "See Every Match":
                         if user_zodiac_full == 'Scorpius':
                              request_zodiac = 'scorpio'
                         else:
                              request_zodiac = user_zodiac_full.lower()

                         scores = []

                         for zodiac in zodiacs_full:
                              if zodiac == 'Scorpius':
                                   raw_data = requests.get(f'https://www.horoscope.com/love/compatibility/{request_zodiac}-scorpio')
                              else:
                                   raw_data = requests.get(f'https://www.horoscope.com/love/compatibility/{request_zodiac}-{zodiac}')

                              parsed_data = BeautifulSoup(raw_data.content, 'html5lib')

                              x, y  = parsed_data.find('div', class_='game-compatibility-score').text.strip().split('/')

                              scores.append(round((int(x)/int(y)) * 100))

                         clear()

                         scores_zodiac = list(zip(zodiacs_full, scores))

                         scores_zodiac = list(sorted(scores_zodiac, key=lambda x: x[1], reverse=True))

                         for index, item in enumerate(scores_zodiac):
                              if index < 4:
                                   text_ = '[green]'
                              elif index < 8:
                                   text_ = '[yellow]'
                              else:
                                   text_ = '[red]'
                              console.print(f"{text_}{index+1}. {item[0]} -> {item[1]}%")

                         console.print("\n[white][bold]Results were scraped from www.horoscope.com\n")
                         sys.exit()

                    if option == 'Match With One Other Person':
                         while True:
                              try:
                                   other_person = Prompt.ask(Text(text="Please Enter the other person's Birthday", style='bold plum3'))
                              except EOFError:
                                   sys.exit("Successfully Exitted the Program :) ")

                              if is_date_valid(other_person):
                                   other_person_date_list = other_person.split('/')
                                   try:
                                        other_person_date = date(const_year, int(other_person_date_list[0]), int(other_person_date_list[1]))
                                   except ValueError:
                                        print("s")

                                   other_person_date_range, other_person_zodiac_full, other_person_zodiac = get_zodiac_from_date(other_person_date)
                                   other_person_four_type_data = (other_person_date, other_person_date_range, other_person_zodiac_full, other_person_zodiac)

                                   user_method  = inquirer.list_input("Method", choices=['traditional - finds compatibility from tradtional elemental relationships between zodiacs: returns a binary output','traditional_percentage - finds compatibility from tradtional elemental relationships between zodiacs: returns a perctage to two decimal places' ,"moon_phase - finds compatibility from the phases of the moon during birth"])

                                   if "traditional" in user_method:

                                        user_algo = inquirer.list_input("Algorithim", choices=["score_high - starts with the first zodiac's end date to the second zodiac's end date", "score_low - starts with the first zodiac's start date to the second zodiac's start date"], carousel=True)
                                   else:
                                        user_algo = "score_high"

                                   clear()
                                   with Progress() as progress:
                                        task = progress.add_task("[bold][plum3]Calculating Compatibility ...", total=1000)

                                        while not progress.finished:
                                             progress.update(task, advance=0.01)

                                   time.sleep(1)
                                   clear()
                                   console.print(zodiac_compatibility_test(user_four_type_data, other_person_four_type_data, method=user_method.split('-')[0].strip(), algorithim=user_algo.split('-')[0].strip()))
                                   break

                    # user date, zodiac date, zodiac name, zodiac symbol

                    break
               else:
                    print(not_valid_string)

          else:
               print(not_valid_string)




def zodiac_compatibility_test(zodiac1, zodiac2, method='traditional', algorithim=None):
     algorithims = ["score_high", 'score_low']
     methods = ['traditional', 'traditional_percentage', 'moon_phase']
     global traditional_matches
     traditional_matches = {'Aries': ('Gemini', "Aquarius"), 'Taurus': ('Cancer', 'Pisces'),
                                 'Gemini': ('Aries', 'Leo'), 'Cancer': ('Taurus', 'Virgo'),
                                 'Leo': ('Gemini','Libra'), 'Virgo': ('Cancer' , 'Scorpius'),
                                 'Libra': ('Leo', 'Sagittarius'), 'Scorpius':('Virgo', 'Capricorn'),
                                 'Sagittarius':('Libra', 'Aquarius'), 'Capricorn':('Scorpius', 'Pisces'),
                                 'Aquarius':('Aries', 'Sagittarius'), 'Pisces':('Taurus', 'Capricorn')}

     if not algorithim in algorithims or not method in methods:
          raise TypeError
     if not isinstance(zodiac1, tuple) or not isinstance(zodiac2, tuple):
          raise TypeError


     if method == methods[2]:
          moon_phase1 = moon.phase(zodiac1[0])
          moon_phase2 = moon.phase(zodiac2[0])

          if abs(moon_phase2 - moon_phase1) < 1:
               return f"[plum3]You both have the same moon phase which is really rare! your compatibilty is [cornflower_blue]100%"

          return f"{get_emoji_from_moon_phase(moon_phase1)} x {get_emoji_from_moon_phase(moon_phase2)} -> [bold]Your moon phase compatibility is [cornflower_blue]{round((((moon_phase1+moon_phase2) % 21)/21) * 100, 2)}%"

     if method == 'traditional':

          zodiac1_matches = traditional_matches[zodiac1[2]]

          if zodiac2[1] in zodiac1_matches:
               return 'Match'
          else:
               return '[bold][cornflower_blue]Unfortunely you two are not a traditional match, please try the moon phase method'

     if method == 'traditional_percentage':

          zodiac1_matches = traditional_matches[zodiac1[2]]

          if zodiac2[2] in zodiac1_matches:
               if algorithim == algorithims[0]:
                    differences_of_zodiacs = abs(zodiac2[1][1] - zodiac1[1][1])

               if algorithim == algorithims[1]: # -> usually gives higher score -> more leinent
                    differences_of_zodiacs = abs(zodiac2[1][0] - zodiac1[1][0])



               differences_of_users = abs(zodiac2[0] - zodiac1[0])
               return f'You two are a match {zodiac1[3]}x {zodiac2[3]}-> with a compatibility of {round((differences_of_zodiacs.days/differences_of_users.days)*100, 2)}%'


          else:
               return '[bold][cornflower_blue]Unfortunely you two are not a traditional match, please try the moon phase method'


def get_zodiac_from_date(date):
     if date.year != 2024:
          raise ValueError
     for zodiac in three_type_data_zodiac:
          if zodiac[0][0] <= date <= zodiac[0][1]:
               return zodiac
     return three_type_data_zodiac[-3]

def get_emoji_from_moon_phase(phase):
     if phase >= 28:
          raise ValueError
     if 0 <= phase <= 6.99:
          return "🌑"
     elif 7 <= phase <= 13.99:
          return "🌓"
     elif 14 <= phase <= 20.99:
          return "🌕"
     elif 21 <= phase <= 27.99:
          return "🌗"


def is_date_valid(s):
     # Dymanic Input: enter string as M/D/Y not MM/DD/YYYY -> accepts any year under 4 characters
     matches = re.search(r"^([0-9]|1[0-2])\/([0-9]|1[0-9]|2[0-9]|3[0-1])\/([0-9])?([0-9])?([0-9])?([0-9])$", s)

     if matches:
          return True
     else:
          return False

if __name__ == '__main__':
    typer.run(main)
