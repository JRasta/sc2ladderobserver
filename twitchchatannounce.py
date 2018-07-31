import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'irc.chat.twitch.tv'
channel = '#starcraft2ai'
botnick = 'Starcraft2ai'
oauth = 'oauth:yourtwitchoauth'


ircsock.connect((server, 6667))
ircsock.send(bytes("PASS " + oauth + "\n", "UTF-8"))
ircsock.send(
    bytes("USER " + botnick + " " + botnick + " " + botnick + " " + botnick + "\n", "UTF-8"))
ircsock.send(bytes("NICK " + botnick + "\n", "UTF-8"))

def joinchan(chan):
    ircsock.send(bytes("JOIN " + chan + "\n", "UTF-8"))


def ping():
    ircsock.send(bytes("PONG :pingis\n", "UTF-8"))


def sendmsg(msg, target=channel):
    ircsock.send(bytes("PRIVMSG " + target + " :" + msg + "\n", "UTF-8"))


def readfile(filename):
    file = open(filename, "r")
    for line in file.readlines():
        print(line)
        sendmsg(line, channel)


def main():
    joinchan(channel)

    readfile('temp/round.txt')

    readfile('temp/bot_1.txt')
    sendmsg("VS", channel)
    readfile('temp/bot_2.txt')

    ircsock.send(bytes("QUIT \n", "UTF-8"))

main()

