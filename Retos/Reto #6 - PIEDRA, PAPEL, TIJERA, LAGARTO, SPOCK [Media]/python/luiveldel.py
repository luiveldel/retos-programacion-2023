# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4
    
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
    }
    
def determine_winner(duels):
    
    score_p1: int = 0
    score_p2: int = 0
    
    for duel in duels:
        player_1 = duel[0]
        player_2 = duel[1]
        if player_1 != player_2:
            if player_2 in victories[player_1]:
                score_p1 += 1
            else:
                score_p2 += 1
        
        return "Tie" if score_p1 == score_p2 else "Player 1" if score_p1 > score_p2 else "Player 2"

    
print(determine_winner([(Action.Rock, Action.Scissors), (Action.Scissors, Action.Rock), (Action.Paper, Action.Scissors)]))
print(determine_winner([(Action.Scissors, Action.Scissors), (Action.Scissors, Action.Rock), (Action.Paper, Action.Scissors)]))

print(determine_winner([(Action.Rock, Action.Rock)]))
print(determine_winner([(Action.Rock,  Action.Scissors)]))
