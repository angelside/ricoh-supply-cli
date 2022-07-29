#!/usr/bin/env python
from easysnmp import Session
from easysnmp.exceptions import (EasySNMPTimeoutError, EasySNMPError)
import ipaddress
import sys
import typer

# OIDs
modelNameCode        = '.1.3.6.1.2.1.43.5.1.1.16.1'
serialNumCode        = '.1.3.6.1.2.1.43.5.1.1.17.1'
supplyNamesSNMPCode  = '.1.3.6.1.2.1.43.12.1.1.4.1'
supplyLevelsSNMPCode = '.1.3.6.1.2.1.43.11.1.1.9.1'

def snmp_request(ip):
    try:
        # Create an SNMP session to be used for all our requests
        session = Session(
            hostname  = ip,
            community = 'public',
            version   = 2,
            timeout   = 2,
            retries   = 1,
            abort_on_nonexistent = True
        )

        modelName = session.get(modelNameCode).value # Model name: IM C3500
        serialNum = session.get(serialNumCode).value # Serial num: 3110RA10716

        # Perform an SNMP walk
        supplyNamesSNMP  = session.walk(supplyNamesSNMPCode)  # supply names
        supplyLevelsSNMP = session.walk(supplyLevelsSNMPCode) # supply levels

        supplyNames  = []
        supplyLevels = []

        # Skip waste toner cartridge (index start from 0)
        supplyNames.extend(item.value for i, item in enumerate(supplyNamesSNMP) if i != 1)
        supplyLevels.extend(item.value for i, item in enumerate(supplyLevelsSNMP) if i != 1)

        # {'black': '80', 'cyan': '90', 'magenta': '90', 'yellow': '80'}
        supplyStatus = dict(zip(supplyNames, supplyLevels))

        result = {
            'ip'           : ip,
            'model'        : modelName,
            'serial'       : serialNum,
            'supplyStatus' : supplyStatus
        }
    # https://easysnmp.readthedocs.io/en/latest/exceptions.html
    except EasySNMPTimeoutError as e:
        exit_with_msg(f'Request timed out while connecting to remote host {ip}')
    except EasySNMPError as e:
        exit_with_msg('Something went wrong')
    else:
        return result

def exit_with_msg(msg):
    print(f'[ERROR] {msg}')
    sys.exit(0)

def progress_bar(count, text=''):
    bar_len    = 40
    total      = 100
    empty_fill = '-' # ∙
    fill       = '=' # ▣ ◉

    filled_len = int(round(bar_len * count / float(total)))
    percents   = round(100 * count / float(total), 1)
    bar        = fill * filled_len + empty_fill * (bar_len - filled_len)

    return '[%s] %s%s  %s\r' % (bar, percents, '%', text)

def validate_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"The IP address '{ip}' is not valid")
        sys.exit(0)

def main(ip):

    validate_ip_address(ip)

    result = snmp_request(ip)

    print(f"ip: {result['ip']} - model: {result['model']} - serial: {result['serial']}")
    print()

    for key, value in result['supplyStatus'].items():
        print(progress_bar(int(value), key))

if __name__ == '__main__':
    typer.run(main)
