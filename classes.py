import random
import json
import itertools
VALUES = {"Α": 1,"Β": 8, "Γ": 4, "Δ": 4, "Ε": 1, "Ζ": 10, "Η": 1, "Θ": 10,
            "Ι": 1, "Κ": 2, "Λ": 3, "Μ": 3, "Ν": 1, "Ξ": 10, "Ο": 1, "Π": 2,
            "Ρ": 2, "Σ": 1, "Τ": 1, "Υ": 2, "Φ": 8, "Χ": 8, "Ψ": 10, "Ω": 3}


class SakClass:
    
    def __init__(self):
    #Δημιουργεί και γεμίζει το σακουλάκι.
        self.sak=[]
        self.randomize_sak()

    def add(self, letter, times):
    #Προσθέτει ένα γράμμα πολλαπλές φορές στο σακουλάκι.
        for i in range(times):
            self.sak.append(letter)

    def getletter(self):
    #Βγάζει ένα τυχαίο γράμμα από το σακουλάκι και το επιστρέφει.
        return self.sak.pop(random.randint(0,len(self.sak)-1))

    def randomize_sak(self):
    #Γεμίζει το σακουλάκι με όλα τα γράμματα με τυχαία σειρά.
        self.add("Α", 12)
        self.add("Β", 1)
        self.add("Γ", 2)
        self.add("Δ", 2)
        self.add("Ε", 8)
        self.add("Ζ", 1)
        self.add("Η", 7)
        self.add("Θ", 1)
        self.add("Ι", 8)
        self.add("Κ", 4)
        self.add("Λ", 3)
        self.add("Μ", 3)
        self.add("Ν", 6)
        self.add("Ξ", 1)
        self.add("Ο", 9)
        self.add("Π", 4)
        self.add("Ρ", 5)
        self.add("Σ", 7)
        self.add("Τ", 8)
        self.add("Υ", 4)
        self.add("Φ", 1)
        self.add("Χ", 1)
        self.add("Ψ", 1)
        self.add("Ω", 3)
        random.shuffle(self.sak)

class Player:
    def __init__(self,sak):
        self.score=0
        self.letters=[]
        self.sak=sak
        self.name="Player"
    def __repr__(self):
        return self.name
    def addscore(self,score):
    #Αυξάνει το σκορ του παίκτη κατά το επιθυμητό ποσό
        self.score+=score
    def deal(self,sak):
    #Προσθέτει γράμματα από το σακουλάκι στο τρέχον σύνολο γραμμάτων του παίκτη άμα είναι λιγότερα από 7.
        if len(sak.sak)>=7-len(self.letters):
            if len(self.letters)<7:
                for i in range(7-len(self.letters)):
                    self.letters.append(sak.getletter())
            return True
        else:
            return False

class Human(Player):
    def __init__(self,sak,name):
        super().__init__(sak)
        self.name=name
    def play(self,sak,game,greek7,computer):
    #Παίρνει τη λέξη του παίκτη και ελέγχει άμα είναι έγκυρη. Ξαναζητάει μέχρι να είναι έγκυρη, και όταν είναι προσθέτει στο σκορ, αντικαθιστά τα γράμματα που χρησιμοποιήθηκαν με νέα.
        self.deal(sak)
        self.word=input(f"---------------------------------------\n**Το σακουλάκι περιέχει ακόμα {len(sak.sak)} γράμματα.\n**Τα διαθέσιμα γράμματα σας είναι: {self.letters[0]},{VALUES[self.letters[0]]} - {self.letters[1]},{VALUES[self.letters[1]]} - {self.letters[2]},{VALUES[self.letters[2]]} - {self.letters[3]},{VALUES[self.letters[3]]} - {self.letters[4]},{VALUES[self.letters[4]]} - {self.letters[5]},{VALUES[self.letters[5]]} - {self.letters[6]},{VALUES[self.letters[6]]}\n**Παρακαλώ πληκτρολογήστε τη λέξη σας και πατήστε enter:")
        self.word=self.word.upper()
        while game.check3(self.word,self,self.sak,computer)!=True:
            if game.check1(self.letters,self.word):
                if game.check2(greek7,self.word):
                    print(f"---------------------------------------\n**Η λέξη {self.word} είναι έγκυρη και αξίζει {greek7[self.word]} πόντους.")
                    self.addscore(greek7[self.word])
                    print(f"**Το σκορ του {self.name} είναι {self.score}.\n---------------------------------------")
                    input("**Πιέστε 'Enter' για να συνεχίσετε.\n---------------------------------------")
                    for letter in self.word:
                        self.letters.remove(letter)
                    if self.deal(sak):
                        break
                    else:
                        game.end(self,computer)
                        break
                
                self.word=input(f"---------------------------------------\n**Αυτή η λέξη δεν υπάρχει.\n**Παρακαλώ πληκτρολογήστε μία έγκυρη λέξη και πατήστε enter:")
                self.word=self.word.upper()
            else:
                self.word=input(f"---------------------------------------\n**Αυτή η λέξη δεν δημιουργείται από τα γράμματά σας.\n**Παρακαλώ πληκτρολογήστε μία έγκυρη λέξη και πατήστε enter:")
                self.word=self.word.upper()
        
    
