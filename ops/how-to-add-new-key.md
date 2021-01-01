## If you press a key and the key isn't detected on your system. Check below
## (This is tested on Arch linux)

### 1. Check dmesg and you can see the log `Unknown key pressed ... and Use 'setkeycodes ...'`

### 2. It's time to set keycodes, in order to do that you should know what keycode number should be mapped for the scancode. Check your /usr/include/linux/input-event-codes.h

### 3. Find the keycode you're looking for, in my case they're `KEY_HANGEUL` and `KEY_HANJA`

### 4. However if you just type the commands in your shell, it won't be affected when the next boot. So add a new service into /etc/systemd/system/(???).service. If it's a oneshot type you can write multiple ExecStart commands.
