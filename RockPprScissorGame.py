class Participant:
    def __init__(self,name):
        self.name = name
        self.points = 0
        self.choice = " "
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name = self.name))
        print("{name}, selects {choice} ".format(name = self.name, choice = self.choice))
    def toNumericalChoice(self):
        switcher = {
            "rock":0,
            "paper":1,
            "scissor":2
        }
        return switcher[self.choice]
    def incrementPoints(self):
        self.points +=1
class GameRound:
    def __init__(self,p1,p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        print("Round resulted in a {result}".format(result = self.getResultAsString(result)))
        if(result>0):
            p1.incrementPoints()
        elif(result<0):
            p2.incrementPoints()
        else:
            print("No points for anybody")
    def compareChoices(self,p1,p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def getResultAsString(self,result):
        res = {
            0:"draw",
            1: "win",
            -1: "loss"
        }
        return res[result]
    def awardPoints(self):
        print("implement")
class Game:
    def __init__(self):
        self.endGame = False
        player = input("Enter the name of the player ")
        self.participant = Participant(player)
        player = input("Enter the name of the player ")
        self.secondParticipant = Participant(player)
    def start(self):
        while not self.endGame:
            GameRound(self.participant,self.secondParticipant)
            self.checkEndcondition()
    def checkEndcondition(self):
        ans = input("Continue game? y/n: ")
        if ans == 'y':
            GameRound(self.participant,self.secondParticipant)
            self.checkEndcondition()
        else:
            print("Game Ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name,p1points=self.participant.points,p2name = self.secondParticipant.name,p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        if self.participant.points > self.secondParticipant.points:
            print("Winner is {name}" .format(name = self.participant.name))
        elif self.participant.points < self.secondParticipant.points:
            print("Winner is {name}" .format(name = self.secondParticipant.name))
        else:
            print("It is a Draw")

game = Game()
game.start()