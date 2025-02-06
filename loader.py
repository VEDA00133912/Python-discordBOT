import os
from color import Color

async def load_commands(tree):
    commands_dir = './function/slashcommand'
    
    if not os.path.exists(commands_dir):
        Color.print_red(f'[ERROR] Directory not found: {commands_dir}')
        return

    for filename in os.listdir(commands_dir):
        if filename.endswith('.py'):
            try:
                file_path = f'function/slashcommand/{filename}'
                module_name = f'function.slashcommand.{filename[:-3]}'
                
                module = __import__(module_name, fromlist=['setup'])
                
                await module.setup(tree)
                
            except ImportError as ie:
                Color.print_red(f'[ERROR] Failed to import module {module_name}: {ie}')
            except AttributeError as ae:
                Color.print_red(f'[ERROR] Module {module_name} does not have a setup function: {ae}')
            except Exception as e:
                Color.print_red(f'[ERROR] Failed to load command from {filename}: {e}')
