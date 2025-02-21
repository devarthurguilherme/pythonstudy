class Player:
    # Class Constructor
    def __init__(self, playerName, playerPosition, playerNumber, playerGoals=0):
        self.playerName = playerName  # Attribute
        self.playerPosition = playerPosition  # Attribute
        self.playerNumber = playerNumber  # Attribute
        self.playerGoals = playerGoals  # Attribute


# Instancing and Accessing attributes
player1 = Player("Arthur", "forward", 7)
player2 = Player("Alexander", "forward", 11)


# Acessing attributes


player1.playerGoals += 11
player2.playerGoals += 32

print(f"""
      Player 1\n
      {player1.playerName}
      {player1.playerPosition}
      {player1.playerNumber}
      {player1.playerGoals}
      
      Player 2\n
      {player2.playerName}
      {player2.playerPosition}
      {player2.playerNumber}
      {player2.playerGoals}
      """)

# 10:55
