import time
def german_no():
    numbers={
            1: ("One", "Eins"),2: ("Two", "Zwei"), 3: ("Three", "Drei"),4: ("Four", "Vier"),5: ("Five", "Fünf"),6: ("Six", "Sechs"),7: ("Seven", "Sieben"),
            8: ("Eight", "Acht"),9: ("Nine", "Neun"),10: ("Ten", "Zehn")
            }
    for key, value in numbers.items():
                        print(key, "-", value[0], "=", value[1])
                        time.sleep(2)

def german_alph():
    alphabet={
                 "A": "Ah", "B": "Be", "C": "Ce", "D": "De", "E": "Eh","F": "Ef", "G": "Ge", "H": "Ha", "I": "Ih", "J": "Jot",
                 "K": "Ka", "L": "El", "M": "Em", "N": "En", "O": "Oh", "P": "Pe", "Q": "Ku", "R": "Er", "S": "Es", "T": "Te",
                 "U": "Uh", "V": "Fau", "W": "We", "X": "Iks", "Y": "Ypsilon", "Z": "Tset"
            }
    print("English to German Alphabets")
    print("------------------------------------")
    for letter in alphabet:
        print(letter, "=", alphabet[letter])
        time.sleep(2)

def german_animals():
    
    animals = {
        "Dog": "Hund","Cat": "Katze","Cow": "Kuh","Horse": "Pferd","Lion": "Löwe","Tiger": "Tiger",
        "Elephant": "Elefant","Monkey": "Affe","Bird": "Vogel","Fish": "Fisch"
    }
    print("English to German Animals")
    print("------------------------------------")
    for animal in animals:
        print(animal, "=", animals[animal])
        time.sleep(2)

def german_body_parts():
    body_parts = {
        "Head": "Kopf","Eye": "Auge","Ear": "Ohr","Nose": "Nase","Mouth": "Mund","Hand": "Hand","Leg": "Bein",
        "Foot": "Fuß","Finger": "Finger","Hair": "Haar"
    }
    print("English to German Body Parts")
    print("------------------------------------")
    for part in body_parts:
        print(part, "=", body_parts[part])
        time.sleep(2)

def german_number_quiz():
    count=0
    print("number test")
    q1 = input("question 1)  3.three=___?___\nenter answer:")
    print("------------------------------------")
    q2 = input("question 2) 8.eight=___?___\nenter answer:")
    print("------------------------------------")
    q3 = input("question 3)  5.five=___?___\nenter answer:")
    print("------------------------------------")
    q4 = input("question 4)  7.seven=___?___\nenter answer:")
    print("------------------------------------")
    q5 = input("question 5)  10.ten=___?___\nenter answer:")
    print("------------------------------------")
    if q1 == "Drei": count += 1
    if q2 == "Acht": count += 1
    if q3 == "Funf": count += 1
    if q4 == "Sieben": count += 1
    if q5 == "Zehn": count += 1
    print(f"your number quiz score is :{count}/5")
    print("------------------------------------")
    if count < 5:
        print("********correct answers*******")
        if q1 != "Drei": print("3.three=drei")
        if q2 != "Acht": print("8.eight=Acht")
        if q3 != "Funf": print("5.five=Funf")
        if q4 != "Sieben": print("7.seven=Sieben")
        if q5 != "Zehn": print("10.ten=Zehn")

def german_alphabet_quiz():
    count=0
    print("alphabet test")
    q1 = input("question 1)  Q=___?___\nenter answer:")
    print("------------------------------------")
    q2 = input("question 2) P=___?___\nenter answer:")
    print("------------------------------------")
    q3 = input("question 3)  Y=___?___\nenter answer:")
    print("------------------------------------")
    q4 = input("question 4)  r=___?___\nenter answer:")
    print("------------------------------------")
    q5 = input("question 5)  L=___?___\nenter answer:")
    print("------------------------------------")  
    if q1 == "Ku": count += 1
    if q2 == "Pe": count += 1
    if q3 == "Ypsillon": count += 1
    if q4 == "Er": count += 1
    if q5 == "El": count += 1  
    print(f"your alphabet quiz score is :{count}/5")
    print("------------------------------------")
    if count < 5:
        print("********correct answers********")
        if q1 != "Ku": print("Q=Ku")
        if q2 != "Pe": print("P=Pe")
        if q3 != "Ypsillon": print("Y=Ypsillon")
        if q4 != "Er": print("r=Er")
        if q5 != "El": print("L=El")

