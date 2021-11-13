in=$1
yeet()
{
    dir=$(pwd)
    username=$1
    cd pretend
    cd osintgram
    output=$(python3 main.py $username --command info)
    cd ..
    cd ..
    
    username="${username}_info"
    echo $output | tee -a $username.txt  
}

yeet $in
