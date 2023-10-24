def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for i,competition in enumerate(competitions): #access both index and value of each item
        result = results[i] # 0 or 1
        homeTeam, awayTeam = competition #Destructuring the first and the second item of competition

        winningTeam = homeTeam if result == 1 else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
            
    return currentBestTeam

def updateScores(team, points, scores):
      if team not in scores: #If the team doesn't exist in the scores initialize it and then the points to its value
        scores[team] = 0 
      
      scores[team] += points  
            
        
print(tournamentWinner(
    [
        ["HTML", "C"],
        ["C", "Py"],
        ["Py", "HTML"]
    ],
    [0,0,1]
))        
        