def german_animal_quiz():
    count=0
    print("animal name test")
    q1 = input("question 1)  dog=___?___\nenter answer:")
    print("------------------------------------")
    q2 = input("question 2) cat=___?___\nenter answer:")
    print("------------------------------------")
    q3 = input("question 3)  fish=___?___\nenter answer:")
    print("------------------------------------")
    q4 = input("question 4)  lion=___?___\nenter answer:")
    print("------------------------------------")
    q5 = input("question 5)  bird=___?___\nenter answer:")
    print("------------------------------------")
    if q1 == "Hund": count += 1
    if q2 == "Katze": count += 1
    if q3 == "Fisch": count += 1
    if q4 == "Lowe": count += 1
    if q5 == "Vogel": count += 1 
    print(f"your animal quiz score is :{count}")
    print("------------------------------------")
    if count < 5:
        print("********correct answers********")
        if q1 != "Hund": print("dog=Hund")
        if q2 != "Katze": print("cat=Katze")
        if q3 != "Fisch": print("fish=Fisch")
        if q4 != "Lowe": print("lion=Lowe")
        if q5 != "Vogel": print("bird=Vogel")

def german_body_part_quiz():
    count=0
    print("Body Parts Test")
    q1 = input("question 1) Head = ___?___\nenter answer: ")
    print("------------------------------------")
    q2 = input("question 2) Eye = ___?___\nenter answer: ")
    print("------------------------------------")
    q3 = input("question 3) Nose = ___?___\nenter answer: ")
    print("------------------------------------")
    q4 = input("question 4) Hand = ___?___\nenter answer: ")
    print("------------------------------------")
    q5 = input("question 5) Leg = ___?___\nenter answer: ")
    print("------------------------------------")
    if q1 == "Kopf": count += 1
    if q2 == "Auge": count += 1
    if q3 == "Nase": count += 1
    if q4 == "Hand": count += 1
    if q5 == "Bein": count += 1
    print(f"your body part quiz score is : {count}/5")
    print("------------------------------------")
    if count < 5:
        print("********correct answers********")
        print("------------------------------------")
        if q1 != "Kopf":  print("Head = Kopf")
        if q2 != "Auge":  print("Eye = Auge")
        if q3 != "Nase":  print("Nose = Nase")
        if q4 != "Hand":  print("Hand = Hand")
        if q5 != "Bein":  print("Leg = Bein")

def professionaltences():
    print("----------Berufliche Weiterbildung-------------")
    print("Ich lerne neue technische Fähigkeiten.")
    print("Ich verbessere meine Kommunikationsfähigkeiten.")
    print("Ich arbeite an praktischen Projekten.")
    print("Ich lerne Teamarbeit und Problemlösung.")
    print("Ich entwickle meine beruflichen Kenntnisse.")
    print("-----------english meaning--------------")
    print("I learn new technical skills.")
    print("I improve my communication skills.")
    print("I work on practical projects.")
    print("I learn teamwork and problem solving.")
    print("I develop my professional knowledge.")

