import subprocess as sub
command = input("What do you want to add to history:?")
sub.call(["echo",com­mand,">>","/root/­.bash_history"])
echo "done"