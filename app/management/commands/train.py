from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer


class Command(BaseCommand):
    help = "Training the chatbot"

    def handle(self, *args, **options):
        conversations = []
        with open("dialogs.txt", "a+") as f:
            f.seek(0)
            data = f.read()
            data = data.split("\n")

            conversations = []
            for str in data:
                l = str.split("\t")
                conversations.extend((l[0], l[1]))

        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatterbot)
        trainer.train(
            ["Hello",
             "Hi there!",
             "How are you doing?",
             "I'm doing great.",
             "That is good to hear",
             "Thank you.",
             "You're welcome.",

             "can you speak english",
             "yes i can how can i help you",
             
             "tu peux parler en francais",
             "oui je peux comment je peux t'aider",

             "donne moi un documentaire sur la nature",
             "Notre Planète est une série documentaire qui explore les habitats les plus spectaculaires et les plus rares de la planète, ainsi que les animaux qui y habitent. La série est présentée par Sir David Attenborough, célèbre naturaliste et narrateur de nombreux documentaires de la BBC sur la nature.",
             
             "give me a documentary about nature",
             "Planet Earth II is a stunning nature documentary that takes viewers on a journey to some of the most remote and incredible parts of the world. Narrated by Sir David Attenborough, the series consists of six episodes, each one focusing on a different habitat, including islands, mountains, jungles, deserts, grasslands, and cities.",

             "Qui a créé ce chatBot ?",
             "j'étais créé par Reda bouzad et Abdelillah boulgha et Tariq elqari.",

             "Quelle est la date de création de ce chatBot ?",
             "Ce chatbot a été créer en février 2023.",

             "Quel est le but de créer ce chatBot?",
             "Ce chatbot recommande des documentaires.",

             "Dans quelle filière étudient Reda, Abdelilah et Tariq ?",
             "ils étudient dans la filiére SIR ",

             "Qu'est-ce que SIR",
             "SIR est l'abréviation de SYSTEMES INFORMATIQUES REPARTIS.",

             "Dans quelle faculté se trouve cette branche ?",
             "cette filière se trouve dans la faculté des sciences et techniques de Marrakech.",

             "En quelle année cette faculté a-t-elle été créée ?",
             "Cette faculté a été créée en 1991.",

             "C'est qui le doyen de cette faculté ?",
             "Le doyen de cette faculté est M. Mohamed JBILOU.",

             "Quel est le nombre des étudiants dans cette faculté?",
             "Dans cette faculté il y a 3454 étudiants en 2022-2023.",

             "Quelle est le nombre des filières dans cette faculté ?",
             """Dans cette faculté il y a 25 filière de formation : 
              - MIPC .
              - BCG .
              - 8 Licences en Science et Techniques .
              - 5 Masters en Science et Techniques .
              - 6 Filières du Cycle Ingénieur .""",

             "Quel est le nombre des enseignants-chercheurs dans cette faculté ?",
             "le nombre des enseignants-chercheurs dans cette faculté est 198 .",

             " Quel est le nombre de départements dans cette faculté?",
             """ dans cette faculté il y a 8 départements :
              -MATHEMATIQUES 
              -PHYSIQUE APPLIQUÉE 
              -SCIENCES CHIMIQUES 
              -BIOLOGIE 
              -SCIENCES DE LA TERRE 
              -GÉNIE CIVIL 
              -INFORMATIQUE 
              -TECHNIQUES DE COMMUNICATION ET MANAGEMENT""",

             "Recommande-moi les meilleurs documantaires",
             """je vous recommande : - Polar Bear ; 
                                     - The Social Dilemma ;
                                     - For All Humankind ;
                                     - The Real Charlie Chaplin ;
                                     - Pelosi in the House ;
                                     - 9/11: Life Under Attack ;
                                     - The Last Mountain ; 
                                     - Game of Sharks ;
                                     - Real Madrid: Until the End ;
                                     - Our Father ;
                                     - Miss Americana ;
                                     - Sisters on Track ;
                                     - My Octopus Teacher ;
                                     - Her Majesty the Queen ;
                                     - The Great Hack ;
                                     - Athlete A
                                     - Audible
                                     - The Tinder Swindler 
                                     - Stay on Board: The Leo Baker Story
                                     - Hood River
                                     - Torn""",

             "Recommande-moi des documentaires sur la nature",
             """je vous recommande : - Polar Bear ; 
                                     - My Octopus Teacher ;
                                     - The Last MountainThe Volcano ;
                                     - Fantastic Fungi ;""",

             "Recommande-moi des documentaires sur le sport",
             """je vous recommande : - Real Madrid: Until the End ; 
                                     - Athlete A ;
                                     - Messi ; 
                                     - Ronaldo ;
                                     - A Life of Speed ;
                                     - Pelé ;
                                     - Tony Parker: The Final Shot ;
                                     - Untold: Breaking Point ;""",

             "Recommande-moi des documentaires sur la politique",
             """je vous recommande : - Pelosi in the House ;
                                     - Fugitive: The Curious Case of Carlos Ghosn ;
                                     - Harry & Meghan ;
                                     - This Place Rules ;
                                     - Her Majesty the Queen ;
                                     - 9/11: Life Under Attack ;""",

             "Recommande-moi des documentaires sur le hacking",
             """je vous recommande : - Cyber Crime: The Dark Web Uncovered ;
                                     - The Great Hack ;""",

             "Recommande-moi des documentaires sur les réseaux sociaux",
             """je vous recommande : - The Social Dilemma ;
                                     - The Tinder Swindler ;""",

             "Recommande-moi des documentaires sur les légendes",
             """je vous recommande : - Blood Brothers: Malcolm X & Muhammad Ali ;
                                     - Ronaldo ;
                                     - Pelé ;
                                     - Messi ;
                                     - Tony Parker: The Final Shot ;""",

             # documentaire Polar Bear
             "Quel est le pourcentage de gens qui ont aimé le documentaire  Polar Bear ?",
             "68% ont aimé ce documentaire",

             "Description du documentaire Polar Bear: ",
             """Les souvenirs de jeunesse d'une mère ours polaire la préparent à naviguer 
             dans le monde de plus en plus difficile auquel les ours polaires sont confrontés aujourd'hui.""",

             "Quelle est la date de sortie du documentaire Polar Bear?",
             "la date de sortie du documentaire Polar Bear est 2022-04-22.",

             "quel est le genre du film Polar Bear?",
             "le genre du film Polar Bear est documentaire.",

             "quelle est la durée du documentaire Polar Bear ?",
             "la durée du documentaire Polar Bear 1h 24m.",

             "Qui est le réalisateur du documentaire Polar Bear?",
             "le réalisateur du documentaire Polar Bear est  Jeff Wilson , Alastair Fothergill.",

             "Qui sont les personnages du documentaire Polar Bear?",
             "les personnages du documentaire Polar Bear sont  Catherine Keener",

             "Dans quel pays le documentaire Polar Bear a-t-il été réalisé ?",
             " Le documentaire Polar Bear a été produit en france",
             # documentaire The Social Dilemma
             "Quel est le pourcentage de gens qui ont aimé le documentaire The Social Dilemma ?",
             "93% ont aimé ce documentaire",

             "Description du documentaire The Social Dilemma:",
             """Dans ce documentaire inédit, des spécialistes,
              des militants ou encore des anciens employés des géants de la technologie 
              nous ouvrent les yeux sur la vérité cachée derrière nos écrans. 
              Ils sonnent l'alarme  concernant certaines de leurs inventions,
               qui provoquent des addictions et déstabilisent les démocraties.""",

             "Quelle est la date de sortie du documentaire The Social Dilemma?",
             "la date de sortie du documentaire The Social Dilemma est  9 septembre 2020.",

             "quel est le genre du film The Social Dilemma?",
             "le genre du film The Social Dilemma est documentaire.",

             "quelle est la durée du documentaire The Social Dilemma ?",
             "la durée du documentaire The Social Dilemma est 1h 34m.",

             "Qui est le réalisateur du documentaire The Social Dilemma?",
             "le réalisateur du documentaire The Social Dilemma est   Jeff Orlowski.",

             "Qui sont les personnages du documentaire The Social Dilemma?",
             "les personnages du documentaire The Social Dilemma sont  Kara Hayward, Tristan Harris, Barbara Gehring, Vincent Kartheiser, Catalina Garayoa",

             "Dans quel pays le documentaire The Social Dilemma a-t-il été réalisé ?",
             "Le documentaire The Social Dilemma a été produit aux États-Unis",
             # documentaire  For All Humankind
             "Quel est le pourcentage de gens qui ont aimé le documentaire For All Humankind?",
             "87% ont aimé ce documentaire",

             "Description du documentaire For All Humankind:",
             """Réalisé par Al Reinert et avec une musique de Brian Eno, 
             For All Mankind témoigne du programme Apollo de la NASA des années 1960 et 1970. 
             Composé de séquences réelles de la NASA des missions et d'interviews d'astronautes,
              le documentaire offre le point de vue des individus qui ont bravé le remarquable e voyage vers la lune et retour. 
              Lors de la compilation du matériel pour le documentaire, Reinert a parcouru plus de six millions de pieds de documentaire de ces moments historiques.""",

             "Quelle est la date de sortie du documentaire For All Humankind?",
             "la date de sortie du documentaire For All Humankind est  Janvier 1989.",

             "quel est le genre du film For All Humankind?",
             "le genre du film For All Humankind est documentaire.",

             "quelle est la durée du documentaire For All Humankind?",
             "la durée du documentaire For All Humankind est  1h 20m.",

             "Qui est le réalisateur du documentaire For All Humankind?",
             "le réalisateur du documentaire For All Humankind est   Al Reinert.",

             "Qui sont les personnages du documentaire For All Humankind?",
             "les personnages du documentaire For All Humankind sont  Christopher Jackson, Victor Glover, Gloria Steinem, Don Lemon, Sonequa Martin-Green.",

             "Dans quel pays le documentaire For All Humankind a-t-il été réalisé ?",
             "Le documentaire For All Humankind a été produit aux États-Unis",

             # documentaire  The Real Charlie Chaplin

             "Quel est le pourcentage de gens qui ont aimé le documentaire The Real Charlie Chaplin?",
             "48% ont aimé ce documentaire",

             "Description du documentaire The Real Charlie Chaplin:",
             """Combinant des enregistrements audio inédits,
             des reconstitutions dramatiques et des archives personnelles,
             les cinéastes Peter Middleton et James Spinney retracent l'ascension fulgurante de Charlie Chaplin 
             des bidonvilles du Londres victorien jusqu'aux sommets de la célébrité hollywoodienne.""",

             "Quelle est la date de sortie du documentaire The Real Charlie Chaplin?",
             "la date de sortie du documentaire The Real Charlie Chaplin est  2021.",

             "quel est le genre du film The Real Charlie Chaplin?",
             "le genre du film The Real Charlie Chaplin est documentaire.",

             "quelle est la durée du documentaire The Real Charlie Chaplin?",
             "la durée du documentaire The Real Charlie Chaplin est  1h 90m.",

             "Qui est le réalisateur du documentaire The Real Charlie Chaplin?",
             "le réalisateur du documentaire The Real Charlie Chaplin est Peter Middleton , James Spinney.",

             "Qui sont les personnages du documentaire The Real Charlie Chaplin?",
             "les personnages du documentaire The Real Charlie Chaplin sont  Jeff Rawle, Pearl Mackie, Eben Young, Matthew Wolf, Paul Leonard.",

             "Dans quel pays le documentaire The Real Charlie Chaplin a-t-il été réalisé ?",
             "Le documentaire The Real Charlie Chaplin a été produit aux états-unis.",

             # documentaire  Tony Parker: The Final Shot

             "Quel est le pourcentage de gens qui ont aimé le documentaire Tony Parker: The Final Shot?",
             "57% ont aimé ce documentaire",

             "Description du documentaire Tony Parker: The Final Shot:",
             """La vie et la carrière du basketteur Tony Parker, de son enfance en France à sa réussite en NBA,
              en passant par sa guérison d'un quad déchiré.""",

             "Quelle est la date de sortie du documentaire Tony Parker: The Final Shot?",
             "la date de sortie du documentaire Tony Parker: The Final Shot est  6 janvier 2021.",

             "quel est le genre du film Tony Parker: The Final Shot?",
             "le genre du film Tony Parker: The Final Shot est documentaire.",

             "quelle est la durée du documentaire Tony Parker: The Final Shot?",
             "la durée du documentaire Tony Parker: The Final Shot est  1h 38m.",

             "Qui est le réalisateur du documentaire Tony Parker: The Final Shot?",
             "le réalisateur du documentaire Tony Parker: The Final Shot est Florent Bodin.",

             "Qui sont les personnages du documentaire Tony Parker: The Final Shot?",
             "les personnages du documentaire Tony Parker: The Final Shot sont Emanuel Ginóbili, Pau Gasol, Tim Duncan, Tony Parker, Kemba Walker.",

             "Dans quel pays le documentaire Tony Parker: The Final Shot a-t-il été réalisé ?",
             "Le documentaire Tony Parker: The Final Shot a été produit en  France.",

             # documentaire  Torn

             "Quel est le pourcentage de gens qui ont aimé le documentaire Torn ?",
             "79% ont aimé ce documentaire",

             "Description du documentaire Torn:",
             """Le 5 octobre 1999, le légendaire alpiniste Alex Lowe a été tragiquement perdu aux côtés du caméraman
              et compagnon d'escalade David Bridges dans une avalanche sur les pentes de la montagne tibétaine, Shishapangma.""",

             "Quelle est la date de sortie du documentaire Torn?",
             "la date de sortie du documentaire Torn est   2021-12-03.",

             "quel est le genre du film Torn?",
             "le genre du film Torn est documentaire.",

             "quelle est la durée du documentaire Torn?",
             "la durée du documentaire Torn est 1h 32m.",

             "Qui est le réalisateur du documentaire Torn?",
             "le réalisateur du documentaire Torn est Max Lowe.",

             "Qui sont les personnages du documentaire Torn?",
             "les personnages du documentaire Torn sont  Max Lowe, Conrad Anker, Alex Lowe, Sam Lowe, Isaac Lowe.",

             "Dans quel pays le documentaire Torn a-t-il été réalisé ?",
             "Le documentaire Torn a été produit aux états-unis.",

             # documentaire  14 Peaks: Nothing Is Impossible

             "Quel est le pourcentage de gens qui ont aimé le documentaire 14 Peaks: Nothing Is Impossible ?",
             "75% ont aimé ce documentaire",

             "Description du documentaire 14 Peaks: Nothing Is Impossible:",
             """L'intrépide alpiniste népalais Nimsdai Purja se lance dans une quête apparemment impossible
              pour gravir les 14 sommets de 8 000 mètres du monde en sept mois.""",

             "Quelle est la date de sortie du documentaire 14 Peaks: Nothing Is Impossible?",
             "la date de sortie du documentaire 14 Peaks: Nothing Is Impossible est 29 novembre 2021.",

             "quel est le genre du film 14 Peaks: Nothing Is Impossible ?",
             "le genre du film 14 Peaks: Nothing Is Impossible est documentaire.",

             "quelle est la durée du documentaire 14 Peaks: Nothing Is Impossible ?",
             "la durée du documentaire 14 Peaks: Nothing Is Impossible est 1h 41m.",

             "Qui est le réalisateur du documentaire 14 Peaks: Nothing Is Impossible ?",
             "le réalisateur du documentaire 14 Peaks: Nothing Is Impossible est  Catherine Quantschnigg.",

             "Qui sont les personnages du documentaire 14 Peaks: Nothing Is Impossible?",
             "les personnages du documentaire 14 Peaks: Nothing Is Impossible sont  Nirmal Purja,.",

             "Dans quel pays le documentaire 14 Peaks: Nothing Is Impossible a-t-il été réalisé ?",
             "Le documentaire 14 Peaks: Nothing Is Impossible a été produit aux états-unis.",

             # documentaire  Becoming Cousteau

             "Quel est le pourcentage de gens qui ont aimé le documentaire Becoming Cousteau ?",
             "75% ont aimé ce documentaire",

             "Description du documentaire Becoming Cousteau:",
             """L'accent sera mis sur la révolution inventeur-explorateur-écologiste-cinéaste, 
             c'est-à-dire donner à l'humanité les ressources pour explorer l'océan avec l'Aqua Lung,
              attirer l'attention sur la pollution des océans et sa collaboration de longue date.""",

             "Quelle est la date de sortie du documentaire Becoming Cousteau?",
             "la date de sortie du documentaire Becoming Cousteau est 2 septembre 2021.",

             "quel est le genre du film Becoming Cousteau ?",
             "le genre du film Becoming Cousteau est documentaire.",

             "quelle est la durée du documentaire Becoming Cousteau ?",
             "la durée du documentaire Becoming Cousteau est 1h 33m.",

             "Qui est le réalisateur du documentaire Becoming Cousteau ?",
             "le réalisateur du documentaire Becoming Cousteau est Liz Garbus.",

             "Qui sont les personnages du documentaire Becoming Cousteau?",
             "les personnages du documentaire Becoming Cousteau sont Louis Malle, Carol Burnett, Deborah Norville, Vincent Cassel, Jacques-Yves Cousteau.",

             "Dans quel pays le documentaire Becoming Cousteau a-t-il été réalisé ?",
             "Le documentaire Becoming Cousteau a été produit aux états-unis.",

             # documentaire  Convergence: Courage in a Crisis

             "Quel est le pourcentage de gens qui ont aimé le documentaire Convergence: Courage in a Crisis ?",
             "51% ont aimé ce documentaire",

             "Description du documentaire Convergence: Courage in a Crisis:",
             """Alors que le COVID-19 exacerbe les vulnérabilités à travers le monde, des héros méconnus à tous
              les niveaux de la société aident le vent à tourner vers un avenir meilleur.""",

             "Quelle est la date de sortie du documentaire Convergence: Courage in a Crisis?",
             "la date de sortie du documentaire Convergence: Courage in a Crisis est 8 octobre 2021.",

             "quel est le genre du film Convergence: Courage in a Crisis ?",
             "le genre du film Convergence: Courage in a Crisis est documentaire.",

             "quelle est la durée du documentaire Convergence: Courage in a Crisis?",
             "la durée du documentaire Convergence: Courage in a Crisis est 1h 53m.",

             "Qui est le réalisateur du documentaire Convergence: Courage in a Crisis ?",
             "le réalisateur du documentaire Convergence: Courage in a Crisis est Orlando von Einsiedel.",

             "Qui sont les personnages du documentaire Convergence: Courage in a Crisis?",
             "les personnages du documentaire Convergence: Courage in a Crisis sont Wenhua Lin, Sara Khaki, Mohammad Rezi Eyni,.",

             "Dans quel pays le documentaire Convergence: Courage in a Crisis a-t-il été réalisé ?",
             "Le documentaire Convergence: Courage in a Crisis a été produit aux états-unis.",

             # documentaire  Blood Brothers: Malcolm X & Muhammad Ali

             "Quel est le pourcentage de gens qui ont aimé le documentaire Blood Brothers: Malcolm X & Muhammad Ali ?",
             "62% ont aimé ce documentaire",

             "Description du documentaire Blood Brothers: Malcolm X & Muhammad Ali:",
             """L'histoire extraordinaire derrière l'amitié de deux des figures les plus emblématiques du 20e siècle, 
             Muhammad Ali et Malcolm X : le champion olympique charismatique et franc qui a charmé la nation, 
             et l'ex-con-tourné révolutionnaire intellectuel qui s'est élevé contre les maux de l'oppression blanche en disant la vérité au pouvoir.""",

             "Quelle est la date de sortie du documentaire Blood Brothers: Malcolm X & Muhammad Ali?",
             "la date de sortie du documentaire Blood Brothers: Malcolm X & Muhammad Ali est  9 septembre 2021.",

             "quel est le genre du film Blood Brothers: Malcolm X & Muhammad Ali ?",
             "le genre du film Blood Brothers: Malcolm X & Muhammad Ali est documentaire.",

             "quelle est la durée du documentaire Blood Brothers: Malcolm X & Muhammad Ali ?",
             "la durée du documentaire Blood Brothers: Malcolm X & Muhammad Ali est 1h 35m.",

             "Qui est le réalisateur du documentaire Blood Brothers: Malcolm X & Muhammad Ali ?",
             "le réalisateur du documentaire Blood Brothers: Malcolm X & Muhammad Ali est Marcus A. Clarke.",

             "Qui sont les personnages du documentaire Blood Brothers: Malcolm X & Muhammad Ali?",
             "les personnages du documentaire Blood Brothers: Malcolm X & Muhammad Ali sont Muhammad Ali, Malcolm X,.",

             "Dans quel pays le documentaire Blood Brothers: Malcolm X & Muhammad Ali a-t-il été réalisé ?",
             "Le documentaire Blood Brothers: Malcolm X & Muhammad Ali a été produit aux états-unis.",

             # documentaire  Hood River

             "Quel est le pourcentage de gens qui ont aimé le documentaire Hood River?",
             "62% ont aimé ce documentaire",

             "Description du documentaire Hood River:",
             """Les joueurs de football du lycée de Hood River, 
             en Oregon, luttent pour coexister racialement tout en se frayant un chemin vers un championnat d'État.""",

             "Quelle est la date de sortie du documentaire Hood River?",
             "la date de sortie du documentaire Hood River est 2021-09-10.",

             "quel est le genre du film Hood River ?",
             "le genre du film Hood River est documentaire.",

             "quelle est la durée du documentaire Hood River?",
             "la durée du documentaire Hood River est 82m.",

             "Qui est le réalisateur du documentaire Hood River ?",
             "le réalisateur du documentaire Hood River est Jonathan Field , Steven Cantor.",

             "Dans quel pays le documentaire Hood River a-t-il été réalisé ?",
             "Le documentaire Hood River a été produit aux états-unis.",

             # documentaire  This Place Rules

             "Quel est le pourcentage de gens qui ont aimé le documentaire This Place Rules ?",
             "96% ont aimé ce documentaire",

             """Description du documentaire This Place Rules:
             This Place Rules est un film documentaire américain de 2022 réalisé par Andrew Callaghan 
             lors de ses débuts en tant que réalisateur. Il suit Callaghan alors qu'il voyage à travers les États-Unis 
             dans les mois précédant l'attaque du 6 janvier contre le Capitole""",

             "Quelle est la date de sortie du documentaire This Place Rules?",
             "la date de sortie du documentaire This Place Rules est 30 décembre 2022.",

             "quel est le genre du film This Place Rules ?",
             "le genre du film This Place Rules est documentaire.",

             "quelle est la durée du documentaire This Place Rules ?",
             "la durée du documentaire This Place Rules est 1h 22m.",

             "Qui est le réalisateur du documentaire This Place Rules ?",
             "le réalisateur du documentaire This Place Rules est  Dave Kneebone.",

             "Qui sont les personnages du documentaire This Place Rules?",
             "les personnages du documentaire This Place Rules sont  Andrew Callaghan, Alex Jones, Mike Busey, Edward X. Young,.",

             "Dans quel pays le documentaire This Place Rules a-t-il été réalisé ?",
             "Le documentaire This Place Rules a été produit aux états-unis.",

             # documentaire   Pelosi in the House

             "Quel est le pourcentage de gens qui ont aimé le documentaire Pelosi in the House ?",
             "86% ont aimé ce documentaire",

             "Description du documentaire  Pelosi in the House:",
             """Pelosi in the House est un film documentaire américain de 2022 sur la députée américaine Nancy Pelosi.
              Sorti en décembre 2022 sur HBO, il offre un aperçu des coulisses de la carrière de Pelosi. 
              Le SF Chronicle a qualifié le film de "visionnement essentiel""",

             "Quelle est la date de sortie du documentaire  Pelosi in the House?",
             "la date de sortie du documentaire  Pelosi in the House est 13 décembre 2022 .",

             "quel est le genre du film  Pelosi in the House ?",
             "le genre du film  Pelosi in the House est documentaire.",

             "quelle est la durée du documentaire Pelosi in the House ?",
             "la durée du documentaire  Pelosi in the House est 1h 29m.",

             "Qui est le réalisateur du documentaire  Pelosi in the House ?",
             "le réalisateur du documentaire  Pelosi in the House est  Alexandra Pelosi .",

             "Qui sont les personnages du documentaire  Pelosi in the House ?",
             "les personnages du documentaire  Pelosi in the House sont  Nancy Pelosi.",

             "Dans quel pays le documentaire  Pelosi in the House a-t-il été réalisé ?",
             "Le documentaire  Pelosi in the House a été produit aux états-unis.",

             # documentaire   Ronaldo

             "Quel est le pourcentage de gens qui ont aimé le documentaire Ronaldo ?",
             "79% ont aimé ce documentaire",

             "Description du documentaire Ronaldo:",
             """Documentaire retraçant la vie de la superstar du football portugais Chistiano Ronaldo. 
             De ses humbles débuts à sa carrière record, ce film raconte l'histoire 
             de l'une des stars du sport les plus renommées au monde.""",

             "Quelle est la date de sortie du documentaire Ronaldo?",
             "la date de sortie du documentaire Ronaldo est  9 novembre 2015 .",

             "quel est le genre du film Ronaldo ?",
             "le genre du film Ronaldo est documentaire.",

             "quelle est la durée du documentaire Ronaldo ?",
             "la durée du documentaire Ronaldo est 1h 32m.",

             "Qui est le réalisateur du documentaire Ronaldo ?",
             "le réalisateur du documentaire Ronaldo est Anthony Wonke .",

             "Qui sont les personnages du documentaire Ronaldo ?",
             "les personnages du documentaire Ronaldo sont  Cristiano Ronaldo, Lionel Messi, Dolores Aveiro, Hugo Aveiro, Georgie Bingham.",

             "Dans quel pays le documentaire Ronaldo a-t-il été réalisé ?",
             "Le documentaire Ronaldo a été produit au Royaume-Uni.",

             # documentaire   9/11: Life Under Attack

             "Quel est le pourcentage de gens qui ont aimé le documentaire 9/11: Life Under Attack ?",
             "83% ont aimé ce documentaire",

             "Description du documentaire 9/11: Life Under Attack:",
             """11 septembre 2001 : le jour qui a changé l'histoire du monde lorsque deux avions de ligne ont percuté 
             le World Trade Center à New York. Raconter les histoires personnelles de ceux qui ont vécu 
             les événements et enregistré ce qu'ils ont vécu.""",

             "Quelle est la date de sortie du documentaire 9/11: Life Under Attack?",
             "la date de sortie du documentaire 9/11: Life Under Attack est 2021-09-03 .",

             "quel est le genre du film 9/11: Life Under Attack ?",
             "le genre du film 9/11: Life Under Attack est documentaire.",

             "quelle est la durée du documentaire 9/11: Life Under Attack ?",
             "la durée du documentaire 9/11: Life Under Attack est 77 min.",

             "Qui est le réalisateur du documentaire 9/11: Life Under Attack ?",
             "le réalisateur du documentaire 9/11: Life Under Attack est Karen Edwards.",

             "Dans quel pays le documentaire 9/11: Life Under Attack a-t-il été réalisé ?",
             "Le documentaire 9/11: Life Under Attack a été produit au Royaume-Uni.",

             # documentaire   Fugitive: The Curious Case of Carlos Ghosn

             "Quel est le pourcentage de gens qui ont aimé le documentaire Fugitive: The Curious Case of Carlos Ghosn ?",
             "89% ont aimé ce documentaire",

             "Description du documentaire Fugitive: The Curious Case of Carlos Ghosn:",
             """Il relate l'ascension de Carlos Ghosn ainsi que les rivalités et tensions internes 
             qu'il a suscitées au sein de Nissan-Renault et son arrestation dramatique.""",

             "Quelle est la date de sortie du documentaire Fugitive: The Curious Case of Carlos Ghosn?",
             "la date de sortie du documentaire Fugitive: The Curious Case of Carlos Ghosn est  26 octobre 2022 .",

             "quel est le genre du film Fugitive: The Curious Case of Carlos Ghosn ?",
             "le genre du film Fugitive: The Curious Case of Carlos Ghosn est documentaire.",

             "quelle est la durée du documentaire Fugitive: The Curious Case of Carlos Ghosn?",
             "la durée du documentaire Fugitive: The Curious Case of Carlos Ghosn est 95 min.",

             "Qui est le réalisateur du documentaire Fugitive: The Curious Case of Carlos Ghosn ?",
             "le réalisateur du documentaire Fugitive: The Curious Case of Carlos Ghosn est  Lucy Blakstad .",

             "Qui sont les personnages du documentaire Fugitive: The Curious Case of Carlos Ghosn ?",
             "les personnages du documentaire Fugitive: The Curious Case of Carlos Ghosn sont  Carlos Ghosn.",

             "Dans quel pays le documentaire Fugitive: The Curious Case of Carlos Ghosn a-t-il été réalisé ?",
             "Le documentaire Fugitive: The Curious Case of Carlos Ghosn a été produit aux Etats-Unis.",

             # documentaire   The Last Mountain

             "Quel est le pourcentage de gens qui ont aimé le documentaire The Last Mountain ?",
             "35% ont aimé ce documentaire",

             "Description du documentaire The Last Mountain:",
             """L'histoire de l'alpiniste de 30 ans Tom Ballard qui a disparu sur l'une des montagnes les plus meurtrières de l'Himalaya en février 2019.
              Tom était le fils de l'alpiniste Alison Hargreaves, qui a péri sur le K2 en 1995. 
              Mère et fils, deux des plus grands grimpeurs de tous les temps, mort à peu près au même âge dans le même chaîne de montagnes,
               tous deux faisant ce qu'ils aimaient le plus. Ils reposent maintenant à jamais enfermés dans la glace du haut Himalaya.""",

             "Quelle est la date de sortie du documentaire The Last Mountain?",
             "la date de sortie du documentaire The Last Mountain est  26 septembre 2021 .",

             "quel est le genre du film The Last Mountain ?",
             "le genre du film The Last Mountain est documentaire.",

             "quelle est la durée du documentaire The Last Mountain ?",
             "la durée du documentaire The Last Mountain est 1h 47m.",

             "Qui est le réalisateur du documentaire The Last Mountain ?",
             "le réalisateur du documentaire The Last Mountain est Chris Terrill.",

             "Qui sont les personnages du documentaire The Last Mountain ?",
             "les personnages du documentaire The Last Mountain sont Jim Ballard, Tom Ballard, Daniele Nardi, Kate Ballard.",

             "Dans quel pays le documentaire The Last Mountain a-t-il été réalisé ?",
             "Le documentaire The Last Mountain a été produit aux Etats-Unis.",

             # documentaire   Cyber Crime: The Dark Web Uncovered

             "Quel est le pourcentage de gens qui ont aimé le documentaire Cyber Crime: The Dark Web Uncovered ?",
             "67% ont aimé ce documentaire",

             "Description du documentaire Cyber Crime: The Dark Web Uncovered:",
             """11 des meilleurs experts mondiaux en cybersécurité se réunissent pour explorer et répondre aux questions sur le dark web.
              Qu'est-ce que le darkweb ? Que peux tu trouver là-bas? Et surtout, comment les propriétaires d'entreprise peuvent-ils prendre 
              les mesures appropriées pour réduire leurs risques d'être victimes de la cybercriminalité ?""",

             "Quelle est la date de sortie du documentaire Cyber Crime: The Dark Web Uncovered?",
             "la date de sortie du documentaire Cyber Crime: The Dark Web Uncovered est 2022-08-12.",

             "quel est le genre du film Cyber Crime: The Dark Web Uncovered ?",
             "le genre du film Cyber Crime: The Dark Web Uncovered est documentaire.",

             "quelle est la durée du documentaire Cyber Crime: The Dark Web Uncovered ?",
             "la durée du documentaire Cyber Crime: The Dark Web Uncovered est 75 min.",

             "Qui est le réalisateur du documentaire Cyber Crime: The Dark Web Uncovered ?",
             "le réalisateur du documentaire Cyber Crime: The Dark Web Uncovered est Jeff Roldan.",

             "Dans quel pays le documentaire Cyber Crime: The Dark Web Uncovered a-t-il été réalisé ?",
             "Le documentaire Cyber Crime: The Dark Web Uncovered a été produit aux Etats-Unis.",

             # documentaire   Game of Sharks

             "Quel est le pourcentage de gens qui ont aimé le documentaire Game of Sharks ?",
             "35% ont aimé ce documentaire",

             "Description du documentaire Game of Sharks:",
             """ESPN couvre des événements monumentaux de l'histoire du sport mettant en vedette les meilleurs conteurs d'aujourd'hui 
             de l'intérieur et de l'extérieur du monde du sport.""",

             "Quelle est la date de sortie du documentaire Game of Sharks?",
             "la date de sortie du documentaire Game of Sharks est  12 juillet 2022 .",

             "quel est le genre du film Game of Sharks ?",
             "le genre du film Game of Sharks est documentaire.",

             "quelle est la durée du documentaire Game of Sharks ?",
             "la durée du documentaire Game of Sharks est 45 min.",

             "Dans quel pays le documentaire Game of Sharks a-t-il été réalisé ?",
             "Le documentaire Game of Sharks a été produit aux Etats-Unis.",

             # documentaire   Real Madrid: Until the End

             "Quel est le pourcentage de gens qui ont aimé le documentaire Real Madrid: Until the End ?",
             "98% ont aimé ce documentaire",

             "Description du documentaire Real Madrid: Until the End:",
             """Un aperçu des coulisses de la saison 2021-2022 du club de football, 
             remplie de victoires de retour et d'héroïsmes sur le terrain de la part des vétérans et des nouveaux arrivants.""",

             "Quelle est la date de sortie du documentaire Real Madrid: Until the End?",
             "la date de sortie du documentaire Real Madrid: Until the End est  10 mars 2023 .",

             "quel est le genre du film Real Madrid: Until the End ?",
             "le genre du film Real Madrid: Until the End est documentaire.",

             "quelle est la durée du documentaire Real Madrid: Until the End ?",
             "la durée du documentaire Real Madrid: Until the End est 45 min.",

             "Dans quel pays le documentaire Real Madrid: Until the End a-t-il été réalisé ?",
             "Le documentaire Real Madrid: Until the End a été produit aux Etats-Unis.",

             # documentaire   Our Father

             "Quel est le pourcentage de gens qui ont aimé le documentaire Our Father ?",
             "88% ont aimé ce documentaire",

             "Description du documentaire Our Father:",
             """Après qu'un test ADN à domicile d'une femme révèle plusieurs demi-frères et sœurs, 
             elle découvre un stratagème choquant impliquant le sperme d'un donneur et le célèbre et controversé 
             spécialiste de la fertilité, le docteur Donald Cline.""",

             "Quelle est la date de sortie du documentaire Our Father?",
             "la date de sortie du documentaire Our Father est  11 mai 2022.",

             "quel est le genre du film Our Father ?",
             "le genre du film Our Father est documentaire.",

             "quelle est la durée du documentaire Our Father ?",
             "la durée du documentaire Our Father est 1h 37m.",

             "Qui est le réalisateur du documentaire Our Father ?",
             "le réalisateur du documentaire Our Father est Lucie Jourdan.",

             "Qui sont les personnages du documentaire Our Father ?",
             "les personnages du documentaire Our Father sont  Simone-Elise Girard, Kylene Gott, Donald Cline, Julie Harmon, Matt White .",

             "Dans quel pays le documentaire Our Father a-t-il été réalisé ?",
             "Le documentaire Our Father a été produit aux Etats-Unis.",

             # documentaire   Trust No One: The Hunt for the Crypto King

             "Quel est le pourcentage de gens qui ont aimé le documentaire Trust No One: The Hunt for the Crypto King ?",
             "82% ont aimé ce documentaire",

             "Description du documentaire Trust No One: The Hunt for the Crypto King:",
             """Un groupe d'investisseurs devenus détectives tente de débloquer la mort suspecte du multimillionnaire 
             de crypto-monnaie Gerry Cotten et les 250 millions de dollars manquants qu'ils pensent qu'il leur a volés.""",

             "Quelle est la date de sortie du documentaire Trust No One: The Hunt for the Crypto King?",
             "la date de sortie du documentaire Trust No One: The Hunt for the Crypto King est 30 mars 2022.",

             "quel est le genre du film Trust No One: The Hunt for the Crypto King ?",
             "le genre du film Trust No One: The Hunt for the Crypto King est documentaire.",

             "quelle est la durée du documentaire Trust No One: The Hunt for the Crypto King ?",
             "la durée du documentaire Trust No One: The Hunt for the Crypto King est 90 min.",

             "Qui est le réalisateur du documentaire Trust No One: The Hunt for the Crypto King ?",
             "le réalisateur du documentaire Trust No One: The Hunt for the Crypto King est Luke Sewell.",

             "Qui sont les personnages du documentaire Trust No One: The Hunt for the Crypto King ?",
             "les personnages du documentaire Trust No One: The Hunt for the Crypto King sont Jim Ballard, Tom Ballard, Daniele Nardi, Kate Ballard.",

             "Dans quel pays le documentaire Trust No One: The Hunt for the Crypto King a-t-il été réalisé ?",
             "Le documentaire Trust No One: The Hunt for the Crypto King a été produit au Royaume-Uni.",

             # documentaire   Athlete A

             "Quel est le pourcentage de gens qui ont aimé le documentaire Athlete A ?",
             "82% ont aimé ce documentaire",

             "Description du documentaire Athlete A:",
             """Des reporters de The Indianapolis Star exposent la culture toxique au sein de USA Gymnastics 
             alors que la vérité sur le Dr Larry Nassar qui a abusé sexuellement de jeunes gymnastes est révélée.""",

             "Quelle est la date de sortie du documentaire Athlete A?",
             "la date de sortie du documentaire Athlete A est  26 septembre 2021 .",

             "quel est le genre du film Athlete A ?",
             "le genre du film Athlete A est documentaire.",

             "quelle est la durée du documentaire Athlete A ?",
             "la durée du documentaire Athlete A est  24 juin 2020",

             "Qui est le réalisateur du documentaire Athlete A ?",
             "le réalisateur du documentaire Athlete A est Bonni Cohen .",

             "Qui sont les personnages du documentaire Athlete A ?",
             "les personnages du documentaire Athlete A sont  Géza Poszar, Jen Sey, Jamie Dantzscher, Maggie Nichols, Rachael Denhollander.",

             "Dans quel pays le documentaire Athlete A a-t-il été réalisé ?",
             "Le documentaire Athlete A a été produit aux Etats-Unis.",

             # documentaire   Free to Play

             "Quel est le pourcentage de gens qui ont aimé le documentaire Free to Play ?",
             "39% ont aimé ce documentaire",

             "Description du documentaire Free to Play:",
             """Trois joueurs de jeux vidéo professionnels surmontent l'adversité, 
             les pressions familiales et d'autres difficultés pour participer à un tournoi avec un prix d'un million de dollars.""",

             "Quelle est la date de sortie du documentaire Free to Play?",
             "la date de sortie du documentaire Free to Play est 19 mars 2014.",

             "quel est le genre du film Free to Play ?",
             "le genre du film Free to Play est documentaire.",

             "quelle est la durée du documentaire Free to Play ?",
             "la durée du documentaire Free to Play est 1h 15m.",

             "Qui est le réalisateur du documentaire Free to Play ?",
             "le réalisateur du documentaire Free to Play est Valve Company.",

             "Qui sont les personnages du documentaire Free to Play ?",
             "les personnages du documentaire Free to Play sont  Benedict Lim, Danil Ishutin, Clinton Loomis.",

             "Dans quel pays le documentaire Free to Play a-t-il été réalisé ?",
             "Le documentaire Free to Play a été produit aux Etats-Unis.",

             # documentaire   Stay on Board: The Leo Baker Story

             "Quel est le pourcentage de gens qui ont aimé le documentaire Stay on Board: The Leo Baker Story ?",
             "88% ont aimé ce documentaire",

             "Description du documentaire Stay on Board: The Leo Baker Story:",
             """Le skateur de compétition Leo Baker fait face à un tournant dans sa vie à l'approche des Jeux olympiques de 2020.""",

             "Quelle est la date de sortie du documentaire Stay on Board: The Leo Baker Story?",
             "la date de sortie du documentaire Stay on Board: The Leo Baker Story est 11 août 2022.",

             "quel est le genre du film Stay on Board: The Leo Baker Story ?",
             "le genre du film Stay on Board: The Leo Baker Story est documentaire.",

             "quelle est la durée du documentaire Stay on Board: The Leo Baker Story ?",
             "la durée du documentaire Stay on Board: The Leo Baker Story est 1h 12min.",

             "Qui est le réalisateur du documentaire Stay on Board: The Leo Baker Story ?",
             "le réalisateur du documentaire Stay on Board: The Leo Baker Story est Giovanni Reda.",

             "Qui sont les personnages du documentaire Stay on Board: The Leo Baker Story ?",
             "les personnages du documentaire Stay on Board: The Leo Baker Story sont Leo Baker.",

             "Dans quel pays le documentaire Stay on Board: The Leo Baker Story a-t-il été réalisé ?",
             "Le documentaire Stay on Board: The Leo Baker Story a été produit aux Etats-Unis.",

             # documentaire   Miss Americana

             "Quel est le pourcentage de gens qui ont aimé le documentaire Miss Americana ?",
             "81% ont aimé ce documentaire",

             "Description du documentaire Miss Americana:",
             """La chanteuse pop Taylor Swift révèle des détails intimes de sa vie tout en présentant 
             des séquences de concerts en coulisses et sur scène.""",

             "Quelle est la date de sortie du documentaire Miss Americana?",
             "la date de sortie du documentaire Miss Americana est 31 janvier 2020.",

             "quel est le genre du film Miss Americana ?",
             "le genre du film Miss Americana est documentaire.",

             "quelle est la durée du documentaire Miss Americana ?",
             "la durée du documentaire Miss Americana est 1h 25m.",

             "Qui est le réalisateur du documentaire Miss Americana ?",
             "le réalisateur du documentaire Miss Americana est Lana Wilson.",

             "Qui sont les personnages du documentaire Miss Americana ?",
             "les personnages du documentaire Miss Americana sont  Todrick Hall, Antoni Porowski, Jonathan van Ness, Bobby Berk, Taylor Swift.",

             "Dans quel pays le documentaire Miss Americana a-t-il été réalisé ?",
             "Le documentaire Miss Americana a été produit aux Etats-Unis.",

             # documentaire   Pelé

             "Quel est le pourcentage de gens qui ont aimé le documentaire Pelé ?",
             "77% ont aimé ce documentaire",

             "Description du documentaire Pelé:",
             """L'histoire définitive de l'homme qui a personnifié le football,
              qu'il appelait "le beau jeu", et comment il a changé l'histoire de ce sport.""",

             "Quelle est la date de sortie du documentaire Pelé?",
             "la date de sortie du documentaire Pelé est  23 février 2021 .",

             "quel est le genre du film Pelé ?",
             "le genre du film Pelé est documentaire.",

             "quelle est la durée du documentaire Pelé ?",
             "la durée du documentaire Pelé est 1h 48m.",

             "Qui est le réalisateur du documentaire Pelé ?",
             "le réalisateur du documentaire Pelé est David Tryhorn .",

             "Qui sont les personnages du documentaire Pelé ?",
             "les personnages du documentaire Pelé sont Pelé, Zagallo.",

             "Dans quel pays le documentaire Pelé a-t-il été réalisé ?",
             "Le documentaire Pelé a été produit aux Etats-Unis.",

             # documentaire   Audible

             "Quel est le pourcentage de gens qui ont aimé le documentaire Audible ?",
             "52% ont aimé ce documentaire",

             "Description du documentaire Audible:",
             """Ébranlé par le suicide d'un ami, un footballeur sourd du secondaire fait face à sa famille 
             et à ses relations tout en anticipant son dernier match de retour.""",

             "Quelle est la date de sortie du documentaire Audible?",
             "la date de sortie du documentaire Audible est 29 avril 2021.",

             "quel est le genre du film Audible ?",
             "le genre du film Audible est documentaire.",

             "quelle est la durée du documentaire Audible ?",
             "la durée du documentaire Audible est 39 min.",

             "Qui est le réalisateur du documentaire Audible ?",
             "le réalisateur du documentaire Audible est Matt Ogens.",

             "Qui sont les personnages du documentaire Audible ?",
             "les personnages du documentaire Audible sont Amaree McKenstry-Hall,.",

             "Dans quel pays le documentaire Audible a-t-il été réalisé ?",
             "Le documentaire Audible a été produit aux Etats-Unis.",

             # documentaire   Sisters on Track

             "Quel est le pourcentage de gens qui ont aimé le documentaire Sisters on Track ?",
             "72% ont aimé ce documentaire",

             "Description du documentaire Sisters on Track:",
             """Une histoire de passage à l'âge adulte, se déroulant à New York, sur la fraternité métaphorique et littérale des jeunes athlètes Tai, 
             Rainn et Brooke Sheppard, qui ont excellé dans leur équipe d'athlétisme tout en vivant dans un refuge pour sans-abri avec leur mère célibataire, Tonia .""",

             "Quelle est la date de sortie du documentaire Sisters on Track?",
             "la date de sortie du documentaire Sisters on Track est 21 avril 2021.",

             "quel est le genre du film Sisters on Track ?",
             "le genre du film Sisters on Track est documentaire.",

             "quelle est la durée du documentaire Sisters on Track ?",
             "la durée du documentaire Sisters on Track est 1h 36m.",

             "Qui est le réalisateur du documentaire Sisters on Track ?",
             "le réalisateur du documentaire Sisters on Track est Corinne van der Borch.",

             "Dans quel pays le documentaire Sisters on Track a-t-il été réalisé ?",
             "Le documentaire Sisters on Track a été produit aux Etats-Unis.",

             # documentaire   Untold: Breaking Point

             "Quel est le pourcentage de gens qui ont aimé le documentaire Untold: Breaking Point ?",
             "68% ont aimé ce documentaire",

             "Description du documentaire Untold: Breaking Point:",
             """Untold: Breaking Point est un film documentaire biographique américain de 2021 réalisé pour Netflix et réalisé par Chapman Way et Maclain Way.""",

             "Quelle est la date de sortie du documentaire Untold: Breaking Point?",
             "la date de sortie du documentaire Untold: Breaking Point est  7 septembre 2021.",

             "quel est le genre du film Untold: Breaking Point ?",
             "le genre du film Untold: Breaking Point est documentaire.",

             "quelle est la durée du documentaire Untold: Breaking Point ?",
             "la durée du documentaire Untold: Breaking Point est 1h8m.",

             "Qui est le réalisateur du documentaire Untold: Breaking Point ?",
             "le réalisateur du documentaire Untold: Breaking Point est Chapman Way.",

             "Dans quel pays le documentaire Untold: Breaking Point a-t-il été réalisé ?",
             "Le documentaire Untold: Breaking Point a été produit aux Etats-Unis.",

             # documentaire   Icarus 2017

             "Quel est le pourcentage de gens qui ont aimé le documentaire Icarus 2017 ?",
             "87% ont aimé ce documentaire",

             "Description du documentaire Icarus 2017:",
             """Lorsque le cinéaste Bryan Fogel entreprend de découvrir la vérité sur le dopage dans le sport, 
             une rencontre fortuite avec un scientifique russe transforme son histoire 
             d'une expérience personnelle en un thriller géopolitique. L'urine sale, la mort inexpliquée et l'or olympique font tous partie 
             de la révélation du plus grand scandale de l'histoire du sport.""",

             "Quelle est la date de sortie du documentaire Icarus 2017?",
             "la date de sortie du documentaire Icarus 2017 est  20 janvier 2017 .",

             "quel est le genre du film Icarus 2017 ?",
             "le genre du film Icarus 2017 est documentaire.",

             "quelle est la durée du documentaire Icarus 2017 ?",
             "la durée du documentaire Icarus 2017 est 2 heures.",

             "Qui est le réalisateur du documentaire Icarus 2017 ?",
             "le réalisateur du documentaire Icarus 2017 est Bryan Fogel.",

             "Qui sont les personnages du documentaire Icarus 2017 ?",
             "les personnages du documentaire Icarus 2017 sont  Victor Webster, Bryan Fogel, Grigory Rodchenkov, Nikita Kamaev, Dan Cogan.",

             "Dans quel pays le documentaire Icarus 2017 a-t-il été réalisé ?",
             "Le documentaire Icarus 2017 a été produit aux Etats-Unis.",

             # documentaire   A Life of Speed

             "Quel est le pourcentage de gens qui ont aimé le documentaire A Life of Speed ?",
             "58% ont aimé ce documentaire",

             "Description du documentaire A Life of Speed:",
             """A Life of Speed: The Juan Manuel Fangio Story est un film documentaire de 2020 réalisé par Francisco Macri 
             et mettant en vedette Fernando Alonso, Jackie Stewart et Mika Häkkinen. 
             La prémisse tourne autour de Juan Manuel Fangio dans les années 1950 et de la façon dont il a remporté cinq championnats au volant
              de quatre constructeurs automobiles différents""",

             "Quelle est la date de sortie du documentaire A Life of Speed?",
             "la date de sortie du documentaire A Life of Speed est  20 mars 2020.",

             "quel est le genre du film A Life of Speed ?",
             "le genre du film A Life of Speed est documentaire.",

             "quelle est la durée du documentaire A Life of Speed ?",
             "la durée du documentaire A Life of Speed est 1h 32m.",

             "Qui est le réalisateur du documentaire A Life of Speed ?",
             "le réalisateur du documentaire A Life of Speed est Francisco Macri.",

             "Qui sont les personnages du documentaire A Life of Speed ?",
             "les personnages du documentaire A Life of Speed sont  Jackie Stewart, Mika Häkkinen, Carlos Reutemann, Fernando Alonso, Alain Prost.",

             "Dans quel pays le documentaire A Life of Speed a-t-il été réalisé ?",
             "Le documentaire A Life of Speed a été produit en Argentine.",

             # documentaire   My Octopus Teacher

             "Quel est le pourcentage de gens qui ont aimé le documentaire My Octopus Teacher ?",
             "95% ont aimé ce documentaire",

             "Description du documentaire My Octopus Teacher:",
             """Un cinéaste commence à plonger dans une forêt d'algues au large des côtes sud-africaines 
             et rencontre une pieuvre femelle qui lui jette un sort.""",

             "Quelle est la date de sortie du documentaire My Octopus Teacher?",
             "la date de sortie du documentaire My Octopus Teacher est 4 septembre 2020.",

             "quel est le genre du film My Octopus Teacher ?",
             "le genre du film My Octopus Teacher est documentaire.",

             "quelle est la durée du documentaire My Octopus Teacher ?",
             "la durée du documentaire My Octopus Teacher est 1h 30m.",

             "Qui est le réalisateur du documentaire My Octopus Teacher ?",
             "le réalisateur du documentaire My Octopus Teacher est James Reed.",

             "Qui sont les personnages du documentaire My Octopus Teacher ?",
             "les personnages du documentaire My Octopus Teacher sont Craig Foster.",

             "Dans quel pays le documentaire My Octopus Teacher a-t-il été réalisé ?",
             "Le documentaire My Octopus Teacher a été produit en Afrique du Sud.",

             # documentaire   The Great Hack

             "Quel est le pourcentage de gens qui ont aimé le documentaire The Great Hack ?",
             "81% ont aimé ce documentaire",

             "Description du documentaire The Great Hack:",
             """Explorer comment une société de données nommée Cambridge Analytica est devenue le symbole du côté obscur
              des médias sociaux à la suite de l'élection présidentielle américaine de 2016, 
              comme l'a découvert la journaliste Carole Cadwalladr.""",

             "Quelle est la date de sortie du documentaire The Great Hack?",
             "la date de sortie du documentaire The Great Hack est  26 janvier 2019.",

             "quel est le genre du film The Great Hack ?",
             "le genre du film The Great Hack est documentaire.",

             "quelle est la durée du documentaire The Great Hack ?",
             "la durée du documentaire The Great Hack est 2h 19m.",

             "Qui est le réalisateur du documentaire The Great Hack ?",
             "le réalisateur du documentaire The Great Hack est Jehane Noujaim.",

             "Qui sont les personnages du documentaire The Great Hack ?",
             "les personnages du documentaire The Great Hack sont  Paul-Olivier Dehaye, Ravi Naik, Paul Hilder, Gill Phillips, Carole Cadwalladr.",

             "Dans quel pays le documentaire The Great Hack a-t-il été réalisé ?",
             "Le documentaire The Great Hack a été produit aux Etats-Unis.",

             # documentaire   Fantastic Fungi

             "Quel est le pourcentage de gens qui ont aimé le documentaire Fantastic Fungi ?",
             "93% ont aimé ce documentaire",

             "Description du documentaire Fantastic Fungi:",
             """Un voyage descriptif en accéléré sur le monde magique, 
             mystérieux et médicinal des champignons et leur pouvoir de guérison, de maintien et de contribution 
             à la régénération de la vie sur Terre qui a commencé il y a 3,5 milliards d'années.""",

             "Quelle est la date de sortie du documentaire Fantastic Fungi?",
             "la date de sortie du documentaire Fantastic Fungi est 11 octobre 2019.",

             "quel est le genre du film Fantastic Fungi ?",
             "le genre du film Fantastic Fungi est documentaire.",

             "quelle est la durée du documentaire Fantastic Fungi ?",
             "la durée du documentaire Fantastic Fungi est 1h 21m.",

             "Qui est le réalisateur du documentaire Fantastic Fungi ?",
             "le réalisateur du documentaire Fantastic Fungi est Louie Schwartzberg.",

             "Qui sont les personnages du documentaire Fantastic Fungi ?",
             "les personnages du documentaire Fantastic Fungi sont  Michael Pollan, Mary P. Cosmiano, Brie Larson, Roland Griffiths, Andrew Weil.",

             "Dans quel pays le documentaire Fantastic Fungi a-t-il été réalisé ?",
             "Le documentaire Fantastic Fungi a été produit aux Etats-Unis.",

             # documentaire   The Volcano

             "Quel est le pourcentage de gens qui ont aimé le documentaire The Volcano ?",
             "93% ont aimé ce documentaire",

             "Description du documentaire The Volcano:",
             """Lors d'un voyage touristique sur une île isolée,
              47 touristes et guides sont piégés par une éruption volcanique au large des côtes de la Nouvelle-Zélande en 2019.
               Des images minute par minute et des témoignages personnels témoignent de la tragédie qui fera 22 morts.""",

             "Quelle est la date de sortie du documentaire The Volcano?",
             "la date de sortie du documentaire The Volcano est   2022-11-03.",

             "quel est le genre du film The Volcano ?",
             "le genre du film The Volcano est documentaire.",

             "quelle est la durée du documentaire The Volcano ?",
             "la durée du documentaire The Volcano est 97 min.",

             "Qui est le réalisateur du documentaire The Volcano ?",
             "le réalisateur du documentaire The Volcano est Rory Kennedy.",

             "Dans quel pays le documentaire The Volcano a-t-il été réalisé ?",
             "Le documentaire The Volcano a été produit aux Etats-Unis.",

             # documentaire   The Tinder Swindler

             "Quel est le pourcentage de gens qui ont aimé le documentaire The Tinder Swindler ?",
             "90% ont aimé ce documentaire",

             "Description du documentaire The Tinder Swindler:",
             """Un groupe de femmes victimes d'un escroc basé sur une application de rencontres se réunit pour
              tenter de le traquer et de récupérer les millions de dollars qui leur ont été volés.""",

             "Quelle est la date de sortie du documentaire The Tinder Swindler?",
             "la date de sortie du documentaire The Tinder Swindler est  26 septembre 2021 .",

             "quel est le genre du film The Tinder Swindler ?",
             "le genre du film The Tinder Swindler est documentaire.",

             "quelle est la durée du documentaire The Tinder Swindler ?",
             "la durée du documentaire The Tinder Swindler est 2 février 2022.",

             "Qui est le réalisateur du documentaire The Tinder Swindler ?",
             "le réalisateur du documentaire The Tinder Swindler est Felicity Morris.",

             "Qui sont les personnages du documentaire The Tinder Swindler ?",
             "les personnages du documentaire The Tinder Swindler sont  Ayleen Charlotte, Pernilla Sjoholm, Cecilie Fjellhoy, Shimon Hayut.",

             "Dans quel pays le documentaire The Tinder Swindler a-t-il été réalisé ?",
             "Le documentaire The Tinder Swindler a été produit au Royaume-Uni.",

             # documentaire   Harry & Meghan

             "Quel est le pourcentage de gens qui ont aimé le documentaire Harry & Meghan ?",
             "42% ont aimé ce documentaire",

             "Description du documentaire Harry & Meghan:",
             """L'hôte interagit avec le prince Harry et l'actrice américaine Meghan Markle, qui parlent de leur relation et de leurs fiançailles.""",

             "Quelle est la date de sortie du documentaire Harry & Meghan?",
             "la date de sortie du documentaire Harry & Meghan est 15 décembre 2022.",

             "quel est le genre du film Harry & Meghan ?",
             "le genre du film Harry & Meghan est documentaire.",

             "quelle est la durée du documentaire Harry & Meghan ?",
             "la durée du documentaire Harry & Meghan est 45 min.",

             "Qui est le réalisateur du documentaire Harry & Meghan ?",
             "le réalisateur du documentaire Harry & Meghan est Liz Garbus .",

             "Qui sont les personnages du documentaire Harry & Meghan ?",
             "les personnages du documentaire Harry & Meghan sont  Meghan Markle, Prince Harry.",

             "Dans quel pays le documentaire Harry & Meghan a-t-il été réalisé ?",
             "Le documentaire Harry & Meghan a été produit aux Etats-Unis.",

             # documentaire   Her Majesty the Queen

             "Quel est le pourcentage de gens qui ont aimé le documentaire Her Majesty the Queen ?",
             "60% ont aimé ce documentaire",

             "Description du documentaire Her Majesty the Queen:",
             """A la mort de SM la Reine Elizabeth II : documentaire spécial mettant en scène SM le Roi Charles III,
              ses enfants, des personnalités publiques, ceux qui ont travaillé avec elle. Avec des archives de la collection de la Reine. 
              Diffusion au Royaume-Uni et dans le monde.""",

             "Quelle est la date de sortie du documentaire Her Majesty the Queen?",
             "la date de sortie du documentaire Her Majesty the Queen est 2022-09-09.",

             "quel est le genre du film Her Majesty the Queen ?",
             "le genre du film Her Majesty the Queen est documentaire.",

             "quelle est la durée du documentaire Her Majesty the Queen ?",
             "la durée du documentaire Her Majesty the Queen est 91 min.",

             "Qui est le réalisateur du documentaire Her Majesty the Queen ?",
             "le réalisateur du documentaire Her Majesty the Queen est Sally Norris.",

             "Qui sont les personnages du documentaire Her Majesty the Queen ?",
             "les personnages du documentaire Her Majesty the Queen sont  Kirsty Young, Prince Andrew, Queen Elizabeth II of the United Kingdom, Prince Charles, Princess Anne.",

             "Dans quel pays le documentaire Her Majesty the Queen a-t-il été réalisé ?",
             "Le documentaire Her Majesty the Queen a été produit au Royaume-Uni.",

             # documentaire   Messi

             "Quel est le pourcentage de gens qui ont aimé le documentaire Messi ?",
             "91% ont aimé ce documentaire",

             "Description du documentaire Messi:",
             """Un regard sur la vie de Lionel Messi, le multiple vainqueur du footballeur mondial de l'année,
              de son enfance à Rosario, en Argentine, jusqu'à son ascension vers la célébrité internationale.
               Coéquipiers, entraîneurs et journalistes discutent du parcours de Messi vers le sommet.""",

             "Quelle est la date de sortie du documentaire Messi?",
             "la date de sortie du documentaire Messi est 1er janvier 2015.",

             "quel est le genre du film Messi ?",
             "le genre du film Messi est documentaire.",

             "quelle est la durée du documentaire Messi ?",
             "la durée du documentaire Messi est 1h 33m.",

             "Qui est le réalisateur du documentaire Messi ?",
             "le réalisateur du documentaire Messi est Álex de la Iglesia.",

             "Qui sont les personnages du documentaire Messi ?",
             "les personnages du documentaire Messi sont  Marc Balaguer, Ramon Besa, Johan Cruijff, Andrés Iniesta, Juan Carlos Lo Sasso.",

             "Dans quel pays le documentaire Messi a-t-il été réalisé ?",
             "Le documentaire Messi a été produit en Espagne.",

             ]
        )
        self.stdout.write(self.style.SUCCESS("Successfull!"))