in=$1
yeet()
{
    dir=$(pwd)
    username=$1
    cd pretend
    cd osintgram
    output=$(python3 main.py $username --command wtagged)
    cd ..
    cd ..
    
    username="${username}_tag"
    echo $output | tee -a $username.txt
}

yeet $in


