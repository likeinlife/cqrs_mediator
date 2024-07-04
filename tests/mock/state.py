from dataclasses import dataclass, field


@dataclass
class State:
    modified: bool = field(default=False)
