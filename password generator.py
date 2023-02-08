import random

lowerCase = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
upperCase = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
number = "0123456789"
symbols = "@#$%*&+-/?/"
combination = lowerCase+upperCase+number+symbols
passwordLength = 13
password = "".join(random.sample(combination, passwordLength))
print("your generated Password is:", password)

