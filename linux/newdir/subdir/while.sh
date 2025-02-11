echo "enter num"
read a
while [ $a -gt 0 ]
do 
a=`expr $a - 1`
echo $a
done
