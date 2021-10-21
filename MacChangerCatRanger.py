import subprocess
import optparse
import re

##made by CatRanger

print("""
....                          .... 
              ..x....                      ....x.. 
             ..xx......     ........     ......xx.. 
            ..xxxx...,,. .............. .,,...xxxx.. 
            ..xxxxx,,,,..................,,,,xxxxx.. 
             .,,,,..,,...................,,..,,,,,. 
           ........ ,,,.................,,, ......... 
         ....... .(((,,,...............,,,))). ........ 
        ..... ..,,a@@@@a,,...........,,a@@@@a,,.. ...... 
       .......,,a@@`  '@@,...........,@@`  '@@a,,........ 
       .......,,@@@    @@@,.a@@@@@a.,@@@    @@@,,........ 
       ....,,,,,,@@@aa@@@,,,,`@@@',,,,@@@aa@@@,,,,,,,.... 
        ...,,,,,,,,,,,,,,,,,,,,|,,,,,,,,,,,,,,,,,,,,,... 
          ...,,,,,,,,,,,,,,,,`   ',,,,,,,,,,,,,,,,,... 
              .. ,,,,,,,,,,,,,...,,,,,,,,,,,,,, .. 
      (     ......... ,,,,,,,,,,,,,,,,,,, ........... 
   (   )  .............._ _ _ _ _ _ _ _................   ( 
    )  ( ...............................................   ) 
   (   ) ...............................................  (  ) 
    ) ( ,,,,,,,,,,,,,,, ................. ,,,,,,,,,,,,,,,, ) ( 
 ,%%%%,,,,,,,,,,,,,,,,,, ............... ,,,,,,,,,,,,,,,,,,%%%%, 
 %%%%%`.,,(,,(,,(,,(,,'%%%%%%%%%%%%%%%%%%`,,,),,),,),,),,.'%%%%% 
 `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%' 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
    ::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::: 
   ::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::: 
  ::::::;;%%;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::::: 
 ::::::;;%%;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%:::::: 
::::::;;%%%;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%:::::: 
::::::;;%%%;;;;A;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%%::::: 
::::::;;;%%;;;;;AA;;;;;;;;;;;;;;;;;;;;A;;;;;;;;;;;;;;;;;;%%%::::: 
::::::;;;;%%;;;;;AAA;;;;;;;;;;;;;;;;AA;;;;;;;;;;;;A;;;;;;%%:::::: 
::::::;;A;;;;;;;;;AAA;;;;;;;;;A;;;;AAA;;;;;;;;;;;;;AA;;;%%;:::::: 
 ::::::;AA;;;;;;;;;AAA;;;;;;;A;;;;;AAAA;;;;;A;;;;;;AAA;;;;:::::: 
  ::::::;AAA;;;;;;;AAA;;A;;;AA;;;;;;AAAA;;;;AA;;;;;AAA;;;:::::: 
    :::::;AAA;;;;;AAA;;AA;;;AAA;;;;;;AAAA;;AAA;;;;AAAA;;::::: 
       :::;AAAA;;AAAA;;AAA;;;AAA;;;;AAAAA;AAA;;;;AAAAAA::: 
          ::AAAAAAAA;;;;AAA;AAAAA;;AAAAA;;;AAA;;AAAAAAA 
            .::::::                           ::::::. 
           :::::::'                           `:::::::
""")

def ChangeMac(interface, new_mac):
    print("[*] Changing MAC address for " + interface + " to " + new_mac + " [*]")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("Thank you for using...")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[!] Please specify an interface, if you need a help then put down --help [!]")
    elif not options.new_mac:
        parser.error("[!] Please specify a mac address, if you need a help then put down --help [!]")
    return options

def getCurrentMac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[!] Could not read MAC address [!]")

options = get_arguments()

CurrentMac = getCurrentMac(options.interface)
print("Current MAC= "+ str(CurrentMac))

ChangeMac(options.interface, options.new_mac)

CurrentMac = getCurrentMac(options.interface)
if CurrentMac == options.new_mac:
    print("[+] MAC address was successfully changed to " + CurrentMac)
else:
    print("[+] MAC address wasn`t successfully changed")
