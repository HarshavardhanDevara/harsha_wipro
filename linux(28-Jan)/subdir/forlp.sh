max=0  # Initialize max
 
# Use seq to generate numbers from 1 to 10
for i in $(seq 1 10); do
  read -p "Enter number $i: " num
  if [ "$num" -gt "$max" ]; then
    max=$num
  fi
done
 
echo "The greatest number is: $max"
