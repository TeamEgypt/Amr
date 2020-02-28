
import os
os.system("clear")

amrpass = input('Enter the pass: ') 

import nexamrpass
from pprint import pprint

client = nexmo.Client(
  application_id='88e4e851-f19a-4a5f-84da-80070eb2c5e2',
  private_key='private.key'
)

amrtxt = input('Enter the masge: ') 
amrnumber = input('Enter number: ')

ncco = [
  {
    'action': 'talk',
    'voiceName': 'Maged',
    'text': amrtxt
 }
]


response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': amrnumber
  }],
  'from': {
    'type': 'phone',
    'number': '2012118666'

  },
  'ncco': ncco
})

import os
os.system("clear")

pprint(response)

import os
os.system("clear")

print("###Done####")

print("designe by Amr Elshrif")
