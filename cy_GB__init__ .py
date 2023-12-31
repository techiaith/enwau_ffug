from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}-{{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
    )

    formats_male = (
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}-{{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
    )

    formats = formats_female + formats_male

    # Names based on UK-wide statistics from
    # http://webarchive.nationalarchives.gov.uk/20160105160709/http://ons.gov.uk/ons/publications/re-reference-tables.html?edition=tcm%3A77-243767
    #
    # adapted by Bangor University's Language Technologies Unit based on frequency lists and
    # corpus-based statistical rankings of personal names found in Welsh-language texts
    # developed for its Cysill spelling and grammar checker https://www.cysgliad.com/cysill/arlein/

    first_names_male = (
        "David",
        "Paul",
        "Christopher",
        "Thomas",
        "John",
        "Mark",
        "James",
        "Stephen",
        "Andrew",
        "Jack",
        "Michael",
        "Daniel",
        "Peter",
        "Richard",
        "Matthew",
        "Robert",
        "Ryan",
        "Joshua",
        "Alan",
        "Ian",
        "Simon",
        "Luke",
        "Samuel",
        "Jordan",
        "Anthony",
        "Adam",
        "Lee",
        "Alexander",
        "William",
        "Kevin",
        "Darren",
        "Benjamin",
        "Philip",
        "Gary",
        "Joseph",
        "Brian",
        "Steven",
        "Liam",
        "Keith",
        "Martin",
        "Jason",
        "Jonathan",
        "Jake",
        "Graham",
        "Nicholas",
        "Craig",
        "George",
        "Colin",
        "Neil",
        "Lewis",
        "Nigel",
        "Oliver",
        "Timothy",
        "Stuart",
        "Kenneth",
        "Raymond",
        "Jamie",
        "Nathan",
        "Geoffrey",
        "Connor",
        "Terence",
        "Trevor",
        "Adrian",
        "Harry",
        "Malcolm",
        "Scott",
        "Callum",
        "Wayne",
        "Aaron",
        "Barry",
        "Ashley",
        "Bradley",
        "Patrick",
        "Gareth",
        "Jacob",
        "Sean",
        "Kieran",
        "Derek",
        "Carl",
        "Dean",
        "Charles",
        "Sam",
        "Shaun",
        "Ben",
        "Roger",
        "Mohammed",
        "Leslie",
        "Ronald",
        "Kyle",
        "Clive",
        "Edward",
        "Antony",
        "Jeremy",
        "Justin",
        "Jeffrey",
        "Christian",
        "Roy",
        "Karl",
        "Alex",
        "Gordon",
        "Dominic",
        "Joe",
        "Marc",
        "Reece",
        "Dennis",
        "Russell",
        "Gavin",
        "Rhys",
        "Phillip",
        "Allan",
        "Robin",
        "Charlie",
        "Gerald",
        "Ross",
        "Francis",
        "Eric",
        "Julian",
        "Bernard",
        "Dale",
        "Donald",
        "Damian",
        "Frank",
        "Shane",
        "Cameron",
        "Norman",
        "Duncan",
        "Louis",
        "Frederick",
        "Tony",
        "Howard",
        "Conor",
        "Douglas",
        "Garry",
        "Elliot",
        "Marcus",
        "Arthur",
        "Vincent",
        "Max",
        "Mathew",
        "Abdul",
        "Henry",
        "Martyn",
        "Ricky",
        "Leonard",
        "Lawrence",
        "Glen",
        "Mitchell",
        "Gerard",
        "Gregory",
        "Iain",
        "Billy",
        "Bryan",
        "Joel",
        "Clifford",
        "Josh",
        "Leon",
        "Stewart",
        "Mohammad",
        "Dylan",
        "Graeme",
        "Terry",
        "Guy",
        "Elliott",
        "Stanley",
        "Danny",
        "Brandon",
        "Victor",
        "Toby",
        "Hugh",
        "Mohamed",
        "Brett",
        "Albert",
        "Tom",
        "Declan",
        "Maurice",
        "Glenn",
        "Leigh",
        "Denis",
        "Damien",
        "Bruce",
        "Jay",
        "Owen",
    )

    welsh_first_names_male = (
        'Idris',
        'Llion',
        'Twm',
        'Bleddyn',
        'Arthur',
        'Macsen',
        'Aron',
        'Gerallt',
        'Rhodri',
        'Iestyn',
        'Idwal',
        'Gerwyn',
        'Elgan',
        'Meirion',
        'Dylan',
        'Osian',
        'Harri',
        'Iolo',
        'Trefor',
        'Tudur',
        'Peredur',
        'Endaf',
        'Ifan',
        'Ianto',
        'Rhys',
        'Eifion',
        'Elidir',
        'Ifor',
        'Wyn',
        'Gethin',
        'Arwel',
        'Emlyn',
        'Eurig',
        'Derfel',
        'Dafydd',
        'Gruffydd',
        'Siôn',
        'Emyr',
        'Arwyn',
        'Dyfan',
        'Tomos',
        'Gwyndaf',
        'Guto',
        'Geraint',
        'Bedwyr',
        'Gwion',
        'Emrys',
        'Gwilym',
        'Ioan',
        'Einion',
        'Elwyn',
        'Trystan',
        'Gwynfor',
        'Iorwerth',
        'Gwydion',
        'Aled',
        'Morgan',
        'Deiniol',
        'Goronwy',
        'Gruffudd',
        'Hywel',
        'Rhun',
        'Dilwyn',
        'Meredudd',
        'Elis',
        'Huw',
        'Elfed',
        'Alun',
        'Dyfrig',
        'Owain',
        'Ieuan',
        'Steffan',
        'Gareth',
        'Cai',
        'Jac',
        'Efan',
        'Eban',
        'Carwyn',
        'Dewi',
        'Bryn',
        'Rhidian',
        'Llŷr',
        'Llywelyn',
        'Meilir',
        'Deian',
        'Glyn',
        'Iwan',
        'Edryd',
        'Tecwyn',
        'Alwyn')

    first_names_female = (
        "Susan",
        "Sarah",
        "Rebecca",
        "Linda",
        "Julie",
        "Claire",
        "Laura",
        "Lauren",
        "Christine",
        "Karen",
        "Nicola",
        "Gemma",
        "Jessica",
        "Margaret",
        "Jacqueline",
        "Emma",
        "Charlotte",
        "Janet",
        "Deborah",
        "Lisa",
        "Hannah",
        "Patricia",
        "Tracey",
        "Joanne",
        "Sophie",
        "Carol",
        "Jane",
        "Michelle",
        "Victoria",
        "Amy",
        "Elizabeth",
        "Helen",
        "Samantha",
        "Emily",
        "Mary",
        "Diane",
        "Rachel",
        "Anne",
        "Sharon",
        "Ann",
        "Tracy",
        "Amanda",
        "Jennifer",
        "Chloe",
        "Angela",
        "Louise",
        "Katie",
        "Lucy",
        "Barbara",
        "Alison",
        "Sandra",
        "Caroline",
        "Clare",
        "Kelly",
        "Bethany",
        "Gillian",
        "Natalie",
        "Jade",
        "Pauline",
        "Megan",
        "Elaine",
        "Alice",
        "Lesley",
        "Catherine",
        "Hayley",
        "Pamela",
        "Danielle",
        "Holly",
        "Wendy",
        "Abigail",
        "Valerie",
        "Olivia",
        "Jean",
        "Dawn",
        "Donna",
        "Stephanie",
        "Leanne",
        "Kathleen",
        "Natasha",
        "Denise",
        "Sally",
        "Katherine",
        "Georgia",
        "Maureen",
        "Maria",
        "Zoe",
        "Judith",
        "Kerry",
        "Debra",
        "Melanie",
        "Stacey",
        "Eleanor",
        "Paula",
        "Shannon",
        "Sheila",
        "Joanna",
        "Paige",
        "Janice",
        "Lorraine",
        "Georgina",
        "Lynn",
        "Andrea",
        "Suzanne",
        "Nicole",
        "Yvonne",
        "Chelsea",
        "Lynne",
        "Anna",
        "Kirsty",
        "Shirley",
        "Alexandra",
        "Marion",
        "Beverley",
        "Melissa",
        "Rosemary",
        "Kimberley",
        "Carole",
        "Fiona",
        "Kate",
        "Joan",
        "Marie",
        "Jenna",
        "Marilyn",
        "Jodie",
        "June",
        "Grace",
        "Mandy",
        "Rachael",
        "Lynda",
        "Tina",
        "Kathryn",
        "Molly",
        "Jayne",
        "Amber",
        "Marian",
        "Jasmine",
        "Brenda",
        "Sara",
        "Kayleigh",
        "Teresa",
        "Harriet",
        "Julia",
        "Ashleigh",
        "Heather",
        "Kim",
        "Ruth",
        "Jemma",
        "Carly",
        "Leah",
        "Eileen",
        "Francesca",
        "Naomi",
        "Hilary",
        "Abbie",
        "Sylvia",
        "Katy",
        "Irene",
        "Cheryl",
        "Rosie",
        "Dorothy",
        "Aimee",
        "Vanessa",
        "Ellie",
        "Frances",
        "Sian",
        "Josephine",
        "Gail",
        "Jill",
        "Lydia",
        "Joyce",
        "Charlene",
        "Hollie",
        "Hazel",
        "Annette",
        "Bethan",
        "Amelia",
        "Beth",
        "Rita",
        "Geraldine",
        "Diana",
        "Lindsey",
        "Carolyn"
    )

    welsh_first_names_female = (
        'Cerys',
        'Rhian',
        'Leusa',
        'Catrin',
        'Erin',
        'Cadi',
        'Llio',
        'Alys',
        'Gwen',
        'Menna',
        'Annest',
        'Siân',
        'Rhiannon',
        'Dwynwen',
        'Eluned',
        'Olwen',
        'Lleuwen',
        'Gwenno',
        'Nest',
        'Sioned',
        'Morfudd',
        'Gwenllïan',
        'Lois',
        'Glenda',
        'Caryl',
        'Angharad',
        'Nanw',
        'Gwenda',
        'Gwladys',
        'Sara',
        'Carys',
        'Luned',
        'Lleucu',
        'Nerys',
        'Megan',
        'Mari',
        'Awen',
        'Siwan',
        'Mererid',
        'Esyllt',
        'Marged',
        'Hawys',
        'Mali',
        'Elena',
        'Sali',
        'Annes',
        'Eirian',
        'Nesta',
        'Tegwen',
        'Eryl',
        'Enid',
        'Teleri',
        'Manon',
        'Ceinwen',
        'Eirwen',
        'Tesni',
        'Anest',
        'Gwyneth',
        'Elen',
        'Mair',
        'Nia',
        'Mared',
        'Elliw',
        'Sara',
        'Lowri',
        'Myfanwy',
        'Anwen',
        'Eleri',
        'Elsi',
        'Branwen',
        'Beca',
        'Elinor',
        'Efa',
        'Betsan',
        'Einir',
        'Meinir',
        'Mabli',
        'Delyth',
        'Elin',
        'Awel',
        'Dilys',
        'Gwawr',
        'Non',
        'Seren',
        'Enfys',
        'Ffion',
        'Eira',
        'Lili',
        'Gwennan',
        'Llinos')
    
    frequent_first_names = (
        "Andrew",
        "Christopher",
        "David",
        "John",
        "Mark",
        "Michael",
        "Paul",
        "Richard",
        "Robert",
        "Thomas",
        "Stephen",
        "William",
        "Ann",
        "Claire",
        "Christine",
        "Elizabeth",
        "Emma",
        "Helen",
        "Julie",
        "Karen",
        "Linda",
        "Margaret",
        "Mary",
        "Sarah",
    )

    first_names_male = welsh_first_names_male + first_names_male

    first_names_female = welsh_first_names_female + first_names_female

    first_names = first_names_male + first_names_female + frequent_first_names

    last_names = OrderedDict(
        (
        ('Jones', 6.0),
        ('Williams', 4.16),
        ('Davies', 3.98),
        ('Evans', 3.89),
        ('Thomas', 2.99),
        ('Roberts', 2.83),
        ('Edwards', 2.77),
        ('Davis', 2.77),
        ('Hughes', 2.76),
        ('Smith', 2.75),
        ('Harris', 2.75),
        ('Lewis', 2.75),
        ('Morgan', 2.75),
        ('Morris', 2.71),
        ('James', 2.73),
        ('Jenkins', 2.67),
        ('Price', 1.99),
        ('Griffiths', 1.95),
        ('Young', 1.90),
        ('Bennett', 1.85),
        ('Parry', 1.80),
        ('Rees', 1.75),
        ('Pritchard', 1.65),
        ('Pugh', 1.64),
        ('Martin', 0.73),
        ('Brown', 0.72),
        ('Harrison', 0.7),
        ('Lee', 0.7),
        ('Baker', 0.7),
        ('Allen', 0.69),
        ('Clark', 0.67),
        ('Wright', 0.67),
        ('Phillips', 0.67),
        ('Moore', 0.66),
        ('Scott', 0.67),
        ('King', 0.65),
        ('Bailey', 0.65),
        ('Collins', 0.65),
        ('Richards', 0.64),
        ('Cox', 0.64),
        ('Francis', 0.64),
        ('Humphreys', 0.64),
        ('Gibbs', 0.64),
        ('Davey', 0.64),
        ('Vaughan', 0.64),
        ('Bowen', 0.64),
        ('Ellis', 0.63),
        ('Howells', 0.63),
        ('Humphries', 0.63),
        ('Hill', 0.62),
        ('Webb', 0.62),
        ('Rogers', 0.62),
        ('Powell', 0.62),
        ('Mason', 0.62),
        ('Ward', 0.61),
        ('Parker', 0.61),
        ('Lloyd', 0.61),
        ('Hussain', 0.61),
        ('Owen', 0.61),
        ('Palmer', 0.61),
        ('Matthews', 0.61),
        ('Hunt', 0.6),
        ('Graham', 0.6),
        ('Barker', 0.6),
        ('Robertson', 0.6),
        ('Payne', 0.59),
        ('Ford', 0.59),
        ('Saunders', 0.59),
        ('Reynolds', 0.59),
        ('Pearce', 0.59),
        ('Andrews', 0.59),
        ('Rose', 0.58),
        ('Burton', 0.58),
        ('Dawson', 0.58),
        ('Parsons', 0.57),
        ('Lowe', 0.57),
        ('Dunn', 0.57),
        ('Armstrong', 0.57),
        ('Carr', 0.57),
        ('Hudson', 0.57),
        ('Wells', 0.57),
        ('Page', 0.57),
        ('Mitchell', 0.56),
        ('Mills', 0.56),
        ('Harper', 0.56),
        ('Hamilton', 0.56),
        ('Hopkins', 0.56),
        ('Williamson', 0.56),
        ('Bates', 0.56),
        ('Hodgson', 0.56),
        ('Ross', 0.56),
        ('Walton', 0.56),
        ('Watkins', 0.56),
        ('Wilson', 0.55),
        ('Cook', 0.55),
        ('Carter', 0.55),
        ('George', 0.55),
        ('Davidson', 0.55),
        ('Stephens', 0.55),
        ('Potter', 0.55),
        ('Goodwin', 0.55),
        ('Gilbert', 0.55),
        ('Buckley', 0.55),
        ('Whitehead', 0.55),
        ('Osborne', 0.55),
        ('Thomson', 0.55),
        ('Lynch', 0.55),
        ('Slater', 0.55),
        ('Walters', 0.55),
        ('Read', 0.55),
        ('Griffin', 0.55),
        ('Nelson', 0.55),
        ('Mann', 0.55),
        ('Sharp', 0.55),
        ('Burke', 0.55),
        ('Barton', 0.55),
        ('Baxter', 0.55),
        ('Wallace', 0.55),
        ('Wheeler', 0.55),
        ('Hutchinson', 0.55),
        ('Poole', 0.55),
        ('Johnston', 0.55),
        ('Hewitt', 0.55),
        ('Arnold', 0.55),
        ('Johnson', 0.54),
        ('Murphy', 0.54),
        ('Stephenson', 0.54),
        ('Fowler', 0.54),
        ('Townsend', 0.54),
        ('Ferguson', 0.54),
        ('Reeves', 0.54),
        ('Barlow', 0.54),
        ('Short', 0.54),
        ('Glover', 0.54),
        ('Baldwin', 0.54),
        ('Sanders', 0.54),
        ('Burrows', 0.54),
        ('Fraser', 0.54),
        ('Jarvis', 0.54),
        ('Lucas', 0.54),
        ('Morton', 0.54),
        ('Haynes', 0.54),
        ('Dodd', 0.54),
        ('Black', 0.54),
        ('Simmons', 0.54),
        ("O'Sullivan", 0.54),
        ('Weston', 0.54),
        ('Norris', 0.54),
        ('Bradshaw', 0.54),
        ('John', 0.54),
        ('Morrison', 0.54),
        ('Flynn', 0.54),
        ('Miah', 0.54),
        ('Banks', 0.54),
        ('Cartwright', 0.54),
        ('Little', 0.54),
        ('Smart', 0.54),
        ('Bull', 0.54),
        ('Bryant', 0.54),
        ('Norman', 0.54),
        ('Howe', 0.54),
        ('Preston', 0.54),
        ('Howell', 0.54),
        ('Taylor', 0.53),
        ('Robinson', 0.53),
        ('Thompson', 0.53),
        ('Wilkinson', 0.53),
        ('Adams', 0.53),
        ('Sims', 0.53),
        ('Collier', 0.53),
        ('Rice', 0.53),
        ('Wyatt', 0.53),
        ('Gould', 0.53),
        ('Dyer', 0.53),
        ('Bryan', 0.53),
        ('Pope', 0.53),
        ('Steele', 0.53),
        ('Ingram', 0.53),
        ('Hyde', 0.53),
        ('Owens', 0.53),
        ('Barry', 0.53),
        ('Carey', 0.53),
        ('Bevan', 0.53),
        ('Conway', 0.53),
        ('Faulkner', 0.53),
        ('Hope', 0.53),
        ('Hobbs', 0.53),
        ('Gardiner', 0.53),
        ('Coates', 0.53),
        ('White', 0.52),
        ('Walker', 0.51),
        ('Green', 0.5),
        ('Rowlands', 0.5),
        ('Llewellyn', 0.5),
        ('Harries', 0.5),
        ('Probert', 0.5),
        ('Isaac', 0.5),
        ('Haines', 0.5),
        ('Daniel', 0.5),
        ('Joseph', 0.5),
        ('Mathias', 0.5),
        ('Wynne', 0.5),
        ('Thorne', 0.5),
        ('Morgans', 0.5),
        ('Pierce', 0.5),
        ('Bowden', 0.5),
        ('Foulkes', 0.5),
        ('Arthur', 0.5),
        ('Harry', 0.5),
        ('Roderick', 0.5),
        ('Coombes', 0.5),
        ('Robbins', 0.5),
        ('Clement', 0.5),
        ('Protheroe', 0.5),
        ('Robins', 0.5),
        ('Elias', 0.5),
        ('Britton', 0.5),
        ('Tudor', 0.5),
        ('Pryce', 0.5),
        ('De Cunha', 0.5),
        ('Coombs', 0.5),
        ('Michael', 0.5),
        ('Rowland', 0.5),
        ('Bellis', 0.5),
        ('Glynne', 0.5),
        ('Gittins', 0.5),
        ('Brace', 0.5),
        ('Welsh', 0.5),
        ('Eynon', 0.5),
        ('Drew', 0.5),
        ('Paul', 0.5),
        ('Beynon', 0.5),
        ('Hall', 0.49),
        ('Clarke', 0.48),
        ('Booth', 0.48),
        ('Cole', 0.48),
        ('Atkinson', 0.48),
        ('Gill', 0.48),
        ('Watts', 0.48),
        ('Jackson', 0.47),
        ('Webster', 0.47),
        ('Newton', 0.47),
        ('Wood', 0.46),
        ('Turner', 0.46),
        ('Cooper', 0.45),
        ('Dean', 0.45),
        ("O'Neill", 0.45),
        ('Kennedy', 0.45),
        ("O'Connor", 0.45),
        ('Burns', 0.45),
        ('Chambers', 0.44),
        ('Wilkins', 0.44),
        ('Jennings', 0.43),
        ('Higgins', 0.43),
        ('Barnett', 0.43),
        ('Hammond', 0.43),
        ('Cunningham', 0.43),
        ('Hardy', 0.43),
        ('Blake', 0.43),
        ('Clayton', 0.43),
        ('Gallagher', 0.43),
        ('Quinn', 0.43),
        ('Barber', 0.43),
        ('Field', 0.43),
        ('Patterson', 0.43),
        ('Heath', 0.43),
        ('Whittaker', 0.43),
        ('French', 0.43),
        ('Henry', 0.43),
        ('Herbert', 0.43),
        ('Patel', 0.4),
        ('Grant', 0.37),
        ('Riley', 0.37),
        ('Hunter', 0.35),
        ('Reid', 0.35),
        ('Porter', 0.35),
        ('Yates', 0.35),
        ('Moss', 0.35),
        ('Warren', 0.35),
        ('Cooke', 0.35),
        ('McDonald', 0.34),
        ('Ashton', 0.34),
        ('Singh', 0.33),
        ('Ahmed', 0.33),
        ('Doyle', 0.33),
        ('Jordan', 0.33),
        ('Gordon', 0.33),
        ('Kemp', 0.33),
        ('Holt', 0.33),
        ('Frost', 0.33),
        ('Stevenson', 0.33),
        ('Rowe', 0.33),
        ('Bond', 0.33),
        ('Lambert', 0.33),
        ('Austin', 0.33),
        ('Woodward', 0.33),
        ('Bray', 0.33),
        ('Shepherd', 0.3),
        ('McCarthy', 0.3),
        ('Byrne', 0.3),
        ('Henderson', 0.3),
        ('Freeman', 0.3),
        ('Atkins', 0.3),
        ('Alexander', 0.3),
        ('Carroll', 0.3),
        ('Goddard', 0.3),
        ('Wall', 0.3),
        ('Hayward', 0.3),
        ('Gibbons', 0.3),
        ('Rowley', 0.3),
        ('Bolton', 0.3),
        ('Power', 0.3),
        ('Hale', 0.3),
        ('Dennis', 0.3),
        ('Randall', 0.3),
        ('Tyler', 0.3),
        ('Horton', 0.3),
        ('Vincent', 0.3),
        ('Clements', 0.3),
        ('Leonard', 0.3),
        ('Summers', 0.3),
        ('Lyons', 0.3),
        ('Giles', 0.3),
        ('Hicks', 0.24),
        ('Begum', 0.23),
        ('Manning', 0.23),
        ('Talbot', 0.23),
        ('Skinner', 0.22),
        ('Birch', 0.22),
        ('Lawson', 0.22),
        ('Abbott', 0.22),
        ('Middleton', 0.22),
        ('Brookes', 0.2),
        ('Stanley', 0.2),
        ('Winter', 0.2),
        ('Holloway', 0.2),
        ('Farmer', 0.2),
        ('Carpenter', 0.2),
        ('Chamberlain', 0.2),
        ('Sheppard', 0.2),
        ('Fry', 0.2),
        ('Watson', 0.17),
        ('Kelly', 0.16),
        ('Richardson', 0.15),
        ('Shaw', 0.15),
        ('Bell', 0.15),
        ('Miles', 0.15),
        ('Khan', 0.14),
        ('Marshall', 0.14),
        ('Miller', 0.14),
        ('Leach', 0.13),
        ('Anderson', 0.13),
        ('Foster', 0.13),
        ('Simpson', 0.13),
        ('Chapman', 0.12),
        ('Ali', 0.12),
        ('Gray', 0.12),
        ('Barnes', 0.11),
        ('Knight', 0.11),
        ('Butler', 0.11),
        ('Holmes', 0.11),
        ('Campbell', 0.11),
        ('Butcher', 0.1),
        ('Harvey', 0.1),
        ('Stevens', 0.1),
        ('Dixon', 0.1),
        ('Fletcher', 0.1),
        ('Fisher', 0.1),
        ('Russell', 0.1),
        ('Pearson', 0.1),
        ('Murray', 0.1),
        ('Day', 0.09),
        ('Howard', 0.09),
        ('Gibson', 0.09),
        ('Walsh', 0.09),
        ('Fox', 0.09),
        ('Brooks', 0.09),
        ('Elliott', 0.09),
        ('West', 0.09),
        ('Lawrence', 0.09),
        ('Stewart', 0.09),
        ('Spencer', 0.08),
        ("O'Brien", 0.08),
        ('Ryan', 0.08),
        ('Bradley', 0.08),
        ('Perry', 0.08),
        ('Ball', 0.08),
        ('Holland', 0.07),
        ('Hayes', 0.07),
        ('Barrett', 0.07),
        ('Stone', 0.07),
        ('Oliver', 0.07),
        ('Woods', 0.07),
        ('Hart', 0.07),
        ('Berry', 0.07),
        ('Newman', 0.07),
        ('Reed', 0.07),
        ('Marsh', 0.07),
        ('Hawkins', 0.07),
        ('Gregory', 0.07),
        ('Harding', 0.07),
        ('Burgess', 0.06),
        ('Long', 0.06),
        ('Nicholson', 0.06),
        ('Lane', 0.06),
        ('Coleman', 0.06),
        ('Gardner', 0.06),
        ('Bird', 0.06),
        ('Nicholls', 0.06),
        ('Bishop', 0.06),
        ('Shah', 0.06),
        ('Sutton', 0.06),
        ('Cross', 0.06),
        ('Curtis', 0.06),
        ('Robson', 0.06),
        ('Tucker', 0.05),
        ('Nash', 0.05),
        ('Akhtar', 0.05),
        ('Stokes', 0.05),
        ('Sullivan', 0.05),
        ('Bibi', 0.05),
        ('Willis', 0.05),
        ('Greenwood', 0.05),
        ('May', 0.05),
        ('Savage', 0.04),
        ('Rhodes', 0.04),
        ('Hancock', 0.04),
        ('Bentley', 0.04),
        ('Hartley', 0.04),
        ('Tomlinson', 0.04),
        ('Archer', 0.04),
        ('Warner', 0.04),
        ('Daniels', 0.04),
        ('Macdonald', 0.04),
        ('Kirk', 0.04),
        ('Dale', 0.04),
        ('Wade', 0.04),
        ('Farrell', 0.04),
        ('Kay', 0.04),
        ('Thorpe', 0.04),
        ('Dobson', 0.04),
        ('Brennan', 0.04),
        ('Kirby', 0.04),
        ('Lamb', 0.04),
        ('Dickinson', 0.04),
        ('Davison', 0.04),
        ('Douglas', 0.04),
        ('Morley', 0.04),
        ('Kent', 0.04),
        ('Duffy', 0.04),
        ('Parkinson', 0.04),
        ('Todd', 0.04),
        ('Waters', 0.04),
        ('Knowles', 0.04),
        ('Peters', 0.04),
        ('Briggs', 0.04),
        ('Perkins', 0.04),
        ('Thornton', 0.04),
        ('Fuller', 0.04),
        ('Holden', 0.04),
        ('Wong', 0.04),
        ('Bartlett', 0.04),
        ('Schofield', 0.04),
        ('Metcalfe', 0.03),
        ('Potts', 0.03),
        ('Boyle', 0.03),
        ('Bruce', 0.03),
        ('Wallis', 0.03),
        ('Hooper', 0.03),
        ('Whitehouse', 0.03),
        ('Iqbal', 0.03),
        ('Lees', 0.03),
        ('Browne', 0.03),
        ('Connor', 0.03),
        ('Daly', 0.03),
        ('Marsden', 0.03),
        ('Lord', 0.03),
        ('Noble', 0.03),
        ('Sharpe', 0.03),
        ('Parkes', 0.03),
        ('Sinclair', 0.03),
        ('McLean', 0.03),
        ('Storey', 0.03),
        ('Turnbull', 0.03),
        ('Duncan', 0.03),
        ('Godfrey', 0.03),
        ('Parri', 0.03),
        ('Hargreaves', 0.03),
        ('Chan', 0.03),
        ('Connolly', 0.03),
        ('Charlton', 0.03),
        ('North', 0.03),
        ('Hanson', 0.03),
        ('Craig', 0.03),
        ('Allan', 0.03),
        ('Sanderson', 0.03),
        ('Huws', 0.03),
        ('Mahmood', 0.03),
        ('Dafis', 0.03),
        ('Meredith', 0.01)
        )
    )

    prefixes_female = ("Mrs", "Ms", "Miss", "Dr")
    prefixes_male = ("Mr", "Dr")