class Computer(Player):
    def __init__(self,sak):
        super().__init__(sak)
        self.name="Υπολογιστής"
    def min(self,greek7):
    #Υλοποίηση του αλγορίθμου min
        for i in range(6):
            p=list(itertools.permutations(self.letters,i+2))
            for w in p:
                wo="".join(w)
                if wo in greek7:
                    return wo
    def max(self,greek7):
    #Υλοποίηση του αλγορίθμου min
        for i in range(6,0,-1):
            p=list(itertools.permutations(self.letters,i+2))
            for w in p:
                wo="".join(w)
                if wo in greek7:
                    return wo
    def smart(self,greek7):
    #Υλοποίηση του αλγορίθμου smart
        wor=""
        worvalue=0
        for i in range(6):
            p=list(itertools.permutations(self.letters,i+2))
            for w in p:
                wo="".join(w)
                if wo in greek7:
                    if greek7[wo]>worvalue:
                        wor=wo
                        worvalue=greek7[wor]
        return wor
    def play(self, sak, game, greek7, difficulty,human):
    #Παίζει με έναν από τους τρεις αλγορίθμους, προσθέτει το σκορ της λέξης και αντικαθιστά τα γράμματα που χρησιμοποιήθηκαν με νέα.
        print(f"**Το σακουλάκι περιέχει ακόμα {len(sak.sak)} γράμματα.\n**Τα διαθέσιμα γράμματα του υπολογιστή είναι: {self.letters[0]},{VALUES[self.letters[0]]} - {self.letters[1]},{VALUES[self.letters[1]]} - {self.letters[2]},{VALUES[self.letters[2]]} - {self.letters[3]},{VALUES[self.letters[3]]} - {self.letters[4]},{VALUES[self.letters[4]]} - {self.letters[5]},{VALUES[self.letters[5]]} - {self.letters[6]},{VALUES[self.letters[6]]}")
        if difficulty=="1":
            word=self.min(greek7)
        elif difficulty=="2":
            word=self.max(greek7)
        elif difficulty=="3":
            word=self.smart(greek7)
        if word=="":
            print("**Ο υπολογιστής δε μπόρεσε να βρει λέξη.\n---------------------------------------")
            game.end(human, self)
        else:
            self.addscore(greek7[word])
            print(f"**Ο υπολογιστής έπαιξε την λέξη '{word}' και πήρε {greek7[word]} πόντους.\n**Το σκορ του υπολογιστή είναι {self.score}.\n---------------------------------------")
            for letter in word:
                self.letters.remove(letter)
            if self.deal(sak):
                return 
            else:
                game.end(human, self)
                return 


