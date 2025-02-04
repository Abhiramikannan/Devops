#!/bin/sh
      #this is used for the interpreter to understand not comment the first line
      #diff b/w bash and sh like diff java versions
echo "enter the score"
read -r score
if ( [ $score -ge 20 ] && [ $score -le 40 ] ); then
echo "batman plays well"
elif [ $score -lt 20 ] 
then
    echo "remove him"
else 
   echo "wooww"
fi


#print 1 to 5

for i in 1 2 3 4 5
do  
     echo "$i"
done

echo " "
for i in {1..5};
do  
     echo "$i"
done

echo " "
for i in $(seq 1 5);
do  
     echo "$i"
done


echo " "
for ((i=1;i<=10;i++))
do  
     echo "$i"
done