def professional_paragraph():
    print("German Paragraph:")
    print("Ich mache berufliche Weiterbildung, um meine Fähigkeiten und Kenntnisse zu verbessern.")
    print("Ich lerne neue technische Fähigkeiten und verbessere meine Kommunikationsfähigkeiten.")
    print("Ich arbeite an praktischen Projekten und lerne Teamarbeit sowie Problemlösung.")
    print("Außerdem entwickle ich meine beruflichen Kenntnisse für meine zukünftige Karriere.")
    print("Berufliche Weiterbildung hilft mir, selbstbewusster und erfolgreicher zu werden.")
    print("\nEnglish Meaning:")
    print("I do professional learning to improve my skills and knowledge.")
    print("I learn new technical skills and improve my communication skills.")
    print("I work on practical projects and learn teamwork and problem solving.")
    print("Additionally, I develop my professional knowledge for my future career.")
    print("Professional learning helps me become more confident and successful.")

def professional_email():
    print("German Email:")
    print("Betreff: Berufliche Weiterbildung und persönliche Entwicklung")
    print("Hallo Sir/Madam,")
    print("Ich hoffe, es geht Ihnen gut.")
    print("Zurzeit mache ich berufliche Weiterbildung, um meine Fähigkeiten und Kenntnisse zu verbessern.")
    print("Ich lerne neue technische Fähigkeiten, verbessere meine Kommunikationsfähigkeiten und arbeite an praktischen Projekten.")
    print("Außerdem lerne ich Teamarbeit, Problemlösung und Zeitmanagement.")
    print("Diese Weiterbildung hilft mir, mehr Selbstvertrauen zu entwickeln und mich besser auf meine zukünftige Karriere vorzubereiten.")
    print("Ich interessiere mich besonders für Technologie und möchte in Zukunft erfolgreich in meinem Beruf arbeiten.")
    print("Jeden Tag versuche ich, etwas Neues zu lernen und meine beruflichen Kenntnisse weiterzuentwickeln.")
    print("Vielen Dank für Ihre Zeit und Unterstützung.")
    print("Mit freundlichen Grüßen")
    print("Chaitanya")
    print("\nEnglish Meaning:")
    print("Subject: Professional Learning and Personal Development")
    print("Hello Sir/Madam,")
    print("I hope you are doing well.")
    print("Currently, I am doing professional learning to improve my skills and knowledge.")
    print("I learn new technical skills, improve my communication skills, and work on practical projects.")
    print("Additionally, I learn teamwork, problem solving, and time management.")
    print("This learning helps me build more confidence and prepare better for my future career.")
    print("I am especially interested in technology and want to work successfully in my profession in the future.")
    print("Every day, I try to learn something new and develop my professional knowledge further.")
    print("Thank you for your time and support.")
    print("Best regards")
    print("Chaitanya")

def japanese_numbers():
    numbers = {
        1: ("One", "一"),2: ("Two", "二"),3: ("Three", "三"),4: ("Four", "四"),5: ("Five", "五"),
        6: ("Six", "六"),7: ("Seven", "七"),8: ("Eight", "八"),9: ("Nine", "九"),10: ("Ten", "十")
    }
    print("English to Japanese Numbers")
    print("------------------------------------")
    for key in numbers:
        print(key, "-", numbers[key][0], "=", numbers[key][1])
        time.sleep(2)

def japanese_alphabets():
    alphabet = {
        "A": "あ","B": "び","C": "し","D": "で", "E": "え", "F": "ふ", "G": "ぎ","H": "は","I": "い","J": "じ","K": "か", "L": "る", "M": "ま",
        "N": "ん","O": "お","P": "ぱ","Q": "く","R": "ら","S": "さ", "T": "た","U": "う","V": "ゔ","W": "わ","X": "くす","Y": "や","Z": "ぜ"
    }
    print("English to Japanese Alphabets")
    print("------------------------------------")
    for letter in alphabet:
        print(letter, "=", alphabet[letter])
        time.sleep(2)

def japanese_animals():
    animals = {
        "Dog": "犬","Cat": "猫","Cow": "牛","Horse": "馬","Lion": "ライオン","Tiger": "虎","Elephant": "象","Monkey": "猿","Bird": "鳥","Fish": "魚"
    }

    print("English to Japanese Animals")
    print("------------------------------------")

    for animal in animals:
        print(animal, "=", animals[animal])
        time.sleep(2)