class Game:

    def __init__(self, greek7,sak, human, computer):
        self.endgame=False
        self.difficulty=""
        self.data={}
        self.data['games']=[]
        self.setup(greek7,sak, human, computer)

    def setup(self, greek7,sak, human, computer):
    #Δημιουργεί το λεξικό greek7
        with open('greek7.txt', 'r', encoding="utf-8") as f:
            for l in f:
                line=l      
                line=line.strip('\n')
                linevalue=self.wordvalue(line)
                greek7[line]=linevalue
        self.startingMenu(sak, greek7, human, computer)
        
    def run(self, sak, greek7, human, computer):
        human.deal(sak)
        computer.deal(sak)
        while self.endgame==False:
            human.play(sak,self,greek7,computer)
            if self.endgame==False:
                computer.play(sak, self, greek7, self.difficulty,human)

    def end(self, human, computer):
        self.endgame=True
        self.saveGame(human,computer,self.data)
        print(f"---------------------------------------\n**Το παιχνίδι έχει τελειώσει. Ο υπολογιστής μάζεψε {computer.score} πόντους και ο {human} μάζεψε {human.score} πόντους.\n---------------------------------------")
        if computer.score>human.score:
            print("**Κερδίζει ο υπολογιστής\n---------------------------------------")
        elif computer.score<human.score:
            print(f"**Κερδίζει ο {human}\n---------------------------------------")
        else:
            print("**Έχουμε ισοπαλία!\n---------------------------------------")
    
    def startingMenu(self, sak, greek7, human, computer):
        menu='''
        ***** SCRABBLE *****
        --------------------
        Πλήκτρα πλοήγησης:

        1.Σκορ
        2.Ρυθμίσεις
        3.Παιχνίδι
        q.Έξοδος
        --------------------
        '''
        viablechoices=["1","2","3","q"]
        viablediff=["1","2","3"]
        if self.difficulty not in viablediff: 
            self.difficulty="1"

        print(menu)
        choice=input("**Το πλήκτρο της επιλογής σας και enter: ")
        while choice not in viablechoices:
                print(menu)
                choice=input("**Παρακαλώ πληκτρολογήστε 1,2,3 ή q.\n**Το πλήκτρο της επιλογής σας και enter: ")

        if choice=="1":
            self.printoldgames(self.data)
            input("**Πιέστε 'Enter' για να επιστρέψετε στο μενού.\n---------------------------------------")
            self.startingMenu(sak, greek7, human, computer)
        elif choice=="2":

            print("---------------------------------------\n**Η δυσκολία αυξάνεται από το επίπεδο 1 μέχρι το επίπεδο 3. \nΤρέχον επίπεδο δυσκολίας: "+ self.difficulty+"\n---------------------------------------")
            diffchoice=input("**Παρακαλώ πληκτρολογήστε το επιθυμητό επίπεδο δυσκολίας και enter: ")
            while diffchoice not in viablediff:
                diffchoice=input("**Παρακαλώ πληκτρολογήστε 1, 2 ή 3.\n**Επιθυμητό επίπεδο δυσκολίας και enter: ")
            if diffchoice!=self.difficulty:
                self.difficulty=diffchoice
                print("Το επίπεδο δυσκολίας άλλαξε σε: "+self.difficulty+"\n---------------------------------------")
            else:
                print("Το επίπεδο δυσκολίας παραμένει: "+self.difficulty+"\n---------------------------------------")
            input("**Πιέστε 'Enter' για να επιστρέψετε στο μενού.\n---------------------------------------")
            self.startingMenu(sak, greek7, human, computer)
        elif choice=="3":
            human.name=input("**Παρακαλώ πληκτρολογήστε το όνομά σας:\n")
            self.run(sak, greek7, human, computer)

        if choice=="q":
            input("---------------------------------------\n**Πιέζοντας 'Enter' το παιχνίδι θα κλείσει. Εις το επανιδείν!\n---------------------------------------")
            exit()

    def wordvalue(self,word):
    #Υπολογίζει την αξία της λέξης "word".
        valuecount=0
        for letter in word:
            valuecount+=VALUES[letter]
        return valuecount

    def check1(self,letters,word):
    #Επιστρέφει True ή False αναλόγως άμα δημιουργείται η λέξη από τα διαθέσιμα γράμματα.
        p=list(itertools.permutations(letters,len(word)))
        word=word.upper()
        wordcheck=False
        for i in p:
            pstr="".join(i)
            if word==pstr:
                wordcheck=True
                break
        return wordcheck

    def check2(self,greek7,word):
    #Επιστρέφει True ή False αναλόγως άμα υπάρχει η λέξη στο greek7.txt.
        if word in greek7:
            return True
        return False
    
    def check3(self,word,human,sak,computer):
    #Ελέγχει εάν η είσοδος είναι "p" ή "q" και επιστρέφει True αν είναι κάποιο από τα 2, αλλιώς False. 
        if word=="P":
            if len(sak.sak)>6:
                for letter in range(7):
                    sak.add(human.letters.pop(),1)
                human.deal(sak)
                print(f"**Τα νέα σας γράμματα είναι: {human.letters[0]},{VALUES[human.letters[0]]} - {human.letters[1]},{VALUES[human.letters[1]]} - {human.letters[2]},{VALUES[human.letters[2]]} - {human.letters[3]},{VALUES[human.letters[3]]} - {human.letters[4]},{VALUES[human.letters[4]]} - {human.letters[5]},{VALUES[human.letters[5]]} - {human.letters[6]},{VALUES[human.letters[6]]}\n---------------------------------------")
                return True
            else:
                print("**Δεν υπάρχουν αρκετά γράμματα στο σακουλάκι.\n---------------------------------------")
                return True
        elif word=="Q":
            self.end(human,computer)
            return True
        else:
            return False
    def saveGame(self, human, computer, data):
        try:
            with open('data.txt') as json_file:
                data=json.load(json_file)
        except FileNotFoundError:
            pass

        data["games"].append({
            'playername':human.name,
            'playerscore':human.score,
            'computerscore':computer.score
        })
        with open('data.txt','w') as outfile:
            json.dump(data,outfile)
    def printoldgames(self,data):
        try:
            with open('data.txt') as json_file:
                data=json.load(json_file)
                for game in data['games']:
                    print(f"**Παρτίδα {data['games'].index(game)+1}:\n**Ο/Η {game['playername']} μάζεψε {game['playerscore']} πόντους.\n**Ο υπολογιστής μάζεψε {game['computerscore']} πόντους.\n---------------------------------------")
        except FileNotFoundError:
            print("---------------------------------------\n**Δεν υπάρχουν αποθηκευμένες παρτίδες.\n---------------------------------------")