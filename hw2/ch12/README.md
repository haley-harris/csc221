# Homework 2: Chapter 12: Process Management

the running instance of a program is called a process

the instructions from a running program are copied into memory and space is allocated for variables and other things required to manage its execution

use `top` program to get a snapshot of what is currently happening on the system

    user@bash: top
    Tasks: 174 total, 3 running, 171 sleeping, 0 stopped
    KiB Mem: 4050604 total, 3114428 used, 936176 free
    Kib Swap: 2104476 total, 18132 used, 2086344 free
    
    PID  USER %CPU %MEM COMMAND
    6978 ryan 3.0  21.2 firefox
    11   root 0.3  0.0  rcu_preempt
    6601 ryan 2.0  2.4  kwin

- **tasks** is another name for processes - most of the tasks are system processes
- shows a breakdown of working memory (RAM) and virtual memory
- lists most resource intensive processes on the system in order of resource usage

**top** gives a realtime view of the system

`ps` is a program that shows just the processes running in your current terminal
- adding `aux` argument will show the complete system


## Killing a crashed process

example: a running web browser locks up and you're unable to close the window - the program has become completely unresponsive
- kill the browser (Firefox, Chrome, Safari, etc) and reopen it

must identify process id using

    user@bash ps aux | grep 'firefox'
    ryan 6978 8.8 23.5 2344096 945452 ? Sl 08:03 49:53 /usr/lib64/firefox/firefox

the PID (process ID) `6978` is the number next to the owner and is used to identify the process

kill the process using `kill [signal] <PID>`

    user@bash: kill 6978
    user@bash: ps aux | grep 'firefox'
    ryan 6978 8.8 23.5 2344096 945452 ? Sl 08:03 49:53 /usr/lib64/firefox/firefox

when a process is killed `kill` sends the default signal (1) to the process which asks the process nicely to quit

**always use `kill <PID>` first**

if the default signal fails to kill the process - use signal `9` which forces the process to close

run `ps aux | grep 'firefox'` to test if process is still running or not - if it does not return output, the process has successfully been killed

**normal users may only kill processes which they are the owner of - the root user on the system may kill anyone's processes**

## Foreground and background jobs

run a program in the background when it doesn't need intervention from us, which allows us to continue working in the foreground

`sleep` program waits for a given number of seconds and then quits

`job` lists currently running jobs for us

running the following command tells terminal to 'sleep' for 5 seconds before presenting a prompt

    user@bash: sleep 5


adding an ampersand (&) at the end of the aforementioned command tells terminal to run this process in the background

    user@bash: sleep 5 &
    [1] 21634
    user@bash:
    user@bash:
    [1]+ Done sleep 5

move jobs between foreground and background
- use `CTRL + z` to pause and move the current running foreground process to the background
- then use `fg` program to bring background processes into the foreground

`fg <job number>`

use `jobs` to figure out what job number a process has been assigned

    user@bash: sleep 15 &
    [1] 21637
    user@bash: sleep 10
    (you press CTRL + z, notice the prompt comes back.)
    user@bash: jobs
    [1]- Running sleep 15 &
    [2]+ Stopped sleep 10
    user@bash: fg 2
    [1] Done sleep 15

