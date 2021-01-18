'''
File name: Rai_Tanveer_Hangman.py
Authors: Muhammad Tanveer and Lokansh Rai
Description: Hangman Game, with Hint feature, Picture feature, and Guess the Word Feature. 13 Categories, 236 words.
Python Version: 3.7.0
IDLE Version: 3.7.0
EasyGui Version: 0.97
'''
import easygui#imports system-specific parameters and functions that are only in the easygui library, easygui library parameters handle all of the graphics in the program 
from easygui import *
import random#imports the random function
import sys#imports the system-specific parameters and function that are only in the sys library
# The following are images from the internet that are saved within the same file in the '.gif'type.
start_game_pic = 'start_game_pic.gif' # Image displayed when user starts the game. 
intro_image = 'intro_image.gif' # This image will be shown after the user presses 'Continue' in the first window. Defined by 'intro_image'.
correct_image = 'correct_image.gif' # This image will be shown Whenever the user chooses a letter that is in the word. Defined by 'correct_image'.
hangman_dead = 'hangman_dead.gif' # This image will be shown when the user fails to guess the word, in which case the hangman has died. Defined by 'hangman_dead'.
hangman_lives = 'hangman_lives.gif' # This image will be shown when the user succeeds in guessing the word, in which case the hangman has survives. Defined by 'hangman_lives'.
hangman_image = 'hangman_1.gif' # This image will be shown after the user enters the game and are handed instructions. Defined by 'hangman_image'.
hint_feature = 'hint-feature.gif' # This image will be shown when the user is presented with the hint. Defined by 'hint_feature'.
# The following are images that will be displayed to the user if they select the 'Help' button at the start.
# Each image displays a picture of each stage of a game, with the word 'RAM' used as an example.
help_pic_1 = 'help_pic_1.gif'
help_pic_2 = 'help_pic_2.gif'
help_pic_3 = 'help_pic_3.gif'
help_pic_4 = 'help_pic_4.gif'
help_pic_5 = 'help_pic_5.gif'
help_pic_6 = 'help_pic_6.gif'
help_pic_7 = 'help_pic_7.gif'
help_pic_8 = 'help_pic_8.gif'
help_pic_9 = 'help_pic_9.gif'
help_pic_10 = 'help_pic_10.gif'
help_pic_11 = 'help_pic_11.gif'
help_pic_picture_1 = 'help_pic_picture_1.gif'
help_pic_picture_2 = 'help_pic_picture_2.gif'
help_pic_guessword_1 = 'help_pic_guessword_1.gif'
help_pic_guessword_2 = 'help_pic_guessword_2.gif'

# The following dictionary assigns each letter from the English alphabet with it's box-letter image (.gif file) from the file. Defined by 'letters'.
# A blank box indicates the positions in a word that have not been identified by the user and is assigned the number 1.
# Each letter on the left side of the dictionary is a key and the right side is its corresponding value, in this case it is an image 
letters  = {
    'A' : 'letter_A.gif',
    'B' : 'letter_B.gif',
    'C' : 'letter_C.gif',
    'D' : 'letter_D.gif',
    'E' : 'letter_E.gif',
    'F' : 'letter_F.gif',
    'G' : 'letter_G.gif',
    'H' : 'letter_H.gif',
    'I' : 'letter_I.gif',
    'J' : 'letter_J.gif',
    'K' : 'letter_K.gif',
    'L' : 'letter_L.gif',
    'M' : 'letter_M.gif',
    'N' : 'letter_N.gif',
    'O' : 'letter_O.gif',
    'P' : 'letter_P.gif',
    'Q' : 'letter_Q.gif',
    'R' : 'letter_R.gif',
    'S' : 'letter_S.gif',
    'T' : 'letter_T.gif',
    'U' : 'letter_U.gif',
    'V' : 'letter_V.gif',
    'W' : 'letter_W.gif',
    'X' : 'letter_X.gif',
    'Y' : 'letter_Y.gif',
    'Z' : 'letter_Z.gif',
    '1' : 'letter_BLANK.gif'
}# Closing the dictionary 

# The following dictionary assigns each stage if the hangman with the numbers 1-6 assigned to each stage.
# Each stage is assigned an image (.gif file) from the file. Defined by 'hangman'.
# Each letter on the left side of the dictionary is a key and the right side is its corresponding value, in this case it is an image
hangman = {
    1: "hangman_1_head.gif",
    2: "hangman_1_body.gif",
    3: "hangman_1_right_arm.gif",
    4: "hangman_1_left_arm.gif",
    5: "hangman_1_right_foot.gif",
    6: "hangman_1_left_foot.gif",
}#Closing the dictionary 
      
def cateory_choice(): # This function will decide the category, based on a user input. Defined by 'cateory_choice()'.
    # There are 12 categories for the users to choose from, all of which are placed into the array defined by 'categories;.
    categories = ['Candy/Chocolate Brands [TUTORIAL]', 'Countries', 'Companies', 'Computer Terms', 'Elements of the Periodic Table', 'Films',
                  'Musicians', 'Professions', 'Sports Stars', 'Superheroes', 'Video Game Characters',
                  'World Leaders - Last Name (Past and Present)', 'Random Selection [VERY HARD]',]

    category = choicebox("Pleas select a category from the choices below. A word will be selected that associated with you category.",choices = categories) # A choicebox window is used to display the elements of 'categories' which are the categories the user may choose.
    # each choice will open a filed, defined by 'category_file'.
    if category == 'Elements of the Periodic Table':
        category_file = open("Word_bank - Elements.txt", "r") # If the user presses the 'Elements of the Periodic Table' button, the "Word_bank - Elements" text file is open and read.
    elif category == 'Superheroes':
        category_file = open("Word_bank - Superheroes.txt", "r") # If the user presses the 'Superheroes' button, the "Word_bank - Superheroes" text file is open and read.
    elif category == 'Films':
        category_file = open("Word_bank - Movies.txt", "r") # If the user presses the 'Films' button, the "Word_bank - Movies" text file is open and read.
    elif category == 'Sports Stars':
        category_file = open("Word_bank - Sports Stars.txt", "r") # If the user presses the 'Sports Stars (Past Present)' button, the "Word_bank - Sports Stars" text file is open and read.
    elif category == 'Candy/Chocolate Brands [TUTORIAL]':
        category_file = open("Word_bank - Candy.txt", "r") # If the user presses the 'Candy/Chocolate Brands [VERY EASY]' button, the Word_bank - Candy" text file is open and read.
    elif category == 'Countries':
        category_file = open("Word_bank - Countries.txt", "r") # If the user presses the 'Countries' button, the "Word_bank - Countries" text file is open and read.
    elif category == 'World Leaders - Last Name (Past and Present)':
        category_file = open("Word_bank - Leaders.txt", "r") # If the user presses the 'World Leaders - Last Name (Past and Present)' button, the "Word_bank - Leaders" text file is open and read.
    elif category == 'Companies':
        category_file = open("Word_bank - Companies.txt", "r") # If the user presses the 'Companies' button, the "Word_bank - Companies" text file is open and read.
    elif category == 'Video Game Characters':
        category_file = open("Word_bank - Video Game Characters.txt", "r") # If the user presses the 'Video Game Characters' button, the "Word_bank - Video Game Characters" text file is open and read.
    elif category == 'Computer Terms':
        category_file = open("Word_bank - Computer Hardware_Accessories.txt", "r") # If the user presses the 'Computer Terms' button, the "Word_bank - Computer Hardware_Accessories" text file is open and read.
    elif category == 'Musicians':
        category_file = open("Word_bank - Musicians.txt", "r") # If the user presses the 'Musicians' button, the "Word_bank - Musicians" text file is open and read.
    elif category == 'Professions':
        category_file = open("Word_bank - Professions.txt", "r") # If the user presses the 'Professions' button, the "Word_bank - Professions" text file is open and read.
    elif category == 'Random Selection [VERY HARD]':
        category_file = open("Word_bank - Random Words.txt", "r") # If the user presses the 'Random Selection [VERY HARD]' button, the "Word_bank - Random Words" text file is open and read.
    else:
        exit() # If the user presses the 'Elements of the Periodic Table' button, the "Word_bank - Elements" text file is open and read.
    print ("The category is:", category) # The category choice is printed on the IDLE panel.
    return category_file # The value of 'category_file' is returned when this function is called.

