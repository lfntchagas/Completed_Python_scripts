import subprocess
import optparse

parser = optparse.OptionParser()  # create an instance of the class OptionParser.

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()  # Allows the object understand what the user has input

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for" + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
