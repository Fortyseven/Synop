import random, re

class Utils:
    last_names = (
         'David', 'Dailey', 'Michael', 'Curtis', 'Hamilton', 'Parker', 'Cameron', 'Turner', 'York', 'Wilson', 'Mann', 'James',
         'Lawrence', 'Wright', 'Thompson', 'Daniel', 'Young', 'Russo', 'England', 'Frank', 'Lee', 'Ewing', 'Roman', 'Richard',
         'Holland', 'Ray', 'Lu', 'Thomas', 'Flynn', 'West', 'Riley', 'Brady', 'Grove', 'Roth', 'Draper', 'Seymour', 'Montgomery',
         'Romero', 'Di', 'Pil-seong', 'Ki-tae','Grandier', 'Welsch', 'Hawthorne', 'Halleck', 'Crichton', 'Bleak\'s',
         'Freeman', 'Martin', 'Blake', 'Downs', 'Taylor', 'John', 'Conrad', 'Gallagher', 'Forrest', 'Cross', 'Adams', 'Dunham',
         'Harris', 'Chappell', 'Lord', 'Hatfield', 'Randall', 'Rosa', 'Allen', 'Walker', 'Arnold', 'Miller', 'Lucas', 'Lang',
         'Ramsey', 'Henry', 'Womack', 'Singh', 'Nicholas', 'Stewart', 'Bishop', 'Griffin', 'Stanley', 'Todd', 'Norton', 'Hunt',
         'Baxter', 'Pierre', 'Lara', 'Powell', 'Hall', 'Quinn', 'Hawkins', 'Wilder', 'Black', 'Hancock', 'Cleveland', 'Ali',
         'Rios', 'Anderson', 'Mason', 'Ross', 'Charles', 'Savage', 'Juarez', 'Wells', 'Lake', 'Walter', 'Albert', 'Dean', 'Muffet',
         'Stafford', 'Kennedy', 'Merritt', 'Ramirez', 'Owen', 'Allison', 'Summers', 'Morris', 'Poole', 'Sawyer', 'Alexander',
         'Beach', 'Tate', 'Weston', 'Arthur', 'George', 'Kendall', 'Vincent', 'Stark', 'Simon', 'Weaver', 'Sullivan', 'Carson',
         'Stevens', 'Spencer', 'Lacy', 'Kelly', 'Paul', 'Faulkner', 'Mitchell', 'Elmore', 'Blair', 'Logan', 'Barrett',
         'Anthony', 'Evans', 'Jackson', 'Nix', 'Holden', 'Case', 'Murillo', 'Hong', 'Craig', 'Johnson', 'Liu', 'Philips', 'Khan',
         'Golden', 'Bruno', 'Gibson', 'Wheeler', 'Moody', 'Lloyd', 'Santos', 'Chapman', 'Scott', 'Head', 'Harvey', 'Hoover',
         'Starr', 'Powers', 'Joseph', 'Costa', 'Andersen', 'Sweeney', 'Carter', 'Hopkins', 'Lewis', 'Lancaster', 'Barnes',
         'Morgan', 'Williams', 'Wade', 'Wu', 'Lam', 'Douglas', 'Benjamin', 'Sparks', 'Harper', 'Madison', 'Doherty', 'Leon',
         'Shannon', 'Ackerman', 'Devine', 'Moses', 'Sheehan', 'Henson', 'Lindsay', 'Tracy', 'Preston', 'Plummer', 'Davis',
         'Burton', 'Solomon', 'Kane', 'Hammond', 'Leonard', 'Ryan', 'Nelson', 'Cortez', 'Norman', 'Hanna', 'Tyler', 'Larkin',
         'Mata', 'Craft', 'Cole', 'Compton', 'Mendoza', 'Rhodes', 'Yang', 'Yu', 'Russell', 'Christopher', 'Morse', 'Doyle',
         'Ellis', 'Phillips', 'Edwards', 'Britton', 'Austin', 'Grimes', 'Burke', 'Page', 'Corbin', 'Leslie', 'Newman', 'Jacobs',
         'Lopez', 'Chandler', 'Carroll', 'Hardy', 'Dixon', 'Brennan', 'Bloom', 'Parra', 'Manuel', 'Olsen', 'Owens', 'Castillo',
         'Bradshaw', 'Patterson', 'Hodges', 'Houston', 'Shepard', 'Murray', 'Whitney', 'Gregory', 'Dale', 'Strickland', 'Coleman',
         'Richmond', 'Cheng', 'Garcia', 'Ford', 'Bernard', 'Kim', 'Watts', 'Hunter', 'Connor', 'Crane', 'Marsh', 'Duke', 'Hammer',
         'Choi', 'Cordero', 'Irwin', 'Neal', 'Knight', 'Houghton', 'Jones', 'Osborn', 'Zhang', 'Ritchie', 'Robinson', 'Prepon',
         'Boyle', 'Downey', 'Watson', 'Ashley', 'Patrick', 'Griffith', 'Ivey', 'Gilbert', 'Foley', 'Graham','Capone',
         'Clark', 'Cunningham', 'Grace', 'Casey', 'Ball', 'Lane', 'Hyde', 'Butcher', 'Schumacher', 'Sutton', 'Ward', 'Brooks',
         'Beaver', 'Meyers', 'Sweet', 'Reid', 'Hoffman', 'Keith', 'Terry', 'Jordan', 'Cooper', 'Brandon', 'Wyatt', 'Bond',
         'Fleming', 'Abraham', 'Davidson', 'Chase', 'Shaw', 'Underwood', 'Chan', 'Francis', 'Hanson', 'Webster', 'Nguyen',
         'Hayes', 'Connelly', 'Stuart', 'Cummings', 'Krueger', 'Hughes', 'Donahue', 'Walters', 'Klein', 'Noble', 'Fitzgerald',
         'Vinson', 'Beck', 'Gunn', 'Potter', 'Burnett', 'Lyons', 'Swan', 'Roy', 'Duncan', 'Bush', 'Torres', 'Harding', 'Richards',
         'Barton', 'Fink', 'Marshall', 'Felix', 'Holt', 'Abbott', 'Drew', 'Hendrix', 'Baez', 'Jefferson', 'Foster', 'Lawson', 'Stander',
         'Belcher', 'Donovan', 'Lambert', 'Dalton', 'Tanner', 'Bravo', 'Boyer', 'Wilkerson', 'Sutherland', 'Palmer', 'Carlson',
         'Knox', 'Vance', 'Pearson', 'Bonner', 'Landry', 'Wang', 'Huang', 'Burns', 'Biggs', 'Manning', 'Booker', 'Kirk', 'Jarvis',
         'Hudson', 'Benson')

    first_names = (
         'Buttercup',
         'Phil', 'Jesus', 'David', 'Michael', 'Curtis', 'Angeles', 'Nick', 'Elly', 'Parker', 'Matt', 'Eddie', 'June','Er', 'Fitz',
         'Irish', 'Liz', 'Cameron', 'Guy', 'Catherine', 'Stella', 'Jack', 'Ferdinand', 'Rebecca', 'Eric', 'Jake', 'El Dorado',
         'Leo', 'Sydney', 'Rod', 'Nova', 'Ben', 'Wilson', 'Fanny', 'Sherwood', 'James', 'Lawrence', 'Candy', 'Jimmy', 'Daniel',
         'Julio', 'Gino', 'Young', 'Aldo', 'Jo', 'Song', 'Jeni', 'Xiao', 'Frank', 'Robert', 'Jan', 'Jason', 'Julie', 'Sung',
         'Cinderella', 'Lee', 'Jae', 'Kyung', 'Queen', 'Bobby', 'Roman', 'Milo', 'Dave', 'Barbara', 'Beverly', 'Claire',
         'Ronald', 'Christine', 'Michel', 'Richard', 'Francisco', 'Jennifer', 'Jenny', 'Mario', 'Freddy', 'Francine', 'Ray',
         'Allie', 'Soon', 'Holly', 'Han', 'Lu', 'King', 'Wei', 'Tessa', 'Josh', 'German', 'Sid', 'Sarah', 'Lucy', 'Jesse',
         'Ethan', 'Troy', 'Paris', 'Rose', 'Thomas', 'Percy', 'Belle', 'Lola', 'Dusty', 'Nancy', 'Molly', 'Mercedes', 'Sophie',
         'Sheba', 'Emma', 'Mike', 'Riley', 'Sparkle', 'Pinkie', 'Brady', 'Russ', 'Easter', 'Bunny', 'Peter', 'Eli', 'Don',
         'Gerda', 'Seymour', 'Aaron', 'Huey', 'Freeman', 'Robin', 'America', 'Carl', 'Georgia', 'Fred', 'Velma', 'Daphne',
         'Crystal', 'Man', 'Martin', 'Florence', 'Blake', 'Ken', 'Taylor', 'Rex', 'Sebastian', 'Horace', 'John', 'Conrad',
         'Muriel', 'Billy', 'Mandy', 'Porsche', 'Louis', 'Dan', 'Alex', 'Forrest', 'Meryl', 'Milly', 'Marie',
         'Ming', 'Olivia', 'Harris', 'Randall', 'Virginia', 'Rosa', 'Allen', 'Walker', 'Julian', 'Arnold', 'Brian', 'Sun',
         'Lucas', 'Olive', 'Lang', 'Sam', 'Henry', 'Benny', 'Mark', 'Esther', 'Su', 'Bob', 'Nicholas', 'Stewart', 'Kyle',
         'Rachel', 'Israel', 'Kiera', 'Fiona', 'Kevin', 'Joe', 'Elsa', 'Era', 'Philip', 'Diana', 'Stanley', 'Oscar', 'Derrick',
         'Katherine', 'Marty', 'Laura', 'Todd', 'Lady', 'Myra', 'Luther', 'Rita', 'Pierre', 'Ariel', 'Lara', 'Susan', 'Waylon',
         'Zack', 'Cecily', 'Matthew', 'Shawn', 'Charlie', 'Cory', 'Brett', 'Virgil', 'Quinn', 'Karl', 'Eva', 'Gus', 'Jim',
         'Long', 'Annie', 'Della', 'Donald', 'Sara', 'Mary', 'Cleveland', 'Eugene', 'Jon', 'Ali', 'Omar', 'Ana', 'Chloe',
         'Stan', 'Gerry', 'Anderson', 'Violet', 'Rosie', 'Amy', 'Mason', 'Greg', 'Ross', 'Elizabeth', 'Naomi', 'Ed',
         'Charles', 'Noelle', 'Adam', 'Chuck', 'Wally', 'Barney', 'Eve', 'Toby', 'Jeffrey', 'Faith', 'Walter', 'Albert',
         'Carolina', 'Dean', 'Phillip', 'Fonda', 'Luke', 'Julia', 'Florida', 'Ted', 'Wes', 'Natalie', 'Jacob', 'Santa',
         'Maria', 'Owen', 'William', 'Andy', 'Allison', 'Rudy', 'Elvis', 'Kit', 'Morris', 'Lenny', 'Joey', 'Tom', 'Becky',
         'Edward', 'Alexander', 'Edmund', 'Sonya', 'Harry', 'Jody', 'Dara', 'Weston', 'Arthur', 'Prince', 'Gary', 'George',
         'Kendall', 'Stephanie', 'Vincent', 'Rodrigo', 'Tony', 'Simon', 'Pete', 'Shane', 'Doug', 'Charley', 'Pat', 'Ann',
         'Angel', 'Cassie', 'Steve', 'Nicole', 'Isabelle', 'Carson', 'Helen', 'Eleanor', 'Spencer', 'Toni', 'Brad', 'Lucien',
         'Lacy', 'Sally', 'Edith', 'Kelly', 'Jane', 'Monty', 'Anne', 'Sheldon', 'Paul', 'Ellie', 'Claude', 'Steven', 'Chad',
         'Princess', 'Dagmar', 'Mitchell', 'Leonardo', 'Madonna', 'Penney', 'Sammy', 'Shelly', 'Cheryl', 'Monte', 'Carlo',
         'Mia', 'Marine', 'Luisa', 'Miss', 'Jay', 'Neil', 'See', 'Hai', 'Blair', 'Logan', 'Barrett', 'Victoria', 'Michelle',
         'Brianne', 'Herb', 'Donnell', 'Anthony', 'Jade', 'Caroline', 'April', 'Raul', 'Roger', 'Jackson', 'Marian',
         'Tommy', 'Laurie', 'Maya', 'Willie', 'Hong', 'Carry', 'Antony', 'Julius', 'Al', 'Craig', 'Johnson', 'Angela',
         'Daniela', 'Jeff', 'Emmy', 'Golden', 'Bruno', 'Carla', 'India', 'Dennis', 'Alan', 'Carmen', 'Doris', 'Lora', 'Max',
         'Jackie', 'Margaret', 'Beau', 'Darby', 'Penny', 'Wayne', 'Teri', 'Tod', 'Mickey', 'Thaddeus', 'Joanna', 'Blythe',
         'Seth', 'Frankie', 'Lloyd', 'Heather', 'Santos', 'Trinidad', 'Nita', 'Willy', 'Piper', 'Kuzco', 'Pacha',
         'Samuel', 'Lauren', 'Scott', 'Karma', 'Deb', 'Reuben', 'Dagny', 'Victor', 'Esmeralda', 'Juan', 'Argentina', 'Harvey',
         'Darryl', 'Forest', 'Garfield', 'Agatha', 'Rosemary', 'Darlene', 'Elliot', 'Beth', 'Clay', 'Jed', 'Johnny', 'Mac',
         'Ginny', 'Starr', 'Emily', 'Ralph', 'Joseph', 'Jessica', 'Krishna', 'Bill', 'Merlin', 'Jerry', 'Hans', 'Regan',
         'Carter', 'Buddy', 'Melanie', 'Lewis', 'Marc', 'Buster', 'Chris', 'Hedwig', 'Roberto', 'Williams', 'Venus','Anthea',
         'Serena', 'Winston', 'Viola', 'Selma', 'Kathi', 'Martha', 'Mona', 'Jeremy', 'Alphonse', 'Dee', 'Emile',
         'Lucille', 'Aubrey', 'Renata', 'Cristobal', 'Bonnie', 'Amanda', 'Gavin', 'Constance', 'Douglas', 'Benjamin', 'Madison',
         'Meghan', 'September', 'Lore', 'Oda', 'Rosalind', 'Leigh', 'Leon', 'Shannon', 'Ned', 'Moses', 'Joan', 'Cody', 'Tania',
         'Paula', 'Colby', 'Maggie', 'Alexis', 'Lindsay', 'Hyun', 'Eden', 'Mimi', 'Lena', 'Tracy', 'Gene', 'Preston', 'Sunday',
         'Davis', 'Alejandra', 'Burton', 'Solomon', 'Reggie', 'Leonard', 'Shelby', 'Andre', 'Emmie', 'Spring', 'Karen', 'Ryan',
         'Wilfred', 'Zola', 'Ling', 'Pearl', 'Nelson', 'Cortez', 'Cecil', 'Mai', 'Norman', 'Dori', 'Harold', 'Hanna', 'Dawn',
         'Jarod', 'Cordelia', 'Tyler', 'Lisa', 'Annabel', 'Anastasia', 'Kai', 'Cole', 'Zane', 'Jonas', 'Samantha',
         'Raphael', 'Edmond', 'Tai', 'Chi', 'Yang', 'Yu', 'Derek', 'Marcus', 'Sunny', 'Chelsea', 'Leroy', 'Blossom', 'Ginger',
         'Lizzie', 'Audrey', 'Russell', 'Stephen', 'Hubert', 'Laure', 'Christopher', 'May', 'Darren', 'Robbie', 'Marion',
         'Collette', 'Alice', 'Darwin', 'Doyle', 'Ellis', 'Jose', 'Melissa', 'Charlotte', 'Kenny', 'Katrina', 'Lori', 'Marry',
         'Ron', 'Austin', 'Rick', 'Marge', 'Venice', 'Hallie', 'Peggy', 'Larry', 'Stanford', 'Jenna', 'Leslie',
         'Tobias', 'Alec', 'Anna', 'Zoe', 'Stefan', 'Damon', 'Elena', 'Love', 'Dylan', 'Carroll', 'Katie', 'Jessie', 'Violeta',
         'Marlon', 'Manuel', 'Corey', 'Ivan', 'Nikita', 'Fernando', 'Star', 'Carlos', 'Ricky', 'Carrie', 'Bruce', 'Chun',
         'Dexter', 'January', 'Chet', 'Minnie', 'Dewey', 'Louie', 'Leta', 'Diane', 'Ursula', 'Bud', 'Houston', 'Wilbur', 'Tia',
         'Murray', 'Whitney', 'Dominic', 'Gregory', 'Dale', 'Earl', 'Coleman', 'Marvel', 'Diego', 'Frances', 'Augustine',
         'Luz', 'Brook', 'Joel', 'Bernard', 'Basil', 'Kim', 'Teresa', 'Sue', 'Sylvester', 'Raoul',
         'Bobbie', 'Mel', 'Sylvia', 'Bart', 'Yasmin', 'Angelina', 'Helena', 'Wendy', 'Trevor', 'Heidi', 'Eun', 'Chae',
         'Hee', 'Hyo', 'Jong', 'Kris', 'Ira', 'Irwin', 'Neal', 'Tina', 'Rocky', 'Rob', 'Winnie', 'Lily',
         'Alison', 'Brain', 'Dani', 'Sasha', 'Hayley', 'Tora', 'Raye', 'Ashley', 'Patrick', 'Cecilia', 'Del', 'Jean', 'Ivey',
         'Jules', 'Gilbert', 'Gracie', 'Sean', 'Graham', 'Jacqueline', 'Carol', 'Millie', 'Clark', 'Shayne', 'Bee', 'My', 'Van',
         'Rodger', 'Dino', 'Grace', 'Winter', 'Sonia', 'Luciana', 'Casey', 'Jamal', 'Viki', 'Lane', 'Dakota', 'Orlando', 'Ward',
         'Hannah', 'Antonio', 'Priscilla', 'Chin', 'Sonja', 'Romeo', 'Oliva', 'Reid', 'Daryl', 'Miguel', 'Keith', 'Lance',
         'Vince', 'Terry', 'Leone', 'Yuri', 'Lili', 'Emerald', 'Gay', 'Mina', 'Ezequiel', 'Josie', 'Kate', 'Jordan', 'Raquel',
         'Bruna', 'Rhett', 'Brandon', 'Wyatt', 'Tim', 'Columbus', 'Ian', 'Abraham', 'Marco', 'Chase', 'Nathan', 'Clara',
         'Alyce', 'Ruby', 'Iris', 'Kitty', 'Dot', 'Sophia', 'Chan', 'Isabel', 'Francis', 'Daisy', 'Skye', 'Malcolm', 'Tara',
         'Milan', 'Camille', 'Lala', 'Adele', 'Hoa', 'Xuan', 'Sabrina', 'Hilda', 'Zelda', 'Mollie', 'Mattie', 'Donnie',
         'Melvin', 'Clarice', 'Stuart', 'Susanna', 'Gwen', 'Christina', 'Lilli', 'Brice', 'Noble', 'Leland', 'Odette',
         'Lincoln', 'Blaine', 'Sidney', 'Rico', 'Isaiah', 'Tad', 'Ernesto', 'Melody', 'Gerard', 'Leena', 'Terese', 'Vicky',
         'Karan', 'Roy', 'Dionne', 'Duncan', 'Adrien', 'Suzanne', 'Hal', 'Benedict', 'Quincy', 'Barton', 'Lorelei', 'Dorothy',
         'Marshall', 'Felix', 'Galen', 'Octavio', 'Drew', 'Jefferson', 'Foster', 'Brooke', 'Meg', 'Hank', 'Jayne', 'Linda', 'Kronk',
         'Celia', 'Denise', 'Donovan', 'Bo', 'Dalton', 'Tanner', 'Caprice', 'Elin', 'Agnes', 'Edie', 'Thea', 'Eddy', 'Laurence', 'Spock',
         'Tijuana', 'Odessa', 'Honey', 'Palmer', 'Hedy', 'Vance', 'Dixie', 'Ester', 'Louise', 'Harriet', 'Tosha', 'Jacques', 'Aku',
         'Marianne', 'Nevada', 'Yan', 'Mitch', 'Bianca', 'Colin', 'Fatima', 'Pablo', 'Taryn', 'Danielle', 'Lorna', 'Yael',
         'Lea', 'Mariah', 'Charity', 'Booker', 'Jana', 'Kirk', 'Scotty', 'Alpha', 'Jarvis', 'Mindy', 'Pingu','Pinga','Caillou',
         'Cornelia', 'Janell', 'Elwood', 'Myung-hoon')

    dismal_characters = (
        'Willem Dafoe', 'Danny DeVito', 'Trent Reznor', 'Brendan Fraser',
        'Jonathan Holmes', 'Val Kilmer (AKA "The Man Who Was The Bat")',
        'Weird Al Yankovic', 'iCarly'
    )

    @staticmethod
    def Jesterize(string):
        cur_actor_inital = 0#random.randrange(0,len(Utils.dismal_characters))
        len_actors = len(Utils.dismal_characters)

        cur_actor = cur_actor_inital

        # This is tricky. Handling some of these manually.
        string = re.sub(r"(?=\W?)(she)(?=\W+)", 'he', string)
        string = re.sub(r"(?=\W?)(herself)(?=\W+)", 'himself', string)
        string = re.sub(r"(?=\W?)(and her)(?=\W+)", 'and his', string)
        string = re.sub(r"(?=\W?)(in her)(?=\W+)", 'in his', string)
        string = re.sub(r"(?=\W?)(her sexual)(?=\W+)", 'his sexual', string)
        string = string.replace('SHIELD.', 'SHIELD')
        string = string.replace('S.H.I.E.L.D.', 'SHIELD')
        #print cur_actor
        for k, name in enumerate(Utils.first_names):
            if (string.find(name) > -1):
                string = re.sub(r"(?=\W?)("+re.escape(name)+")(?=\W+)", Utils.dismal_characters[cur_actor % len_actors], string )
                cur_actor += 1

        #cur_actor = cur_actor_inital
        #print cur_actor
        for k, name in enumerate(Utils.last_names):
            if (string.find(name) > -1):
                string = re.sub(r"(?=\W?)("+re.escape(name)+")(?=\W+)", "", string ) #Utils.dismal_characters[cur_actor % len_actors][1]
                #cur_actor += 1

        return string


def main():
    pass

