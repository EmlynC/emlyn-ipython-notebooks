from pathlib import Path
from subprocess import Popen, DEVNULL, STDOUT
from typing import Union, List, Iterable

from dockstring.utils import PathType, get_resources_dir, parse_search_box_conf, write_mol_to_mol_file
from rdkit import Chem

files_dir = Path().parent.resolve() / 'files'


def view_in_pymol(
        name: str,
        pdbqt_path: str,
        conf_path: str,
        mol: Union[Chem.Mol, List[Chem.Mol], None] = None,
        include_search_box=True,
) -> Popen:
    """
    Launch PyMol and view the receptor and the search box.
    :return: return code of PyMol command
    """
    commands: List[Union[str, PathType]] = ['pymol', pdbqt_path]

    if include_search_box:
        pymol_script = get_resources_dir() / 'view_search_box.py'
        conf = parse_search_box_conf(conf_path)
        # yapf: disable
        commands += [
            pymol_script,
            '-d', 'view_search_box center_x={center_x}, center_y={center_y}, center_z={center_z}, '
                  'size_x={size_x}, size_y={size_y}, size_z={size_z}'.format(**conf)
        ]
        # yapf: enable

    if mol:
        if not isinstance(mol, Iterable):
            mol = [mol]

        for index, pose in enumerate(mol):
            mol_file = files_dir / f'{name}.mol'
            write_mol_to_mol_file(pose, mol_file)
            commands += [str(mol_file)]

    return Popen(commands, stdout=DEVNULL, stderr=STDOUT)