def word_selection(categ_choice): # This function will randomly select a word from the category. Defined by 'word_selection(cateory_choice)'.
    list_of_words = (categ_choice.read()) # the return for the 'categ_choice' function is read, and the output is defined by 'list_of_words'.
    splits_list = list_of_words.split()  # Each word in the list is split into a list, defined by 'splits_list'.
    word_selection_num = random.randint(0, len(splits_list) - 1) # A random integer is selected using the 'random()' function from 0 to the length of 'splits_list' minus one. Defined by 'word_selection_num'.
    word = str(splits_list[word_selection_num]) # A word is selected from the list by slicing a word from the 'splits_list' list, based on the value of 'word_selection_num'.
    upper = word.upper() # The word is uppercased and defined by 'upper'.
    return upper # The value of 'upper' will be returned when this function is called.

def hint__pic_choice(the_word): # This function assigns each word (total of 236) with a unique hint and picture file. Defined by 'hint__pic_choice'.
    # Each word (the_word) is assigned a unique hint (hint) and picture (answer_image) from a file saved in the folder, downloaded from the internet.
    # If the user selects the 'Random Selection' category, any word from any category is chosen.    
    # The following are hints that are given according to what word is picked by the computer from the 'Candy Companies' category.
    if the_word == 'KITKAT':
        hint = 'Have a break...Have a...'
        answer_image = '1_KitKat.gif'
    elif the_word == 'SMARTIES':
        hint = 'Only...have the answer!'
        answer_image = '2_Smarties.gif'
    elif the_word == 'SKITTLES':
        hint = 'Experience the Rainbow. Taste the Rainbow.'
        answer_image = '3_Skittles.gif'
    elif the_word == 'TWIZZLERS':
        hint = 'Make Mouths Happy!'
        answer_image = '4_Twizzlers.gif'
    elif the_word == 'NERDS':
        hint = 'for the love of...'
        answer_image = '5_Nerds.gif'
    elif the_word == 'STARBURST':
        hint = 'Unexplainably Juicy.'
        answer_image = '6_Starbursts.gif'
    elif the_word == 'TWIX':
        hint = 'Two for me, none for you.'
        answer_image = '7_Twix.gif'
    elif the_word == 'SKOR':
        hint = 'A toffee candy bar made by The Hershey Company.'
        answer_image = '8_Skor.gif'
    elif the_word == 'MAYNARDS':
        hint = 'Known for making wine gums and Sour Patch Kids.'
        answer_image = '9_Maynards.gif'
    elif the_word == 'MARS':
        hint = 'Put some play in your day.'
        answer_image = '10_Mars.gif'
    elif the_word == 'HARIBO':
        hint = '...makes children happy - and adults too!'
        answer_image = '11_Haribo.gif'
    elif the_word == 'LINDT':
        hint = 'Master Chocolatier Since 1845'
        answer_image = '12_Lindt.gif'
    elif the_word == 'CADBURY':
        hint = 'Tastes like this feels.'
        answer_image = '13_Cadbury.gif'
    elif the_word == 'REESES':
        hint = 'Two great tastes that taste great together!'
        answer_image = '14_Reeses.gif'
    elif the_word == 'PAYDAY':
        hint = 'Behold, something nutty!'
        answer_image = '15_Payday.gif'
    elif the_word == 'MENTOS':
        hint = 'You should not eat these with Coke!'
        answer_image = '16_Mentos.gif'
    elif the_word == 'LIFESAVERS':
        hint = 'Mints that may save your life one day!'
        answer_image = '17_Lifesavers.gif'
    elif the_word == 'TOBLERONE':
        hint = 'The legendary triangular swiss chocolate.'
        answer_image = '18_Toblerone.gif'
    elif the_word == 'BOUNTY':
        hint = "... - the chocolate bar that's shaped slightly different from other chocolate bars!"
        answer_image = '19_Bounty.gif'
    # NOTE: The word is displayed in the picture, which is why this category is considered the easiest.
        
    # The following are hints that are given according to what word is picked by the computer from the 'Companies' category.
    elif the_word == 'SAMSUNG':
        hint = 'Known for there very innovative, yet expensive Galaxy smartphones.'
        answer_image = '20_Samsung.gif'
    elif the_word == 'PEPSI':
        hint = "It's not Coca-Cola!"
        answer_image = '21_Pepsi.gif'
    elif the_word == 'APPLE':
        hint = "The first company to reach a value of ONE TRILLION USD."
        answer_image = '22_Apple.gif'
    elif the_word == 'AMAZON':
        hint = "The largest online shopping company in the world."
        answer_image = '23_Amazon.gif'
    elif the_word == 'VIACOM':
        hint = "A mass media company that owns Nickelodeon and Paramount Studios!"
        answer_image = '24_Viacom.gif'
    elif the_word == 'STARBUCKS':
        hint = "An American coffee company known for its Vanilla Bean Frappe!"
        answer_image = '25_Starbucks.gif'
    elif the_word == 'LEGO':
        hint = "Originated in Denmark, this company manufactures a popular line of plastic construction toys!"
        answer_image = '26_Lego.gif'
    elif the_word == 'BEATS':
        hint = "Founded by American rapper Dr. Dre and produces some of the finest audio products."
        answer_image = '27_Beats.gif'
    elif the_word == 'FORBES':
        hint = "The best place to find the list of the richest people in the world!"
        answer_image = '28_Forbes.gif'
    elif the_word == 'TESLA':
        hint = "Founded by Elon Musk and known for the line of fully electric automobiles."
        answer_image = '29_Tesla.gif'
    elif the_word == 'PUMA':
        hint = "Founded by Rudolf Dassler, the brother of Adi Dassler who invented Adidas!"
        answer_image = '30_Puma.gif'
    elif the_word == 'HONDA':
        hint = "A Japanese conglomerate known for their line of automobiles including the Civic and Accord."
        answer_image = '31_Honda.gif'
    elif the_word == 'YAHOO':
        hint = "You've got mail!"
        answer_image = '32_Yahoo.gif'
    elif the_word == 'WALMART':
        hint = "Save Money. Live Better."
        answer_image = '33_Walmart.gif'
    elif the_word == 'CANON':
        hint = "A Japanese conglomerate known for their line of cameras."
        answer_image = '34_Canon.gif'
    elif the_word == 'RELIANCE':
        hint = "An Indian conglomerate known for their production of oil and natural gas."
        answer_image = '35_Reliance.gif'
    elif the_word == 'MICROSOFT':
        hint = "Founded by Bill Gates and known for inventing the Windows operating system."
        answer_image = '36_Microsoft.gif'
    elif the_word == 'NIKE':
        hint = "A sportswear company known for their partnership with Michael Jordan and Cristiano Ronaldo."
        answer_image = '37_Nike.gif'
    elif the_word == 'ADIDAS':
        hint = "A sportswear company founded by Adi Dassler, the brother of the founder of Puma."
        answer_image = '38_Adidas.gif'
    elif the_word == 'VIRGIN':
        hint = "A telecommunications company founded by English magnate Richard Branson."
        answer_image == '39_Virgin.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Computer Terms' category.
    elif the_word == 'RAM':
        hint = "Short for 'Random Access Memory'."
        answer_image = '40_RAM.gif'
    elif the_word == 'KEYBOARD':
        hint = "The standard form of this device is the QWERTY format!"
        answer_image = '41_Keyboard.gif'
    elif the_word == 'MONITOR':
        hint = "Used to electronically display information from a computer!"
        answer_image = '42_Monitor.gif'
    elif the_word == 'PROCESSOR':
        hint = "Notable manufactures of this are Intel and Radeon!"
        answer_image = '43_Processor.gif'
    elif the_word == 'HEADSET':
        hint = "Commonly used in gaming and allows for communication and hearing between parties!"
        answer_image = '44_Headset.gif'
    elif the_word == 'NETWORK':
        hint = "A group of two or more devices that can communicate with each other!"
        answer_image = '45_Network.gif'
    elif the_word == 'ROM':
        hint = "Short for 'Read-Only Memory."
        answer_image = '46_ROM.gif'
    elif the_word == 'MODEM':
        hint = "Part that delivers internet connection to the device!"
        answer_image = '47_Modem.gif'
    elif the_word == 'GRAPHICS':
        hint = "NVIDIA is a well-known company that produces this type of card!"
        answer_image = '48_Graphics.gif'
    elif the_word == 'EXTERNAL':
        hint = "USB's are common forms of this type of hard drive."
        answer_image = '49_External.gif'
    elif the_word == 'MOTHERBOARD':
        hint = "Main circuit board of the computer."
        answer_image = '50_Motherboard.gif'
    elif the_word == 'WEBCAM':
        hint = "Allows for streaming of real time imagery through a computer."
        answer_image = '51_Webcam.gif'
    elif the_word == 'STORAGE':
        hint = "Holds information and can be internal or external."
        answer_image = '52_Storage.gif'
    elif the_word == 'PRINTER':
        hint = "Produces a physical version of an online document!"
        answer_image = '53_Printer.gif'
    elif the_word == 'SCANNER':
        hint = "Produces an online version of a physical document!"
        answer_image = '54_Scanner.gif'
    elif the_word == 'TRACKPAD':
        hint = "An input pointing device that is made of a flat surface that detects finger prints!"
        answer_image = '55_Trackpad.gif'
    elif the_word == 'FAN':
        hint = "Made of rotating blades that cools a system."
        answer_image = '56_Fan.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Countries' category.
    elif the_word == 'PARAGUAY':
        hint = "It's capital is Asunción and has a population of around 6.8 million."
        answer_image = '57_Paraguay.gif'
    elif the_word == 'GUINEA':
        hint = "Found in West Africa and has a capital of Conakry."
        answer_image = '58_Guinea.gif'
    elif the_word == 'BARBADOS':
        hint = "Found in the Caribbean and known for being the birthplace of superstar Rihanna."
        answer_image = '59_Barbados.gif'
    elif the_word == 'ECUADOR':
        hint = "Found in South America and shares a name similar to the imaginary line that travels around the world."
        answer_image = '60_Ecuador.gif'
    elif the_word == 'INDONESIA':
        hint = "With a capital of Jakarta, this country is known its 18000 islands!"
        answer_image = '61_Indonesia.gif'
    elif the_word == 'PORTUGAL':
        hint = "With a capital of Lisbon, this country is known for being the birth place of soccer star Cristiano Ronaldo!"
        answer_image = '62_Portugal.gif'
    elif the_word == 'ESTONIA':
        hint = "With a capital of Tallinn, this country has a population of only 1.3 million."
        answer_image = '63_Estonia.gif'
    elif the_word == 'HUNGARY':
        hint = "With a capital of Budapest, this country is known for being the birth place of Erno Rubik, the creator of the Rubik's Cube!"
        answer_image = '64_Hungary.gif'
    elif the_word == 'FRANCE':
        hint = "The champions of the 2018 FIFA World Cup!"
        answer_image = '65_France.gif'
    elif the_word == 'CANADA':
        hint = "The second largest country in the world based on land size!"
        answer_image = '66_Canada.gif'
    elif the_word == 'MALAYSIA':
        hint = "With a capital of Kuala Lumpur, this country is known for the iconic Petronas Towers!"
        answer_image = '67_Malaysia.gif'
    elif the_word == 'URUGUAY':
        hint = "With a capital of Montevideo, this country is found in South America!"
        answer_image = '68_Uruguay.gif'
    elif the_word == 'BELGIUM':
        hint = "With a capital of the City of Brussels, this country is known for its major chocolate industry!"
        answer_image = '69_Belgium.gif'
    elif the_word == 'COLOMBIA':
        hint = "With a capital of Bogotá, this country is known for being the birth place of superstar Shakira!"
        answer_image = '70_Colombia.gif'
    elif the_word == 'EGYPT':
        hint = "With a capital of Cairo, this country is known for its iconic pyramids!"
        answer_image = '71_Egypt.gif'
    elif the_word == 'PHILIPPINES':
        hint = "With a capital of Manila, this country is known for having more than 7000 islands!"
        answer_image = '72_Philippines.gif'
    elif the_word == 'NIGERIA':
        hint = "With a capital of Abuja, this country is largest country in Africa according to population!"
        answer_image = '73_Nigeria.gif'
    elif the_word == 'ARGENTINA':
        hint = "With a capital of Buenos Aires, this country is known for being the birth place of soccer star Lionel Messi!"
        answer_image = '74_Argentina.gif'
    elif the_word == 'LITHUANIA':
        hint = "With a capital of Vilnius, this country is known for being the birth place of several basketball stars including Jonas Valančiūnas!"
        answer_image = '75_Lithuania.gif'
    elif the_word == 'PAKISTAN':
        hint = "With a capital of Islamabad, this country is known for its powerful air force!"
        answer_image = '76_Pakistan.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Elements' category.
    elif the_word == 'NITROGEN':
        hint = "This element has the symbol 'N' and is often used in dynamite."
        answer_image = '77_Nitrogen.gif'
    elif the_word == 'RUTHERFORDIUM':
        hint = "This element has the symbol 'Rf' and can only be synthetically made."
        answer_image = '78_Rutherfordium.gif'
    elif the_word == 'LEAD':
        hint = "This element has the symbol 'Pb' and is the only known material that Superman cannot see through."
        answer_image = '79_Lead.gif'
    elif the_word == 'COPPER':
        hint = "This element has the symbol 'Cu' and is often the primary make-up of electrical wires."
        answer_image = '80_Copper.gif'
    elif the_word == 'OXYGEN':
        hint = "This element has the symbol 'O' and is essential for human life."
        answer_image = '81_Oxygen.gif'
    elif the_word == 'HYDROGEN':
        hint = "This element has the symbol 'H' and can is one of two elements that make up water."
        answer_image = '82_Hydrogen.gif'
    elif the_word == 'EINSTEINIUM':
        hint = "This element has the symbol 'Es' and is a synthetic element that was found as component of debris in the atomic bombing of Japan in 1952."
        answer_image = '83_Einsteinium.gif'
    elif the_word == 'COBALT':
        hint = "This element has the symbol 'Co' and is a key element in the make-up of magnets."
        answer_image = '84_Cobalt.gif'
    elif the_word == 'XENON':
        hint = "This element has the symbol 'Xe' and is used in ultraviolet lighting."
        answer_image = '85_Xenon.gif'
    elif the_word == 'ZINC':
        hint = "This element has the symbol 'Zn' and is an essential vitamin for human health."
        answer_image = '86_Zinc.gif'
    elif the_word == 'IRON':
        hint = "This element has the symbol 'Fe' and makes up much of Earth's cores."
        answer_image = '87_Iron.gif'
    elif the_word == 'NEON':
        hint = "This element has the symbol 'Ne' and is used in lasers and high-voltage indicators."
        answer_image = '88_Neon.gif'
    elif the_word == 'SILVER':
        hint = "This element has the symbol 'Ag' and is usually awarded to second-placed individuals and teams."
        answer_image = '89_Silver.gif'
    elif the_word == 'SODIUM':
        hint = "This element has the symbol 'Na' and is a used in table salt."
        answer_image = '90_Sodium.gif'
    elif the_word == 'LITHIUM':
        hint = "This element has the symbol 'Li' and is a key element in the make-up of batteries."
        answer_image = '91_Lithium.gif'
    elif the_word == 'RADON':
        hint = "This element has the symbol 'Rn' and useful in cancer therapy."
        answer_image = '92_Radon.gif'
    elif the_word == 'BARIUM':
        hint = "This element has the symbol 'Ba' and is used in glassmaking and paint."
        answer_image = '93_Barium.gif'
    elif the_word == 'GALLIUM':
        hint = "This element has the symbol 'Ga' and is a key element in the make-up of brilliant mirrors."
        answer_image = '94_Gallium.gif'
    elif the_word == 'BORON':
        hint = "This element has the symbol 'Bo' and is used as an aid in making strong bones and increasing testosterone levels."
        answer_image = '95_Boron.gif'
    elif the_word == 'YTTRIUM':
        hint = "This element has the symbol 'Y' and has often been classified as a 'rare-earth element'."
        answer_image = '96_Yttrium.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'World Leaders' category
    elif the_word == 'TOJO':
        hint = "Was the general of the Imperial Japanese Army during World War 2."
        answer_image = '97_Tojo.gif'
    elif the_word == 'STALIN':
        hint = "He ruled the Soviet Union from the mid 1920's until his death, including during World War 2."
        answer_image = '98_Stalin.gif'
    elif the_word == 'TRUDEAU':
        hint = "Is the 23rd and current Prime Minister of Canada."
        answer_image = '99_Trudeau.gif'
    elif the_word == 'MACRON':
        hint = "Has served as the President of France since 2017."
        answer_image = '100_Macron.gif'
    elif the_word == 'LINCOLN':
        hint = "Was the 16th President of the United States and led the nation during the American Civil War."
        answer_image = '101_Lincoln.gif'
    elif the_word == 'DIEFENBAKER':
        hint = "Was the 13th Prime Minister of Canada, serving from June 21, 1957 to April 22, 1963."
        answer_image = '102_Diefenbaker.gif'
    elif the_word == 'WASHINGTON':
        hint = "One of the Founding Fathers of the United States and served as their first President."
        answer_image = '103_Washington.gif'
    elif the_word == 'MERKEL':
        hint = "Chancellor of Germany since 2005."
        answer_image = '104_Merkel.gif'
    elif the_word == 'TRUMP':
        hint = "Is the 45th and current President of the United States."
        answer_image = '105_Trump.gif'
    elif the_word == 'ERDOGAN':
        hint = "Current President of Turkey since 2014."
        answer_image = '106_Erdogan.gif'
    elif the_word == 'PUTIN':
        hint = "Current President of Russia since 2012."
        answer_image = '107_Putin.gif'
    elif the_word == 'OBAMA':
        hint = "First African-American to serve as President of the United States, from 2009 to 2017."
        answer_image = '108_Obama.gif'
    elif the_word == 'MACDONALD':
        hint = "Was the first Prime Minister of Canada and a dominant figure in Canadian Confederation."
        answer_image = '109_Macdonald.gif'
    elif the_word == 'JINPING':
        hint = "President and 'core leader' of the People's Republic of China."
        answer_image = '110_Jinping.gif'
    elif the_word == 'ABE':
        hint = "Current President of Japan since 2012."
        answer_image = '111_Abe.gif'
    elif the_word == 'MATTARELLA':
        hint = "Current President of Italy since 2015."
        answer_image = '112_Mattarella.gif'
    elif the_word == 'FRANCIS':
        hint = "Current Head of the Catholic Church and Sovereign of the Vatican City."
        answer_image = '113_Francis.gif'
    elif the_word == 'TRUMAN':
        hint = "Served as the 33rd President of the United States following the death of Franklin D. Roosevelt."
        answer_image = '114_Truman.gif'
    elif the_word == 'EISENHOWER':
        hint = "Served as the 34th President of the United States, following his achievements as a five-star general of the United States Army."
        answer_image = '115_Eisenhower.gif'
    elif the_word == 'CAMPBELL':
        hint = "First and only female Prime Minister of Canada."
        answer_image = '116_Campbell.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Movies' category.
    elif the_word == 'GREASE':
        hint = "Released in 1978, this musical romantic comedy stars John Travolta an Olivia Newton-John."
        answer_image = '117_Grease.gif'
    elif the_word == 'HELLBOY':
        hint = "This 2004 fantasy/action film stars Ron Perlman in the title role."
        answer_image = '118_Hellboy.gif'
    elif the_word == 'CONJURING':
        hint = "Released in 2013, this supernatural horror film is directed by James Wan and depicts a family haunted by demons."
        answer_image = '119_Conjuring.gif'
    elif the_word == 'SAW':
        hint = "Released in 2004, this psychological horror film tells the story of two men trapped in a sadistic game hosted by the 'Jigsaw' killer."
        answer_image = '120_Saw.gif'
    elif the_word == 'INSOMNIA':
        hint = "This 2002 movie is directed by Christopher Nolan and stars Al Pacino as a damaged detective in Alaska."
        answer_image = '121_Insomnia.gif'
    elif the_word == 'MEMENTO':
        hint = "This 2000 movie is directed by Christopher Nolan and depicts a man who is unable to recall the past fifteen minutes of his life."
        answer_image = '122_Memento.gif'
    elif the_word == 'DUNKIRK':
        hint = "This 2017 movie is directed by Christopher Nolan and recalls the events that took place as over 330000 Allied troop were safely rescued from Germany's trap."
        answer_image = '123_Dunkirk.gif'
    elif the_word == 'JAWS':
        hint = "Released in 1975, this horror film directed by Steven Spielberg spawned a generation of people who were too afraid to go to the beach."
        answer_image = '124_Jaws.gif'
    elif the_word == 'FACEOFF':
        hint = "This 1997 film sees Nicolas Cage and John Travolta battle it out with tons of face-swapping."
        answer_image = '125_Faceoff.gif'
    elif the_word == 'MATRIX':
        hint = "A modern sci-fi classic, this 1999 film from the Wachowski's stars Keanu Reeves and Laurence Fishburne."
        answer_image = '126_Matrix.gif'
    elif the_word == 'GODFATHER':
        hint = "Often regarded as the greatest film in history, this 1972 film stars Marlon Brando as the ultimate family man."
        answer_image = '127_Godfather.gif'
    elif the_word == 'MONEYBALL':
        hint = "This 2011 film stars Brad Pitt as Bill Beane who revolutionised the game of baseball with this unconventional idealisms."
        answer_image = '128_Moneyball.gif'
    elif the_word == 'AVENGERS':
        hint = "This 2012 blockbuster was the first culmination of the Marvel Cinematic Universe's famed heroes."
        answer_image = '129_Avengers.gif'
    elif the_word == 'ALIEN':
        hint = "The prefect combination of sci-fi and horror, this 1979 film from Ridley Scott depicts a space crew hunted by an unknown yet terrifying specimen."
        answer_image = '130_Alien.gif'
    elif the_word == 'UP':
        hint = "This heartwarming film from Pixar was released in 2009 and became only the second animated film to be nominated for Best Picture at the Oscars."
        answer_image = '131_Up.gif'
    elif the_word == 'PADDINGTON':
        hint = "This heartwarming 2015 film depicts a young bear who travels to England to find a new home."
        answer_image = '132_Paddington.gif'
    elif the_word == 'GRAVITY':
        hint = "This 2013 thriller stars Sandra Bullock as Dr. Ryan Stone, an astronaut stuck in in isolation in space."
        answer_image = '133_Gravity.gif'
    elif the_word == 'TITANIC':
        hint = "This 1997 romantic tragedy became highest grossing film of all time and the first to record 1 BILLION dollars at the global box office."
        answer_image = '134_Titanic.gif'
    elif the_word == 'MARTIAN':
        hint = "This 2015 film is directed by Ridley Scott and stars Matt Damon as an astronaut stranded on Mars."
        answer_image = '135_Martian.gif'
    elif the_word == 'CASABLANCA':
        hint = "This 1942 classic stars Humphrey Bogart and Ingrid Bergman."
        answer_image = '136_Casablanca.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Musicians' category.
    elif the_word == 'EMINEM':
        hint = "The best selling artist of the 2000s, this American rapper made a name for himself from his movie '8 Mile'."
        answer_image = '137_Eminem.gif'
    elif the_word == 'DRAKE':
        hint = "The best selling rapper of the 2010s, this Canadian rapper had produced critically-acclaimed albums such as 'Take Care' and 'Nothing Was the Same'."
        answer_image = '138_Drake.gif'
    elif the_word == 'LORDE':
        hint = "This New Zealand singer broke out after releasing hits such as 'Royals' and 'Team'."
        answer_image = '139_Lorde.gif'
    elif the_word == 'SKRILLEX':
        hint = "One of the most notable electronic artists currently, this artist is known for his explosive 2012 hit 'Bangarang'."
        answer_image = '140_Skrillex.gif'
    elif the_word == 'NAS':
        hint = "Highly regarded as the greatest lyricist in rap history, this American rapper is known for his instant classic 'Illmatic'."
        answer_image = '141_Nas.gif'
    elif the_word == 'MADONNA':
        hint = "'Vogue' and 'Like a Prayer' are some of this American artist's most popular songs."
        answer_image = '142_Madonna.gif'
    elif the_word == 'BEATLES':
        hint = "This British rock band are the best-selling musical artist/band of all time worldwide."
        answer_image = '143_Beatles.gif'
    elif the_word == 'RIHANNA':
        hint = "This Barbadian singer-songwriter won the Grammy Award for Best Urban Contemporary Album for her 2012 hit 'Unapologetic'."
        answer_image = '144_Rihanna.gif'
    elif the_word == 'COLDPLAY':
        hint = "This British rock band is lead by Chris Martin and has produced albums such as 'A Head Full of Dreams; and 'Parachutes'."
        answer_image = '145_Coldplay.gif'
    elif the_word == 'NIRVANA':
        hint = "Lead by Kurt Cobain, this American rock band was known for their 1991 hit 'Smells Like Teen Spirit'."
        answer_image = '146_Nirvana.gif'
    elif the_word == 'BEYONCE':
        hint = "This is American singer is known for her single 'Single Ladies' and is married to American rapper 'Jay-Z'."
        answer_image = '147_Beyonce.gif'
    elif the_word == 'SINATRA':
        hint = "One of the most popular and influential musical artists of the 20th century, this artist not only made classic songs such as 'My Way', but was also successful as an actor."
        answer_image = '148_Sinatra.gif'
    elif the_word == 'ELVIS':
        hint = "The King of Rock and Roll."
        answer_image = '149_Elvis.gif'
    elif the_word == 'PRINCE':
        hint = "This late American singer-songwriter was known for iconic songs such as 'Raspberry Beret' and 'Little Red Corvette'."
        answer_image = '150_Prince.gif'
    elif the_word == 'BEETHOVEN':
        hint = "A German composer who was crucial for classical music in the 18th and 19th century."
        answer_image = '151_Beethoven.gif'
    elif the_word == 'CHER':
        hint = "The Goddess of Pop."
        answer_image = '152_Cher.gif'
    elif the_word == 'BONO':
        hint = "Irish singer-songwriter known for the frontman for U2."
        answer_image = '153_Bono.gif'
    elif the_word == 'BJORK':
        hint = "Icelandic singer know for her work in the fields of electronic, pop, experimental, classical, trip hop, IDM, and avant-garde music."
        answer_image = '154_Bjork.gif'
    elif the_word == 'QUEEN':
        hint = "Highly successful British rock band, lead by iconic frontman Freddie Mercury."
        answer_image = '155_Queen.gif'
    elif the_word == 'MOZART':
        hint = "A musical prodigy who was born in Austria and became one of the most successful composers in history."
        answer_image = '156_Mozart.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Sports Stars' category.
    elif the_word == 'WESTBROOK':
        hint = "Current #0 for Oklahoma City Thunder and 2017 NBA MVP."
        answer_image = '157_Westbrook.gif'
    elif the_word == 'RONALDO':
        hint = "Current footballer (soccer) and top goalscorer for Spanish team Real Madrid and the Portugal national team."
        answer_image = '158_Ronaldo.gif'
    elif the_word == 'MESSI':
        hint = "Current footballer (soccer) and top goalscorer for Spanish team FC Barcelona and the Argentina national team."
        answer_image = '159_Messi.gif'
    elif the_word == 'NEYMAR':
        hint = "Current Brazilian footballer (soccer) known for his flair and skill, currently playing for French team Paris Saint German."
        answer_image = '160_Neymar.gif'
    elif the_word == 'NADAL':
        hint = "Spanish tennis player, currently ranked Number 2 in the world among men, and holds the record for the most titles won at a single tournament by a male player ."
        answer_image = '161_Nadal.gif'
    elif the_word == 'MAYWEATHER':
        hint = "American boxer who has won championships across five weight divisions, the first being super featherweight in 1998."
        answer_image = '162_Mayweather.gif'
    elif the_word == 'MCGREGOR':
        hint = "Irish mixed martial artist whose first boxing match was against American boxer Floyd Mayweather."
        answer_image = '163_Mcgregor.gif'
    elif the_word == 'BOLT':
        hint = "Former sprinter and Olympic athlete who holds the record in the 100-metre race."
        answer_image = '164_Bolt.gif'
    elif the_word == 'JORDAN':
        hint = "Former basketball player known for his 15-year playing career for the Chicago Bulls of the NBA, and often considered the greatest of the game."
        answer_image = '165_Jordan.gif'
    elif the_word == 'HARDEN':
        hint = "Current #13 for Houston Rockets and 2018 NBA MVP."
        answer_image = '166_Harden.gif'
    elif the_word == 'FEDERER':
        hint = "Swiss tennis player, currently ranked Number 3 in the world among men."
        answer_image = '167_Federer.gif'
    elif the_word == 'DJOKOVIC':
        hint = "Serbian tennis player, currently ranked Number 1 in the world among men."
        answer_image = '168_Djokovic.gif'
    elif the_word == 'SHARAPOVA':
        hint = "Russian tennis player who was ranked Number 1 in the world among women on five separate occasions."
        answer_image = '169_Sharapova.gif'
    elif the_word == 'IBRAHIMOVIC':
        hint = "Current footballer (soccer) playing for MLS club LA Galaxy and top goalscorer for the Sweden national team."
        answer_image = '170_Ibrahimovic.gif'
    elif the_word == 'DONCIC':
        hint = "Current Rookie basketball player in the NBA, playing for the Dallas Mavericks and Slovenian national team."
        answer_image = '171_Doncic.gif'
    elif the_word == 'BAUTISTA':
        hint = "Dominican professional baseball player, well-known for his bat flip."
        answer_image = '172_Bautista.gif'
    elif the_word == 'ANTETOKOUNMPO':
        hint = "Current basketball player in the NBA for the Milwaukee Bucks, nicknamed 'The Greek Freak'."
        answer_image = '173_Giannis.gif'
    elif the_word == 'ROUSEY':
        hint = "Current American professional wrestler, and current champion of the RAW Women's Championship."
        answer_image = '174_Rousey.gif'
    elif the_word == 'WAMBACH':
        hint = "American retired soccer player, who holds the record for most international goals scored among women's association football players."
        answer_image = '175_Wambach.gif'
    elif the_word == 'SINCLAIR':
        hint = "Canadian soccer player, who holds the record for the second-mots international goals scored among women's association football players."
        answer_image = '176_Sinclair.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Superheroes' category.
    elif the_word == 'BATMAN':
        hint = "AKA Bruce Wayne, the Dark Knight."
        answer_image = '177_Batman.gif'
    elif the_word == 'SUPERMAN':
        hint = "AKA Clark Kent, the Man of Steel."
        answer_image = '178_Superman.gif'
    elif the_word == 'FLASH':
        hint = "After Barry Allen was involved in freak accident in his lab, he became this speedster superhero."
        answer_image = '179_Flash.gif'
    elif the_word == 'CYBORG':
        hint = "The half-human, half-robot member of DC's Teen Titans."
        answer_image = '180_Cyborg.gif'
    elif the_word == 'WOLVERINE':
        hint = "A Canadian mutant whose abilities allow him to regenerate and pierce his enemies with his powerful claws."
        answer_image = '181_Wolverine.gif'
    elif the_word == 'ROBIN':
        hint = "Batman's loyal sidekick, a role that has been occupied by several people including Dick Grayson and Tim Drake."
        answer_image = '182_Robin.gif'
    elif the_word == 'RAVEN':
        hint = "The daughter of Trigon, this celestial superhero is a prominent member of DC's Teen Titans."
        answer_image = '183_Raven.gif'
    elif the_word == 'IRONMAN':
        hint = "AKA Tony Stark, the genius-billionaire-playboy-philanthropist himself."
        answer_image = '184_Ironman.gif'
    elif the_word == 'SPIDERMAN':
        hint = "Just a normal teen from Queens, until he was bitten by a spider and used the power and responsibility that come from it for good."
        answer_image = '185_Spiderman.gif'
    elif the_word == 'HUNTRESS':
        hint = "A member of DC's Birds of Prey, she is a skilled fighter and great with crossbows."
        answer_image = '186_Huntress.gif'
    elif the_word == 'DAREDEVIL':
        hint = "Blinded at a young age only enhanced his other senses, which allowed him to keep Hell's Kitchen a safe place."
        answer_image = '187_Daredevil.gif'
    elif the_word == 'HAWKEYE':
        hint = "A masterful archer and a part of Marvel's Avengers."
        answer_image = '188_Hawkeye.gif'
    elif the_word == 'ELEKTRA':
        hint = "She is a skillful fighter in Marvel's lineup, equipped with a pair of Sai."
        answer_image = '189_Elektra.gif'
    elif the_word == 'QUICKSILVER':
        hint = "AKA Pietro Maximoff, the speedster son of the supervillain Magneto."
        answer_image = '190_Quicksilver.gif'
    elif the_word == 'DEADPOOL':
        hint = "More of anti-hero, but always willing to crack a few jokes and break the fourth wall."
        answer_image = '191_Deadpool.gif'
    elif the_word == 'AQUAMAN':
        hint = "AKA Arthur Curry, the King of Atlantis and a member of DC's Justice League."
        answer_image = '192_Aquaman.gif'
    elif the_word == 'SHAZAM':
        hint = "AKA Billy Baxton, a teenager who can transform into this mighty superhero simply by saying its name."
        answer_image = '193_Shazam.gif'
    elif the_word == 'NIGHTWING':
        hint = "AKA Dick Grayson, the first Robin, who eventually decided to take on this new role and protect the fictional city of Bludhaven."
        answer_image = '194_Nightwing.gif'
    elif the_word == 'SUPERGIRL':
        hint = "AKA Kara Zor-El, cousin of Superman, and played by American actress Melissa Benoist in the television series of the same name."
        answer_image = '195_Supergirl.gif'
    elif the_word == 'VISION':
        hint = "An android created by Tony Stark, and powerful member of Marvel's Avengers."
        answer_image = '196_Vision.gif'
        
    # The following are hints that are given according to what word is picked by the computer from the 'Video Game Characters' category.
    elif the_word == 'STARFOX':
        hint = "The mammalian protagonist of Ubisoft's space adventure games of the same name."
        answer_image = '197_Starfox.gif'
    elif the_word == 'MARIO':
        hint = "An Italian plumber, he is one of the most popular video game characters ever created."
        answer_image = '198_Mario.gif'
    elif the_word == 'KRATOS':
        hint = "The main protagonist of the God of War series, who has slain Gods such as Zeus and Apollo."
        answer_image = '199_Kratos.gif'
    elif the_word == 'LINK':
        hint = "The main protagonist of the Legend of Zelda series."
        answer_image = '200_Link.gif'
    elif the_word == 'LUIGI':
        hint = "Another Italian plumber, but who isn't as popular as his brother."
        answer_image = '201_Luigi.gif'
    elif the_word == 'PIKACHU':
        hint = "Equipped with the power of lightning, this adorable yet powerful creature has aided Ash Ketchum throughout his entire adventure."
        answer_image = '202_Pikachu.gif'
    elif the_word == 'MARTH':
        hint = "The protagonist of Nintendo's first and third 'Fire Emblem' games, this character is well-known for his role in the Super Smash Bros. games."
        answer_image = '203_Marth.gif'
    elif the_word == 'EEVEE':
        hint = "A mammalian Pokémon known for its ability to evolve into one of eight different forms, including Jolteon and Glaceon."
        answer_image = '204_Eevee.gif'
    elif the_word == 'SPYRO':
        hint = "A young purple dragon, he is the protagonist of several games under this series of the same name."
        answer_image = '205_Spyro.gif'
    elif the_word == 'SNAKE':
        hint = "A skilled and stealthy fighter who is the protagonist of Konami's 'Metal Gear Solid' series."
        answer_image = '206_Snake.gif'
    elif the_word == 'PEACH':
        hint = "A damsel in distress who needs to be saved from the powerful Bowser."
        answer_image = '207_Peach.gif'
    elif the_word == 'SAMUS':
        hint = "The main protagonist of the Metroid series."
        answer_image = '208_Samus.gif'
    elif the_word == 'BOWSER':
        hint = "The main antagonist of the Super Mario Bros. series who is constantly kidnapping Mario's lover, Peach."
        answer_image = '209_Bowser.gif'
    elif the_word == 'SONIC':
        hint = "A blue and speedy hedgehog who is the protagonist of several games under the series of the same name."
        answer_image = '210_Sonic.gif'
    elif the_word == 'MEGAMAN':
        hint = "The title character and main protagonist that resembles a blue Rocket man, who has also appeared in the Super Smash Bros. games."
        answer_image = '211_Megaman.gif'
    elif the_word == 'KIRBY':
        hint = "A puffy pink creature that is the title character and has the ability to suck his opponents into himself."
        answer_image = '212_Kirby.gif'
    elif the_word == 'CONKER':
        hint = "An anthropomorphic squirrel who first appeared alongside Donkey Kong, but received his own very mature spin-off game."
        answer_image = '213_Conker.gif'
    elif the_word == 'KNUCKLES':
        hint = "The red hedgehog that often fights alongside Sonic in his adventures."
        answer_image = '214_Knuckles.gif'
    elif the_word == 'TOAD':
        hint = "The mushroom protagonist of the Super Mario Bros. games that guides Mario along his quest to save Peach."
        answer_image = '215_Toad.gif'
    elif the_word == 'EZIO':
        hint = "The main character of Assassin's Creed II and the most recognizable assassin in the series."
        answer_image = '216_Ezio.gif'

    # The following are hints that are given according to what word is picked by the computer from the 'Professions' category.
    elif the_word == 'NEUROLOGIST':
        hint = "A medical professional who is licensed to treat and diagnose patients with respect to the nervous system and its organs, including the brain and spinal cord."
        answer_image = '217_Neurologist.gif'
    elif the_word == 'TEACHER':
        hint = "Commonly found in schools, this is a person who licensed to aid others in acquiring knowledge of a certain subject area."
        answer_image = '218_Teacher.gif'
    elif the_word == 'CHIROPRACTOR':
        hint = "A medical professional who is treats others through massage therapy and orthotics."
        answer_image = '219_Chiropractor.gif'
    elif the_word == 'CARPENTER':
        hint = "A person who possesses the skilled trade including the cutting and installing of building materials, primarily for housing."
        answer_image = '220_Carpenter.gif'
    elif the_word == 'MUSICIAN':
        hint = "A person who performs songs and/or plays instruments for entertainment purposes."
        answer_image = '221_Musician.gif'
    elif the_word == 'PHYSICIST':
        hint = "A scientist who specializes in the field of science that includes terms such as matter, energy, and space."
        answer_image = '222_Physicist.gif'
    elif the_word == 'ENGINEER':
        hint = "Professionals who specialize in designing, inventing, and analyzing technology or infrastructures."
        answer_image = '223_Engineer.gif'
    elif the_word == 'CHEF':
        hint = "A professional who cooks food and is knowledgeable in all aspects of food preparation."
        answer_image = '224_Chef.gif'
    elif the_word == 'ZOOLOGIST':
        hint = "Professionals who study the branch of biology that deal with the studies of animal kingdoms."
        answer_image = '225_Zoologist.gif'
    elif the_word == 'ELECTRICIAN':
        hint = "A professional with the skilled trade of electrical wiring, especially those that are found in buildings."
        answer_image = '226_Electrician.gif'
    elif the_word == 'EXTERMINATOR':
        hint = "Licensed professionals who regulate/eliminate the population of pests."
        answer_image = '227_Exterminator.gif'
    elif the_word == 'DENTIST':
        hint = "TA licensed medical professional who specializes in the treatment of human teeth."
        answer_image = '228_Dentist.gif'
    elif the_word == 'PHOTOGRAPHER':
        hint = "A professional who creates images through cameras or other recording devices."
        answer_image = '229_Photographer.gif'
    elif the_word == 'DIRECTOR':
        hint = "The professional in the production crew that is tasked with working with both screenwriters and actors to construct the film or television show."
        answer_image = '230_Director.gif'
    elif the_word == 'ACTOR':
        hint = "The professional in the production crew of a film or television show that is tasked with practising and performing a script that is proved for them."
        answer_image = '231_Actor.gif'
    elif the_word == 'VETERINARIAN':
        hint = "A medical professional who treats animals, mainly household pets."
        answer_image = '232_Vet.gif'
    elif the_word == 'ENTREPRENEUR':
        hint = "An individual who aspires to start their own business."
        answer_image = '233_Entrep.gif'
    elif the_word == 'ATTORNEY':
        hint = "A professional that practises law and civil rights."
        answer_image = '234_Attorney.gif'
    elif the_word == 'PILOT':
        hint = "a professional who navigates an aircraft."
        answer_image = '235_Pilot.gif'
    elif the_word == 'DETECTIVE':
        hint = "A member of law enforcement that collect information and evidence to solve a case.."
        answer_image = '236_Detective.gif'
    return hint, answer_image