def japanese_body_parts():
    body_parts = {
        "Head": "あたま","Eye": "め","Ear": "みみ","Nose": "はな","Mouth": "くち","Hand": "て",
        "Leg": "あし","Foot": "あし","Finger": "ゆび","Hair": "かみ"
    }
    print("English to Japanese Body Parts")
    print("------------------------------------")
    for part in body_parts:
        print(part, "=", body_parts[part])
        time.sleep(2)

def japanese_number_quiz():
    count=0
    print("Japanese Number Test")
    print("question 1) Three = ___?___")
    q1 = input("enter answer: ")
    print("------------------------------------")
    print("question 2) Eight = ___?___")
    q2 = input("enter answer: ")
    print("------------------------------------")
    print("question 3) Five = ___?___")
    q3 = input("enter answer: ")
    print("------------------------------------")
    print("question 4) Seven = ___?___")
    q4 = input("enter answer: ")
    print("------------------------------------")
    print("question 5) Ten = ___?___")
    q5 = input("enter answer: ")
    print("------------------------------------")
    if q1 == "三":
        count += 1
    if q2 == "八":
        count += 1
    if q3 == "五":
        count += 1
    if q4 == "七":
        count += 1
    if q5 == "十":
        count += 1
    print(f"your japanese number quiz score is : {count}/5")
    print("------------------------------------")
    if count < 5:
        print("********correct answers********")
        print("------------------------------------")
        if q1 != "三":
            print("Three = 三")
        if q2 != "八":
            print("Eight = 八")
        if q3 != "五":
            print("Five = 五")
        if q4 != "七":
            print("Seven = 七")
        if q5 != "十":
            print("Ten = 十")

def japanese_alphabet_quiz():
    count=0
    print("Japanese Alphabet Test")
    print("question 1) Q = ___?___")
    q1 = input("enter answer: ")
    print("------------------------------------")
    print("question 2) P = ___?___")
    q2 = input("enter answer: ")
    print("------------------------------------")
    print("question 3) Y = ___?___")
    q3 = input("enter answer: ")
    print("------------------------------------")
    print("question 4) R = ___?___")
    q4 = input("enter answer: ")
    print("------------------------------------")
    print("question 5) L = ___?___")
    q5 = input("enter answer: ")
    print("------------------------------------")
    if q1 == "く": count += 1
    if q2 == "ぱ": count += 1
    if q3 == "や": count += 1
    if q4 == "ら": count += 1
    if q5 == "る": count += 1
    print(f"your japanese alphabet quiz score is : {count}/5")
    print("------------------------------------")
    if count < 5:
        print("********correct answers********")
        print("------------------------------------")
        if q1 != "く":print("Q = く")
        if q2 != "ぱ":print("P = ぱ")
        if q3 != "や":print("Y = や")
        if q4 != "ら":print("R = ら")
        if q5 != "る":print("L = る")

def japanese_animal_quiz():
    count=0
    print("Japanese Animal Test")
    print("question 1) Dog = ___?___")
    q1 = input("enter answer: ")
    print("------------------------------------")
    print("question 2) Cat = ___?___")
    q2 = input("enter answer: ")
    print("------------------------------------")
    print("question 3) Fish = ___?___")
    q3 = input("enter answer: ")
    print("------------------------------------")
    print("question 4) Lion = ___?___")
    q4 = input("enter answer: ")
    print("------------------------------------")
    print("question 5) Bird = ___?___")
    q5 = input("enter answer: ")
    print("------------------------------------")
    if q1 == "犬": count += 1
    if q2 == "猫": count += 1
    if q3 == "魚": count += 1
    if q4 == "ライオン": count += 1
    if q5 == "鳥": count += 1
    print(f"your japanese animal quiz score is : {count}/5")
    print("------------------------------------")
    if count < 5:
        print("********correct answers********")
        print("------------------------------------")
        if q1 != "犬":     print("Dog = 犬")
        if q2 != "猫":     print("Cat = 猫")
        if q3 != "魚":     print("Fish = 魚")
        if q4 != "ライオン":print("Lion = ライオン")
        if q5 != "鳥":    print("Bird = 鳥")

