import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from pdoc import pdoc, render

here = Path(__file__).parent
out = here / "docs" / "api"
shutil.rmtree(out, ignore_errors=True)
out.mkdir()

# Render pdoc's documentation into docs/api...
render.configure(template_directory=here / "pdoc_templates")
with TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    pdoc(
        "reprexlite.code",
        "reprexlite.reprex",
        "reprexlite.session_info",
        output_directory=tmp_path,
    )

    # ...and rename the .html files to .md so that mkdocs picks them up!
    rendered = sorted(tmp_path.glob("**/reprexlite/*.html"))
    print(rendered)
    for f in rendered:
        # file will look like: .../reprexlite/code/index.html
        module_name: str = f.stem
        shutil.copy(f, out / f"{module_name}.md")
