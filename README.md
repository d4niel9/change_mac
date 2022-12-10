# Change MAC


## Install  :gear:

```console
1. Install package tool 
    $ sudo apt-get install macchanger
    $ sudo apt install net-tools

2. Clone this repo
    $ git clone https://github.com/d4niel9/change_mac.git

3. Change the working directory
    $ cd change_mac

4. Run the script
    $ sudo 
    python3 main.py
```


## Use :video_game:

```consol
$ python3 master.py

Network interface-> wlp3s0
ifconfig wlp3s0 down
macchanger --mac=08:00:27:xx:xx:xx wlp3s0
ifconfig wlp3s0 up

```
