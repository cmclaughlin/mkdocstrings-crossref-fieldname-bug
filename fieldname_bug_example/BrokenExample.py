from __future__ import annotations

from fieldname_bug_example.Tag import Tag

from typing import List

@dataclass
class BrokenExample:
    """ Broken Example class"""

    Tag: Tag
    """ This crossref does not work. The field name matches the field type. """