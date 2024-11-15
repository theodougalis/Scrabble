import classes

def guidelines():
    '''
    Κλάσεις που υλοποιήθηκαν:
        SakClass
        Player
        Human
        Computer
        Game
    Ανάλυση κάθε κλάσης:
        Η SakClass είναι η κλάση που περιγράφει το σακουλάκι με τα γράμματα.
            Έχει τις εξής μεθόδους:
                
                __init__: Δημιουργεί και ετοιμάζει το σακουλάκι για το ξεκίνημα της παρτίδας.
                
                add: Προσθέτει ένα γράμμα όσες φορές θέλουμε στο σακουλάκι.
                
                getletter: Βγάζει ένα τυχαίο γράμμα από το σακουλάκι και το επιστρέφει.
                
                randomize_sak: Γεμίζει το σακουλάκι με όλα τα γράμματα με τυχαία σειρά.

        Η Player είναι η κλάση γονέας των Human και Computer από την οποία κληρωνομούν
        κάποιες κοινές μεταβλητές και συναρτήσεις.
            Έχει τις εξής μεθόδους:

                __init__: Αρχικοποιεί τις μεταβλητές που θα χρησιμοποιηθούν μετέπειτα.
                         (Σκορ παίκτη, διαθέσιμα γράμματα, το σακουλάκι της παρτίδας και το όνομα του παίκτη.)

                __repr__: Επιστρέφει την τιμή της μεταβλητής name.

                addscore: Αυξάνει το σκορ του παίκτη κατά το επιθυμητό ποσό.

                deal: Προσθέτει γράμματα από το σακουλάκι στο τρέχον σύνολο γραμμάτων του παίκτη, 
                      εφόσον είναι λιγότερα από 7. Επιστρέφει True άμα υπάρχουν αρκετά γράμματα στο 
                      σακουλάκι και False άμα δεν υπάρχουν.
        
        Η Human είναι η κλάση που περιγράφει τον χρήστη που θα παίξει. Κληρονομεί από την Player.
            Έχει τις εξής μεθόδους(Δεν γράφω τις μεθόδους που κληρονομούνται αυτούσιες):

                __init__: Χρησιμοποιεί την μέθοδο κατασκευαστή της Player και αλλάζει μόνο τη μεταβλητή name σε όνομα που δίνει ο παίκτης.

                play: Παίρνει τη λέξη του παίκτη και ελέγχει άμα είναι έγκυρη. Αν δεν είναι, ζητάει άλλη μέχρι 
                      να είναι έγκυρη και όταν είναι, προσθέτει στο σκορ, αντικαθιστά τα γράμματα που χρησιμοποιήθηκαν με νέα.
                      Αν δεν υπάρχουν γράμματα στο σακουλάκι για να συμπληρωθεί επτάδα, τελειώνει το παιχνίδι.

        Η Computer είναι η κλάση που περιγράφει τον υπολογιστή ως παίκτη. Επίσης κληρονομεί από την Player.
            Έχει τις εξής μεθόδους:

                __init__: Χρησιμοποιεί την μέθοδο κατασκευαστή της Player και αλλάζει μόνο τη μεταβλητή name σε 'Υπολογιστής'.

                min: Υλοποιεί τον αλγόριθμο MIN του 1ου σεναρίου μέσω μεταθέσεων με την itertools.permutations().

                max: Αντίστοιχα με τη min αλλά για τον αλγόριθμο MAX με ανεστραμμένη επανάληψη.

                smart: Για την υλοποίηση του SMART, η φιλοσοφία είναι ίδια με του MIN απλά κρατάω τη μέγιστη αξία λέξης όσο ελέγχω
                       τις μεταθέσεις και αφού ελεγχθούν όλες οι μεταθέσεις, παίρνω αυτή με τη μεγαλύτερη αξία.
                
                play: Παίζει με έναν από τους τρεις αλγορίθμους, αναλόγως με τη δυσκολία που επέλεξε ο παίκτης (by default MIN)
                      προσθέτει το σκορ της λέξης και αντικαθιστά τα γράμματα που χρησιμοποιήθηκαν με νέα από το σακουλάκι άμα υπάρχουν.

        Η Game είναι η κλάση που περιγράφει το παιχνίδι και αναλαμβάνει το μεγαλύτερο φορτίο του διαμεσολαβητή μεταξύ όλων των κλάσεων.
            Έχει τις εξής μεθόδους:

                __init__: Αρχικοποιεί τις μεταβλητές που θα χρησιμοποιηθούν μετέπειτα
                         (Τερματική συνθήκη, δυσκολία, δεδομένα από παρτίδες) και τρέχει την setup().

                setup: Δημιουργεί το λεξικό από το greek7.txt και εμφανίζει το αρχικό μενού.

                run: Μοιράζει τα πρώτα 7 γράμματα σε παίκτη και υπολογιστή και όσο η τερματική συνθήκη παραμένει false, καλεί εναλλάξ τις 
                     συναρτήσεις play του καθενός.
                
                end: Κάνει True την τερματική συνθήκη, καλεί τη μέθοδο αποθήκευσης παρτίδας και ανακοινώνει τον νικητή.

                startingMenu: Εμφανίζει το αρχικό μενού, ζητάει από το χρήστη να επιλέξει τι θέλει και το ανακατευθύνει αναλόγως.
                            (1.Παλιές παρτίδες εφόσον υπάρχουν, 2. Επιλογή δυσκολίας, 3. Εκκίνηση παιχνιδιού, q Έξοδος, οτιδήποτε άλλο ζητάει ξανά επιλογή).

                wordvalue: Υπολογίζει την αξία λέξεων.

                check1: Ελέγχει άμα η λέξη του χρήστη δημιουργείται από τα διαθέσιμα γράμματά του.

                check2: Ελέγχει άμα η λέξη του χρήστη υπάρχει μέσα στο greek7.txt

                check3: Ελέγχει εάν η είσοδος του χρήστη είναι 'p' ή 'q', για 'p' του αντικαθιστά τα γράμματα εφόσον υπάρχουν στο σακουλάκι αρκετά, για Q τελειώνει.
    
                saveGame: Εάν υπάρχουν αποθηκευμένες παρτίδες σε data.txt προσθέτει και την τρέχουσα, αλλιώς δημιουργεί αρχείο data.txt και την αποθηκεύει.

                printoldgames: Εάν υπάρχουν αποθηκευμένες παρτίδες, τις εμφανίζει αριθμημένες, αλλιώς εμφανίζει μήνυμα ότι δεν υπάρχουν αποθηκευμένες παρτίδες.
    
        Για τη δομή των λέξεων χρησιμοποιήθηκε λεξικό, αφού λόγω του ότι υλοποιείται με hashtable, μας επιστρέφει σε O(1).

        Έχει υλοποιηθεί το 1ο σενάριο για τον αλγόριθμο play του υπολογιστή, δηλαδή ο παίκτης δύναται να επιλέξει ανάμεσα σε τρεις δυσκολίες, MIN, MAX και SMART.

        Η εργασία αποτελείται από τα εξής τρία αρχεία:
            
            main3544.py
            classes.py
            greek7.txt

            Την πρώτη φορά που το τρέχω (χρησιμοποιώ Visual Studio Code) δημιουργείται ένας φάκελος __pycache__ που περιλαμβάνει ένα αρχείο classes.cpython-37.pyc 
            μέσα στον φάκελο του project.
            Επίσης από την πρώτη παρτίδα που θα τελειώσει με οποιοδήποτε τρόπο και μετά, δημιουργείται και το αρχείο data.txt που αποθηκεύει και φορτώνει τις παλιές παρτίδες. 

    '''
    pass

sak=classes.SakClass()
human=classes.Human(sak,"")
computer=classes.Computer(sak)
greek7={}
game=classes.Game(greek7,sak,human,computer)