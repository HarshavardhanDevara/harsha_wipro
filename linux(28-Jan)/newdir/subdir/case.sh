echo "1. current directory"
echo "2. current date"
echo "3. current user"
echo "enter your choice"
read choice
case $choice in
1) pwd;;
2) date;;
3) who;;
*) echo "invalid choice"
esac
