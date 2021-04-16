class RPSLS:
    def __init__(self, name, action):

        self.rules = ("The rules are simple. Rock beats paper and lizard. Paper beats rock and spock. Scissors"
                      "beats paper and lizard. Lizard beats paper and spock. Spock beats rock and scissors."
                      "Each player picks an action at the same time. Whoever wins gets a point. If the players"
                      "do the same action, it's a tie! First player to get 3 points is the winner! ")
        self.name = name
        self.action = action
        self.score = 0

    def display_rules(self, rules):
        print(f"{self.rules}")

    def make_actions(self, action):
        pass

    
