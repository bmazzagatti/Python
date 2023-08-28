var totalTurns = 3
var turnsLeft = true
while turnsLeft
{
  totalTurns -= 1
  if totalTurns < 1 {
    turnsLeft = false
}
  print("got another turn")
}