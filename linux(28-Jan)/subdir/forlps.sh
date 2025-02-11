if [ "$#" -lt 2 ]; then
  echo "Please provide at least two numbers as arguments."
  exit 1
fi
 
echo "You entered the following numbers:"
for num in "$@"
do
  echo $num
done
 
greatest=$1  
 
for num in "$@"; do
  if [ "$num" -gt "$greatest" ]; then
    greatest=$num
  fi
done
 
echo "The greatest number is: $greatest"
