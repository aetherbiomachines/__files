import os
import re
import webbrowser
import periodictable

from django.core.management.base import BaseCommand
from jinja2 import Environment, PackageLoader, select_autoescape


CHEMICAL_FORMULA_REGEX = '[A-Z][a-z]?|\d+'
env = Environment(
    loader=PackageLoader('aether.management.commands'),
    autoescape=select_autoescape()
)


class Command(BaseCommand):

    help = 'Turn a molecular formula into an HTML snippet.'


    def add_arguments(self, parser):
        parser.add_argument('formula', type=str, nargs='+')


    def handle(self, *args, **options):
        chemical_formula = options['formula'][0]

        dir_path = os.path.dirname(os.path.realpath(__file__))
        output_dir = os.path.join(dir_path, 'html', f'{chemical_formula}.html')
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f'{chemical_formula}.html')

        with open(output_path, 'w') as output_file:
            chemical_formula = re.findall(CHEMICAL_FORMULA_REGEX, chemical_formula)

            chemical_formula = list(zip(chemical_formula[::2], chemical_formula[1::2]))

            weight = 0
            for element, num_atoms in chemical_formula:
                element = eval(f'periodictable.{element}')
                weight += element.mass*int(num_atoms)


            template = env.get_template('chemical_formula.html')
            html_snippet = template.render(chemicalFormula=chemical_formula, weight=weight)

            output_file.write(html_snippet)

        webbrowser.open_new_tab(f'file:///{output_path}')
