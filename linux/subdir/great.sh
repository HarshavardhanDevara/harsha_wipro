echo "enter a number a"
read a
echo "enter a number b"
read b
echo "enter a number c"
read c
if [ $a -gt $b ] && [ $a -gt $c ] 
then 
	echo "the greater number is a:$a"
elif [ $b -gt $c ] 
then 
       echo "the great number is b:$b"
else
    echo "the greater number is c:$c"
fi

