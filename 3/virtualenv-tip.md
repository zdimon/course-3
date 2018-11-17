## How to activate the virtual environment automatically.

###Create env.sh

    #!/bin/bash
    source ../bin/activate

### Add this code to ~/.bashrc file

cd () {
    builtin cd ${1:+"$@"} 
    if [ -f "env.sh" ]
    then
     . ./env.sh
    fi  
}