# The following function will analyze each selection from the user.
# The values of variables 'the_word', 'user_options' are passed into the function.
def guess_indicator(the_word, user_options):
    correct = True#variable correct is equal to Boolean True, this variable will change according to the conditional statements below
    if (user_options in the_word):#if user_options is in the word 
        correct = True#correct is equal to boolean True
    elif (user_options not in the_word):#else if user_options is not in the word
        correct = False#correct is equal to boolean False
    return correct#return the boolean value of variable correct to the function

def guess_word(the_word,wrong,word_image):#define guess_word as a function and pass in the values of variable the_word,wrong, and word_image, this function allows the user to guess an entire word and check if they got the word right or wrong
    beta = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']# The choices the user is presented with (the alphabet). Defined by 'beta'.
    backspace = [' <--- ']#backspace is equal to an array, inside the array is a symbol for backspace
    beta1 = beta + backspace#beta1 is equal to the array of beta and backspace combined
    joined_word = ''.join(the_word)#joins the word to make a single word with no spaces
    while True:#Creates a while True loop that runs as long as the above conditional statement evaluates as True, because the statements above will always be true the While True loop will run indefinitely, unless something within the loop breaks
        seq1 = [letters['1'] for r in range(len(the_word))]# The number of blank boxes (letters['1']) will be displayed based on the number of letters in the word. Defined by 'seq1'.
        i = 0#variable i is equal to 0
        while i < (len(the_word)):#while variable i is less than the total length (len takes the word value and returns the length of the word value as an integer) of variable the_word run the following code
            user_options1 = buttonbox("Please guess the word:", images=seq1, choices = beta1)#displays a window prompting the user to make a choice, displays the image with the name seq1 and clickable choice boxes filled with the items in array beta1 
            if user_options1 == ' <--- ' and (i > 0):#if user_options is equal to '<---' and the length of variable i is greater than 0 run the following code
                seq1[i-1] = letters['1']#if the user click '<---' override the past sequence and replace it with the value that key '1' holds in dictionary letters, in this case the value is a blank letter, so the previous values is replaced with a blank letter 
                i = i - 1#variable i is equal to i - 1
            elif user_options1 != ' <--- ':#else if user_options is not equal to '<---' run the following code
                seq1[i] = letters[user_options1]#if user does not click '<---' continue to add in letters based on what the user clicks, this is done by searching in the dictionary called letters and finding the keys when a letter is clicked and replacing the blank letters with the values of the keys
                i = i + 1#variable i is equal to i + 1
        correct = True#variable correct is equal to a boolean of True 
        for g in range (len(the_word)):#creates a for loop to run to the total length (len takes the word value and returns the length of the word value as an integer) of variable the_word 
            if seq1[g] != letters[the_word[g]]:
                correct = False#variable correct is equal to a boolean of False
                break#break the while True loop
        if correct == False:#if correct is equal to boolean False run the following code
            wrong = wrong + 1#variable wrong is equal to wrong + 1
            msgbox("WRONG!", image= hangman[wrong])#displays and image informing the user they have guessed wrong and displays an image of the hangman and corresponding to how many wrong points they have accumulated 
            break#break the while True loop
        elif correct == True:#else if correct is equal to boolean True run the following code
            msgbox ("THAT'S RIGHT!! The word was...")#displays a window informing the user they have gotten the word correct and will be directed to the screen of the word 
            msgbox (joined_word, image = word_image)#displays the joined_word and the image of the word that was chosen
            msgbox ("CONGRATS! The hangman survives. You won!", image= hangman_lives)#displays a window informing the user they have won the game and displays the image of a hangman alive

        break#break the while True loop

    return correct#return the boolean value of variable correct to the function 

