# -*- coding: utf-8 -*-
WIN_PL2 = "Win for player2"
WIN_PL1 = "Win for player1"
ADV_PL2 = "Advantage player2"
ADV_PL1 =  "Advantage player1"


class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore=0
        if (self.p1points==self.p2points):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            result = self.GET_WINNER(minusResult, result)
        else:
            for i in range(1,3):
                result = self.GET_PLACE(i, result)
        return result

    def GET_PLACE(self, i, result):
        if (i == 1):
            tempScore = self.p1points
        else:
            result += "-"
            tempScore = self.p2points
        result += {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[tempScore]
        return result

    def GET_WINNER(self, minusResult, result):
        if (minusResult == 1):
            result = ADV_PL1
        elif (minusResult == -1):
            result = ADV_PL2
        elif (minusResult >= 2):
            result = WIN_PL1
        else:
            result = WIN_PL2
        return result
