var firstDice = Int.random(in: 1...6)
var secondDice = Int.random(in: 1...6)
while firstDice != secondDice {
  firstDice = Int.random(in: 1...6)
  secondDice = Int.random(in: 1...6)
}
print("You rolled a double \(firstDice).")