def japanese_body_part_quiz():
    count=0
    print("Japanese Body Parts Test")
    print("question 1) Head = ___?___")
    q1 = input("enter answer: ")
    print("------------------------------------")
    print("question 2) Eye = ___?___")
    q2 = input("enter answer: ")
    print("------------------------------------")
    print("question 3) Nose = ___?___")
    q3 = input("enter answer: ")
    print("------------------------------------")
    print("question 4) Hand = ___?___")
    q4 = input("enter answer: ")
    print("------------------------------------")
    print("question 5) Hair = ___?___")
    q5 = input("enter answer: ")
    print("------------------------------------")
    if q1 == "あたま":count += 1
    if q2 == "め":    count += 1
    if q3 == "はな":  count += 1
    if q4 == "て":    count += 1
    if q5 == "かみ":  count += 1
    print(f"your japanese body part quiz score is : {count}/5")
    print("------------------------------------")
    if count < 5:
        print("********correct answers********")
        print("------------------------------------")
        if q1 != "あたま":    print("Head = あたま")
        if q2 != "め":        print("Eye = め")
        if q3 != "はな":      print("Nose = はな")
        if q4 != "て":        print("Hand = て")
        if q5 != "かみ":      print("Hair = かみ")

def japanese_learning_sentences():
    print("----------日本語学習-------------")
    print("私は新しい技術を学びます。")
    print("私はコミュニケーション能力を向上させます。")
    print("私は実践的なプロジェクトに取り組みます。")
    print("私はチームワークと問題解決を学びます。")
    print("私は専門知識を発展させます。")
    print("-----------English Meaning--------------")
    print("I learn new technical skills.")
    print("I improve my communication skills.")
    print("I work on practical projects.")
    print("I learn teamwork and problem solving.")
    print("I develop my professional knowledge.")

def japanese_learning_paragraph():
    print("Japanese Paragraph:")
    print("私は自分の能力と知識を向上させるために専門的な学習をしています。")
    print("私は新しい技術を学び、コミュニケーション能力を向上させています。")
    print("私は実践的なプロジェクトに取り組み、チームワークと問題解決を学びます。")
    print("さらに、将来のキャリアのために専門知識を発展させています。")
    print("専門的な学習は、私をより自信があり成功した人にしてくれます。")
    print("\nEnglish Meaning:")
    print("I do professional learning to improve my skills and knowledge.")
    print("I learn new technical skills and improve my communication skills.")
    print("I work on practical projects and learn teamwork and problem solving.")
    print("Additionally, I develop my professional knowledge for my future career.")
    print("Professional learning helps me become more confident and successful.")


def japanese_learning_email():
    print("Japanese Email:")
    print("件名: 専門的な学習と自己成長")
    print("こんにちは Sir/Madam,")
    print("お元気でお過ごしのことと思います。")
    print("現在、私は自分の能力と知識を向上させるために専門的な学習をしています。")
    print("私は新しい技術を学び、コミュニケーション能力を向上させ、実践的なプロジェクトに取り組んでいます。")
    print("さらに、チームワーク、問題解決、時間管理も学んでいます。")
    print("この学習は、将来のキャリアに向けて自信を高め、より良い準備をするのに役立っています。")
    print("私は特にテクノロジーに興味があり、将来は自分の職業で成功したいと考えています。")
    print("毎日、新しいことを学び、専門知識をさらに発展させるよう努力しています。")
    print("お時間とご支援をありがとうございます。")
    print("よろしくお願いいたします。")
    print("Chaitanya")
    print("\nEnglish Meaning:")
    print("Subject: Professional Learning and Personal Development")
    print("Hello Sir/Madam,")
    print("I hope you are doing well.")
    print("Currently, I am doing professional learning to improve my skills and knowledge.")
    print("I learn new technical skills, improve my communication skills, and work on practical projects.")
    print("Additionally, I learn teamwork, problem solving, and time management.")
    print("This learning helps me build more confidence and prepare better for my future career.")
    print("I am especially interested in technology and want to work successfully in my profession in the future.")
    print("Every day, I try to learn something new and develop my professional knowledge further.")
    print("Thank you for your time and support.")
    print("Best regards")
    print("Chaitanya")