while True:#Creates a while True loop that runs as long as the above conditional statement evaluates as True, because the statements above will always be true the While True loop will run indefinitely, unless something within the loop breaks
    user_choice = buttonbox ("Press 'Let's Start' to use this program. To quit, press 'Quit'.", choices = ["Let's Start", 'Quit'], image = start_game_pic)
    # The user is prompted to press the ENTER key to begin.
    # If the user types 'quit' here, the program will stop.

    if user_choice == "Let's Start": # The user has chosen to begin the game.
    
        continue1 = msgbox("\nWelcome to Tanveer's and Rai's HANGMAN!", image = intro_image) # The user is introduced to the game and the intro image is displayed.
        continue2 = msgbox("\nThe game is simple enough, just don't let ol' Jimmy here die!", image = hangman_image) # The user is introduced to the hangman and is told the main purpose of the game.
        continue3 = msgbox("\nFor each turn, you will be assigned to complete a word using the letters provided for you, based on the category of your choice.", image = hangman_image) # More information is provided to the user.
        start_options = buttonbox("What would you like to do?",
                                            choices = ["Start", "Help", "Quit"], # The user is prompted to press either the "Start", "Help", or "Quit" buttons, their choice is defined by 'start_options'.
                                            image = intro_image) # The introduction image is displayed.
        while start_options == "Help": # The following code will run if the user presses the 'Help' button.
            msgbox("To start, simply press the start button.", image = help_pic_1) # This picture image shows the window where the user decides one of three previous starting choices with a red circle around the 'Start' button to show how to start.
            msgbox("Then you will be presented with a category to choose from. Each contains 17-20 words associated with that topic, one of which will be randomly selected for you to guess.", image = help_pic_2) # This picture shows the categories available and how to choose.
            msgbox("You will then be presented with each letter from the alphabet to choose, or a 'HINT' feature.", image = help_pic_3) # This image shows all the choices available, including the letters and the three features. the 'HINT' feature is circled.
            msgbox("If you press the hint button, you will be presented with a clue as to what the word may be. Although this can only be pressed once, the hint will be displayed in the IDLE panel for the whole game.", image = help_pic_4) # This image shows a window that will display the image.
            msgbox("Another help feature is the 'PICTURE' button, which can only be pressed once.", image = help_pic_picture_1) # This image shows the 'PICTURE' button circled.
            msgbox("If you press the 'PICTURE' button, you will be presented with a picture associated with the word.", image = help_pic_picture_2) # This image shows a window that will display the image for that picture. 
            msgbox("If you select a letter that is correct, this will pop up indicating that said letter is in the word.", image = help_pic_5) # This image shows a window with a happy hangman that indicates that the user has selected the correct letter.
            msgbox("If you select a letter that is incorrect, this will pop up indicating that said letter is not in the word and that a new limb will be drawn to the hangman.", image = help_pic_6) # This image shows a window with a limb attached to the hangman that indicates that the user has not selected the correct letter.
            msgbox("Another feature is the 'GUESS THE WORD', where you are allowed to guess the word directly.", image = help_pic_guessword_1) # The user is informed about the 'GUESS THE WORD' feature.
            msgbox("You will be taken to this page, where you must successively pick letters to construct the word. You may also press the backspace button if you select a letter by mistake. If the wrong word is constructed, a limb will be attached.", image = help_pic_guessword_2) # The user is told how to pick a word. # This i
            msgbox("Continue guessing at letters until the game is complete.", image = help_pic_7) # This image shows the game being played.
            msgbox("When the game is complete, you will be presented with word.", image = help_pic_8) # This image shows a window that displays the word and its picture once the game is complete
            msgbox("If you correctly guess the word, the hangman survives and you have won.", image = help_pic_9) # This picture displays the hangman of the rope, indicating that he has survived and the user has won.
            msgbox("If you cannot guess the word, the hangman has died and you have lost because all 6 limbs have been drawn.", image = help_pic_10) # This picture displays the hangman of the rope, indicating that he has survived and the user has lost.
            msgbox("You will then be presented with the options to either choose 'Continue' to play again, or 'Quit' to quit the game", image = help_pic_11, ok_button = "Alright, let's start!") # An image displaying the two beginning choice is displayed.
            start_options = buttonbox("What would you like to do?",
                                            choices = ["Start", "Help", "Quit"],
                                            image = intro_image) # The user is prompted again to press either the "Start", "Help", or "Quit" buttons.
        if start_options == 'Quit':
            exit() # If the user presses quit, the program ends.
        elif start_options == 'Start':
            categ_choice = cateory_choice() # The return for the 'cateory_choice()' is defined by 'categ_choice'.
            the_word = word_selection(categ_choice) # The return for the 'word_selection(cateory_choice)' is defined by 'the_word'.
            hints = hint__pic_choice(the_word)[0] # The first return for the 'hint__pic_choice(the_word)' function is defined by 'hints'.
            word_image = hint__pic_choice(the_word)[1] # The second return for the 'hint__pic_choice(the_word)' function is defined by 'word_image'.
            wrong = 0 # Prior to starting the selection process, the number of wrong guesses is 0. Define by 'wrong'.
            the_word = list(the_word) # The word (the_word) is split into letters which are inputted into a list.
            joined_word = ''.join(the_word) # The original word is preserved by joining the letters of 'the_word'. Defined by 'joined_word'.
            seq = [letters['1'] for r in range(len(the_word))] # The number of blank boxes (letters['1']) will be displayed based on the number of letters in the word. Defined by 'seq'.
            guessed_letters = []
            # The following are the choices the user is presented, including the alphabet, hint, picture, and 'guess the word'. Defined by 'alpha'.
            alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HINT', 'PICTURE', 'CLICK HERE TO GUESS THE WORD']

            while True:#Creates a while True loop that runs as long as the above conditional statement evaluates as True, because the statements above will always be true the While True loop will run indefinitely, unless something within the loop breaks
                user_options = buttonbox("What is your choice? PLEASE DO NOT CLICK ON THE BOXES!",image=seq, choices = alpha)#displays a window prompting the user to make a choice, displays the image with the name seq and clickable choice boxes filled with the items in array alpha
                if user_options == 'HINT': # The following code will run of the user presses the 'HINT' button.
                    msgbox (hints, image= hint_feature) # The window will display the word's unique hint and the hint image.
                    alpha.remove(str(user_options))#.remove() is a builtin function of python which removes a given value, in this case this line strings each value then removes the value that the user has clicked (or picked)
                    print ("HINT:", hints) # The IDLE will display the word's unique hint.
                elif user_options == 'PICTURE': # The following code will run of the user presses the 'PICTURE' button.
                    msgbox ("PICTURE:", image = word_image) # The window will display the word's image.
                    alpha.remove(str(user_options))#.remove() is a builtin function of python which removes a given value, in this case this line strings each value then removes the value that the user has clicked (or picked)
                elif user_options == 'CLICK HERE TO GUESS THE WORD':#else if user_options is equal to 'CLICK HERE TO GUESS THE WORD' run the following code
                    correct = guess_word(the_word,wrong,word_image)#variable correct is equal to the function guess_word, runs the function
                    alpha.remove(str(user_options))#.remove() is a builtin function of python which removes a given value, in this case this line strings each value then removes the value that the user has clicked (or picked)
                    if correct == True:#if variable correct is equal to True run the following code
                        break#break the while True loop
                    else:#else if the above conditional statements are false run the following code
                        wrong = wrong + 1#variable wrong is equal to wrong + 1

                if user_options != 'HINT' and user_options != 'PICTURE' and user_options != 'CLICK HERE TO GUESS THE WORD' and user_options not in alpha: # If the user's decision is not in the 'alpha' array, the following code will run.
                    msgbox("PLEASE SELECT A VALID OPTION. DON'T CLICK ON THE BOXES.") # If the user decides to click on the boxes rather than the word, they are not allowed to do so.

                elif user_options != 'HINT' and user_options != 'PICTURE' and user_options != 'CLICK HERE TO GUESS THE WORD': # The following code will run if the user's choice is not 'HINT' or 'PICTURE' or 'GUESS THE WORD'.            
                    guessed_letters.append(str(user_options))
                    print ('Here are the letters you have picked so far:', guessed_letters)
                    alpha.remove(str(user_options))#.remove() is a builtin function of python which removes a given value, in this case this line strings each value then removes the value that the user has clicked (or picked)
                    correct = guess_indicator(the_word, user_options) # The return for the 'guess_indicator(the_word, user_options)' function is defined with 'correct' .
                    if correct == True: # If the user's letter choice is in the word, the following code will be run.
                        msgbox ("Correct", image = correct_image) # The user is informed that their choice is correct, and the appropriate picture will be displayed in a window.
                        for t in range (len(the_word)):#creates a for loop to run to the total length (len takes the word value and returns the length of the word value as an integer) of variable the_word 
                            if user_options == the_word[t]:#if user_options is equal to the_word and all the assigned numbers of length t, run the following code 
                                seq[t] = letters[user_options] # If the user's choice is in the word, all the blank boxes (t) will be replaced with this letter's box in all of its instances in the word.
                        if seq.count(str(letters['1'])) == 0: # If the number of blank boxes (letters['1']) reaches 0, before all the limbs have been draw, the user has correctly guessed all the letters.
                            msgbox ("THAT'S RIGHT!! The word was...")# displays a msgbox in a window informing the user they have guessed correctly and the program will direct them to a new window informing them of the word they have guessed
                            msgbox (joined_word, image = word_image) # The user is informed that they have correctly guessed the word, and are presented with both the word (joined_word) and the word's image (word_image).
                            msgbox ("CONGRATS! The hangman survives. You won!", image= hangman_lives) # The user is informed that they have won and are the winning image is printed in the window.
                            break # The while loop will break now.
                    else: # If the user's letter choice is not in the word, the following code will be run.
                       wrong = wrong + 1 # The number of wrong guesses increases by 1.
                       msgbox("WRONG!", image= hangman[wrong]) # The user is informed that they have chosen wrong, and the appropriate hangman image is displayed based on indexing the 'hangman' dictionary with the value of 'wrong'.

                if wrong == 6: # If the number of wrong guesses reaches 6, this means that all have limbs have been attached and the hangman has died.
                    msgbox ("THAT'S WRONG!! The word was...")# displays a msgbox in a window informing the user they used all of their guesses and the program will tell them what the word is
                    msgbox (joined_word, image = word_image) # The user is informed that they not have correctly guessed the word, and are presented with both the word (joined_word) and the word's image (word_image).
                    msgbox ("The hangman has died. You lost...Well done.", image= hangman_dead) # The user is informed that they have lost and are the dead image is printed in the window.
                    break # The 'while loop will now  break'.
            
    elif user_choice == "Quit": #else if user_choice is equal to "Quit" run the following code or they press the 'X' button. 
        exit() # If the user presses the 'Quit' or 'X' button, they will be prompted to end the program.
