echo "Enter a number"
read a
until [ $a -lt 0 ]
do 
a=`expr $a - 1`
echo $a
done
