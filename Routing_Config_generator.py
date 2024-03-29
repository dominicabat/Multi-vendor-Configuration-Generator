"""
Purpose: Automate the generation of configuration and commands - Different platforms routing configuration
John Dominic Abat, December 2023
"""

#import modules
#import variable_list, a .py file containing my defined variable values 

from jinja2 import Environment, FileSystemLoader
from variable_list import *


#define the environment, where the template value is rendered 
#template is rendered to the environment and assigned to tpl 
#output contains the text that is generated by the render, where the text is produced from the template and its pre-defined variables. (previously defined in variable_list)

env = Environment(loader=FileSystemLoader("templates"))
tpl = env.get_template("configuration_template.txt")
output = tpl.render(mask = mask, advertise_prefix = advertise_prefix, prefix_seq_input = prefix_seq_input)

print(output)








