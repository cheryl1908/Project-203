import socket
from threading import Thread
import random
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.0'
port_number = 7000

server.bind((ip_address, port_number))
server.listen()

clients = []
nicknames = []

questions = [
    'What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Patty\n d.Pizza',
    'Water boils at 212 units at which scale? \n a.Fahrenheit\n b.Celsius\n c.Rankine\n d.Kelvin',
    'Which sea creatures has three hearts? \n a.Dolphine\n b.Octopus\n c.Walrus d.Seal',
    'Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Jack\n c.Johnny\n d.Khurram',
    'How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196',
    'How many wonders are there in the world? \n a.7\n b.8\n c.10\n d.4',
    'What element does dot exist? \n a.Xf\n b.Re\n c.Si\n d.Pa',
    'How Many States are there in India? \n a.24\n b.28\n c.29\n d.31',
    'Who invented the telephone? \n a.A.G Bell\n b.Donald stefen Trump\n c.Wright brothers\n d.T.Edision',
    'Who is Loki? \n a.God of Thunder\n b.God of Dwarves\n c.God of Miachief\n d.God of Gods',
    'Who was the first indian female astronaut? \n a.Sunita Williams\n b.Kalpana Chawla\n c.None of them\n d.Both of them',
    'Which is the smallest continent? \n a.Asia\n b.Antarctica\n c.Africa\n d.Australia',
    'The beaver is the nation embelem of which country? \n a.Zimbabwe\n b.Iceland\n c.Argentina\n d.Canada',
    'How many players are on the field in baseball? \n a.6\n b.7\n c.9\n d.8',
    'Hg Stands for..... \n a.Mercury\n b.Helium\n c.Thorium\n d.Selenium',
    'Who gifted the statue of liberty to US? \n a.Brazil\n b.France\n c.Wales\n d.Germany',
    'Which planet is closest to the sun? \n a.Mercury\n b.pluto\n c.Earth\n d.Venus'
]
answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a']
print('Server is running...')

print('Sever has started...')

def get_random_question_answer(conn):
    random_index = random.randint(0, len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(conn):
    score = 0
    conn.send('Welcome to thsi quiz game'.encode('utf-8'))
    conn.send('You will receive a question. The answer to that question will be one of a, b, c, or d\n'.encode('utf-8'))
    conn.send('Good Luck!!\n\n'.encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    print(answer)

    while True:
        message = conn.recv(2048).decode('utf-8')
        try:
            if message:
                if message.lower() == 'answers':
                    score = score + 1
                    conn.send(f'Your score is {score}\n\n'.encode('utf-8'))
                else:
                    conn.send('Incorrect answer!!\n\n'.encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
                print(answer)
            else:
                remove(conn)
                remove_nickname(nickname)
        except Exception as e:
            print(str(e))
            continue
        
def remove(connection):
    if connection in clients:
        clients.remove(connection)
        
def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while True:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    clients.append(conn)
    nicknames.append(nickname)
    print(nickname + " Connected!")
    new_thread = Thread(target = clientthread, args = (conn, nickname))
    new_thread.start()