# -*- coding: utf-8 -*-
WIN_PL2 = "Win for player2"
WIN_PL1 = "Win for player1"
ADV_PL2 = "Advantage player2"
ADV_PL1 = "Advantage player1"
FORTY = "Forty"
DEUCE = "Deuce"
ALL = "-All"
THIRTY = "Thirty"
FIFTEEN = "Fifteen"
LOVE = "Love"


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points==0):
                result = LOVE
            if (self.p1points==1):
                result = FIFTEEN
            if (self.p1points==2):
                result = THIRTY
            result += ALL
        if (self.p1points==self.p2points and self.p1points>2):
            result = DEUCE

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = FIFTEEN
            if (self.p1points==2):
                P1res = THIRTY
            if (self.p1points==3):
                P1res = FORTY

            P2res = LOVE
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = FIFTEEN
            if (self.p2points==2):
                P2res = THIRTY
            if (self.p2points==3):
                P2res = FORTY

            P1res = LOVE
            result = P1res + "-" + P2res


        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res= THIRTY
            if (self.p1points==3):
                P1res= FORTY
            if (self.p2points==1):
                P2res= FIFTEEN
            if (self.p2points==2):
                P2res= THIRTY
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res= THIRTY
            if (self.p2points==3):
                P2res= FORTY
            if (self.p1points==1):
                P1res= FIFTEEN
            if (self.p1points==2):
                P1res= THIRTY
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = ADV_PL1

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = ADV_PL2

        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = WIN_PL1
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = WIN_PL2
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points +=1


    def P2Score(self):
        self.p2points +=1
