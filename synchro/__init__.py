# flake8: noqa
from signals import DisableSynchroLog, disable_synchro_log
from utility import NaturalManager, reset_synchro
#generates import warning in Django 1.8 
#from management.commands.synchronize import call_synchronize

default_app_config = 'synchro.apps.SynchroConfig'
