// sum the input of a number to one digit ie 21 = 3 untill it is less than 10
// so 2568 ==> 3

function sumtoone(number){
  var value = number
  sum = value
  while (sum >9){
    sum = value
        .toString()
        .split('')
        .map(Number)
        .reduce(function (a, b) {
            return a + b;
        }, 0);
        console.log(sum)
        if (sum > 9){
          newsum = sum
          .toString()
          .split('')
          .map(Number)
          .reduce(function (a, b) {
              return a + b;
          }, 0);
          console.log(newsum)

        }
      }

    console.log(sum);
}
sumtoone(2568);