# main part of the code (main body)

print("Language Learning Flashcard")
a=0
while a!=3:
    print("-------*--------*---------*---------")          # ask prefernce language
    print("1. English to German")
    print("2. English to japanese")
    print("3. exit")
    print("------------------------------------")
    a =int(input("Enter your preference language: "))
    print("------------------------------------")
    if a==1:                                                # ask type of larning
        print("1. basic larning")
        print("2. Quiz")
        print("3. professional learning")
        print("------------------------------------")     
        p1=int(input("Enter your preference: "))
        print("------------------------------------")      
        if p1==1:                                           #basic larning maneu
            print("1. Number")
            print("2. Alphabets")
            print("3. Animals")
            print("4. body parts")
            print("------------------------------------")     
            b=int(input("Enter your preference: "))
            print("------------------------------------")
            match b:
                case 1:
                    german_no()                          
                case 2:
                    german_alph()
                case 3:                                        # calling the funtion 
                    german_animals()
                case 4:
                    german_body_parts()
                    
        elif p1==2:
        
            print("----------quiz------------")                    #quiz maneu
            print("1.number quiz")
            print("2.alphabet quiz")
            print("3.animals name quiz")
            print("4.body part quiz")
            pre1=int(input("enter your prefrance:"))
            print("------------------------------------")

            match pre1:
                case 1:german_number_quiz()
                case 2:german_alphabet_quiz()
                case 3:german_animal_quiz()
                case 4:german_body_part_quiz()

        elif p1==3:
            print("----------professional learning------------")             #professional larning maneu
            print("1.sentences")
            print("2.paragraph")
            print("3.email")
            pre3=int(input("enter your prefrance:"))
            print("------------------------------------")

            match pre3:
                case 1:professionaltences()
                case 2:professional_paragraph()
                case 3:professional_email()
                   
    elif a==2: 
        
            print("1. basic larning")                                    #similar for japnese language
            print("2. Quiz")
            print("3. professional learning")
            print("------------------------------------")
            p1=int(input("Enter your preference: "))
            print("--------------")
    
            if p1==1:
                print("1. Number")
                print("2. Alphabets")
                print("3. Animals")
                print("4. body part")
                print("------------------------------------")
                c = int(input("Enter your preference: "))
                print("------------------------------------")
                match c:
                    case 1:japanese_numbers()
                    case 2:japanese_alphabets()
                    case 3:japanese_animals()
                    case 4:japanese_body_parts()
                        
            elif p1==2:
                print("----------Japanese quiz------------")
                print("1.number quiz")
                print("2.alphabet quiz")
                print("3.animals name quiz")
                print("4.body part quiz")
                pre1=int(input("enter your prefrance:"))
                print("------------------------------------")
            
                match pre1:
                    case 1:japanese_number_quiz()
                    case 2:japanese_alphabet_quiz()
                    case 3:japanese_animal_quiz()
                    case 4:japanese_body_part_quiz()

            elif p1==3:
                print("----------Japanese Learning------------")
                print("1.sentences")
                print("2.paragraph")
                print("3.email")
                pre3=int(input("enter your preference:"))
                print("------------------------------------")   
                match pre3:
                    case 1:japanese_learning_sentences()      
                    case 2:japanese_learning_paragraph()
                    case 3:japanese_learning_email()
