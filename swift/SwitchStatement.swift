let freeApp = true
if freeApp == true {
    print("You are using the free version of the app. Buy the full version to get full access to all of its features")
}
let morningTemperature = 70
let eveningTemperature = 80
if morningTemperature < eveningTemperature{
    print("it should warm up later")
}else {
    print("it should cool down later")
}
let temperatureDegree = "Fahrenheit"
if temperatureDegree == "Fahrenheit" {
  print("The weather app works with Fahrenheit degrees.")
} else {
  print("The weather app works with Celsius degrees.")
}
if temperatureDegree == "Celsius" || temperatureDegree == "Fahrenheit"{
    print("the app is configured correctly")
} else{
    print("the app is not configured proplerly")
}
switch temperatureDegree{
    case "Fahrenheit": print("the app measures temperature in Fahrenheit")
    case "Celsius": print("the app measures temperature in Celsius")
    default: print("The app does not use Fahrenheit or Celsius")
}